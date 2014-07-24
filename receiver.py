#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler
from flask import Flask, url_for, json, request, render_template, jsonify
from collections import namedtuple
import urllib2
import json
import os
import psycopg2
import urlparse
#import pri

app = Flask(__name__)
# heroku pg:psql

counter = 0
data = 'default'
# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )



def storeCallLog(callLog):
	return "call Log"

def storeTextLog(callLog):
	arg = "r"


@app.route('/receiver', methods=['POST'])
def receiver():

	global counter
	global data

	if (request.headers['Content-Type'] == 'application/json'):
		# jsonList is list, jsonObjectDict is dict
		jsonList = request.json
		for jsonObject in jsonList:
			jsonObjectDict = json.loads(jsonObject)
			if jsonObjectDict.get("type") == "call":
				storeCallLog(jsonObjectDict)
			elif jsonObjectDict.get("type") == "text":
				storeTextLog(jsonObjectDict)


@app.route('/receiver', methods=['GET'])
def other():
	global data
	global counter
	counter += 1
	return "received GET request, counter is " + str(counter) + " data >" + data

# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL]")

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )





# if request.headers['Content-Type'] == 'application/json':
	# 	data = 'json'
	# 	counter += 1
	# 	jstr = request.json
	# 	for var in jstr:
	# 		varType = type(var)
	# 		info = json.loads(var)

	# 	# jstr = request.get_json
		
	# 	# jsonObject = get_json()
	# 	# jsonString = request.data
	# 	#Log = namedtuple('Log', 'dateTimeMillis, contactNumber, durationMillis, isNew, contactName, callType, isRead')
	# 	# info = json.loads(jsonObject)
	# 	# logs = [Log(**k) for k in data["logs]"]]
	# 	return "JSON: counter is "+ str(counter) + " :::: "+ str(type(jstr)) +":::"+str(jstr)+":::"+str(varType)+":::"+str(type(info))
	# else:
	# 	return "Content received does not have Content-Type = 'json/application', counter is "+str(counter)
