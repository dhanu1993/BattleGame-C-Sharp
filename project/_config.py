import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'T(\x9d\xeb\xb4JT\xe6\xf1\xf8\xce\xfd\xcf\x8f--k\x87==?s7l'

DATABASE_PATH = os.path.join(basedir, DATABASE)

