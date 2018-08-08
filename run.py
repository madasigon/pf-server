from app import app


try:
    from experiment import app_modify
    app_modify(app)
except ImportError:
    pass

app.run(debug=True)