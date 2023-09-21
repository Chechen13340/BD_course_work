from config import config
from DB_class import DBManager
from utils import create_database, save_data_to_database


def main():
    params = config()
    create_database('headhunter', params)
    save_data_to_database('headhunter', params)
    db_headhunter = DBManager('headhunter', params)
    print(db_headhunter.get_companies_and_vacancies_count())
    print(db_headhunter.get_all_vacancies())
    print(db_headhunter.get_avg_salary())
    print(db_headhunter.get_vacancies_with_higher_salary())
    key_word = input('Введите ключевое слово: ')
    print(db_headhunter.get_vacancies_with_keyword(key_word))


if __name__ == '__main__':
    main()
