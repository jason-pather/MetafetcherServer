#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler
from flask import Flask
#import pri

app = Flask(__name__)

@app.route('/receiver', methods=['POST'])
def receiver():

	return 'receiver got post'
