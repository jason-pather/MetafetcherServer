#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler
from flask import Flask, url_for, json, request, render_template, jsonify
from collections import namedtuple
import urllib2
import json
#import pri

app = Flask(__name__)

counter = 0
data = 'default'

@app.route('/receiver', methods=['POST'])
def receiver():

	global counter
	global data

	if request.headers['Content-Type'] == 'application/json':
		data = 'json'
		counter += 1
		jstr = request.json
		for var in jstr:
			varType = type(var)

		# jstr = request.get_json
		
		# jsonObject = get_json()
		# jsonString = request.data
		#Log = namedtuple('Log', 'dateTimeMillis, contactNumber, durationMillis, isNew, contactName, callType, isRead')
		# info = json.loads(jsonObject)
		# logs = [Log(**k) for k in data["logs]"]]
		return "JSON: counter is "+ str(counter) + " :::: "+ str(type(jstr)) +":::"+str(jstr)+":::"+str(type(varType))
	else:
		return "Content received does not have Content-Type = 'json/application', counter is "+str(counter)

@app.route('/receiver', methods=['GET'])
def other():
	global data
	global counter
	counter += 1
	return "received GET request, counter is " + str(counter) + " data >" + data
