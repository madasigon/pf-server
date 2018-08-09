from flask import redirect, Markup, escape, send_from_directory
from WebApp import db
import WebApp.model as models
from WebApp.space import chpath
def app_modify(app):
    
    @app.route("/pic")
    def pic():
        return redirect("https://pfinder.nyc3.digitaloceanspaces.com/doge.jpg")
    
    @app.route("/")
    def index():
        return '<img src="/pac"></img>'
    
    @app.route("/pac")
    def pac():
        return redirect("/pic")
    
    @app.route("/error")
    def err():
        db.session.add(User(username="g",email="hali"))
        db.session.commit()
        return escape(User.query.all())

    @app.route("/challenge/<string:hash>")
    def get_ch(hash):
        challenge = models.Challenge.query.filter_by(url=hash).one()
        return send_from_directory(chpath, challenge.local_name)
