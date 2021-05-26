from flask import Flask
from flask_restful import Api, Resource
from utils.DataBase import db, createDB
from utils.SetUP import SETUP
import os
from utils.test import Akhilesh_get

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


api.add_resource(Akhilesh_get, "/")


if __name__ == "__main__":
    app.run(debug=True)
