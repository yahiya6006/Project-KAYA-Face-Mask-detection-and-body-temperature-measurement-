from flask_restful import Api, Resource, fields, marshal_with, reqparse
from utils.DataBase import db, Get_all_data_from_DB, Add_data_DB
from flask import request, jsonify

#-- These are the fields that our database recquires
Resource_fields = {
	'id': fields.Integer,
	'time': fields.String,
	'date': fields.String,
	'temp': fields.Float
}

#-- We are checking if user has sent or provided all the recquired fields
AddData_post_args = reqparse.RequestParser()
AddData_post_args.add_argument("time", type=str, help='You have not sent "time":type - string', required=True)
AddData_post_args.add_argument("date", type=str, help='You have not sent "date":type - string', required=True)
AddData_post_args.add_argument("temp", type=float, help='You have not sent "temp":type - float', required=True)

#-- This class is used to get the Analytics
class Analytics(Resource):
	@marshal_with(Resource_fields)
	def get(self):
		data = Get_all_data_from_DB()
		return data

#-- this class will add data to the database
class AddData(Resource):
	def post(self):
		args = AddData_post_args.parse_args()
		Add_data_DB(args['time'], args['date'], args['temp'])
		return args