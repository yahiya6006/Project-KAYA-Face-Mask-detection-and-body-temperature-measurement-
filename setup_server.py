from pip._internal import main

packages = ['Flask==2.0.0',
		    'Flask_RESTful==0.3.9',
		    'Flask_SQLAlchemy==2.5.1'
		   ]

for package in packages:
    main(['install', package])
     
