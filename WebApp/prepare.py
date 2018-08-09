from hashlib import sha1

import WebApp.model as models
from WebApp import db
from WebApp.space import upload_challenge, initialize_storage, write_content
from instance.config import START_URL

from Challenges import generate_challenges


def hash_function(s):
    return s
    #return sha1(s.encode("utf-8")).hexdigest()

def clear_database():
    db.drop_all()
    db.create_all()



def create_challenges():
    model_chs = []
    prev_hash = START_URL
    for challenge in generate_challenges():
        current_hash = hash_function(challenge.get_solution())
        model_chs.append(models.Challenge(
            solution_hash=current_hash,
            url=prev_hash,
            local_name=upload_challenge(write_content(challenge.get_html()))
        )),
        prev_hash = current_hash
    
    for challenge in model_chs:
        db.session.add(challenge)

    db.session.commit()

def prepare(app):
    clear_database()
    initialize_storage()
    create_challenges()

    
    
    