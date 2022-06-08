#import pymongo
from flask import g, current_app
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash

DB_NAME = "universal_tagger"


def create_user_offline(username, password):
    client = MongoClient('localhost', 27017)

    db = client[DB_NAME]

    collection = db['users']

    if collection.find_one({'username': username}) is None:
        collection.insert_one({'username': username, 'password': generate_password_hash(password)})


def get_db(database_name=DB_NAME):
    if 'db' not in g:
        client = MongoClient('localhost', 27017)

        # Getting the database instance
        g.db = client[database_name]
    return g.db


def save_to_collection(collection_name, json_doc):
    db = get_db
    collection = db[collection_name]
    the_list = list(collection.find({}))
    id = len(list)

    try:
        collection.insert_one({"_id": id, "jsonDoc": json_doc})
        return 1
    except:
        return 0


def get_latest_from_collection(collection_name):
    db = get_db()
    collection = db[collection_name]
    the_list = list(collection.find({}))

    latest = collection.find_one({"_id": len(the_list)-1 })

    if latest is None:
        return None
    else:
        return latest['jsonDoc']


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()


if __name__ == "__main__":
    create_user_offline('admin', 'password')