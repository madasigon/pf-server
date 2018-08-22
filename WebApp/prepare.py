from hashlib import sha1

import WebApp.model as models
from instance.config import START_URL
from Challenges import generate_challenges

def hash_function(s):
    return s
    #return sha1(s.encode("utf-8")).hexdigest()

def clear_database(app):
    app.db.drop_all()
    app.db.create_all()

def create_challenges(app):
    koztes = generate_challenges(app.asset_storage)
    print (type(koztes))
    app.challenge_storage.save_challenges(koztes)

def prepare(app):
    clear_database(app)
    create_challenges(app)

    
    
    