from flask import Blueprint
from controllers import create_account

bluePrint = Blueprint('create_account', __name__, template_folder='templates')

@bluePrint.route('/create_account', methods=['GET'])
def main():
	return create_account.show()