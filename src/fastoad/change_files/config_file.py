"""
Config file class
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

from IPython.display import clear_output, display, Markdown
import ipyvuetify as v
from fastoad.change_files.model_class import Model

class ConfigFile:

    def __init__(self):

        self.model = None

        self.txt = None

        self.btn = None

    def initialize(self):

        self.model = Model("model")

        self.txt = ""

        self.btn = v.Btn(
            color="blue",
            elevation=4,
            style_="width:150px;margin:auto",
            outlined=True,
            children=[v.Icon(children=["get_app"]), "Save"],
        )

        def on_save_button_clicked(widget, event, data):

            self.save()

        self.btn.on_event("click", on_save_button_clicked)

    def save(self):

        self.txt = ""

        self.txt = self.model.save()

        display(Markdown("```yaml\n" + self.txt + "\n```"))

    def display(self):

        self.initialize()
        self.model.display()
        display(self.btn)

