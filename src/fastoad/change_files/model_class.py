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

        self.usesolver = None

        self.linear = None

        self.nonlinear = None

        self.models = []

        self.addMod = None

        self.delMod = None

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

    def newvbox(self):

        if len(self.models) == 1:

            self.vbox2 = v.Html(
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

            self.vbox.children[0].children = []
            self.vbox.children[1].children = []

            self.vbox2.children[0].children = [self.addMod]
            self.vbox2.children[1].children = [self.delMod]

            display(self.vbox2)

        elif len(self.models) == 2:

            self.vbox3 = v.Html(
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

            self.vbox2.children[0].children = []
            self.vbox2.children[1].children = []

            self.vbox3.children[0].children = [self.addMod]
            self.vbox3.children[1].children = [self.delMod]

            display(self.vbox3)

        elif len(self.models) == 3:

            self.vbox4 = v.Html(
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

            self.vbox3.children[0].children = []
            self.vbox3.children[1].children = []

            self.vbox4.children[0].children = [self.addMod]
            self.vbox4.children[1].children = [self.delMod]

            display(self.vbox4)

        elif len(self.models) == 4:

            self.vbox5 = v.Html(
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

            self.vbox4.children[0].children = []
            self.vbox4.children[1].children = []

            self.vbox5.children[0].children = [self.addMod]
            self.vbox5.children[1].children = [self.delMod]

            display(self.vbox5)

        elif len(self.models) == 5:

            self.vbox6 = v.Html(
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

            self.vbox5.children[0].children = []
            self.vbox5.children[1].children = []

            self.vbox6.children[0].children = [self.addMod]
            self.vbox6.children[1].children = [self.delMod]

            display(self.vbox6)

        elif len(self.models) == 6:

            self.vbox7 = v.Html(
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

            self.vbox6.children[0].children = []
            self.vbox6.children[1].children = []

            self.vbox7.children[0].children = [self.addMod]
            self.vbox7.children[1].children = [self.delMod]

            display(self.vbox7)

        elif len(self.models) == 7:

            self.vbox8 = v.Html(
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

            self.vbox7.children[0].children = []
            self.vbox7.children[1].children = []

            self.vbox8.children[0].children = [self.addMod]
            self.vbox8.children[1].children = [self.delMod]

            display(self.vbox8)

        elif len(self.models) == 8:

            self.vbox9 = v.Html(
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

            self.vbox8.children[0].children = []
            self.vbox8.children[1].children = []

            self.vbox9.children[0].children = [self.addMod]
            self.vbox9.children[1].children = [self.delMod]

            display(self.vbox9)

        elif len(self.models) == 9:

            self.vbox10 = v.Html(
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

            self.vbox9.children[0].children = []
            self.vbox9.children[1].children = []

            self.vbox10.children[0].children = [self.addMod]
            self.vbox10.children[1].children = [self.delMod]

            display(self.vbox10)

        elif len(self.models) == 10:

            self.vbox10.children[0].children = [self.delMod]
            self.vbox10.children[1].children = []

    def initialize(self):

        self.namew = v.TextField(
            v_model=self.name,
            label="Name :",
            outlined=True,
            style_="margin-top:20px",
        )

        self.usesolver = v.Checkbox(
            v_model=True,
            label='Use solver',
            style_="margin-bottom:10px",
        )

        if self.namew.v_model == 'model':
            self.namew.readonly = True

        self.linear = LinearSolver()

        self.nonlinear = NonLinearSolver()

        def disabled (widget, event, data):

            if self.usesolver.v_model == False:
                self.linear.expansionPanel.disabled = True
                self.nonlinear.expansionPanel.disabled = True
            else:
                self.linear.expansionPanel.disabled = False
                self.nonlinear.expansionPanel.disabled = False


        self.usesolver.on_event("click", disabled)

        self.addMod = v.Btn(
            color="blue",
            elevation=4,
            style_="width:240px",
            outlined=True,
            children=["Add subgroup"],
        )

        def on_addMod_button_clicked (widget, event, data):

            if (len(self.models) != 10):
                self.models.append(Model("subgroup" + str(len(self.models)+1)))
                if (len(self.models) == 1):
                    self.models[0].newsub()
                    self.newvbox()
                elif (len(self.models) == 2):
                    self.models[1].newsub()
                    self.newvbox()
                elif (len(self.models) == 3):
                    self.models[2].newsub()
                    self.newvbox()
                elif (len(self.models) == 4):
                    self.models[3].newsub()
                    self.newvbox()
                elif (len(self.models) == 5):
                    self.models[4].newsub()
                    self.newvbox()
                elif (len(self.models) == 6):
                    self.models[5].newsub()
                    self.newvbox()
                elif (len(self.models) == 7):
                    self.models[6].newsub()
                    self.newvbox()
                elif (len(self.models) == 8):
                    self.models[7].newsub()
                    self.newvbox()
                elif (len(self.models) == 9):
                    self.models[8].newsub()
                    self.newvbox()
                elif (len(self.models) == 10):
                    self.models[9].newsub()

        self.addMod.on_event("click", on_addMod_button_clicked)

        self.delMod = v.Btn(
            color="blue",
            elevation=4,
            style_="width:240px; margin-left:50px;",
            outlined=True,
            children=["Delete last subgroup"],
        )

        def on_delMod_button_clicked (widget, event, data):

            self.models.pop()

        self.delMod.on_event("click", on_delMod_button_clicked)

        self.vbox.children[0].children = [self.addMod]
        self.vbox.children[1].children = [self.delMod]

    def save(self)->str:

        self.name = self.namew.v_model

        self.linear.save()

        self.nonlinear.save()

        self.txt = ""

        self.txt += self.name+":\n"

        self.txt += "\t"

        if self.usesolver.v_model == False:
            self.txt += "#"

        self.txt += self.linear.solver_value()+"\n"

        self.txt += "\t"

        if self.usesolver.v_model == False:
            self.txt += "#"

        self.txt += self.nonlinear.solver_value()+"\n"

        for i in self.models:
            texte = i.save()
            ligne = texte.splitlines()
            for a in range(0,len(ligne)):
                self.txt += "\t"+ligne[a]+"\n"

        return self.txt

    def display(self):

        self.initialize()
        display(self.namew, self.usesolver)
        self.linear.display()
        self.nonlinear.display()
        display(self.vbox)

    def newsub(self):
        self.initialize()
        display(self.namew, self.usesolver)
        self.linear.display()
        self.nonlinear.display()
