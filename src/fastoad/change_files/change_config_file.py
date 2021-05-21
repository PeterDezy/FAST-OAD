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

        self.vboxtext = v.Html(
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

        def drivers():
            """
            Initialize widgets for drivers
            """

            drive = driver.scipy_optimizer.ScipyOptimizeDriver()

            optimizers = v.Select(
                items=list(drive.options.__dict__["_dict"]["optimizer"].get("values")),
                v_model=drive.options.__dict__["_dict"]["optimizer"].get("value"),
                label="Optimizers :",
                outlined=True,
                style_="width:500px;margin-top:5px",
            )

            tol = v.TextField(
                v_model=drive.options.__dict__["_dict"]["tol"].get("value"),
                min=drive.options.__dict__["_dict"]["tol"].get("lower"),
                max=1,
                label="Tol :",
                type="number",
                outlined=True,
                style_="width:500px;margin-left:50px;margin-top:6px",
            )

            maxiter = v.TextField(
                v_model=drive.options.__dict__["_dict"]["maxiter"].get("value"),
                min=drive.options.__dict__["_dict"]["maxiter"].get("lower"),
                max=1000,
                label="Maxiter :",
                type="number",
                outlined=True,
            )

            disp = v.Checkbox(
                v_model=drive.options.__dict__["_dict"]["disp"].get("value"),
                label="Disp",
                style_="margin-left:50px",
            )

            def scipy_optimizer_change():
                """
                Adapt widgets & vbox widgets to only display widgets you need in this driver
                """

                self.vboxgenerator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vboxdriver.children[0].children = [optimizers, maxiter]
                self.vboxdriver.children[1].children = [tol, disp]


            drive = driver.differential_evolution_driver.DifferentialEvolutionDriver()
            

            maxgendiff = v.TextField(
                v_model=drive.options.__dict__["_dict"]["max_gen"].get("value"),
                min=0,
                max=1000,
                label="Max generations :",
                type='number',
                outlined=True,
                style_='width:500px;margin-top:5px'
            )

            popsizediff = v.TextField(
                v_model=drive.options.__dict__["_dict"]["pop_size"].get("value"),
                min=0,
                max=100,
                label="Number of points in the GA :",
                type="number",
                outlined=True,
                style_='width:500px;margin-left:50px;margin-top:5px'
            )

            runparalleldiff = v.Checkbox(
                v_model=drive.options.__dict__["_dict"]["run_parallel"].get("value"),
                label="Run parallel",
                style_='margin-bottom:20px'
            )

            procspermodeldiff = v.TextField(
                v_model=drive.options.__dict__["_dict"]["procs_per_model"].get("value"),
                min=drive.options.__dict__["_dict"]["procs_per_model"].get("lower"),
                max=100,
                label="Processors per model :",
                type="number",
                outlined=True,
                style_='width:500px;margin-left:50px'
            )

            penaltyparameterdiff = v.TextField(
                v_model=drive.options.__dict__["_dict"]["penalty_parameter"].get("value"),
                min=drive.options.__dict__["_dict"]["penalty_parameter"].get("lower"),
                max=100,
                label="Penalty parameter :",
                type="number",
                outlined=True,
                style_='width:500px'
            )

            penaltyexponentdiff = v.TextField(
                v_model=drive.options.__dict__["_dict"]["penalty_exponent"].get("value"),
                min=0,
                max=100,
                label="Penalty exponent :",
                type="number",
                outlined=True,
                style_='width:500px;margin-left:50px'
            )

            cross_probdiff = v.TextField(
                v_model=drive.options.__dict__["_dict"]["Pc"].get("value"),
                min=drive.options.__dict__["_dict"]["Pc"].get("lower"),
                max=drive.options.__dict__["_dict"]["Pc"].get("upper"),
                label="Crossover probability :",
                type="number",
                outlined=True,
                style_='width:500px'
            )

            diff_rate = v.TextField(
                v_model=drive.options.__dict__["_dict"]["F"].get("value"),
                min=drive.options.__dict__["_dict"]["F"].get("lower"),
                max=drive.options.__dict__["_dict"]["F"].get("upper"),
                label="Differential rate :",
                type="number",
                outlined=True,
                style_='width:500px;margin-left:50px'
            )

            multiobjweightsdiff = v.TextField(
                v_model="{}",
                label="Multi objective weights :",
                outlined=True,
                style_='width:500px'
            )

            multiobjexponentdiff = v.TextField(
                v_model=drive.options.__dict__["_dict"]["multi_obj_exponent"].get("value"),
                min=drive.options.__dict__["_dict"]["multi_obj_exponent"].get("lower"),
                max=100,
                label="Multi-objective weighting exponent :",
                type="number",
                outlined=True,
                style_='width:500px;margin-left:50px'
            )

            def differential_evolution_driver_change():
                """
                Adapt widgets & vbox widgets to only display widgets you need in this driver
                """

                self.vboxgenerator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vboxdriver.children[0].children = [maxgendiff, runparalleldiff, penaltyparameterdiff, cross_probdiff, multiobjweightsdiff]
                self.vboxdriver.children[1].children = [popsizediff, procspermodeldiff, penaltyexponentdiff, diff_rate, multiobjexponentdiff]

            def doe_driver_change():
                """
                Adapt widgets & vbox widgets to only display widgets you need in this driver
                """

                self.vboxdriver.children[0].children = []
                self.vboxdriver.children[1].children = []

                drive = driver.doe_driver.DOEDriver()

                def onchangegenerator(widget, event, data):
                    """
                    A function which start the function you need for your generator
                    """

                    if data == "DOEGenerator":
                        doe_generator()
                    elif data == "ListGenerator":
                        list_generator()
                    elif data == "CSVGenerator":
                        csv_generator()
                    elif data == "UniformGenerator":
                        uniform_generator()
                    elif data == "_pyDOE_Generator":
                        pydoe_generator()
                    elif data == "FullFactorialGenerator":
                        full_factorial_generator()
                    elif data == "GeneralizedSubsetGenerator":
                        generalized_subset_generator()
                    elif data == "PlackettBurmanGenerator":
                        plackett_burman_generator()
                    elif data == "BoxBehnkenGenerator":
                        box_behnken_generator()
                    elif data == "LatinHypercubeGenerator":
                        latin_hypercube_generator()

                self.generator = v.Select(
                    items=[
                        "DOEGenerator",
                        "ListGenerator",
                        "CSVGenerator",
                        "UniformGenerator",
                        "_pyDOE_Generator",
                        "FullFactorialGenerator",
                        "GeneralizedSubsetGenerator",
                        "PlackettBurmanGenerator",
                        "BoxBehnkenGenerator",
                        "LatinHypercubeGenerator",
                    ],
                    v_model="DOEGenerator",
                    label="Generator :",
                    outlined=True,
                    style_="width:500px;margin-top:5px",
                )

                self.vboxgenerator.children[0].children = [self.generator]
                self.generator.on_event("change", onchangegenerator)

                procspermodeldoe = v.TextField(
                    v_model=drive.options.__dict__["_dict"]["procs_per_model"].get("value"),
                    min=drive.options.__dict__["_dict"]["procs_per_model"].get("lower"),
                    max=100,
                    label="Processors per model :",
                    outlined=True,
                    type='number',
                    style_='width:500px;margin-top:5px'
                )

                runparalleldoe = v.Checkbox(
                    v_model=drive.options.__dict__["_dict"]["run_parallel"].get("value"),
                    label="Run parallel",
                    outlined=True,
                    type='number',
                    style_='width:500px;margin-left:50px'
                )

                drive = driver.doe_generators.DOEGenerator()

                def doe_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [procspermodeldoe]
                    self.vboxdoedriver.children[1].children = [runparalleldoe]

                drive = driver.doe_generators.ListGenerator()

                _data = v.TextField(
                    v_model="[]",
                    label="List of collections of name :",
                    outlined=True,
                    style_='width:500px;margin-top:5px'
                )

                def list_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [_data, runparalleldoe]
                    self.vboxdoedriver.children[1].children = [procspermodeldoe]


                _filename = v.TextField(
                    label="File name  :",
                    outlined=True,
                    style_='width:500px;margin-top:5px'
                )

                def csv_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [_filename, runparalleldoe]
                    self.vboxdoedriver.children[1].children = [procspermodeldoe]

                drive = driver.doe_generators.UniformGenerator()

                _num_samples = v.TextField(
                    v_model=drive.__dict__["_num_samples"],
                    min=0,
                    max=100,
                    label="Number of samples :",
                    outlined=True,
                    type='number',
                    style_='width:500px;margin-top:5px'
                )

                _seeduniform = v.TextField(
                    v_model=drive.__dict__["_seed"],
                    min=0,
                    max=100,
                    label="Seed :",
                    outlined=True,
                    type='number',
                    style_='width:500px;margin-left:50px;margin-top:5px',
                )

                def uniform_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [_num_samples, procspermodeldoe]
                    self.vboxdoedriver.children[1].children = [_seeduniform, runparalleldoe]


                drive = driver.doe_generators._pyDOE_Generator()

                def onchangelevels(widget, event, data):
                    """
                    A function which change the type of the levels widget ( Int or Dict )
                    """

                    if self.generator.v_model == '_pyDOE_Generator':
                        drive = drive = driver.doe_generators._pyDOE_Generator()

                        if data == "Int":

                            _levelspydoe = v.TextField(
                                v_model=drive.__dict__["_levels"],
                                label="Levels  :",
                                min=0,
                                max=1000,
                                outlined=True,
                                type='number',
                                style_='width:500px;margin-top:27px'
                            )

                        elif data == "Dict":

                            _levelspydoe = v.TextField(
                                v_model="[]",
                                label="Levels  :",
                                outlined=True,
                                style_='width:500px;margin-top:27px'
                            )

                        self.vboxdoedriver.children[1].children = [_levelspydoe, procspermodeldoe]

                    elif self.generator.v_model == 'FullFactorialGenerator':
                        drive = driver.doe_generators.FullFactorialGenerator()

                        if data == "Int":

                            _levelsfull = v.TextField(
                                v_model=drive.__dict__["_levels"],
                                label="Levels  :",
                                min=0,
                                max=1000,
                                outlined=True,
                                type='number',
                                style_='width:500px;margin-top:27px'
                            )

                        elif data == "Dict":

                            _levelsfull = v.TextField(
                                v_model="[]",
                                label="Levels  :",
                                outlined=True,
                                style_='width:500px;margin-top:27px'
                            )

                        self.vboxdoedriver.children[1].children = [_levelsfull, procspermodeldoe]

                    elif self.generator.v_model == 'PlackettBurmanGenerator':
                        drive = driver.doe_generators.PlackettBurmanGenerator()

                        if data == "Int":

                            _levelsplackett = v.TextField(
                                v_model=drive.__dict__["_levels"],
                                label="Levels  :",
                                min=0,
                                max=1000,
                                outlined=True,
                                type='number',
                                style_='width:500px;margin-top:27px'
                            )

                        elif data == "Dict":

                            _levelsplackett = v.TextField(
                                v_model="[]",
                                label="Levels  :",
                                outlined=True,
                                style_='width:500px;margin-top:27px'
                            )

                        self.vboxdoedriver.children[1].children = [_levelsplackett, procspermodeldoe]

                    elif self.generator.v_model == 'BoxBehnkenGenerator':
                        drive = driver.doe_generators.BoxBehnkenGenerator()

                        if data == "Int":

                            _levelsbox = v.TextField(
                                v_model=drive.__dict__["_levels"],
                                label="Levels  :",
                                min=0,
                                max=1000,
                                outlined=True,
                                type='number',
                                style_='width:500px;margin-top:27px'
                            )

                        elif data == "Dict":

                            _levelsbox = v.TextField(
                                v_model="[]",
                                label="Levels  :",
                                outlined=True,
                                style_='width:500px;margin-top:27px'
                            )

                        self.vboxdoedriver.children[1].children = [_levelsbox, procspermodeldoe]


                selectlevels = v.RadioGroup(
                    children=[
                        v.Radio(label='Int', value='Int'),
                        v.Radio(label='Dict', value='Dict'),
                    ],
                    v_model="Int",
                    label="Levels type  :",
                )

                selectlevels.on_event('change', onchangelevels)


                _levelspydoe = v.TextField(
                    v_model=drive.__dict__["_levels"],
                    label="Levels  :",
                    min=0,
                    max=1000,
                    outlined=True,
                    type='number',
                    style_='width:500px;margin-top:27px'
                )

                _sizespy = v.TextField(
                    v_model=drive.__dict__["_sizes"],
                    min=0,
                    max=100,
                    label="Sizes  :",
                    outlined=True,
                    type='number',
                    style_='width:500px'
                )

                def pydoe_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizespy, runparalleldoe]
                    self.vboxdoedriver.children[1].children = [_levelspydoe, procspermodeldoe]


                drive = driver.doe_generators.FullFactorialGenerator()

                _levelsfull = v.TextField(
                    v_model=drive.__dict__["_levels"],
                    label="Levels  :",
                    min=0,
                    max=1000,
                    outlined=True,
                    type='number',
                    style_='width:500px;margin-top:27px'
                )

                _sizesfull = v.TextField(
                    v_model=drive.__dict__["_sizes"],
                    min=0,
                    max=100,
                    label="Sizes  :",
                    outlined=True,
                    type='number',
                    style_='width:500px'
                )

                def full_factorial_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizesfull, runparalleldoe]
                    self.vboxdoedriver.children[1].children = [_levelsfull, procspermodeldoe]


                def generalized_subset_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [procspermodeldoe]
                    self.vboxdoedriver.children[1].children = [runparalleldoe]

                drive = driver.doe_generators.PlackettBurmanGenerator()

                _levelsplackett = v.TextField(
                    v_model=drive.__dict__["_levels"],
                    label="Levels  :",
                    min=0,
                    max=1000,
                    outlined=True,
                    type='number',
                    style_='width:500px;margin-top:27px'
                )

                _sizesplackett = v.TextField(
                    v_model=drive.__dict__["_sizes"],
                    min=0,
                    max=100,
                    label="Sizes  :",
                    outlined=True,
                    type='number',
                    style_='width:500px'
                )

                def plackett_burman_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizesplackett, runparalleldoe]
                    self.vboxdoedriver.children[1].children = [_levelsplackett, procspermodeldoe]


                drive = driver.doe_generators.BoxBehnkenGenerator()

                _levelsbox = v.TextField(
                    v_model=drive.__dict__["_levels"],
                    label="Levels  :",
                    min=0,
                    max=1000,
                    outlined=True,
                    type='number',
                    style_='width:500px;margin-top:27px;margin-left:50px'
                )

                _sizesbox = v.TextField(
                    v_model=drive.__dict__["_sizes"],
                    min=0,
                    max=100,
                    label="Sizes  :",
                    outlined=True,
                    type='number',
                    style_='width:500px'
                )

                _center = v.TextField(
                    v_model=drive.__dict__["_center"],
                    min=0,
                    max=100,
                    label="Center  :",
                    type='number',
                    outlined=True,
                    style_='width:500px;margin-top:5px;margin-left:50px'
                )

                def box_behnken_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizesbox, procspermodeldoe]
                    self.vboxdoedriver.children[1].children = [_levelsbox, _center, runparalleldoe]


                drive = driver.doe_generators.LatinHypercubeGenerator()

                _samples = v.TextField(
                    v_model=drive.__dict__["_samples"],
                    min=0,
                    max=100,
                    label="Number of samples to generate :",
                    type='number',
                    outlined=True,
                    style_="width:500px;margin-top:5px",
                )

                _criterion = v.Select(
                    items=["None", "center", "maximin", "centermaximin", "correlation"],
                    v_model=drive.__dict__["_criterion"],
                    label="Criterion :",
                    outlined=True,
                    style_="width:500px;margin-top:5px;margin-left:50px",
                )

                _iterations = v.TextField(
                    v_model=drive.__dict__["_iterations"],
                    min=0,
                    max=100,
                    label="Iterations  :",
                    outlined=True,
                    type='number',
                    style_="width:500px;margin-top:5px",
                )

                _seedlatin = v.TextField(
                    v_model=drive.__dict__["_seed"],
                    min=0,
                    max=100,
                    label="Seed :",
                    outlined=True,
                    type='number',
                    style_="width:500px;margin-top:5px;margin-left:50px",
                )

                def latin_hypercube_generator():
                    """
                    Adapt widgets & vbox widgets to only display widgets you need in this generator
                    """

                    self.vboxdoedriver.children[0].children = [_samples, _iterations, procspermodeldoe]
                    self.vboxdoedriver.children[1].children = [_criterion, _seedlatin, runparalleldoe]

                doe_generator()


            drive = driver.genetic_algorithm_driver.SimpleGADriver()


            bits = v.TextField(
                v_model="{}",
                label="Number of bits of resolution :",
                outlined=True,
                style_='width:500px;margin-top:5px',
            )

            elitism = v.Checkbox(
                v_model=drive.options.__dict__["_dict"]["elitism"].get("value"),
                label="Elitism",
                style_='width:500px;margin-left:50px;margin-bottom:40px',
            )

            gray = v.Checkbox(
                v_model=drive.options.__dict__["_dict"]["gray"].get("value"),
                label="Gray",
                style_='width:500px;margin-bottom:20px',
            )

            crossbits = v.Checkbox(
                v_model=drive.options.__dict__["_dict"]["cross_bits"].get("value"),
                label="Cross bits",
                style_='width:500px;margin-left:50px;margin-bottom:20px',
            )

            maxgengenetic = v.TextField(
                v_model=drive.options.__dict__["_dict"]["max_gen"].get("value"),
                min=0,
                max=1000,
                label="Number of generations :",
                type='number',
                outlined=True,
                style_='width:500px',
            )

            popsizegenetic = v.TextField(
                v_model=drive.options.__dict__["_dict"]["pop_size"].get("value"),
                min=0,
                max=100,
                label="Number of points in the GA :",
                type='number',
                outlined=True,
                style_='width:500px;margin-left:50px',
            )

            runparallelgenetic = v.Checkbox(
                v_model=drive.options.__dict__["_dict"]["run_parallel"].get("value"),
                label="Run parallel",
                style_='width:500px;margin-bottom:20px',
            )

            procspermodelgenetic = v.TextField(
                v_model=drive.options.__dict__["_dict"]["procs_per_model"].get("value"),
                min=drive.options.__dict__["_dict"]["procs_per_model"].get("lower"),
                max=100,
                label="Processors per model :",
                type='number',
                outlined=True,
                style_='width:500px;margin-left:50px',
            )

            penaltyparametergenetic = v.TextField(
                v_model=drive.options.__dict__["_dict"]["penalty_parameter"].get("value"),
                min=drive.options.__dict__["_dict"]["penalty_parameter"].get("lower"),
                max=100,
                label="Penalty parameter :",
                type='number',
                outlined=True,
                style_='width:500px',
            )

            penaltyexponentgenetic = v.TextField(
                v_model=drive.options.__dict__["_dict"]["penalty_exponent"].get("value"),
                min=0,
                max=100,
                label="Penalty exponent :",
                type='number',
                outlined=True,
                style_='width:500px;margin-left:50px',
            )

            cross_probgenetic = v.TextField(
                v_model=drive.options.__dict__["_dict"]["Pc"].get("value"),
                min=drive.options.__dict__["_dict"]["Pc"].get("lower"),
                max=drive.options.__dict__["_dict"]["Pc"].get("upper"),
                label="Crossover probability :",
                type='number',
                outlined=True,
                style_='width:500px',
            )

            mut_rate = v.TextField(
                v_model=drive.options.__dict__["_dict"]["Pm"].get("value"),
                min=drive.options.__dict__["_dict"]["Pm"].get("lower"),
                max=drive.options.__dict__["_dict"]["Pm"].get("upper"),
                label="Mutation rate :",
                type='number',
                outlined=True,
                style_='width:500px;margin-left:50px',
            )

            multiobjweightsgenetic = v.TextField(
                v_model="{}",
                label="Multi objective weights :",
                outlined=True,
                style_='width:500px',
            )

            multiobjexponentgenetic = v.TextField(
                v_model=drive.options.__dict__["_dict"]["multi_obj_exponent"].get("value"),
                min=drive.options.__dict__["_dict"]["multi_obj_exponent"].get("lower"),
                max=100,
                label="Multi-objective weighting exponent :",
                type='number',
                outlined=True,
                style_='width:500px;margin-left:50px',
            )

            computepareto = v.Checkbox(
                v_model=drive.options.__dict__["_dict"]["compute_pareto"].get("value"),
                label="Compute pareto",
                style_='width:500px',
            )

            def genetic_algorithm_driver_change():
                """
                Adapt widgets & vbox widgets to only display widgets you need in this driver
                """

                self.vboxgenerator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vboxdriver.children[0].children = [bits, gray, maxgengenetic, runparallelgenetic, penaltyparametergenetic, cross_probgenetic, multiobjweightsgenetic, computepareto]
                self.vboxdriver.children[1].children = [elitism, crossbits, popsizegenetic, procspermodelgenetic, penaltyexponentgenetic, mut_rate, multiobjexponentgenetic]

            def pyoptsparse_driver_change():
                """
                Adapt widgets & vbox widgets to only display widgets you need in this driver
                """

                self.vboxgenerator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vboxdriver.children[0].children = []
                self.vboxdriver.children[1].children = []


            def onchange(widget, event, data):
                """
                A function which start the function you need for your driver
                """

                if data == "scipy_optimizer":
                    scipy_optimizer_change()
                elif data == "differential_evolution_driver":
                    differential_evolution_driver_change()
                elif data == "doe_driver":
                    doe_driver_change()
                elif data == "genetic_algorithm_driver":
                    genetic_algorithm_driver_change()
                elif data == "pyoptsparse_driver":
                    pyoptsparse_driver_change()

            self.selectDriver = v.Select(
                items=[
                    "differential_evolution_driver",
                    "doe_driver",
                    "genetic_algorithm_driver",
                    "pyoptsparse_driver",
                    "scipy_optimizer",
                ],
                v_model="scipy_optimizer",
                label="Driver :",
                outlined=True,
                style_="margin-top:5px",
            )

            self.selectDriver.on_event("change", onchange)


            panel = v.ExpansionPanel(
                children=[
                    v.ExpansionPanelHeader(
                        color='#eaeaea',
                        children=['Driver'],
                        style_='margin-bottom:25px;'
                    ),
                    v.ExpansionPanelContent(
                        children=[self.selectDriver,self.vboxdriver,self.vboxgenerator,self.vboxdoedriver]
                    ),
                ]
            )

            expansionPanel = v.ExpansionPanels(
                focusable=True,
                children=[panel],
            )

            display(expansionPanel)
            scipy_optimizer_change()

        title()
        inputoutput()
        drivers()
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
