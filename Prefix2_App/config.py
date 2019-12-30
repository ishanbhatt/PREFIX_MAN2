import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DB_LOCATION = os.environ["DB_LOCATION"]


class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DB_LOCATION, 'prefix.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
