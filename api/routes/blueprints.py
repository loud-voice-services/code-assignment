from routes import create, info, movements

def register(app):
	app.register_blueprint(create.bluePrint)
	app.register_blueprint(movements.bluePrint)
	app.register_blueprint(info.bluePrint)