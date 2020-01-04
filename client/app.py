from flask import Flask
from routes import index, create_account, balance

app = Flask(__name__)

app.app_context().push()

app.register_blueprint(index.bluePrint)
app.register_blueprint(create_account.bluePrint)
app.register_blueprint(balance.bluePrint)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)