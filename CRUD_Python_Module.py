# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId

import json

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    # Adjustments for Module 5+ authentication, Travis W.
    def __init__(self, USER = None, PASS = None): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        if USER is None:
            USER = 'aacuser' 
        if PASS is None:
            PASS = 'password1' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    def nextRecord(self):
        return ++self.database.animals.count_documents({}) # next rec_num is number of documents + 1
        
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None:
            data['rec_num'] = self.nextRecord() # add rec_num key value pair, or update to actual next rec_num
            result = self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else: 
            return False

    # Create method to implement the R in CRUD.
    # Updated per module 4 feedback
    def fetch_all(self, params):
        result = list()
        if params is not None:
            cursor = self.database.animals.find(params)
            for document in cursor:
                result.append(document)
        return result
    
    # Update documents matching provided key, value pairs
    def update(self, data, update):
        if data is not None:
            result = self.database.animals.update_many(data,update)
            return result.modified_count
        return 0
    
    # Delete documents matching provided key,  value pairs
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            return result.deleted_count
        return 0
    
    
    

        