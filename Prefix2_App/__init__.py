from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from Prefix2_App.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from Prefix2_App import routes
from Prefix2_App import models

db.create_all()


def init_db():
    if db.session.query(models.PrefixClassDefaults).count() == 0:
        db.session.add(models.PrefixClassDefaults(prefix="A", start=10, end=19))
        db.session.add(models.PrefixClassDefaults(prefix="B", start=200, end=399))
        db.session.add(models.PrefixClassDefaults(prefix="C", start=4000, end=5999))
        db.session.add(models.PrefixClassDefaults(prefix="D", start=60000, end=79999))
        db.session.add(models.PrefixClassDefaults(prefix="E", start=800000, end=999999))
        db.session.commit()

    if db.session.query(models.Prefix).count() == 0:
        db.session.add(models.Prefix(prefix="A", next=10))
        db.session.add(models.Prefix(prefix="B", next=200))
        db.session.add(models.Prefix(prefix="C", next=4000))
        db.session.add(models.Prefix(prefix="D", next=60000))
        db.session.add(models.Prefix(prefix="E", next=800000))
        db.session.commit()

init_db()
