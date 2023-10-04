from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_driver(self, nota: int, corridas: int):
        try:
            res = self.db.collection.insert_one({"nota": nota, "corridas": corridas})
            print(f"Driver created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating driver: {e}")
            return None

    def read_driver_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Driver found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading driver: {e}")
            return None

    def update_driver(self, id: str, nota: int, corridas: int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": nota, "corridas": corridas}})
            print(f"driver updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating driver: {e}")
            return None

    def delete_driver(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"driver deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting driver: {e}")
            return None