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
from ruamel.yaml import YAML
import openmdao.drivers as driver
import openmdao.solvers.nonlinear as solversnonlinear
import openmdao.solvers.linear as solvers
from fastoad.change_files.linear_solver_class import LinearSolver
from fastoad.change_files.non_linear_solver_class import NonLinearSolver


class ChangeConfigFile:
    """
    A class which display all widgets to change the configuration file
    """

    def __init__(self):
        # The path & name of the data file that will be viewed/edited
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml ( read the .yml file )
        self.yaml = YAML()
        
        # Parameters config file
        self.inputf = None

        self.outputf = None
        
        self.titlef = None

        self.input = None

        self.output = None

        self.title = None

        self.textfile = ""

        self.selectDriver = None

        self.generator = None

        self.linear = None

        self.nonlinear = None

        # Vbox to display several widgets and hide them
        self.vboxdriver = v.Html(
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

        self.vboxdoedriver = v.Html(
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

        self.vboxnonlinearsolver = v.Html(
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

        self.vboxaitken = v.Html(
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

        self.vboxsubsolves = v.Html(
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

        self.vboxlinearsolver = v.Html(
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

        self.vboxaitkenlinear = v.Html(
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

        self.button = v.Html(
            tag="div",
            class_="d-flex justify-center mb-6",
            children=[
                v.Html(
                    tag="div", children=[]
                ),
            ],
        )

        self.vboxgenerator = v.Html(
            tag="div",
            children=[
                v.Html(
                    tag="div", children=[]
                ),
            ],
        )


    def read(self):
        """
        Read the configuration file
        """

        with open(self.file_name) as file:
            content = self.yaml.load(file)

        self.inputf = content["input_file"]
        self.outputf = content["output_file"]
        self.titlef = content["title"]

        self.inputf = self.inputf[2 : len(self.inputf) - 4]

        self.outputf = self.outputf[2 : len(self.outputf) - 4]

    def save(self, widget, event, data):
        """
        Save the new values in the configuration file
        """

        with open(self.file_name) as file:
            content = self.yaml.load(file)

            self.inputf = content["input_file"]
            self.outputf = content["output_file"]
            self.titlef = content["title"]

            self.inputf = self.inputf[2 : len(self.inputf) - 4]
            self.outputf = self.outputf[2 : len(self.outputf) - 4]

        try:
            content["input_file"] = "./" + self.input.v_model + ".xml"
            content["output_file"] = "./" + self.output.v_model + ".xml"
            content["title"] = self.title.v_model
            if (self.selectDriver.v_model == "differential_evolution_driver"):
                content["driver"] = "om.DifferentialEvolutionDriver("
                content["driver"] += "max_gen="+str(self.vboxdriver.children[0].children[0].v_model)
                content["driver"] += ",pop_size="+str(self.vboxdriver.children[1].children[0].v_model)
                content["driver"] += ",run_parallel="+str(self.vboxdriver.children[0].children[1].v_model)
                content["driver"] += ",procs_per_model="+str(self.vboxdriver.children[1].children[1].v_model)
                content["driver"] += ",penalty_parameter="+str(self.vboxdriver.children[0].children[2].v_model)
                content["driver"] += ",penalty_exponent="+str(self.vboxdriver.children[1].children[2].v_model)
                content["driver"] += ",Pc="+str(self.vboxdriver.children[0].children[3].v_model)
                content["driver"] += ",F="+str(self.vboxdriver.children[1].children[3].v_model)
                content["driver"] += ",multi_obj_weights="+str(self.vboxdriver.children[0].children[4].v_model)
                content["driver"] += ",multi_obj_exponent="+str(self.vboxdriver.children[1].children[4].v_model)+")"
            elif (self.selectDriver.v_model == "doe_driver"):
                if (self.generator.v_model == "DOEGenerator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "ListGenerator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "CSVGenerator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "UniformGenerator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "_pyDOE_Generator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "FullFactorialGenerator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "GeneralizedSubsetGenerator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "PlackettBurmanGenerator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "BoxBehnkenGenerator"):
                    content["driver"] = ""
                elif (self.generator.v_model == "LatinHypercubeGenerator"):
                    content["driver"] = ""
            elif (self.selectDriver.v_model == "genetic_algorithm_driver"):
                content["driver"] = "om.SimpleGADriver("
                content["driver"] += "bits="+str(self.vboxdriver.children[0].children[0].v_model)
                content["driver"] += ",elitism="+str(self.vboxdriver.children[1].children[0].v_model)
                content["driver"] += ",gray="+str(self.vboxdriver.children[0].children[1].v_model)
                content["driver"] += ",cross_bits="+str(self.vboxdriver.children[1].children[1].v_model)
                content["driver"] += ",max_gen="+str(self.vboxdriver.children[0].children[2].v_model)
                content["driver"] += ",pop_size="+str(self.vboxdriver.children[1].children[2].v_model)
                content["driver"] += ",run_parallel="+str(self.vboxdriver.children[0].children[3].v_model)
                content["driver"] += ",procs_per_model="+str(self.vboxdriver.children[1].children[3].v_model)
                content["driver"] += ",penalty_parameter="+str(self.vboxdriver.children[0].children[4].v_model)
                content["driver"] += ",penalty_exponent="+str(self.vboxdriver.children[1].children[4].v_model)
                content["driver"] += ",Pc="+str(self.vboxdriver.children[0].children[5].v_model)
                content["driver"] += ",Pm="+str(self.vboxdriver.children[1].children[5].v_model)
                content["driver"] += ",multi_obj_weights="+str(self.vboxdriver.children[0].children[6].v_model)
                content["driver"] += ",multi_obj_exponent="+str(self.vboxdriver.children[1].children[6].v_model)
                content["driver"] += ",compute_parato="+str(self.vboxdriver.children[0].children[7].v_model)+")"
            elif (self.selectDriver.v_model == "pyoptsparse_driver"):
                content["driver"] = "om.pyOptSparseDriver()"
            elif (self.selectDriver.v_model == "scipy_optimizer"):
                content["driver"] = "om.ScipyOptimizeDriver("
                content["driver"] += "optimizer=\'" + self.vboxdriver.children[0].children[0].v_model + "\'"
                content["driver"] += ",tol="+str(self.vboxdriver.children[1].children[0].v_model)
                content["driver"] += ",maxiter="+str(self.vboxdriver.children[0].children[1].v_model)
                content["driver"] += ",disp="+str(self.vboxdriver.children[1].children[1].v_model)+")"
            with open(self.file_name, "w") as file:
                self.yaml.dump(content, file)

            success = v.Alert(
                type='success',
                children=['Successfuly changed values'],
                elevation='2',
            )

            with open(self.file_name, "r") as file:
                for i in range(20):
                    self.textfile += file.readline()

            display(success)
            display(Markdown("```yaml\n" + self.textfile + "\n```"))

        except:
            raise ValueError("Error while modifying.\n")

    def _initialize_widgets(self):
        """
        Initialize all widgets to display them
        """

        self.title = v.TextField(
            v_model=self.titlef,
            label="Title :",
            outlined=True,
            clearable=True,
            style_="margin-top:20px",
        )

        def title():
            """
            Display the title widget
            """

            display(self.title)


        self.input = v.TextField(
            v_model=self.inputf,
            label="Input_file :",
            suffix=".yml",
            outlined=True,
            clearable=True,
            style_="margin-top:5px",
        )

        self.output = v.TextField(
            v_model=self.outputf,
            label="Output_file :",
            suffix=".yml",
            outlined=True,
            clearable=True,
            style_="margin-top:5px",
        )


        def inputoutput():
            """
            Display the input & output widgets
            """

            display(self.input, self.output)


        btn = v.Btn(
            color="blue",
            elevation=4,
            style_="width:150px",
            outlined=True,
            children=[v.Icon(children=["get_app"]), "Save"],
        )

        btn.on_event("click", self.save)

        def button():
            """
            Display the save button widget
            """

            self.button.children[0].children = [btn]


        title()
        inputoutput()
        self.nonlinear = NonLinearSolver()
        self.nonlinear.display()
        self.linear = LinearSolver()
        self.linear.display()
        button()
        display(self.button)


    def display(self):
        """
        Read the configuration file, and display all widgets
        """

        clear_output(wait=True)
        self.read()
        self._initialize_widgets()
