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

from IPython.display import clear_output, display
import ipyvuetify as v
import ipywidgets as widgets
from fastoad.change_files.linear_solver_class import LinearSolver
from fastoad.change_files.non_linear_solver_class import NonLinearSolver

class Model:

    def __init__(self, name):

        # Parameters config file
        self.name = name

        self.linear = None

        self.nonlinear = None

        self.btn = None

        self.models = None

        self.components = None

        self.txt = None

    def initialize(self):

        self.linear = LinearSolver()

        self.nonlinear = NonLinearSolver()

        self.btn = v.Btn(
            color="blue",
            elevation=4,
            style_="width:150px",
            outlined=True,
            children=[v.Icon(children=["get_app"]), "Save"],
        )

        def on_save_button_clicked(widget, event, data):

            self.save()

        self.btn.on_event("click", on_save_button_clicked)

        self.models = []

        self.components = []

        self.txt = ""

    def save(self):

        self.linear.save()

        self.nonlinear.save()

        self.txt += self.name+":\n"

        self.txt += "\t"+self.linear.solver_value() +"\n"

        self.txt += "\t"+self.nonlinear.solver_value()

        print(self.txt)

    def display(self):

        self.initialize()
        self.linear.display()
        self.nonlinear.display()
        display(self.btn)
