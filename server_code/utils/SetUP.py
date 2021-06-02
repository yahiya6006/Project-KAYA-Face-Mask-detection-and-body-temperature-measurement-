# this program is used for initial setup of the file directory

import os

def SETUP():
	cur_path = os.getcwd()

	if not (os.path.exists(cur_path+'/DataBase')):
		print('-'*50)
		print('folder DataBase does not exist in your current working directory')
		print('[INFO] Creating directory "DataBase"')
		os.mkdir("DataBase")
		print('-'*50)