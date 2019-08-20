import os
import pymongo
from datetime import datetime
from bson.decimal128 import Decimal128
import hashlib
from swagger_server.models.user import User as userModel
from swagger_server.models.order import Order as orderModel

URI = os.getenv('MONGO_URI', "mongodb://127.0.0.1:27017")


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def get_database(URI=URI):
    try:
        mongo = pymongo.MongoClient(URI)
        return mongo.database
    except:
        return 'Error connecting to database.'


class Operation:
    def __init__(self, email, value, date, op_type, balance):
        self.email = email
        self.value = value
        self.date = date
        self.op_type = op_type
        self.balance = balance

    def to_dict(self):
        return {
            'email': self.email,
            'value': str(self.value.to_decimal()),
            'date': str(datetime.fromtimestamp(self.date).strftime("%m/%d/%Y, %H:%M:%S")),
            'type': self.op_type,
            'balance': str(self.balance.to_decimal())
        }


class dboperations:
    def __init__(self, URI=URI):
        self.databse = get_database(URI)
        self.users_collection = self.databse.users
        self.operations_collection = self.databse.operations

    def insert_operation(self, operation):
        return self.operations_collection.insert_one(operation)

    def insert_user(self, user):
        finded = self.users_collection.find_one({"email": user.email})
        if (finded != None):
            return 'usuario ja cadastrado'
        self.users_collection.insert_one({
            "email": user.email,
            "password": user.password,
            "sha": user.sha
        })
        return 'ok'

    def login(self, user):
        finded = self.users_collection.find_one({"email": user.email})
        if (finded != None and finded['email'] == user.email and finded['password'] == user.password):
            return finded['sha']

    def register_user(self, user):
        user_sha = encrypt_string(user.email+user.password)
        user.sha = user_sha
        return (self.insert_user(user), user_sha)

    def deposit(self, email, value):
        last_op = self.get_last_operation(email)
        dep = {
            'email': email,
            'value': Decimal128(value),
            'date': datetime.timestamp(datetime.now()),
            'type': 'Deposit',
            'balance': Decimal128(last_op.balance.to_decimal()+Decimal128(value).to_decimal())
        }

        insert = self.insert_operation(dep)
        return 'deposit successful'

    def withdraw(self, email, value):
        last_op = self.get_last_operation(email)
        new_balance = Decimal128(
            last_op.balance.to_decimal()-Decimal128(value).to_decimal())
        wit = {
            'email': email,
            'value': Decimal128(value),
            'date': datetime.timestamp(datetime.now()),
            'type': 'Withdraw',
            'balance': new_balance
        }

        insert = self.insert_operation(wit)
        return 'withdraw successful'

    def balance(self, email):
        return str(self.get_last_operation(email).balance.to_decimal())

    def get_sha(self, user):
        finded = self.users_collection.find_one({"email": user.email})
        if (finded != None):
            return finded['sha']
        return finded

    def get_email_by_sha(self, sha):
        finded = self.users_collection.find_one({"sha": sha})
        if (finded != None):
            return finded['email']
        return finded

    def get_last_operation(self, email):
        finded = self.operations_collection.find_one(
            {"email": email}, sort=[("date", pymongo.DESCENDING)])
        if(finded != None):
            return Operation(finded['email'], finded['value'], finded['date'], finded['type'], finded['balance'])
        else:
            return Operation(email, Decimal128('0'), datetime.timestamp(datetime.now()), 'Initial  balance', Decimal128('0'))

    def get_history(self, email, from_date, to_date):
        from_timestamp = datetime.timestamp(from_date)
        to_timestamp = datetime.timestamp(to_date)
        finded = self.operations_collection.find(
            {"email": email, "date": {"$gte": from_timestamp, "$lte": to_timestamp}}, sort=[("date", pymongo.DESCENDING)])
        operation_list = []
        for oper in finded:
            operation_list.append(Operation(
                oper['email'], oper['value'], oper['date'], oper['type'], oper['balance']).to_dict())
        return operation_list