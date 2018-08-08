from app import app
from WebApp import db


try:
    from experiment import app_modify
    app_modify(app)
except ImportError:
    pass

db.drop_all()
db.create_all()
app.run(debug=True)