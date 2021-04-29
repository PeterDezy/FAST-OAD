"""
Change the name of the input/output file in the configuration file
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

        # self.i = ChangeNameInputOutput().ivalue()
        #
        # self.o  = ChangeNameInputOutput().ovalue()

        # Css esthetics
        self.css = "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;}"
        self.css += ".save {margin-left: 6%;} .green {background-color: lightgreen;} </style>"
        self.html = HTML(self.css)

    def save(self):
        """
        Save the new values, and displays them
        """
        clear_output(wait=True)
        self.display()

        with open(self.file_name) as f:
            content = self.yaml.load(f)

            self.inputf = content["input_file"]
            self.outputf = content["output_file"]

            self.inputf = self.inputf[2:len(self.inputf) - 4]
            self.outputf = self.outputf[2:len(self.outputf) - 4]

        try:
            content['input_file'] = "./" + self.i.value + ".xml"
            content['output_file'] = "./" + self.o.value + ".xml"
            with open(self.file_name, 'w') as f:
                self.yaml.dump(content, f)
                if self.inputf == self.i.value and self.outputf == self.o.value:
                    print("Valeurs inchangées.\n")
                else:
                    print("Successfuly changed values !\n")
                    print("Your new values :\n")
                    print("./" + self.i.value+ ".xml")
                    print("./" + self.o.value + ".xml\n")
        except:
            raise ValueError("Error while modifying.\n")

    def _initialize_widgets(self):
        """
        Initialize the button widget
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

        self._initialize_widgets()
        return display(ChangeNameInputOutput().display(),ChangeTitle().display(),self.button)