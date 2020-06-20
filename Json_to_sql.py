import pandas as pd
from sqlalchemy import create_engine
import sql_acount

engine=sql_acount.acount()
def df_to_sql(table_name,my_df):

    try:
        my_df.to_sql(table_name,engine)
        print("Write to MySQL successfully!")
    except Exception as e:
        print(e)

def recipe(data):
    df=pd.read_json(data)['Recipe']
    recipeName = []
    recipeURL = []
    recipeImageURL = []
    for item in df:
        # print(item)
        recipeName.append(item['RecipeName'])
        recipeURL.append(item['RecipeURL'])
        recipeImageURL.append(item['RecipeImageURL'])
    recipe= {"RecipeName":recipeName,"RecipeURL":recipeURL,"RecipeImageURL":recipeImageURL}
    r_df=pd.DataFrame(recipe)
    return r_df

def ingredients(data):
    df = pd.read_json(data)['Recipe']
    big_df = pd.DataFrame()
    for item in df:
        recipename = []
        r_name = item["RecipeName"]
        it_name = []
        it_quantity = []
        it_unit = []

        for it in item["Ingredients"]:
            recipename.append(r_name)
            it_name.append(it["It_name"])
            it_quantity.append("{}".format(it["It_quantity"]))
            it_unit.append("{}".format(it["It_unit"]))

        i= {"RecipeName": recipename, "It_name": it_name, "It_quantity": it_quantity, "unit": it_unit}

        dff = pd.DataFrame(i)
        # print(dff)

        big_df = big_df.append(dff, ignore_index=True)
    # big_df = pd.concat([dff],axis=0)

    return big_df



def synonyms(data):
    df4 = pd.read_csv(data)
    print(df4)
    return df4


def govfood(data):
    df = pd.read_excel(data)
    df0 = list(x for x in df["Ingredient_Catalog"])
    df1 = list(y for y in df["Ingredient_Name"])
    gov_food = pd.DataFrame({"Ingredient_Catalog":df0,"Ingredient_Name":df1})
    return gov_food



def main():
    food = synonyms("for_database/only_nutrients.csv")



    df_to_sql("nutrients",food)

if __name__ == '__main__':
    main()







