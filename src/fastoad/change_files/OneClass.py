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
import ipyvuetify as v
from ruamel.yaml import YAML


class OneClass:
    """
    A class which display all the widgets for the configuration file
    """

    def __init__(self):
        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Css esthetics
        self.css = "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;}"
        self.css += ".save {margin-left: 6%;} .green {background-color: lightgreen;} </style>"
        self.html = HTML(self.css)

        # Ruamel yaml
        self.yaml = YAML()

    def read(self):
        """
        Read the configuration file
        """

        with open(self.file_name) as f:
            content = self.yaml.load(f)

        self.inputf = content["input_file"]
        self.outputf = content["output_file"]
        self.title = content["title"]

        self.inputf = self.inputf[2:len(self.inputf) - 4]

        self.outputf = self.outputf[2:len(self.outputf) - 4]

    def save(self):
        """
        Save the new values, and displays them
        """

        with open(self.file_name) as f:
            content = self.yaml.load(f)

            self.inputf = content["input_file"]
            self.outputf = content["output_file"]
            self.title = content["title"]

            self.inputf = self.inputf[2:len(self.inputf) - 4]
            self.outputf = self.outputf[2:len(self.outputf) - 4]

        try:
            content['input_file'] = "./" + self.i.v_model + ".xml"
            content['output_file'] = "./" + self.o.v_model + ".xml"
            content['title'] = self.t.v_model
            with open(self.file_name, 'w') as f:
                self.yaml.dump(content, f)
                if self.inputf == self.i.v_model and self.outputf == self.o.v_model and self.title == self.t.v_model:
                    print("Values inchanched.\n")
                else:
                    print("Successfuly changed values !\n")
                    print("Your new values :\n")
                    print("Input file : ./" + self.i.v_model + ".xml")
                    print("Output file : ./" + self.o.v_model + ".xml")
                    print("Title : " + self.t.v_model)
        except:
            raise ValueError("Error while modifying.\n")


    def _initialize_widgets(self):
        """
        Initialize the button widget
        """

        self.t = v.TextField(
            v_model=self.title,
            label='Title :',
            filled=True,
            shaped=True,
            clearable=True,
            style_='width:500px'
        )

        self.i = v.TextField(
            v_model=self.inputf,
            label='Input_file :',
            suffix = ".yml",
            filled=True,
            shaped=True,
            clearable=True,
            style_='width:500px'
        )

        self.o = v.TextField(
            v_model=self.outputf,
            label='Output_file :',
            suffix = ".yml",
            filled=True,
            shaped=True,
            clearable=True,
            style_='width:500px'
        )

        self.button = v.Btn(color='blue', elevation=4, style_='width:100px', outlined=True, children=[
            v.Icon(left=True, children=[
                'get_app'
            ]),
            'Save'
        ])

        def on_save_button_clicked(widget, event, data):
            self.save()

        self.button.on_event('click', on_save_button_clicked)


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
        return display(ui,self.html)