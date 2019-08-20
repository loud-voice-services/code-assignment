from flask import Flask
import swagger_server
import time
import connexion
from pymongo import MongoClient
from swagger_server import encoder
from swagger_server.models.order import Order
from dboperations import dboperations
from swagger_server.models.user import User as userModel


def basic_auth(key, required_scopes=None):
    user_email = dboperations().get_email_by_sha(key)
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())
        if(body.email == user_email):
            return {'sub': 'operation'}
    return None


class base_api:
    def __init__(self, database):
        self.swagger_file = './swagger.yaml'
        self.app = connexion.App(__name__, specification_dir='./')
        self.app.app.json_encoder = encoder.JSONEncoder
        self.app.add_api(self.swagger_file, arguments={'title': 'Bank API'})
        self.database = database

    def get_api(self):
        return self.app


if __name__ == "__main__":
    api.app.run(host='0.0.0.0')
else:
    api = base_api(dboperations())
