import MySQLdb, time
import pandas as pd
import concurrent.futures
import re



# def to_mysql(df_send):

    # 內部網路
    # db = MySQLdb.connect(
    #     host='localhost',
    #     port = 3306,
    #     user = 'YunJu',
    #     password = '1234',
    #     db = 'i_nutrition')
    #

def insert_db_data(insert_data):

    db = MySQLdb.connect(host='localhost', user='YunJu', passwd='1234',
                         db='i_nutrition', port=3306, charset='utf8')
    cursor = db.cursor()  # 設定游標
    #db.autocommit(True)  # 設定自動確認
    #print('a')

    try:
        #print(insert_data[0])
        sql_str = f'''insert into recipe(RecipeName,RecipeURL,RecipeImageURL)
                  values('{insert_data[0]}','{insert_data[1]}','{insert_data[2]}')'''

        print(sql_str)
        cursor.execute(sql_str)


    except Exception as err:
        print('unable to insert data to db')
        print(err)
        print(insert_data)


    db.commit()
    db.close()



def main():
    df_json = pd.read_json(r'./[200613_2]recipe.json')["Recipe"]
    # df_json = pd.read_json("recipe(silver).json")
    # print(type(df_json))
    # print(len(df_json))
    # df_json=df_json[0:10]
    for item in df_json:
        ll=[]
        kkkk = re.sub(r"[^\u4e00-\u9fa5]", "", item["RecipeName"])
        ll.append(kkkk)
        ll.append((item["RecipeURL"]))
        ll.append((item["RecipeImageURL"]))
        #print(ll)
        insert_db_data(ll)

if __name__ == "__main__":
    main()







# food_dict = {"RecipeName":recipename, "RecipeURL":recipeurl,"RecipeImageURL":recipeimageurl}
# df = pd.DataFrame(food_dict)
#
# #把Key取出轉成字串
#
# headers =list(food_dict.keys())
# headers_str = ''
# for h in headers:
#     headers_str += h+ ', '
#
# headers_str = headers_str.rstrip(', ')
# # print(headers_str)







