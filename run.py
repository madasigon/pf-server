from app import app
from WebApp import db
from WebApp.prepare import prepare

try:
    from experiment import app_modify
    app_modify(app)
except ImportError:
    print("WARNING: COULD NOT LOAD EXPERIMENT.PY")

prepare(app)
app.run(debug=True)