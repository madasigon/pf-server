import jinja2
import webbrowser
import Maze_Generator as MG
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "Jinja2_Template.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(maze=MG.make_maze(10,10))  # this is where to put args to the template renderer
with open("Maze_DFS.html", "wb") as fh:
    fh.write(outputText)
print(outputText)
'''
url = 'file:///Dokumentumok/Andor/Computer Science/Lynx Analitics/Jinja2_Template.html'
webbrowser.open(url,new=2)
print(outputText)
'''