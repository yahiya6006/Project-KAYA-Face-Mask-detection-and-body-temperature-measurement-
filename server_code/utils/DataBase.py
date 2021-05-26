from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createDB():
	db.create_all()
	print('[INFO] "ServerData.db" was created inside directory "DataBase"')