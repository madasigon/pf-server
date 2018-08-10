from jinja2 import Template
from WebApp.space import static_storage, copy_from, write_content

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('Challenges', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def generate_challenges():
    return map(Challenge, range(1,11))


class Challenge(object):

    def get_html(self):
        doge = static_storage.create_file(copy_from("doge.jpg"), ext="jpg")
        return env.get_template("example.jinja2").render(num=self.num, doge=doge)
    

    def get_solution(self):
        return str(self.num*2)
    
    def __init__(self, number):
        self.num = number
