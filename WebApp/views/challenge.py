from flask import Blueprint, render_template, send_from_directory

import WebApp.model as models
from WebApp.space import challenge_storage, static_storage

bp = Blueprint("challenge", import_name="challenge")


@bp.route("/static/<string:name>")
def static(name):
    print(static_storage.path)
    return static_storage.send_from(name)

@bp.route("/<string:hash>")
def challenge(hash):
    hash = hash.lower()
    challenge = models.Challenge.query.filter_by(url=hash).one()
    return challenge_storage.send_from(challenge.local_name)
    
