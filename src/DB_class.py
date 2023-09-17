from collections import Counter

import requests

from settings import HH_API_URL


class DBManager:
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def get_companies_and_vacancies_count(self):
        """
         Метод для получения списка всех компаний
          и количества вакансий у каждой компании.
        """
        employer_information = []
        for page in range(0, 20):
            params = {
                'text': 'мироэлектроника',
                'area': 113,
                'per_page': 100,
                'page': page,
                'only_with_vacancies': True
            }

            url = HH_API_URL
            headers = {"User-Agent": "HH-User-Agent"}
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            for num in data['items']:
                company_name = num['employer']['name']

                if (company_name == 'Радар ММС' or company_name == 'Авангард' or company_name == 'Светлана-Рост'
                        or company_name == 'Группа компаний Микрон' or company_name == 'Ангстрем'
                        or company_name == 'ОКБ-ПЛАНЕТА' or company_name == 'НПЦ ЭЛВИС' or company_name == 'НИИ Гириконд'
                        or company_name == 'Точных Приборов, НИИ' or company_name == 'Российские космические системы'):
                    employer_information.append(company_name)
        list_name_count_vacancies = Counter(employer_information)
        return list_name_count_vacancies

    def get_all_vacancies(self):
        """
        Метод для получения списка всех вакансий с указанием названия компании,
        названия вакансии и зарплаты, и ссылки на вакансию.
        """
        employer_information = []
        for page in range(0, 20):
            params = {
                'text': 'мироэлектроника',
                'area': 113,
                'per_page': 100,
                'page': page,
                'only_with_vacancies': True
            }

            url = HH_API_URL
            headers = {"User-Agent": "HH-User-Agent"}
            response = requests.get(url, headers=headers, params=params)
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
                    elif num['salary']['from'] is None:
                        salary_min = 0
                        salary_max = num['salary']['to']
                    elif num['salary']['to'] is None:
                        salary_min = num['salary']['from']
                        salary_max = 0
                    else:
                        salary_min = num['salary']['from']
                        salary_max = num['salary']['to']

                    employer_information.append({
                        'Название компании': company_name,
                        'Название вакансии': vacancies_name,
                        'Заработная плата от': salary_min,
                        'Заработная плата до': salary_max,
                        'Ссылка на вакансию': url_vacancies
                    })

        return employer_information

    def get_avg_salary(self):
        """
        Метод для получения средней
        зарплаты по вакансиям.
        """
        avg_salary_all = []
        for vacancy in self.get_all_vacancies():
            if vacancy['Заработная плата от'] == 0:
                avg_salary = vacancy['Заработная плата до']
            elif vacancy['Заработная плата до'] == 0:
                avg_salary = vacancy['Заработная плата от']
            elif vacancy['Заработная плата от'] == 0 and vacancy['Заработная плата до'] == 0:
                avg_salary = 0
            else:
                avg_salary = (vacancy['Заработная плата от'] + vacancy['Заработная плата до']) // 2
            avg_salary_all.append(avg_salary)
        return avg_salary_all

    def get_vacancies_with_higher_salary(self):
        """
        Метод для получения списка всех вакансий,
        у которых зарплата выше средней по всем вакансиям.
        """
        higher_salary = []
        total_salary = 0
        count = 0
        for salary in self.get_avg_salary():
            if salary != 0:
                total_salary += salary
                count += 1
        total_avg_salary = total_salary // count
        for salary in self.get_all_vacancies():
            if salary['Заработная плата от'] > total_avg_salary or salary['Заработная плата до'] > total_avg_salary:
                higher_salary.append(salary)
        return higher_salary

    def get_vacancies_with_keyword(self, key_word: str):
        """
        Метод для получения списка всех вакансий,
        в названии которых содержатся переданные в метод слова.
        """
        key_word_vacancies = []
        for vacancy in self.get_all_vacancies():
            if key_word in vacancy['Название вакансии']:
                key_word_vacancies.append(vacancy)
        return key_word_vacancies
