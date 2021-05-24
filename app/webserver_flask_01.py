#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Web App
Purpose: Template Flask with Bootstrap navbar
Version: 01/2021 Roboball 
"""
from flask import Flask, render_template, url_for, flash, redirect
# from markupsafe import escape # not necessary for render_template()
import sys
import json

app = Flask(__name__)

# init routes
# @app.route('/')
# def index():
#     # post = {'title': 'Friend'}
#     # post = "Friend"
#     post = 3333
#     # post = json.dumps(post)
#     # html = "<h1>Hello!!</h1>"
#     # html = render_template('index_01.html')
#     html = render_template('bootstrap_02.html', posts=post)
#     # html = render_template('index_01.html', posts=post)
#     return html


@app.route("/")
def view_home():
    return render_template("bootstrap_03.html", title="Home page")

@app.route("/first")
def view_first_page():
    return render_template("bootstrap_03.html", title="First page")

@app.route("/second")
def view_second_page():
    return render_template("bootstrap_03.html", title="Second page")

# init globals
IP = '0.0.0.0' # localhost
PORT = 9999 # set custom port

if __name__ == '__main__':  
    app.run(debug=True, host=IP) # http://localhost:5000/
    

    # without debugging
    # app.run(threaded=True, debug=False,use_debugger=False,use_reloader=False, host=IP,port= PORT) # http://192.168.1.126:9999/

    # https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https
    # app.run(debug=False,use_debugger=False,use_reloader=False,ssl_context='adhoc', host=IP,port= PORT) # https://192.168.1.126:9999/
    # for deployment:
    # from waitress import serve (https does not work)
    # serve(app, url_scheme='https', host=IP, port=8080) # http://192.168.1.126:8080/

    # gunicorn production server
    # https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04


    #################### Tutorials
    # flask, 3d js
    # https://www.cedwards.info/projects/japanvis/#DataVis

    # https://branetheory.org/2014/12/18/data-visualization-using-d3-js-and-flask/

    # https://www.reddit.com/r/flask/comments/4emd2c/learning_how_to_build_a_web_application_with/

    # https://medium.com/@rchang/learning-how-to-build-a-web-application-c5499bd15c8f#.bdph6phki
    # http://bl.ocks.org/anonymous/7ac8ca5bd97724e51fc5a845a3ca6c97