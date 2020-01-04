import re
import jwt
from models import Account

def success():
	return {
		'success' : True
	}

def error(errorCode, message):
	# Default JSON with variable message to map common errors
	return {
		'success' : False,
		'errorMessage': message,
		'errorCode': errorCode
	}


def requestJSON(request):
	# Used to accept both application/x-www-form-urlencoded and application/json requests
	return request.form or request.json


def emailIsValid(emailInput):
	# E-mail validation

	# It must be string
	if type(emailInput) != str:
		return False

	emailRegex = r'[a-zA-Z0-9]+([-+._][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([-.][a-zA-Z0-9]+)*\.[a-zA-Z]{2,4}'

	if not re.match(emailRegex, emailInput):
		return False

	return True


def passwordIsValid(passwordInput):
	# Password validation

	# It must be in string format
	if type(passwordInput) != str:
		return False

	# It must have at least 8 characters, 1 letter, 1 digit and 1 non-alphanumeric
	passwordRegex = r'^(?=.*[a-zA-Z])(?=.*[\d])(?=.*[^\w\s\d])[\w\W\S]{8,}$'

	if not re.match(passwordRegex, passwordInput):
		return False

	return True


def encodeJWT(JSON, secret):
	# Uses jwt library to create a JWT token from dicts

	# It must be a dict
	if type(JSON) != dict:
		return error(7, "Received invalid format when encoding JSON.")

	# jwt returns tokens in bytes, so I decode it to 'utf-8'
	return jwt.encode(JSON, secret, algorithm='HS256').decode('utf-8')


def decodeJWT(JWTToken, secret):
	# Uses jwt library to retrieve JSON from JWT tokens

	# Validates jwt format
	jwtRegex = r'^[\w-=]+\.[\w-=]+\.?[\w-.+/=]*$'

	if not re.match(jwtRegex, JWTToken):
		return error(8, "Received invalid format when decoding JWT token.")

	return jwt.decode(JWTToken, secret, algorithm='HS256')

def movementsValidation(data, secretKey):

	if not all (param in data for param in ("email", "password", "value")):
		return error('Missing email/password/value.')

	email = data['email']

	if emailIsValid(email) != True:
		return error(2, 'Invalid e-mail.') 

	movementValue = data['value']

	if type(movementValue) != int and type(movementValue) != float:
		try:
			movementValue = float(movementValue)
		except:
			return error(9, 'Value must be in number format.')

	if movementValue <= 0:
		return error(10, 'O valor deve ser maior que zero.')

	accountToken = encodeJWT({
		'email': email,
		'password': data['password']
		}, secretKey)

	account = Account.query.filter_by(email=email, password=accountToken).first()

	if not account:
		return error(6, 'Account not found.')

	return {'success': True, 'account': account, 'movementValue': movementValue}