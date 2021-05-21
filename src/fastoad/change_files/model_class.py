"""
Model class
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
import ipywidgets as widgets
from fastoad.change_files.linear_solver_class import LinearSolver
from fastoad.change_files.non_linear_solver_class import NonLinearSolver

class Model:

    def __init__(self, name):

        # Parameters config file
        self.name = name

        self.namew = None

        self.linear = None

        self.nonlinear = None

        self.models = []

        self.addMod = None

        self.components = []

        self.txt = None

    def initialize(self):

        self.namew = v.TextField(
            v_model=self.name,
            label="Name :",
            outlined=True,
            style_="margin-top:20px",
        )

        self.linear = LinearSolver()

        self.nonlinear = NonLinearSolver()

        self.addMod = v.Btn(
            color="blue",
            elevation=4,
            style_="width:150px",
            outlined=True,
            children=["Add subgroup"],
        )

        def on_addMod_button_clicked(widget, event, data):

            self.models.append(Model("subgroup"))

        self.addMod.on_event("click", on_addMod_button_clicked)

        self.txt = ""

    def save(self)->str:

        self.name = self.namew.v_model

        self.linear.save()

        self.nonlinear.save()

        self.txt += self.name+":\n"

        self.txt += "\t"+self.linear.solver_value()+"\n"

        self.txt += "\t"+self.nonlinear.solver_value()+"\n"

        for i in self.models:
            self.txt += "\t"+i.save()+"\n"

        return self.txt

    def disabled_name(self):

        self.namew.readonly = True

    def display(self):

        self.initialize()
        if (self.name == "model"):
            self.disabled_name()
        display(self.namew)
        self.linear.display()
        self.nonlinear.display()
        for i in self.models:
            i.display()
        display(self.addMod)
