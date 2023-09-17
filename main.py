from settings import HH_API_URL
from src.DB_class import DBManager


def main():
    url = HH_API_URL
    headers = {"User-Agent": "HH-User-Agent"}
    params = {
        'text': 'мироэлектроника',
        'area': 113,
        'per_page': 100,
        'page': range(0, 20),
        'only_with_vacancies': True
    }
    i = DBManager(url, headers, params)
    print(i.get_companies_and_vacancies_count())
    print(i.get_all_vacancies())
    print(i.get_avg_salary())
    print(i.get_vacancies_with_higher_salary())
    key_word = input('Введите ключевое слово: ')
    print(i.get_vacancies_with_keyword(key_word))

if __name__ == '__main__':
    main()
