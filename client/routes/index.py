from flask import Blueprint
from controllers import index

bluePrint = Blueprint('index', __name__, template_folder='templates')

@bluePrint.route('/', methods=['GET'])
def main():
	return index.show()