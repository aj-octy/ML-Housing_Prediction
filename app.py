# from crypt import methods
from housing.logger import logging
from flask import Flask
import sys
from housing.exception import HousingException


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
	try:
		raise Exception("test exception")
	except Exception as e:
		housing = HousingException(e,sys)
		logging.info(housing.error_message)
		logging.info("we are testing loggong module")
	return "hola"

if __name__ =="__main__":
	app.run(debug=True)
