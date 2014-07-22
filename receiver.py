#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler
from flask import Flask, url_for
from flask import json
from flask import request
from flask import render_template, jsonify
from collections import namedtuple
#import pri

app = Flask(__name__)

counter = 0
data = 'default'

@app.route('/receiver', methods=['POST'])
def receiver():

	global counter
	global data

	if request.headers['Content-Type'] == 'text/plain':
		data = request.data
		counter += 1
		return "Text/plain Message: counter is "+ str(counter)
	elif request.headers['Content-Type'] == 'application/json':
		data = 'json'
		counter += 1
		jsonObject = get_json()
		jsonString = request.data
		#Log = namedtuple('Log', 'dateTimeMillis, contactNumber, durationMillis, isNew, contactName, callType, isRead')
		# info = json.loads()
		#logs = [Log(**k) for k in data["logs]"]]
		return "JSON: counter is "+ str(counter) + " data:"
	else:
		return "Content received does not have Content-Type = 'text/plain', counter is "+str(counter)

@app.route('/receiver', methods=['GET'])
def other():
	global data
	global counter
	counter += 1
	return "received GET request, counter is " + str(counter) + " data >" + data
