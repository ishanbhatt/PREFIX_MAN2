import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'prefix.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
