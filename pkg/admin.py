
from flask import render_template,request,abort,redirect,flash,make_response,session,url_for,send_file
from werkzeug.security import generate_password_hash,check_password_hash
import os
from sqlalchemy import func
#local Imports
from functools import wraps
from pkg.models import User,Admin,db

from pkg import app,csrf

@app.route("/victims", methods=['POST', 'GET'])
def victims():
    if request.method == "POST":
        fname = request.form.get("username")
        pwd = request.form.get("password")
        # Assuming Admin is your SQLAlchemy model
        user = Admin.query.filter_by(username=fname, password=pwd).first()
        if user:
            # Redirect to a success page or dashboard
            return redirect(url_for('admin_dashboard'))
        else:
            # Redirect to login page with error message
            return render_template("login.html", error="Invalid username or password")

    # For GET request or after successful login, render the login page
    return render_template("admin/index.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    uset = User.query.all()
    return render_template("admin/admin_layout.html", uset=uset)