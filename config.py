import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Flask Configuration Object"""

    SECRET_KEY = os.getenv("SECRET_KEY") or "fuck-this-shit"
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL") or f"sqlite:///{os.path.join(basedir, 'fuck.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
