from . import db


class Stupid(db.Model):
    """A Stupid Table for a Stupid App"""

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime(timezone=False))
