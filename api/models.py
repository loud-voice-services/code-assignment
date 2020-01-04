from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Init database
db = SQLAlchemy()

# Database model
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(30))
    balance = db.Column(db.Float, default=0.0)
    date_created = db.Column(db.DateTime, default=datetime.now)
    date_updated = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, email, password):
        self.email = email
        self.password = password


ma = Marshmallow()

# Account schema
class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'balance', 'date_created', 'date_updated')

# Initialize schema
account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)