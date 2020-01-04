from flask import Blueprint
from controllers import info

bluePrint = Blueprint('info', __name__)

@bluePrint.route('/all_accounts', methods=['GET'])
def get_all_acounts():
	return info.all_accounts()

@bluePrint.route('/account_info', methods=['POST'])
def account_info():
	return info.account()