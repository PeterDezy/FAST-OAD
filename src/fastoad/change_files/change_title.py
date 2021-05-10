"""
Display the title of the configuration file
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


class ChangeTitle:
    """
    A class to Display the title of the configuration file
    """

    def __init__(self):

        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()

    def read(self):
        """
        Read the configuration file
        """

        with open(self.file_name) as file:
            content = self.yaml.load(file)

        self.title = content["title"]

    def init_widgets(self):

        self.title = v.TextField(
            v_model=self.title,
            label="Title :",
            outlined=True,
            clearable=True,
            style_="margin-top:20px",
        )

        display(self.title)

    def display(self):

        self.read()
        self.init_widgets()

    def returntitle(self):
        return self.title