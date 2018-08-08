from flask import redirect

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