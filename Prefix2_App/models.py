from Prefix2_App import db


class PrefixClassDefaults(db.Model):
    prefix = db.Column(db.CHAR, primary_key=True)
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)

    def to_dict(self):
        return {"prefix": self.prefix, "start": self.start, "end": self.end}


class Prefix(db.Model):
    prefix = db.Column(db.CHAR, primary_key=True)
    next = db.Column(db.Integer)

    def to_dict(self):
        return {"prefix": self.prefix, "next": self.next}
