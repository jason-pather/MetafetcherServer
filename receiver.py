#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler
from flask import Flask
from flask import json
#import pri

app = Flask(__name__)

@app.route('/receiver', methods=['POST'])
def receiver():

	if request.headers['Content-Type'] == 'text/plain':
		return "text received"
	else:
		return "other"

@app.route('/receiver', methods=['GET'])
def other():
	return "received GET request"
