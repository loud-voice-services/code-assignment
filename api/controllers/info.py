from flask import jsonify, request
from models import *
from config import JWT_SECRET_KEY
from helpers import requestJSON, error, encodeJWT, emailIsValid


def all_accounts():

	allAccounts = Account.query.all()

	result = accounts_schema.dump(allAccounts)

	if len(result) == 0:
		return error(5, 'No accounts found.')

	return jsonify(result)



def account():

	data = requestJSON(request)

	if not all (param in data for param in ("email", "password")):
		return error('Missing email/password.')

	email = data['email']

	if not emailIsValid(email):
		return error(2, 'Invalid e-mail.')

	accountToken = encodeJWT({
		'email': email,
		'password' : data['password']
		}, JWT_SECRET_KEY)

	account = Account.query.filter_by(email=email, password=accountToken).first()

	if not account:
		return error(6, 'Account not found.')

	return account_schema.jsonify(account)