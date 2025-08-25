import requests
from bs4 import BeautifulSoup
from config import HEADERS

url = "https://career.habr.com/vacancies?q=python&type=all"

response = requests.get(url,headers=HEADERS)

soup = BeautifulSoup(response.text,"lxml")

vacancies = soup.find_all("div",class_="vacancy-card__info")

for vacancy in vacancies:
    title = vacancy.find("div",class_="vacancy-card__title").text.strip()
    company = vacancy.find("div",class_="vacancy-card__company").text.strip()
    salary = vacancy.find("div",class_="basic-salary").text

    print(f"Название - {title}")
    print(f"Компания - {company}")
    print(f"Зарплата - {salary}")
    print()