from flask import redirect, Markup, escape
from WebApp import db
from WebApp.model import User
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