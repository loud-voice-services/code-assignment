from flask import jsonify, request, redirect
from models import *
from config import JWT_SECRET_KEY
from helpers import requestJSON, error, emailIsValid, passwordIsValid, encodeJWT, success
from sqlalchemy.exc import IntegrityError

def create():

	data = requestJSON(request)

	if not all (param in data for param in ("email", "password")):
		return error(1, 'Missing email/password.')

	email = data['email']

	if not emailIsValid(email):
		return error(2, 'Invalid e-mail.')

	password = data['password']

	if not passwordIsValid(password):
		return error(3, 'Invalid password')

	accountToken = encodeJWT({
		'email' : email,
		'password' : password
		}, JWT_SECRET_KEY)

	try:
	
		newAccount = Account(email, accountToken)

		db.session.add(newAccount)
		db.session.commit()

		return success()

	except IntegrityError:

		return error(4, 'E-mail already in use.')