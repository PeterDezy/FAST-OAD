"""
Change the title of the configuration file
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


class ChangeTitle:
    """
    A class to change the title of the configuration file
    """
    def __init__(self):
        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()

        # Title name
        self.title = None

        # Widgets
        self.t = None

    def read(self):
        """
        Read the configuration file to display the title of the configuration file
        """

        with open(self.file_name) as f:
            content = self.yaml.load(f)

        self.title = content["title"]

    def _initialize_widgets(self):
        """
        Initialize the widget to change the title of the configuration file
        """

        # self.t = widgets.Text(
        #     value=self.title,
        #     description='title:',
        # )

        self.t = v.Textarea(
            v_model=self.title,
            label='title:',
            rows="1",
            auto_grow=True
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
            [self.t]
        )
        return ui