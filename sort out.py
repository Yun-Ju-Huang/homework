import pandas as pd
import re
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

df_json = pd.read_json("[200614]recipe.json")["Recipe"]

recipename = []
recipeurl = []
recipeimageurl=[]




for item in df_json:


    recipename.append(item["RecipeName"])
    recipeurl.append((item["RecipeURL"]))
    recipeimageurl.append((item["RecipeImageURL"]))
    # print(item)
    it_name = []
    it_quantity = []
    it_unit = []


    # for it in item["Ingredients"]:
    #     it_name.append(it["It_name"])
    #     it_quantity.append("---{}---".format(it["It_quantity"]))
    #     it_unit.append("---{}---".format(it["It_unit"]))
    # it_df = pd.DataFrame({"It_name":it_name, "unit":it_unit})
    # print(it_df)
        # it_df = pd.DataFrame(it)
        # print(it_df)
food_dict = {"RecipeName":recipename, "RecipeURL":recipeurl,"RecipeImageURL":recipeimageurl}
# food_dict = {"RecipeName":recipename,"RecipeURL":recipeurl,"RecipeImageURL":recipeimageurl}
df = pd.DataFrame(food_dict)
print(df)
#
# df.to_csv("test.csv",index=False,sep=',')
# print(df)



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
    # df1 = pd.read_csv('./test.csv',encoding='utf8')
    # print(df1)
    df.to_sql('recipe111',engine)
    print("Write to MySQL successfully!")
except Exception as e:
    print(e)
