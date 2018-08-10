import os
from shutil import copyfile, rmtree
from instance.config import STORAGE_PATH
from random import randint

from flask import send_from_directory

CHDIR = "challenges/"
STDIR = "static/"

def relative_(l):
    def right_(r):
        return os.path.join(l, r)
    return right_

relative = relative_(STORAGE_PATH)

def clear_dir(dirPath):
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath+"/"+fileName)
    pass

def initialize_storage():
    rmtree(STORAGE_PATH)
    os.makedirs(relative(STDIR))
    os.makedirs(relative(CHDIR))
    
def copy_from(src):
    def to(dst):
        copyfile(src, dst)
    return to

def write_content(content):
    def to(dst):
        with open(dst, "wb") as file:
            file.write(content.encode("utf-8"))
    return to

def random_name():
    return "".join([str(randint(0,9)) for i in range(15)])


class Storage(object):
    def __init__(self, path, url_path, ext=None):
        self.path = path
        self.url_path = url_path
        self.ext = ext
    
    def create_file(self, creator, ext=None):
        new_name = random_name()
        need = ext or self.ext
        if need:
            new_name = "{}.{}".format(new_name, need)
        creator(os.path.join(self.path, new_name))
        return relative_(self.url_path)(new_name)
    def send_from(self, name):
        return send_from_directory(self.path, name)
    

challenge_storage = Storage(relative(CHDIR), "/challenge", ext="html")
static_storage = Storage(relative(STDIR), "/challenge/static")



