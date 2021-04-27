import yaml
from IPython.display import display
from IPython.display import clear_output
import ipywidgets as widgets
from ruamel.yaml import YAML

css = "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;} .save {margin-left: 6%;}"
css += ".green {background-color: lightgreen;} </style>"
html = HTML(css)
display(html)

file_name = "./workdir/oad_process.yml"
yaml = YAML()

with open(file_name) as f:
    content = yaml.load(f)

title = content["title"]

t = widgets.Text(
    value=title,
    description='title:',
)


def save(b):
    clear_output(wait=True)
    display(t, button)

    with open(file_name) as f:
        content = yaml.load(f)

        title = content["title"]

    try:
        content['title'] = t.value
        with open(file_name, 'w') as f:
            yaml.dump(content, f)
            if title == t.value:
                print("Title unchanged.\n")
            else:
                print("Successfuly changed title !\n")
                print("Your new title :\n")
                print(t.value + "\n")
    except:
        raise ValueError("Error while modifying.\n")


button = widgets.Button(
    description='Save',
    icon='save'
)

button.add_class("save")
button.add_class("top")
button.add_class("green")

display(t, button)
button.on_click(save)