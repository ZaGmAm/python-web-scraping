# Парсер вакансий с Habr Career🎯

Простой и эффективный скрипт на Python для сбора актуальных вакансий по запросу "python" с платформы Habr Career.

## Как это работает🎯

Скрипт использует:
- `requests` для отправки HTTP-запросов к сайту
- `BeautifulSoup` для парсинга HTML-разметки и извлечения данных
- Кастомные заголовки (`HEADERS`) для корректного отображения на стороне сервера

## Установка и запуск🎯

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Zedmlu/python-web-scraping.git
2. Установите необходимые зависимости:
bash
pip install requests beautifulsoup4
3. Создайте файл config.py и добавьте туда ваши заголовки:
HEADERS = {
    "User-Agent": "Your User-Agent Here"
}
4. Запустите скрипт:

```bash
python habr_vacancies.py
Пример вывода

# Пример вывода🎯
Название - Python-разработчик
Компания - ООО «Технологии будущего»
Зарплата - от 150 000 ₽

Название - Backend Developer (Python)
Компания - DataTech Solutions
Зарплата - По договорённости
