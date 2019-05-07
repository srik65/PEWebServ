from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import models

db.create_all()
db.session.commit()

if app.debug:
  if not os.path.exists('logs'):
    os.mkdir('logs')
  file_handler = RotatingFileHandler('logs/tests.log', maxBytes=10240, backupCount=10)
  file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
  file_handler.setLevel(logging.INFO)
  app.logger.addHandler(file_handler)

  app.logger.setLevel(logging.INFO)
  app.logger.info("Srik Test Startup!!")


from app import routes
