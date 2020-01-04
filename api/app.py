from flask import Flask
from flask_cors import CORS
from models import db
from routes import blueprints

app = Flask(__name__)

app.config.from_pyfile('config.py')

app.app_context().push()

blueprints.register(app)

# CORS allows cross-origin requests
CORS(app)

# Inserts db into the app
db.init_app(app)
# Creates the database tables
db.create_all()


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)