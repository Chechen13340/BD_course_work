import psycopg2
import requests

from settings import HH_API_URL


def create_database(database_name, params):
    """
    Функция для создания БД.
    """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                name_comp VARCHAR NOT NULL,
                name_vac VARCHAR NOT NULL,
                salary_from INTEGER,
                salary_to INTEGER,
                salary_avg INTEGER,
                url TEXT
            )
        """)

    conn.commit()
    conn.close()


def get_data_companies_vacancies():
    """
    Функция для получения списка всех вакансий с указанием названия компании,
    названия вакансий зарплаты, и ссылки на вакансию через API
    """
    employer_information = []
    for page in range(0, 20):
        param = {
            'text': 'мироэлектроника',
            'area': 113,
            'per_page': 100,
            'page': page,
            'only_with_vacancies': True
        }

        url = HH_API_URL
        headers = {"User-Agent": "HH-User-Agent"}
        response = requests.get(url, headers=headers, params=param)
        data = response.json()
        for num in data['items']:
            company_name = num['employer']['name']

            if (company_name == 'Радар ММС' or company_name == 'Авангард' or company_name == 'Светлана-Рост'
                    or company_name == 'Группа компаний Микрон' or company_name == 'Ангстрем'
                    or company_name == 'ОКБ-ПЛАНЕТА' or company_name == 'НПЦ ЭЛВИС' or company_name == 'НИИ Гириконд'
                    or company_name == 'Точных Приборов, НИИ' or company_name == 'Российские космические системы'):
                vacancies_name = num['name']
                url_vacancies = num['alternate_url']
                if num.get('salary') is None:
                    salary_min = 0
                    salary_max = 0
                    salary_avg = 0
                elif num['salary']['from'] is None:
                    salary_min = 0
                    salary_max = num['salary']['to']
                    salary_avg = num['salary']['to']
                elif num['salary']['to'] is None:
                    salary_min = num['salary']['from']
                    salary_max = 0
                    salary_avg = num['salary']['from']
                else:
                    salary_min = num['salary']['from']
                    salary_max = num['salary']['to']
                    salary_avg = (num['salary']['from'] + num['salary']['to']) // 2

                employer_information.append({
                    'Название компании': company_name,
                    'Название вакансии': vacancies_name,
                    'Заработная плата от': salary_min,
                    'Заработная плата до': salary_max,
                    'Средняя заработная плата': salary_avg,
                    'Ссылка на вакансию': url_vacancies
                })

    return employer_information


def save_data_to_database(database_name, params):
    """
    Функция для сохранения данных в БД.
    """
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for vacancies in get_data_companies_vacancies():
            vacancies_name = vacancies['Название компании']
            company_name = vacancies['Название вакансии']
            salary_from = vacancies['Заработная плата от']
            salary_to = vacancies['Заработная плата до']
            salary_avg = vacancies['Средняя заработная плата']
            url_vacancies = vacancies['Ссылка на вакансию']

            cur.execute(
                """
                INSERT INTO vacancies (name_comp, name_vac, salary_from, salary_to, salary_avg, url)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (vacancies_name, company_name, salary_from, salary_to, salary_avg, url_vacancies)
            )

        conn.commit()
        conn.close()
