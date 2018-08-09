import os
from shutil import copyfile
from instance.config import STORAGE_PATH
from random import randint

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
    clear_dir(relative("."))
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


def directory_filler(dir, ext=None):
    def create_file(creator):
        new_name = random_name()
        if ext:
            new_name = "{}.{}".format(new_name, ext)
        creator(os.path.join(dir, new_name))
        return new_name
    return create_file

upload_challenge = directory_filler(relative(CHDIR),ext="html")
upload_static = directory_filler(relative(STDIR))
chpath = relative(CHDIR)
chrelative = relative_(chpath)
strelative = relative_(relative(STDIR))




