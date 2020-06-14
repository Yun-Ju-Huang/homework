import pandas as pd
import re
from sqlalchemy import create_engine
import pymysql


host= 'localhost'
port= 3306
user= 'YunJu'
password= '1234'
db = 'i_nutrition'
#
#
engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}:{port}/{db}?charset=utf8')
#
try:
    df1 = pd.read_csv('./Ingredient.csv',encoding='utf8')
    print(df1)
    df1.to_sql('Ingredient',engine)
    print("Write to MySQL successfully!")
except Exception as e:
    print(e)
