import os
from shutil import copyfile, rmtree
from random import randint

from flask import send_from_directory, Blueprint, url_for, render_template
import WebApp.model as models
from instance.config import hash_function



def copy_from(src):
    def to(dst):
        copyfile(src, dst)
    return to

def write_content(content):
    def to(dst):
        with open(dst, "wb") as file:
            file.write(content.encode("utf-8"))
    return to

class StaticStorage(object):
    def __init__(self, app, name):
        subdirectory = name
        self.path = os.path.abspath(os.path.join(app.config["STORAGE_PATH"], subdirectory))
        if os.path.exists(self.path):
            rmtree(self.path)
        os.mkdir(self.path)
        self.app = app
        self.bp = Blueprint(name, name)
        self.bp.route("/<string:filename>")(self.access)
        app.register_blueprint(self.bp, url_prefix="/"+name)
        


    def save_at(self, new_filename, file_creator):
        new_path = os.path.join(self.path, new_filename)
        print ("which is", new_path)
        file_creator(new_path)

    def send_at(self, filename, mimetype=None):
        return send_from_directory(self.path, filename, mimetype=mimetype)

    @staticmethod
    def random_name(ext=None):
        res = "".join([str(randint(0,9)) for i in range(15)])
        if ext is not None:
            res += "." + ext
        return res
class AssetStorage(StaticStorage):

    def access(self, filename):
        return self.send_at(filename)
    
    def create_asset(self, file_creator, *args, **kwargs):
        new_filename = self.random_name(*args, **kwargs)
        self.save_at(new_filename, file_creator)
        with self.app.app_context():
            new_url = url_for("{}.{}".format(self.bp.name, "access"), filename=new_filename)
        return new_url

class ChallengeStorage(StaticStorage):

    def access(self, filename):
        filename = filename.lower()
        challenge = models.Challenge.query.filter_by(url=filename).one()
        with open(os.path.join(self.path, filename)) as f:
            ch_content = f.read()
        #error
        return render_template("challenge_wrapper.jinja2", ch_content=ch_content, challenge=challenge)
        #return self.send_at(filename, mimetype="html")
    
    def save_challenges(self, challenges):
        prev_hash = self.app.config["START_URL"]
        db = self.app.db
        print (len(challenges))
        for challenge in challenges:
            current_solution = challenge.get_solution()
            current_hash = hash_function(current_solution)
            challenge_row = models.Challenge(
                solution_hash=current_hash,
                url=prev_hash,
                solution = current_solution
            )
            print ("saving at", challenge_row.url)
            self.save_at(challenge_row.url, write_content(challenge.get_html()))
            db.session.add(challenge_row)
            db.session.commit()
            prev_hash = current_hash
