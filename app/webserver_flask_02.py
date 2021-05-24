#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Web App
Purpose: Template Flask with Bootstrap navbar
Version: 01/2021 Roboball 
"""
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
def view_home():
    return render_template("bootstrap_01.html", title="Home page")

@app.route("/first")
def view_first_page():
    return render_template("bootstrap_01.html", title="First page")

@app.route("/second")
def view_second_page():
    return render_template("bootstrap_01.html", title="Second page")

# init globals
IP = '0.0.0.0' # localhost
PORT = 5000 # set custom port

if __name__ == '__main__':  
    app.run(debug=True, host=IP,port= PORT) # http://localhost:5000/
    