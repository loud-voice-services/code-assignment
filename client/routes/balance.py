from flask import Blueprint
from controllers import balance

bluePrint = Blueprint('balance', __name__, template_folder='templates')

@bluePrint.route('/balance', methods=['GET'])
def main():
	return balance.show()