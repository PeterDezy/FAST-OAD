"""
Display the name of the input / output file in the configuration file
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

import ipyvuetify as v
from ruamel.yaml import YAML


class ChangeNameInputOutput:
    """
    A class to Display the name of the input / output file in the configuration file
    """

    def __init__(self):

        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()

        # Parameters config file
        self.inputf = None
        self.outputf = None

    def read(self):
        """
        Read the configuration file
        """

        with open(self.file_name) as file:
            content = self.yaml.load(file)

        self.inputf = content["input_file"]
        self.outputf = content["output_file"]

        self.inputf = self.inputf[2 : len(self.inputf) - 4]

        self.outputf = self.outputf[2 : len(self.outputf) - 4]


    def init_widgets(self):

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

        display(self.input,self.output)

    def display(self):

        self.read()
        self.init_widgets()

    def returninputoutput(self):

        return self.input.v_model, self.output.v_model