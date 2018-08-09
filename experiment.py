from flask import redirect, Markup, escape, send_from_directory, render_template
from WebApp import db
import WebApp.model as models
from WebApp.space import chpath
def app_modify(app):
    
    @app.route("/chs")
    def get_all():
        return escape(str([ch.url for ch in models.Challenge.query.all()]))