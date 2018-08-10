from jinja2 import Template
from WebApp.space import static_storage, copy_from

def generate_challenges():
    return map(Challenge, range(1,11))

class Challenge(object):

    def get_html(self):
        doge = static_storage.create_file(copy_from("doge.jpg"))
        return Template("<h1>{{ num }}*2</h1><br><img src=\"{{ doge }}\"></img>").render(num=self.num, doge=doge)
    

    def get_solution(self):
        return str(self.num*2)
    
    def __init__(self, number):
        self.num = number
