import pymongo
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
user= str(os.getenv("USER"))
password= str(os.getenv("PASSWORD"))
# 連線到 mongoDB
client= pymongo.MongoClient("mongodb+srv://"+user+":"+password+"@mycluster0.gcfkgiv.mongodb.net/?retryWrites=true&w=majority")
# 把資料放入資料庫中
db=client.website #選擇要操作的資料庫(website)
collection=db.members #選擇要操作的集合(members)

#====================================================
# 排序資料(塞選條件, sort=排序方式)
# DESCENDING(由大到小) ASCENDING(由小到大)
cursor= collection.find({}, sort=[
    ("rank",pymongo.ASCENDING)
])
for i in cursor:
    print(i["username"])
# 篩選資料 $and $or (會員登入時的條件 帳號$and密碼)
data= collection.find_one({
    "$and":[
        {"email":"weichu@test.com"},
        {"password":"weichu123"}
    ]
})
print(data)
cursor=collection.find({
    "rank":2
})
for i in cursor:
    print(i["username"])
data= collection.find_one({
    "email":"alan@test.com"
})
print(data)
#====================================================
# 刪除資料
# result= collection.delete_one({
#     "email":"hehe@test.com"
# })
# print("實際刪除的文件數量", result.deleted_count)
# result= collection.delete_many({
#     "email":"hehe@test.com"
# })
# print("實際刪除的文件數量", result.deleted_count)
#====================================================
# 更新資料 $set $inc $mul $unset
# 更新集合中的一份文件資料
# result= collection.update_one({
#     'email':"jimmy@test.com"
# },{
#     "$set":{
#         "rank": 3
#     }
# })
# print("符合條件的文件數量", result.matched_count)
# print("實際執行的文件數量", result.modified_count)
# 更新集合中的多筆資料
# result= collection.update_many({
#     "rank":"2"
# },{
#     "$set":{
#         "rank":2
#     }
# })
# print("符合條件的文件數量", result.matched_count)
# print("實際執行的文件數量", result.modified_count)
#=====================================================
# 取得集合中的第一筆資料
# data= collection.find_one()
# print(data)
# 根據ObjectId 取得文件資料
# data= collection.find_one(
#     ObjectId("62a14b4f6badfe5b9a2521d8")
# )
# print(data)
# 取得文件資料中的欄位
# print(data["email"])
# 一次取得多筆文件資料
# cursor= collection.find() #cursor 是物件(讀寫頭) 需要用for迴圈依序取出
# for i in cursor:
#     print(i["username"])
#=======================================================
# 把文件資料新增到集合中(一次一個)
# reslt= collection.insert_one({
#     "username":"艾倫",
#     "email":"alan@test.com",
#     "password":"alan123",
#     "rank":"2"
# })
# print("成功")
# print(result.inserted_id)
# 把文件資料新增到集合中(一次多個)
# result= collection.insert_many([{
#     "username":"zac",
#     "email":"zac@test.com",
#     "password":"zac123",
#     "rank":"3"
# },{
#     "username":"jimmy",
#     "email":"jimmy@test.com",
#     "password":"jimmy123",
#     "rank":"2"
# }])
# print("成功")
# print(result.inserted_ids)