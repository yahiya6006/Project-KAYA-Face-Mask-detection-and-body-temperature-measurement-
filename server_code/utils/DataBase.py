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

# This is the structure of our database. 
class createDB(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.String(30), nullable=False)
	date = db.Column(db.String(30), nullable=False)
	temp = db.Column(db.Float, nullable=False)