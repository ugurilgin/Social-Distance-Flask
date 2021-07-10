from SocialDistanceDetector import SocialDistance
import json
from flask import Flask
from flask import request ,jsonify,Response
from flask import render_template,redirect,url_for
import os
import json
app=Flask(__name__,template_folder='templates')
app.secret_key=os.urandom(24)
header=["Sultanbeyli","Esenler","Uskudar","Zeytinburnu","Kcekmece","Ortakoy"]
file = open('mobese.json',) 
data = json.load(file)
file.close()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/city')
def city():
    global header
    cities=[]
    global data
    for head in header:
        rows=[data[head]["id"],data[head]["name"],data[head]["link"],data[head]["img"]]
        cities.append(rows)
    return render_template('city.html',cities=cities,color="color")
@app.route('/detectCity' ,defaults={'city':'default'})
@app.route('/detectCity/<city>')
def detectCity(city):
    global header
    global data
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
    return render_template("detectCity.html",cities=cities,cityname=cityname,color="color",imglink=cityimg,link=link)
@app.route('/streamVideo' ,defaults={'video':'default'})
@app.route('/streamVideo/<video>')
def streamVideo(video):
    global header
    global data
    if video in header:
        link=data[video]["link"]
        socialDistance=SocialDistance(link)
    else:
        return redirect(url_for('city'))
    return Response(socialDistance.Detect(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=False)
