from pip._internal import main
from flask import jsonify, make_response

try:
	from flask_sqlalchemy import SQLAlchemy
except:
	main(['install', "Flask_SQLAlchemy==2.5.1"])
	from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# This function will add data to the database
def Add_data_DB(time=None, date=None, temp=0):
	test = createDB(time=time, date=date, temp=temp)
	db.session.add(test)
	db.session.commit()

#-- this function will get all the data from the database
def Get_all_data_from_DB():
	data = createDB.query.all()
	return data

def Test(val):
	return_data_dict = { 
							"id": None,
							"time": None,
							"date": None,
							"temp": None
	}
	return_data = []

	data = createDB.query.filter_by(date=val).all()
	#print(data.date)
	if len(data) != 0:
		for i in range(len(data)):
			return_data_dict['id'] = data[i].id
			return_data_dict['time'] = data[i].time
			return_data_dict['date'] = data[i].date
			return_data_dict['temp'] = data[i].temp

			return_data.append(return_data_dict.copy())
			#print(i, return_data_dict)
		return return_data
	else: 
		return {'message':"data not found"}

# This is the structure of our database. 
class createDB(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.String(30), nullable=False)
	date = db.Column(db.String(30), nullable=False)
	temp = db.Column(db.String(30), nullable=False)
