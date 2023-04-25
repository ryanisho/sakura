"""
Created by: Ryan Ho
Date: October 15th, 2022

Project Name: Sakura
Language/Framework: Python/Flask

Description:
Created apart of the 2022 Big Red Hacks Hackathon for Cornell University.
This program uses the machine learning API, openAI, to generate, debug, and explain Python code.

Contact:
Ryan Ho (rh564@cornell.edu)
"""

#Import modules
import os
from flask import Flask, redirect, render_template, request, url_for
from request import *


#Initiate flask app and integrate API source key
app = Flask(__name__)

#Define route for home index
@app.route("/")
def index():
    return render_template("index.html")

#Define route for search index, call API with python code parameters.
@app.route("/search", methods=("GET", "POST"))
def search():
    if request.method == "POST":
        input = request.form.get('input')
        response = searchCustom(input)
        # return redirect(url_for("search", result=response.choices[0].text))
        return redirect(url_for("search", result=response))

    result = request.args.get("result")
    return render_template("search.html", result=result)

#Create route for debug, call API with text-engine to debug Python code
@app.route("/debug", methods=("GET", "POST"))
def debug():
    if request.method == "POST":
        input = request.form.get("input")
        response = debugCustom(input)
        return redirect(url_for("debug", result=response))

    result = request.args.get("result")
    return render_template("debug.html", result=result)

#Create route natural language, and call API for natural language explanation
@app.route("/ntrlang", methods=("GET", "POST"))
def ntrlang():
    if request.method == "POST":
        input = request.form.get('input')
        response = ntrCustom(input)
        return redirect(url_for("ntrlang", result=response))

    result = request.args.get("result")
    return render_template("ntrlang.html", result=result)

#Enable debug mode for development purposes
app.run(debug=True)
