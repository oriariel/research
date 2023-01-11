# Here, we import the forms, since they are used for routing.
# We also add routing to the registration and the login pages.

import json
from flask import Flask, render_template, request
from flask import render_template, url_for, flash, redirect, send_file
from flask_example import app
from distutils.log import debug
from fileinput import filename
from flask import request
import sys
import os, pathlib
from algorithm1 import algorithm1,Course,Student,random,TabuList,copy,map_price_demand,reset_update_prices,cmp_to_key,reset_students,time
from json_algo import load_from_json_algorithm1,load_from_json_algorithm2,load_from_json_algorithm3

@app.route('/')
def myhome():
     return render_template('home.html', 
        username = myhome.username, 
         file=myhome.file
         )
myhome.username = "Guest" #Global variable
myhome.file = None

@app.route('/upload1')
def upload_file_algo1():
  return render_template('upload1.html')
	
@app.route('/uploader1', methods = ['GET', 'POST'])
def uploaded_file_algo1():
  if request.method == 'POST':
      f = request.files['file']
      f.save((f.filename))
      st = str(f.filename)
      file = open(f.filename, 'r')
      file_contents = file.read()
      ans = (file_contents)
      file.close()
      json_algo_ans = load_from_json_algorithm1(st)
      results = "Input:"+'\n'+ ans + '\n' + json_algo_ans
      return (results)

@app.route('/upload2')
def upload_file_algo2():
   return render_template('upload2.html')
	
@app.route('/uploader2', methods = ['GET', 'POST'])
def uploaded_file_algo2():
   if request.method == 'POST':
      f = request.files['file']
      f.save((f.filename))
      st = str(f.filename)
      file = open(f.filename, 'r')
      file_contents = file.read()
      ans = (file_contents)
      file.close()
      json_algo_ans = load_from_json_algorithm2(st)
      results = "Input:"+'\n'+ ans + '\n' + json_algo_ans
      return (results)
    
@app.route('/upload3')
def upload_file_algo3():
   return render_template('upload3.html')
	
@app.route('/uploader3', methods = ['GET', 'POST'])
def uploaded_file_algo3():
   if request.method == 'POST':
      f = request.files['file']
      f.save((f.filename))
      st = str(f.filename)
      print(load_from_json_algorithm3(st)[1])
      return load_from_json_algorithm3(st)