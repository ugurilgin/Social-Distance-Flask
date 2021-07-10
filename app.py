from SocialDistanceDetector import SocialDistance
import json
from flask import Flask
from flask import request ,jsonify
from flask import render_template,redirect,url_for
import os
#import mysql.connector
############## </ Import Files > ##############
app=Flask(__name__,template_folder='templates')
app.secret_key=os.urandom(24)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
