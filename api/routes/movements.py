from flask import Blueprint
from controllers import movements

bluePrint = Blueprint('movements', __name__)

@bluePrint.route('/deposit_money', methods=['POST'])
def deposit_money():
	return movements.deposit()

@bluePrint.route('/withdraw_money', methods=['POST'])
def withdraw_money():
	return movements.withdraw()