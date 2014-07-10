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
	if request.headers['Content-Type'] == 'text/plain':
		counter+=1
		return "text received, counter is "+ str(counter)
	else:
		counter+=1
		return "other, counter is "+ str(counter)

@app.route('/receiver', methods=['GET'])
def other():
	return "received GET request, counter is " + str(counter)
