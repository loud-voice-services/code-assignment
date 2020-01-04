from flask import Blueprint
from controllers import create

bluePrint = Blueprint('create_account', __name__)

@bluePrint.route('/create', methods=['POST'])
def create_account():
	return create.create()
