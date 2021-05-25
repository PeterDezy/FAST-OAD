"""
Change the configuration file
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
from fastoad.change_files.title_and_files_class import TitleAndFiles
from fastoad.change_files.driver_class import Driver
from fastoad.change_files.model_class import Model

class ChangeConfigFile:
    """
    A class which display all widgets to change the configuration file
    """

    def __init__(self):

        # The path & name of the data file that will be viewed/edited
        self.file_name = "./workdir/oad_process.yml"

        # A variable which take the title_and_files class
        self.title_and_files = None

        # A variable which take the driver class
        self.driver = None

        # A variable which take the model class
        self.model = None

        # The text to write on the yaml file
        self.txt = None

        # Widgets button to save the values
        self.btn = None


    def save(self, widget, event, data):
        """
        Save the new values in the configuration file and display an overview
        """

        success = v.Alert(
            type='success',
            children=['Successfuly changed values'],
            elevation='2',
        )

        self.txt = self.title_and_files.save()
        self.txt += self.driver.save()
        self.txt += self.model.save()

        display(success)
        display(Markdown("```yaml\n" + self.txt + "\n```"))


    def _initialize_widgets(self):
        """
        Initialize all widgets to display them
        """

        self.btn = v.Btn(
            color="blue",
            elevation=4,
            style_="width:150px;margin:auto;",
            outlined=True,
            children=[v.Icon(children=["get_app"]), "Save"],
        )

        self.reset = v.Btn(
            color="red",
            elevation=4,
            style_="width:150px;margin:auto;",
            outlined=True,
            children=["Reset"],
        )

        def resetwidgets(widget, event, data):

            clear_output(wait=True)
            self.display()


        self.btn.on_event("click", self.save)

        self.reset.on_event("click", resetwidgets)

        self.title_and_files = TitleAndFiles()
        self.title_and_files.display()
        self.driver = Driver()
        self.driver.display()
        self.model = Model("model")
        self.model.display()

    def display(self):
        """
        Display all widgets
        """

        clear_output(wait=True)
        self._initialize_widgets()
        display(self.reset)
        display(self.btn)