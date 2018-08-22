from WebApp import create_app
from WebApp.prepare import prepare


app = create_app()
try:
    from experiment import app_modify
    app_modify(app)
except ImportError:
    print("WARNING: COULD NOT LOAD EXPERIMENT.PY")

prepare(app)
app.run(debug=True)