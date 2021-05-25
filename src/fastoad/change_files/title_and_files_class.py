"""
Title & Input/Output file class
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

from IPython.display import display
import ipyvuetify as v
from ruamel.yaml import YAML
import openmdao.drivers as driver

class TitleAndFiles:
    """
    A class which display the title and the input / output file widgets
    """

    def __init__(self):

        # The path & name of the data file that will be viewed/edited
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml ( read the .yml file )
        self.yaml = YAML()

        # Text to return in the yaml file
        self.title_and_files = None

        # Ipyvuetify widgets
        self.input = None

        self.output = None

        self.title = None

        # Parameters config file
        self.inputf = None

        self.outputf = None

        self.titlef = None

    def read(self):
        """
        Read the configuration file to display the title and the input / output file values
        """

        with open(self.file_name) as file:
            content = self.yaml.load(file)

        self.inputf = content["input_file"]
        self.outputf = content["output_file"]
        self.titlef = content["title"]

        self.inputf = self.inputf[2: len(self.inputf) - 4]

        self.outputf = self.outputf[2: len(self.outputf) - 4]

    def initialize(self):
        """
        All ipyvuetify widgets to display for the title and the input / output file
        """

        self.title = v.TextField(
            v_model=self.titlef,
            label="Title :",
            outlined=True,
            clearable=True,
            style_="margin-top:20px",
        )

        self.input = v.TextField(
            v_model=self.inputf,
            label="Input_file :",
            suffix=".yml",
            outlined=True,
            clearable=True,
            style_="margin-top:5px",
        )

        self.output = v.TextField(
            v_model=self.outputf,
            label="Output_file :",
            suffix=".yml",
            outlined=True,
            clearable=True,
            style_="margin-top:5px",
        )

        display(self.title, self.input, self.output)

    def save(self) -> str :
        """
        Return the text to write in the yaml file for the title and the input / output file
        """

        self.title_and_files = "title: "

        self.title_and_files += self.title.v_model
        self.title_and_files += "\n\n"
        self.title_and_files += "# List of folder paths where user added custom registered OpenMDAO components\n"
        self.title_and_files += "module_folders:\n\n"
        self.title_and_files += "# Input and output files\n"
        self.title_and_files += "input_file: "
        self.title_and_files += "./" + self.input.v_model + ".xml\n"
        self.title_and_files += "output_file: "
        self.title_and_files += "./" + self.output.v_model + ".xml\n\n"

        return self.title_and_files

    def display(self):

        self.read()
        self.initialize()