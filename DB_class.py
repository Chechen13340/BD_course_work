import psycopg2


class DBManager:
    def __init__(self, database_name: str, params: dict):
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """
        Метод для получения списка всех компаний
        и количества вакансий у каждой компании.
        """
        query = """
                SELECT name_comp, COUNT(name_vac)
                FROM vacancies
                GROUP BY name_comp
                """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_all_vacancies(self):
        """
        Метод для получения списка всех вакансий с указанием названия компании,
        названия вакансии и зарплаты, и ссылки на вакансию.
        """
        query = """
                SELECT name_comp, name_vac, salary_from, salary_to, url
                FROM vacancies
                """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_avg_salary(self):
        """
        Метод для получения средней
        зарплаты по вакансиям.
        """
        query = """
                SELECT ROUND((salary_avg) ,0)
                FROM vacancies
                """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        """
        Метод для получения списка всех вакансий,
        у которых зарплата выше средней по всем вакансиям.
        """
        query = """
                SELECT  *
                FROM vacancies
                WHERE salary_avg > (SELECT ROUND(AVG(salary_avg), 0)
                FROM vacancies)
                """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, key_word: str):
        """
        Метод для получения списка всех вакансий,
        в названии которых содержатся переданные в метод слова.
        """
        query = f"""
                SELECT name_comp, name_vac, salary_avg FROM vacancies
                WHERE name_vac LIKE '%{key_word}%'
                """
        self.cur.execute(query)
        return self.cur.fetchall()