import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    from pkg.models import db
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile("config.py",silent=True)


   
    db.init_app(app)
    csrf.init_app(app)
    migrate = Migrate(app,db)
    return app

app = create_app()
from pkg import user_routes,admin
from pkg import *