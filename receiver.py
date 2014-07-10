#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler
from flask import Flask, url_for
from flask import json
from flask import request
#import pri

app = Flask(__name__)

counter = 0

@app.route('/receiver', methods=['POST'])
def receiver():

	global counter
	global typeOf
	counter+=1;
	typeOf = 'default'

	if request.headers['Content-Type'] == 'text/plain':
		typeOf = 'textplain'
		return "Text Message: counter is "+ str(counter)+ " last type: "+str(typeOf)
	elif request.headers['Content-Type'] == 'application/json':
		typeOf = 'json'
		return "JSON Message: counter is "+ str(counter)+ " last type: "+str(typeOf)
	else:
		typeOf = 'unknown'
		return "unknown type, counter is "+str(counter)+ "last type: "+ str(typeOf)

@app.route('/receiver', methods=['GET'])
def other():
	return "received GET request, counter is " + str(counter)
