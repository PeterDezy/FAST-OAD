"""
Change the configuration file
"""
#  This file is part of FAST-OAD : A framework for rapid Overall Aircraft Design
#  Copyright (C) 2021 ONERA & ISAE-SUPAERO
#  FAST is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from IPython.display import clear_output, display, HTML
import ipywidgets as widgets
from ruamel.yaml import YAML


class OneClass:
    """
    A class which display all the widgets for the configuration file
    """

    def __init__(self):
        # The file name
        self.file_name = "../notebooks/workdir/oad_process.yml"

        # Css esthetics
        self.css = "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;}"
        self.css += ".save {margin-left: 6%;} .green {background-color: lightgreen;} </style>"
        self.html = HTML(self.css)

        # Ruamel yaml
        self.yaml = YAML()

        # Title name
        self.title = None

        # Input file name
        self.inp = None

        # Output file name
        self.oup = None

        # Widgets
        self.t = None
        self.i = None
        self.o = None
        self.button = None

    def read(self):
        """
        Read the configuration file to display the name of the input & output file
        """

        with open(self.file_name) as f:
            content = self.yaml.load(f)
            self.title = content["title"]
            self.inp = content["input_file"]
            self.oup = content["output_file"]

        self.inp = self.inp[2:len(self.inp) - 4]

        self.oup = self.oup[2:len(self.oup) - 4]

    def save(self):
        """
        Save the new values, and displays them
        """
        clear_output(wait=True)
        display(self.t, self.i, self.o, self.button)
        with open(self.file_name) as f:
            content = self.yaml.load(f)
        try:
            content['title'] = self.t.value
            content['input_file'] = "./" + self.i.value + ".xml"
            content['output_file'] = "./" + self.o.value + ".xml"
            with open(self.file_name, 'w') as f:
                self.yaml.dump(content, f)
                if self.inp == self.i.value and self.oup == self.o.value and self.title == self.t.value:
                    print("Values unchanged\n")
                else:
                    print("Successfully changed values !\n")
                    print("Your new values :\n")
                    print(self.t.value+"\n")
                    print("./" + self.i.value + ".xml\n")
                    print("./" + self.o.value + ".xml\n")
        except:
            raise ValueError("Error while modifying.\n")

    def _initialize_widgets(self):
        """
        Initialize the button widget
        """

        self.t = widgets.Text(
            value=self.title,
            description='title :'
        )

        self.i = widgets.Text(
            value=self.inp,
            description='input_file :'
        )

        self.o = widgets.Text(
            value=self.oup,
            description='output_file :'
        )

        self.button = widgets.Button(
            description='Save',
            icon='save'
        )

        self.button.add_class("save")
        self.button.add_class("top")
        self.button.add_class("green")

        def on_save_button_clicked(b):
            self.save()

        self.button.on_click(on_save_button_clicked)

    def display(self, change=None) -> display:
        """
        Display the user interface
        :return the display object
        """
        clear_output(wait=True)
        self.read()
        self._initialize_widgets()
        ui = widgets.VBox(
            [self.t, self.i, self.o, self.button]
        )
        return display(ui)
