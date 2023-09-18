import psycopg2


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


def save_data_to_database(data, database_name, params):
    """
    Функция для сохранения данных в БД.
    """
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for vacancies in data:
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
