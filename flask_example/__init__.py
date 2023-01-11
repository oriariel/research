# Here, we add a secret key:

from flask import Flask, render_template
from json_algo import load_from_json_algorithm1


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ecf6e975838a2f7bf3c5dbe7d55ebe5b'  ###
#app.config['UPLOAD_FOLDER'] = "C:\Users\oriar\Desktop\research-5783\11-python-web\code\7.upload\flask_example"
#app.config['MAX_CONTENT_PATH'] = 

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
# db = SQLAlchemy(app)

from flask_example import routes
from algorithm1 import algorithm1,Course,Student,random,TabuList,copy,map_price_demand,reset_update_prices,cmp_to_key,reset_students,time
