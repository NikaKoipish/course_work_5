from utils import get_vacancies, create_database,save_data_to_database
from config import HH_URL, params, config
from dbmanager import DBManager
def main():
    req = get_vacancies(HH_URL, params)
    par = config()
    create_database('hh_info14', par)
    save_data_to_database('hh_info14', par, req)

    info = DBManager('hh_info14', par)
    #info.get_companies_and_vacancies_count()
    info.get_all_vacancies()





if __name__ == '__main__':
    main()