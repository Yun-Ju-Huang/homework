from sqlalchemy import create_engine

def acount():
    host = 'localhost'
    port = 3306
    user = 'YunJu'
    password = '1234'
    db = 'i_nutrition'
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}:{port}/{db}?charset=utf8')
    return engine