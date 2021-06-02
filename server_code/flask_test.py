from flask import Flask
from flask_restful import Api
from utils.DataBase import db, createDB
from utils.SetUP import SETUP
import os
from utils.REST_Methods import Analytics, AddData

# set up the directory
SETUP()

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase/ServerData.db'

db.init_app(app)

if not os.path.exists('DataBase/ServerData.db'):
    with app.app_context():
        db.create_all()
        print('[INFO] "ServerData.db" was created inside directory "DataBase"')


api.add_resource(Analytics, "/view/All-database")
api.add_resource(AddData, "/addData")

if __name__ == "__main__":
    app.run(debug=True)
