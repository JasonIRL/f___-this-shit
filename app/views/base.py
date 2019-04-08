from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from app.models import db
from app.models.db_models import Stupid

base = Blueprint("base", __name__)


@base.route("/", methods=["GET", "POST"])
def index():
    complaints = [row for row in Stupid.query.order_by(Stupid.timestamp.desc()).all()]
    void_list = []
    for complaint in complaints:
        void_data = (f"{complaint.text}", f"{complaint.timestamp}")
        void_list.append(void_data)
    if request.method == "POST":
        form = request.form
        new_bullshit = Stupid(
            text=(form["gripe"]).upper(), timestamp=datetime.utcnow().isoformat()
        )
        db.session.add(new_bullshit)
        db.session.commit()
        return redirect(url_for("base.index"))
    return render_template("index.html", bullshit=void_list)
