from flask import redirect, Markup, escape, send_from_directory, render_template, jsonify
from inspect import getsource
from WebApp import db
import WebApp.model as models
from WebApp.prepare import hash_function
def app_modify(app):
    @app.route("/chs")
    def get_all():
        return render_template("chs.jinja2", hf=getsource(hash_function), urls=str([ch.url for ch in models.Challenge.query.all()]))
