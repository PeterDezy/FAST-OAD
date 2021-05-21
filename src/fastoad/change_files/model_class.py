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

        self.txt = ""

        self.vbox = v.Html(
            tag="div",
            class_="d-flex justify-center mb-6",
            children=[
                v.Html(
                    tag="div", children=[]
                ),
                v.Html(
                    tag="div", children=[]
                ),
            ],
        )

    def initialize(self):

        self.namew = v.TextField(
            v_model=self.name,
            label="Name :",
            outlined=True,
            style_="margin-top:20px",
        )

        if self.namew.v_model == 'model':
            self.namew.readonly = True

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

            if (len(self.models) != 10):
                self.models.append(Model("subgroup" + str(len(self.models)+1)))
                if (len(self.models) == 1):
                    self.models[0].display()
                elif (len(self.models) == 2):
                    self.models[1].display()
                elif (len(self.models) == 3):
                    self.models[2].display()
                elif (len(self.models) == 4):
                    self.models[3].display()
                elif (len(self.models) == 5):
                    self.models[4].display()
                elif (len(self.models) == 6):
                    self.models[5].display()
                elif (len(self.models) == 7):
                    self.models[6].display()
                elif (len(self.models) == 8):
                    self.models[7].display()
                elif (len(self.models) == 9):
                    self.models[8].display()
                elif (len(self.models) == 10):
                    self.models[9].display()
                    self.vbox.children = []

        self.addMod.on_event("click", on_addMod_button_clicked)

        self.delMod = v.Btn(
            color="blue",
            elevation=4,
            style_="width:150px",
            outlined=True,
            children=["Delete last subgroup"],
        )

        self.vbox.children = [self.addMod]

    def save(self)->str:

        self.name = self.namew.v_model

        self.linear.save()

        self.nonlinear.save()

        self.txt = ""

        self.txt += self.name+":\n"

        self.txt += "\t"+self.linear.solver_value()+"\n"

        self.txt += "\t"+self.nonlinear.solver_value()+"\n"

        for i in self.models:
            texte = i.save()
            ligne = texte.splitlines()
            for a in range(0,len(ligne)):
                self.txt += "\t"+ligne[a]+"\n"

        return self.txt

    def display(self):

        self.initialize()
        display(self.namew)
        self.linear.display()
        self.nonlinear.display()
        display(self.vbox)
