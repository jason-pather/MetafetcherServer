#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler
from flask import Flask, url_for
from flask import json
from flask import request
#import pri

app = Flask(__name__)

global counter = 0;

@app.route('/receiver', methods=['POST'])
def receiver():

	if request.headers['Content-Type'] == 'text/plain':
		counter++;
		return "text received, counter is "+counter
	else:
		counter++;
		return "other, counter is "+counter

@app.route('/receiver', methods=['GET'])
def other():
	return "received GET request, counter is "+counter
