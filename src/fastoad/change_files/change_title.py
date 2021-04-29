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
from ruamel.yaml import YAML


class ChangeTitle:
    """
    A class to change the title of the configuration file
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

        # Title name
        self.title = None

        # Widgets
        self.t = None
        self.button = None

    def save(self):
        """
        Save the new value of the title configuration file in the yaml file, and displays them
        """
        clear_output(wait=True)
        display(self.t, self.button)

        with open(self.file_name) as f:
            content = self.yaml.load(f)

            title = content["title"]

        try:
            content['title'] = self.t.value
            with open(self.file_name, 'w') as f:
                self.yaml.dump(content, f)
                if self.title == self.t.value:
                    print("Title unchanged.\n")
                else:
                    print("Successfuly changed title !\n")
                    print("Your new title :\n")
                    print(self.t.value + "\n")
        except:
            raise ValueError("Error while modifying.\n")

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

        self.t = widgets.Text(
            value=self.title,
            description='title:',
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
            [self.t, self.button]
        )
        return display(ui)