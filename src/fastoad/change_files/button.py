"""
Display the save button
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
from fastoad.change_files.change_name_input_output import ChangeNameInputOutput
from fastoad.change_files.change_title import ChangeTitle

class Button:
    """
    A class to Display the save button
    """

    def __init__(self):

        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()

        self.button = v.Html(
            tag="div",
            class_="d-flex justify-center mb-6",
            children=[
                v.Html(
                    tag="div", children=[]
                ),
            ],
        )

    def save(self):
        """
        Save the new values, and displays them
        """

        with open(self.file_name) as file:
            content = self.yaml.load(file)

            self.inputf = content["input_file"]
            self.outputf = content["output_file"]
            self.title = content["title"]

            self.inputf = self.inputf[2: len(self.inputf) - 4]
            self.outputf = self.outputf[2: len(self.outputf) - 4]

        try:
            content["input_file"] = "./" + ChangeNameInputOutput().returninputoutput().children[0] + ".xml"
            content["output_file"] = "./" + ChangeNameInputOutput().returninputoutput().children[1] + ".xml"
            content["title"] = "hh"
            with open(self.file_name, "w") as file:
                self.yaml.dump(content, file)
                if (
                        self.inputf == self.ChangeNameInputOutput().returninputoutput().children[0]
                        and self.outputf == self.ChangeNameInputOutput().returninputoutput().children[0]
                        and self.title == "hh"
                ):
                    print("Values inchanched.\n")
                else:
                    print("Successfuly changed values !\n")
                    print("Your new values :\n")
                    print("Input file : ./" + ChangeNameInputOutput().returninputoutput().children[0] + ".xml")
                    print("Output file : ./" + ChangeNameInputOutput().returninputoutput().children[1] + ".xml")
                    print("Title : " + "hh")
        except:
            raise ValueError("Error while modifying.\n")

    def init_widgets(self):

        btn = v.Btn(
            color="blue",
            elevation=4,
            style_="width:150px",
            outlined=True,
            children=[v.Icon(children=["get_app"]), "Save"],
        )

        def on_save_button_clicked(widget, event, data):
            self.save()

        btn.on_event("click", on_save_button_clicked)

        def button():
            self.button.children[0].children = [btn]

        display(btn)

    def display(self):
        self.init_widgets()