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


class ChangeNameInputOutput:
    """
    A class to change the name of the input/output file in the configuration file
    """
    def __init__(self):
        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()

        # Input file name
        self.inputf = None

        # Output file name
        self.outputf = None

        # Widgets
        self.i = None
        self.o = None

    def save(self):
        """
        Save the new values of input & output file in the yaml file, and displays them
        """
        clear_output(wait=True)
        display(self.i, self.o)

        with open(self.file_name) as f:
            content = yaml.load(f)

            self.inputf = content["input_file"]
            self.outputf = content["output_file"]

            self.inputf = self.inputf[2:len(self.inputf) - 4]

            self.outputf = self.outputf[2:len(self.outputf) - 4]
        try:
            content['input_file'] = "./" + self.i.value + ".xml"
            content['output_file'] = "./" + self.o.value + ".xml"
            with open(file_name, 'w') as f:
                yaml.dump(content, f)
                if self.inputf == self.i.value and self.outputf == self.o.value:
                    print("Valeurs inchangées.\n")
                else:
                    print("Successfuly changed values !\n")
                    print("Your new values :\n")
                    print("./" + self.i.value + ".xml")
                    print("./" + self.o.value + ".xml\n")
        except:
            raise ValueError("Error while modifying.\n")

    def read(self):
        """
        Read the configuration file to display the name of the input & output file
        """

        with open(self.file_name) as f:
            content = self.yaml.load(f)

        self.inputf = content["input_file"]
        self.outputf = content["output_file"]

        self.inputf = self.inputf[2:len(self.inputf) - 4]

        self.outputf = self.outputf[2:len(self.outputf) - 4]

    def _initialize_widgets(self):
        """
        Initialize the widgets to change the name of the input/output file
        """

        self.i = widgets.Text(
            value=self.inputf,
            description='input_file:',
        )

        self.o = widgets.Text(
            value=self.outputf,
            description='output_file:',
        )

    def display(self, change=None) -> display:
        """
        Display the user interface
        :return the display object
        """
        clear_output(wait=True)
        self.read()
        self._initialize_widgets()
        ui = widgets.VBox(
            [self.i, self.o]
        )
        return ui
