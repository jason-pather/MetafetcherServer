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
global data
data = 'default'

@app.route('/receiver', methods=['POST'])
def receiver():

	global counter

	if request.headers['Content-Type'] == 'text/plain':
		data = request.data
		return "Text Message: counter is "+ str(counter)
	else:
		return "Content received does not have Content-Type = 'text/plain', counter is "+str(counter)

@app.route('/receiver', methods=['GET'])
def other():
	global data
	return "received GET request, counter is " + str(counter) + " data >" + data
