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
import ipyvuetify as v
from ruamel.yaml import YAML
from fastoad.change_files.change_name_input_output import ChangeNameInputOutput
from fastoad.change_files.change_title import ChangeTitle
from fastoad.change_files.change_driver import ChangeDriver

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
            content['input_file'] = "./" + self.i.value + ".xml"
            content['output_file'] = "./" + self.o.value + ".xml"
            content['title'] = self.t.v_model
            with open(self.file_name, 'w') as f:
                self.yaml.dump(content, f)
                if self.inputf == self.i.value and self.outputf == self.o.value and self.title == self.t.v_model:
                    print("Values inchanched.\n")
                else:
                    print("Successfuly changed values !\n")
                    print("Your new values :\n")
                    print("Input file : ./" + self.i.value + ".xml")
                    print("Output file : ./" + self.o.value + ".xml")
                    print("Title : " + self.t.v_model)
        except:
            raise ValueError("Error while modifying.\n")

    def _initialize_widgets(self):
        """
        Initialize the button widget, and add css to him
        """
        self.button = v.Btn(color='blue', elevation=4, style_='width:100px', outlined=True, children=[
            v.Icon(left=True, children=[
                'get_app'
            ]),
            'Save'
        ]
                            )
        def on_save_button_clicked(widget, event, data):
            self.save()

        self.button.on_event('click', on_save_button_clicked)

    def display(self, change=None) -> display:
        """
        Display the user interface
        :return the display object
        """
        self._initialize_widgets()

        self.i = ChangeNameInputOutput().display().children[0]
        self.o = ChangeNameInputOutput().display().children[1]
        self.t = ChangeTitle().display().children[0]
        self.d = ChangeDriver().display().children[0]

        ui = widgets.VBox(
            [self.t, self.i,self.o,self.d,self.button]
        )

        return ui
