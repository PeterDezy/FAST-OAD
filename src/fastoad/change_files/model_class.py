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

from IPython.display import display
import ipyvuetify as v
from fastoad.change_files.linear_solver_class import LinearSolver
from fastoad.change_files.non_linear_solver_class import NonLinearSolver

class Model:
    """
    A class which display the model widgets ( nonlinear & linear solver, subgroup, component )
    """

    def __init__(self, name):

        # Name of the model
        self.name = name

        # Widget TextField to change the name of the model
        self.namew = None

        # Widget checkbox to use solver or not
        self.usesolver = None

        # A variable which take the linear solver class
        self.linear = None

        # A variable which take the nonlinear solver class
        self.nonlinear = None

        # Widget button to add a subgroup
        self.addMod = None

        # List of the models
        self.models = []

        # List of the components
        self.components = []

        # The text to write on the yaml file
        self.txt = ""

        # Vbox to display several widgets and hide them
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

        # Call the initialize function
        self.initialize()

    def initialize(self):
        """
        All ipyvuetify widgets to display for the model
        """

        self.namew = v.TextField(
            v_model=self.name,
            label="Name :",
            outlined=True,
            style_="margin-top:20px",
        )

        self.usesolver = v.Checkbox(
            v_model=True,
            label='Use solver',
            style_="margin-bottom:10px; margin-left:10px;",
        )

        if self.namew.v_model == 'model':
            self.namew.readonly = True

        self.linear = LinearSolver()

        self.nonlinear = NonLinearSolver()

        def disabled (widget, event, data):
            """
            Disabled linear & nonlinear solver widgets if you don't use it
            """

            if self.usesolver.v_model == False:
                self.linear.expansionPanel.disabled = True
                self.nonlinear.expansionPanel.disabled = True
            else:
                self.linear.expansionPanel.disabled = False
                self.nonlinear.expansionPanel.disabled = False


        self.usesolver.on_event("change", disabled)

        self.addMod = v.Btn(
            color="blue",
            elevation=4,
            style_="width:240px",
            outlined=True,
            children=["Add subgroup"],
        )

        def on_addMod_button_clicked (widget, event, data):
            """
            Display the widgets for each subgroup ( until 10 )
            """

            if (len(self.models) != 10):
                self.models.append(Model(self.name+ str(len(self.models)+1)))
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

        self.vbox.children = [self.addMod]

    def save(self)->str:
        """
        Return the text to write in the yaml file for the model
        """

        self.name = self.namew.v_model

        self.linear.save()

        self.nonlinear.save()

        self.txt = ""

        self.txt += self.name+":\n"

        self.txt += "\t"

        if self.usesolver.v_model == False:
            self.txt += "# "

        self.txt += self.linear.solver_value()+"\n"

        self.txt += "\t"

        if self.usesolver.v_model == False:
            self.txt += "# "

        self.txt += self.nonlinear.solver_value()+"\n"

        for i in self.models:
            texte = i.save()
            ligne = texte.splitlines()
            for a in range(0,len(ligne)):
                self.txt += "\t"+ligne[a]+"\n"

        return self.txt

    def display(self):
        """
        Display all widgets for the model
        """

        display(self.namew, self.usesolver)
        self.linear.display()
        self.nonlinear.display()
        display(self.vbox)