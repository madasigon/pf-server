from flask import Blueprint, render_template


bp = Blueprint("index", import_name="index")

@bp.route("/")
def index():
    return render_template("index.jinja2")