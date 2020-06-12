import pymongo
import csv
import pandas as pd
import _json
mongo = pymongo.MongoClient(host='localhost', port=27017)
# a = {'name': 'balao', 'age': 36}
ccc = {'name':'dddd', 'phonenuber':'0988461105'}
#
db = mongo.ed101
collection = db.XXX
# print(db.list_collection_names())
print(collection.insert(ccc))

mongo = pymongo.MongoClient(host='localhost', port=27017)
db = mongo.foodtitle
collection=db.food

with open('./food1.csv','r',encoding='utf-8-sig')as csvfile:
    df1 = pd.read_csv(csvfile)


    records = df1.to_dict('records')
    print(collection.insert(records))
    #print(records)












