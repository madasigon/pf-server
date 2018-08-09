from flask import Blueprint, render_template, send_from_directory

import WebApp.model as models
from WebApp.space import chpath

bp = Blueprint("challenge", import_name="challenge")


@bp.route("/<string:hash>")
def challenge(hash):
    challenge = models.Challenge.query.filter_by(url=hash).one()
    return send_from_directory(chpath, challenge.local_name)
