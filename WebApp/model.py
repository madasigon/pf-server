
def register(db):
    global Challenge
    class Challenge(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        url = db.Column(db.String(80), unique=True, nullable=False)
        solution = db.Column(db.Text(), unique=True, nullable=False)
        solution_hash = db.Column(db.String(80), unique=True, nullable=False)
