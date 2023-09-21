Данный проект собирает данные о вакансиях из 10 компаний по API с платформы HeadHunter.
Данные включают в себя:
Список всех компаний и количество вакансий у каждой компании.
Список всех вакансий с указанием названия компании, названия вакансии, заработной плате и ссылки на вакансию.
Список средней заработной платы.
Список всех вакансий, у которых заработная плата выше средней по всем вакансиям.
Список вакансий по ключевому слову.
Также данная программа создает таблицы в БД PostgreSQL и сохраняет данные о вакансиях.
Для сборки проекта необходимо:
1. Склонировать репозиторий.
2. Создать виртуальное окружение.
3. Установить зависимости проекта из pyproject.toml.
4. Создать файл database.ini и заполнить данные для подключения к PostgresSQL
Пример заполнения файла database.ini:
[postgresql]
host=your_host
user=your_name
password=your_password
port=your_port
5. Откройте файл .bashrc с помощью команды: nano ~/.bashrc -> введите переменную: export YOUR_NAME = API_KEY -> сохраните изменения, после чего в консоле введите source ~/.bashrc. Таким образом создана переменная содержащая API_Token.
