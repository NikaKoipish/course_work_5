import os
from configparser import ConfigParser

ROOT_DIR = os.path.dirname(__file__)
OPERATIONS_PATH = os.path.join(ROOT_DIR, "hh_vac.json")
HH_URL = "https://api.hh.ru/vacancies"
params ={
    'employer_id': ['9498120','78638','2748','3529','5557093','1035394','2510287','4164896','224839','10419023'],
    'page': 0,
    'per_page': 100
}

def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db