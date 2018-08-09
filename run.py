from app import app
from WebApp import db
from WebApp.prepare import prepare

try:
    from experiment import app_modify
    app_modify(app)
except ImportError:
    pass

prepare(app)
app.run(debug=True)