import pip

packages = ['Flask==2.0.0',
		    'Flask-RESTful==0.3.9',
		    'Flask-SQLAlchemy==2.5.1'
		   ]

for package in packages:
	pip.main(['install'], package)
