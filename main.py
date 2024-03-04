from utils import get_vacancies, create_database,save_data_to_database
from config import HH_URL, params, config

def main():
    req = get_vacancies(HH_URL, params)
    par = config()
    create_database('hh_info23', par)

    save_data_to_database('hh_info11', par, req)




if __name__ == '__main__':
    main()