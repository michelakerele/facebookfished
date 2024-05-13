from flask import render_template,request,abort,redirect,flash,make_response,session,url_for,send_file
from werkzeug.security import generate_password_hash,check_password_hash
import os
from sqlalchemy import func
#local Imports
from functools import wraps
from pkg.models import db,User,Admin

from pkg import app,csrf
from flask import flash

@app.route("/", methods=['POST','GET'])
def home():
    if request.method == "POST":
        uname = request.form.get("fname")
        passwrd = request.form.get("pwd")
        info = User(username=uname,password=passwrd)
        db.session.add(info)
        db.session.commit()
    else:
        pass

    return render_template("user/index.html")
