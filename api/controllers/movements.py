from flask import jsonify, request, make_response
from models import db
from config import JWT_SECRET_KEY
from helpers import requestJSON, movementsValidation, error, success
from datetime import datetime


def deposit():

	data = requestJSON(request)

	depositPrep = movementsValidation(data, JWT_SECRET_KEY)

	if depositPrep['success'] != True:
		return depositPrep

	depositValue = depositPrep['movementValue']

	account = depositPrep['account']

	account.balance += depositValue
	account.date_updated = datetime.now()

	db.session.commit()

	return success()


def withdraw():

	data = requestJSON(request)

	withdrawalPrep = movementsValidation(data, JWT_SECRET_KEY)

	if withdrawalPrep['success'] != True:
		return withdrawalPrep

	account = withdrawalPrep['account']
	withdrawalValue = withdrawalPrep['movementValue']

	if withdrawalValue > account.balance:
		return error(11, 'Not enough money.')

	account.balance -= withdrawalValue
	account.date_updated = datetime.now()
	
	db.session.commit()

	return success()
