"""
User DAO (Data Access Object) MONGO
Auteurs : Gabriel Lessard, 2026
"""
import os
from dotenv import load_dotenv
from models.user import User
from pymongo import MongoClient
from bson import ObjectId

class UserDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)
            self.client = MongoClient(
                host=os.getenv("MONGODB_HOST"),
                port=int(os.getenv("MONGODB_PORT")),
                username=os.getenv("MONGO_USER"),
                password=os.getenv("MONGO_PASSWORD"),
                authSource=os.getenv("MONGO_DB")
            )
            self.db = self.client[os.getenv("MONGO_DB")]
            self.collection = self.db.get_collection("users")
            print("Mongo DAO initialized, collection =", self.collection)
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        users = []
        for doc in self.collection.find():
            users.append(
                User(
                    str(doc["_id"]),
                    doc.get("name"),
                    doc.get("email")
                )
            )
        return users

    def insert(self, user):
        """ Insert given user into MongoDB """
        new_user = self.collection.insert_one({
            "name": user.name,
            "email": user.email
        })
        return str(new_user.inserted_id)


    def update(self, user):
        """ Update given user in MongoDB """
        update_user = self.collection.update_one(
            { "_id": ObjectId(user.id) },
            {
                "$set": {
                    "name": user.name,
                    "email": user.email
                }
            }
        )
        return update_user.matched_count == 1


    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        delete_filter = { "_id": ObjectId(user_id) }
        delete_user = self.collection.delete_one(delete_filter)
        return delete_user.deleted_count == 1