import pandas as pd
from sqlalchemy import create_engine


host= 'localhost'
port= 3306
user= 'YunJu'
password= '1234'
db = 'i_nutrition'


engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}:{port}/{db}?charset=utf8')

try:
    df = pd.read_csv('./food_all.csv',encoding='utf8')
    print(df)
    df.to_sql('recipe1111',engine)
    print("Write to MySQL successfully!")
except Exception as e:
    print(e)