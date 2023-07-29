import pymongo

# 获取链接mongodb的对象
client = pymongo.MongoClient('127.0.0.1',port=27017)
# 获取数据库（如果没有pythonMongoDB数据库，则会自动创建）
db = client.pythonMongo
# 获取集合（表）
collection = db.qa

# # 加入一条文档数据到集合中
# collection.insert_one({"title": "abcc","password":"heihei"})

# 加入多条文档数据到集合中
# item_1 = {
#   "_id" : "U1IT00001",
#   "item_name" : "Blender",
#   "max_discount" : "10%",
#   "batch_number" : "RR450020FRG",
#   "price" : 340,
#   "category" : "kitchen appliance"
# }
#
# item_2 = {
#   "_id" : "U1IT00002",
#   "item_name" : "Egg",
#   "category" : "food",
#   "quantity" : 12,
#   "price" : 36,
#   "item_description" : "brown country eggs"
# }
# collection.insert_many([item_1,item_2])

# 查找一条文档数据
# result = collection.find_one()
# print(result)
# # 条件查找，查找title为abc的文档数据
# result = collection.find_one({"title":'abc'})
# print(result)
result = collection.find()
for x in result:
    print(x)

# 更新一条文档数据
# collection.update_one({"title":'abcc'},{"$set":{"title":'abc'}})

# 更新多条文档数据
myquery = {"title":"123",}
newvalues = {"$set": {"title": "123"}}
x = collection.update_many(myquery, newvalues)
print("文档已修改",x.modified_count)

# 删除数据
x = collection.delete_one(myquery)
print("文档已删除：",x.deleted_count)
# 填入空集合，则删除所有数据
x= collection.delete_many({})
# print("文档已删除：",x.deleted_count)