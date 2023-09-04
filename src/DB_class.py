class DBManager:
    def __init__(self):
        pass

    def get_companies_and_vacancies_count(self, company_name: list, count_vacancies: int):
        """
         Метод для получения списка всех компаний
          и количества вакансий у каждой компании.
        """
        pass

    def get_all_vacancies(self, vacancies_info: list[dict]):
        """
        Метод для получения списка всех вакансий с указанием названия компании,
        названия вакансии и зарплаты, и ссылки на вакансию.
        """
        pass

    def get_avg_salary(self, avg_salary: int):
        """
        Метод для получения средней
        зарплатыпо вакансиям.
        """
        pass

    def get_vacancies_with_higher_salary(self, top_vacancies: list):
        """
        Метод для получения списка всех вакансий,
        у которых зарплата выше средней по всем вакансиям.
        """
        pass

    def get_vacancies_with_keyword(self, key_word_vacancies: list):
        """
        Метод для получения списка всех вакансий,
        в названии которых содержатся переданные в метод слова.
        """
        pass
