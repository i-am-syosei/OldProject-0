from flask import Flask
from flask import render_template
from redis import Redis, RedisError
from flask_socketio import SocketIO
import os
import socket

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__,static_folder='./static')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/solo')
def solo():
    return render_template('solo.html')

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/enter")
def enter():
    return render_template("enter.html")

@app.route("/match")
def match():
    return render_template("match.html")

@app.route("/online")
def online():
    return render_template("online.html")

@app.route("/waitingRoom")
def waite():
    return render_template("waitingRoom.html")

@app.route("/soloresult")
def soloresult():
    return render_template("soloresult.html")

@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
        
	app.run(host='0.0.0.0', port=80)
        
