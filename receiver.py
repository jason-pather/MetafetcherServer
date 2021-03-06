#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler
from flask import Flask, url_for, json, request, render_template, jsonify
from collections import namedtuple
from flask.ext.sqlalchemy import SQLAlchemy
import urllib2
import json
import os
import psycopg2
import urlparse
#import pri

app = Flask(__name__)
# heroku pg:psql
# db name: deu22ov7a7ojk6

counter = 0
data = 'default'
connected = False
db = None
cur = None
# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

# postgres://lktnxhpcfqcgqn:u20nbLpjDVw9t8I32vGeZFtJ_s@ec2-54-204-44-31.compute-1.amazonaws.com:5432/deu22ov7a7ojk6



def storeCallLog(callLog):
	global cur
	# query = "SELECT * from calllogs;"
	# query = "INSERT INTO calllogs VALUES (\'calltype\', \'name\', 100, 100, true, false, \'contactNo\', \'callType\');"
	# cur.execute(query)
	# conn.close()
	return "call Log"

def storeTextLog(callLog):
	return "text log"

def connectToDB():
	global connected
	global app
	global db
	global cur
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ['DATABASE_URL'])
	conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname))
	cur = conn.cursor()
	query = "INSERT INTO fake VALUES (\'calltype\', \'name\', 100, 100, true, false, \'contactNo\', \'callType\');"
	cur.execute(query)
	conn.close()
	return "connected to db"


	# conn = psycopg2.connect(
	#     database=url.path[1:],
	#     user=url.username,
	#     password=url.password,
	#     host=url.hostname,
	#     port=url.port
	# )
	# db = SQLAlchemy(app)

	connected = True


@app.route('/receiver', methods=['POST'])
def receiver():

	global counter
	global data
	global connected


	return connectToDB()

	if (request.headers['Content-Type'] == 'application/json'):
		# jsonList is list, jsonObjectDict is dict
		jsonList = request.json
		for jsonObject in jsonList:
			jsonObjectDict = json.loads(jsonObject)
			if jsonObjectDict.get("type") == "call":
				return storeCallLog(jsonObjectDict)
			elif jsonObjectDict.get("type") == "text":
				return storeTextLog(jsonObjectDict)


@app.route('/receiver', methods=['GET'])
def other():
	global data
	global counter
	counter += 1
	return "received GET request, counter is " + str(counter) + " data >" + data



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
