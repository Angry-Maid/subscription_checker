import os
from pathlib import Path

from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.') / '.flaskenv')


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SECRET_KEY = os.getenv('SECRET_KEY') or 'default'
    LOCAL_CURRENCY = os.getenv('LOCAL_CURRENCY') or 'USD'
    SYMBOLS = os.getenv('SYMBOLS') or 'USD,EUR'
    API_KEY = os.getenv('API_KEY') or None
