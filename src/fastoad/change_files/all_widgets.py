"""
Display all the wiggets to change the configuration file
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
from fastoad.change_files.change_name_input_output import ChangeNameInputOutput
from fastoad.change_files.change_title import ChangeTitle

class AllWidgets:
    """
    A class which display all the widgets for the configuration file
    """
    def __init__(self):

        self.button = None

        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()

        self.inputf = None

        self.outputf = None

        self.title = None

        # Css esthetics
        self.css = "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;}"
        self.css += ".save {margin-left: 6%;} .green {background-color: lightgreen;} </style>"
        self.html = HTML(self.css)

    def save(self):
        """
        Save the new values, and displays them
        """

        clear_output(wait=True)

        with open(self.file_name) as f:
            content = self.yaml.load(f)

            self.inputf = content["input_file"]
            self.outputf = content["output_file"]
            self.title = content["title"]

            self.inputf = self.inputf[2:len(self.inputf) - 4]
            self.outputf = self.outputf[2:len(self.outputf) - 4]

        try:
            content['input_file'] = "./" + self.i.value + ".xml"
            content['output_file'] = "./" + self.o.value + ".xml"
            content['title'] = self.t.value
            with open(self.file_name, 'w') as f:
                self.yaml.dump(content, f)
                if self.inputf == self.i.value and self.outputf == self.o.value and self.title == self.t.value:
                    print("Values inchanched.\n")
                else:
                    print("Successfuly changed values !\n")
                    print("Your new values :\n")
                    print("Input file : ./" + self.i.value + ".xml")
                    print("Output file : ./" + self.o.value + ".xml")
                    print("Title : " + self.t.value)
        except:
            raise ValueError("Error while modifying.\n")

    def _initialize_widgets(self):
        """
        Initialize the button widget, and add css to him
        """

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

        self._initialize_widgets()

        self.i = ChangeNameInputOutput().display().children[0]
        self.o = ChangeNameInputOutput().display().children[1]
        self.t = ChangeTitle().display().children[0]

        ui = widgets.VBox(
            [self.i, self.o,self.t,self.button]
        )

        return ui
