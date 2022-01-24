
from flask import Flask, render_template,request,redirect,url_for,flash,send_from_directory

import os

# app = Flask(__name__) # to make the app run without any

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    if name=='not':
        return 'enter the correct Roll number or In case if you participated and still not getting certificate contact the coordinators'



@app.route("/pyt",methods=['GET','POST'])
def pyt():
    if request.method == 'POST':
        user = request.form['nm']
        if user=='' or user==None:
            user='not'
            return redirect(url_for('success', name = user))
        user=user+'.pdf'
        if user not in os.listdir('static/styles/im'):
            user='not'
            return redirect(url_for('success', name = user))
        else:
            return send_from_directory(directory='static',as_attachment=True, filename='styles/im/' +user) 
    else:
        return render_template('pyt.html')

      

@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/tasks")
def tasks():
    return render_template('syllabus.html')
@app.route("/events")
def events():
    return render_template('event.html')


@app.route("/faq")
def faq():
    return render_template('faq.html')
