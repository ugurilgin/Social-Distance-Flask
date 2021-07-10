from SocialDistanceDetector import SocialDistance
import json
from flask import Flask
from flask import request ,jsonify
from flask import render_template,redirect,url_for
import os
import json
app=Flask(__name__,template_folder='templates')
app.secret_key=os.urandom(24)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/city')
def city():
    header=["Sultanbeyli","Esenler","Uskudar","Zeytinburnu","Kcekmece","Ortakoy"]
    cities=[]
    file = open('mobese.json',) 
    data = json.load(file)
    for head in header:
        rows=[data[head]["id"],data[head]["name"],data[head]["link"],data[head]["img"]]
        cities.append(rows)
    file.close()
    return render_template('city.html',cities=cities,color="color")
@app.route('/detectCity' ,defaults={'city':'default'})
@app.route('/detectCity/<city>')
def detectCity(city):
    header=["Sultanbeyli","Esenler","Uskudar","Zeytinburnu","Kcekmece","Ortakoy"]
    file = open('mobese.json',) 
    data = json.load(file)
    cities=[]
    link=""
    if city in header:
        link=data[city]["link"]
        cityname=data[city]["name"]
        cityimg=data[city]["img"]
        for head in header:
            if data[head]["name"] !=city:
                rows=[data[head]["id"],data[head]["name"],data[head]["link"],data[head]["img"]]
                cities.append(rows)
    else:
        return redirect(url_for('city'))
    return render_template("detectCity.html",cities=cities,cityname=cityname,color="color",imglink=cityimg)
    file.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
