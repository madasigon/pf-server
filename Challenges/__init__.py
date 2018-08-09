from jinja2 import Template

def generate_challenges():
    return map(Challenge, range(1,11))

class Challenge(object):

    def get_html(self):
        return Template("<h1>{{ num }}*2</h1>").render(num=self.num)
    

    def get_solution(self):
        return str(self.num*2)
    
    def __init__(self, number):
        self.num = number
