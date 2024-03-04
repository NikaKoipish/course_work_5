import psycopg2

class DBManager:
    def __init__(self, db_name, params):
        self.db_name = db_name
        self.params = params
        self.conn = psycopg2.connect(dbname=self.db_name, **self.params)

    def get_companies_and_vacancies_count(self):
        '''получает список всех компаний и количество вакансий у каждой компании'''
        with self.conn.cursor() as cur:
            cur.execute("""SELECT companies.title as company_name, count(vacancies.title) as quantity_of_vacancies
                    FROM companies
                    JOIN vacancies
                    ON companies.company_db_id=vacancies.company_db_id
                    GROUP BY companies.title""")
            companies_and_vacancies = cur.fetchall()
            for row in companies_and_vacancies:
                print(f'Компания: {row[0]}\n'
                      f'Количество вакансий: {row[1]}')
        self.conn.close()

    def get_all_vacancies(self):
        '''получает список всех вакансий
        с указанием названия компании, названия вакансии и зарплаты
        и ссылки на вакансию'''
        with self.conn.cursor() as cur:
            cur.execute("""SELECT companies.title as company_name, vacancies.title as vacancy_name, vacancies.salary_from as salary, vacancies.vacancy_url as url
                        FROM companies
                        JOIN vacancies
                        ON companies.company_db_id=vacancies.company_db_id""")
            companies_and_vacancies = cur.fetchall()
            for row in companies_and_vacancies:
                print(f'Компания: {row[0]}\n'
                      f'Вакансия: {row[1]}\n'
                      f'Зарплата от: {row[2]}\n'
                      f'Ссылка на вакансию: {row[3]}\n')
        self.conn.close()

    def get_avg_salary():
        '''получает среднюю зарплату по вакансиям'''
        pass

    def get_vacancies_with_higher_salary():
        '''получает список всех вакансий, у которых зарплата
        выше средней по всем вакансиям'''
        pass

    def get_vacancies_with_keyword():
        '''получает список всех вакансий,
        в названии которых содержатся
        переданные в метод слова, например python'''
        pass

