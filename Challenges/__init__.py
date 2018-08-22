from jinja2 import Template
from WebApp.space import copy_from, write_content

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('Challenges', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def generate_challenges(asset_storag):
    global asset_storage
    asset_storage = asset_storag
    return list([Challenge(i) for i in range(1,11)])


class Challenge(object):

    def get_html(self):
        doge = asset_storage.create_asset(copy_from("doge.jpg"), ext="jpg")
        return env.get_template("example.jinja2").render(num=self.num, doge=doge)
    

    def get_solution(self):
        return str(self.num*2)
    
    def __init__(self, number):
        self.num = number
