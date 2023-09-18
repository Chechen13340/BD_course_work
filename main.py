from config import config
from settings import HH_API_URL
from DB_class import DBManager
from utils import create_database, save_data_to_database


def main():
    url = HH_API_URL
    headers = {"User-Agent": "HH-User-Agent"}
    param = {
        'text': 'мироэлектроника',
        'area': 113,
        'per_page': 100,
        'page': range(0, 20),
        'only_with_vacancies': True
    }
    db_headhunter = DBManager(url, headers, param)
    print(db_headhunter.get_companies_and_vacancies_count())
    print(db_headhunter.get_all_vacancies())
    print(db_headhunter.get_avg_salary())
    print(db_headhunter.get_vacancies_with_higher_salary())
    key_word = input('Введите ключевое слово: ')
    print(db_headhunter.get_vacancies_with_keyword(key_word))
    params = config()
    create_database('headhunter', params)
    save_data_to_database(db_headhunter.get_all_vacancies(), 'headhunter', params)


if __name__ == '__main__':
    main()
