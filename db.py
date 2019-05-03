import pymongo

client = pymongo.MongoClient("mongodb+srv://dangduylan:lJCJiSpJuNpzDatG@cluster0-noolz.mongodb.net/test?retryWrites=true")
db = client.users

def add_user(username,nick_name,password):
    return  db.users.insert_one({
             "username":username,
            "nick_name":nick_name,
            "password":password
            })
    

def find_username(username):
    return db.users.find_one({"username":username})

def get_all():
    return list(db.users.find({}))