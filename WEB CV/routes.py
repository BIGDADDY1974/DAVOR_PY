from flask import Flask, url_for, request, render_template;
from app import app;
import redis;
r = redis.StrictRedis('localhost',6379,0,charset="UTF-8",decode_responses=True);

@app.route('/')
def hello():
    return render_template("index.html")
