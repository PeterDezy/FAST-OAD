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

from IPython.display import clear_output, display
import ipywidgets as widgets
import ipyvuetify as v
from ruamel.yaml import YAML
import openmdao.drivers as driver


class ChangeConfigFile:
    """
    A class which display all the widgets for the configuration file
    """

    def __init__(self):
        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()
        # Parameters config file
        self.inputf = None
        self.outputf = None
        self.title = None
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
        self.button = v.Html(
            tag="div",
            class_="d-flex justify-center mb-6",
            children=[
                v.Html(
                    tag="div", children=[]
                ),
            ],
        )
        self.generator = v.Html(
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
        self.title = content["title"]

        self.inputf = self.inputf[2 : len(self.inputf) - 4]

        self.outputf = self.outputf[2 : len(self.outputf) - 4]

    def save(self):
        """
        Save the new values, and displays them
        """

        with open(self.file_name) as file:
            content = self.yaml.load(file)

            self.inputf = content["input_file"]
            self.outputf = content["output_file"]
            self.title = content["title"]

            self.inputf = self.inputf[2 : len(self.inputf) - 4]
            self.outputf = self.outputf[2 : len(self.outputf) - 4]

        try:
            content["input_file"] = "./" + self.i.v_model + ".xml"
            content["output_file"] = "./" + self.o.v_model + ".xml"
            content["title"] = self.t.v_model
            with open(self.file_name, "w") as file:
                self.yaml.dump(content, file)
                if (
                    self.inputf == self.i.v_model
                    and self.outputf == self.o.v_model
                    and self.title == self.t.v_model
                ):
                    print("Values inchanched.\n")
                else:
                    print("Successfuly changed values !\n")
                    print("Your new values :\n")
                    print("Input file : ./" + self.i.v_model + ".xml")
                    print("Output file : ./" + self.o.v_model + ".xml")
                    print("Title : " + self.t.v_model)
        except:
            raise ValueError("Error while modifying.\n")

    def _initialize_widgets(self):
        """
        Initialize the button widget
        """

        title = v.TextField(
            v_model=self.title,
            label="Title :",
            outlined=True,
            clearable=True,
            style_="margin-top:20px",
        )

        def title():

            display(title)


        input = v.TextField(
            v_model=self.inputf,
            label="Input_file :",
            suffix=".yml",
            outlined=True,
            clearable=True,
            style_="margin-top:5px",
        )

        output = v.TextField(
            v_model=self.outputf,
            label="Output_file :",
            suffix=".yml",
            outlined=True,
            clearable=True,
            style_="margin-top:5px",
        )


        def inputoutput():

            display(input, output)


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

        def drivers():

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
                class_="d-flex justify-center mb-6",
            )

            def scipy_optimizer_change():

                self.generator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vbox.children[0].children = [optimizers, maxiter]
                self.vbox.children[1].children = [tol, disp]


            drive = driver.differential_evolution_driver.DifferentialEvolutionDriver()

            style = {"description_width": "initial"}

            maxgen = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["max_gen"].get("value"),
                min=0,
                max=1000,
                description="Max generations :",
                style=style,
                disabled=False,
            )

            popsize = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["pop_size"].get("value"),
                min=0,
                max=100,
                description="Number of points in the GA :",
                style=style,
                disabled=False,
            )

            runparallel = widgets.Checkbox(
                value=drive.options.__dict__["_dict"]["run_parallel"].get("value"),
                description="Run parallel",
                disabled=False,
            )

            procspermodel = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["procs_per_model"].get("value"),
                min=drive.options.__dict__["_dict"]["procs_per_model"].get("lower"),
                max=100,
                description="Processors per model :",
                style=style,
                disabled=False,
            )

            penaltyparameter = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["penalty_parameter"].get("value"),
                min=drive.options.__dict__["_dict"]["penalty_parameter"].get("lower"),
                max=100,
                description="Penalty parameter :",
                style=style,
                disabled=False,
            )

            penaltyexponent = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["penalty_exponent"].get("value"),
                min=0,
                max=100,
                description="Penalty exponent :",
                style=style,
                disabled=False,
            )

            cross_prob = widgets.BoundedFloatText(
                value=drive.options.__dict__["_dict"]["Pc"].get("value"),
                min=drive.options.__dict__["_dict"]["Pc"].get("lower"),
                max=drive.options.__dict__["_dict"]["Pc"].get("upper"),
                description="Crossover probability :",
                style=style,
                disabled=False,
            )

            diff_rate = widgets.BoundedFloatText(
                value=drive.options.__dict__["_dict"]["F"].get("value"),
                min=drive.options.__dict__["_dict"]["F"].get("lower"),
                max=drive.options.__dict__["_dict"]["F"].get("upper"),
                description="Differential rate :",
                style=style,
                disabled=False,
            )

            multiobjweights = widgets.Text(
                value="{}", description="Multi objective weights :", style=style, disabled=False
            )

            multiobjexponent = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["multi_obj_exponent"].get("value"),
                min=drive.options.__dict__["_dict"]["multi_obj_exponent"].get("lower"),
                max=100,
                description="Multi-objective weighting exponent :",
                style=style,
                disabled=False,
            )

            def differential_evolution_driver_change():

                self.generator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vbox.children[0].children = [maxgen, runparallel, penaltyparameter, cross_prob, multiobjweights]
                self.vbox.children[1].children = [popsize, procspermodel, penaltyexponent, diff_rate, multiobjexponent]

            def doe_driver_change():

                self.vbox.children[0].children = []
                self.vbox.children[1].children = []
                self.button.children[0].children = []

                drive = driver.doe_driver.DOEDriver()

                style = {"description_width": "initial"}

                def onchangegenerator(widget, event, data):


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

                generator = v.Select(
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

                procspermodel = widgets.BoundedIntText(
                    value=drive.options.__dict__["_dict"]["procs_per_model"].get("value"),
                    min=drive.options.__dict__["_dict"]["procs_per_model"].get("lower"),
                    max=100,
                    description="Processors per model :",
                    style=style,
                    disabled=False,
                )

                runparallel = widgets.Checkbox(
                    value=drive.options.__dict__["_dict"]["run_parallel"].get("value"),
                    description="Run parallel",
                    disabled=False,
                )

                drive = driver.doe_generators.DOEGenerator()

                def doe_generator():

                    self.vboxdoedriver.children[0].children = [procspermodel]
                    self.vboxdoedriver.children[1].children = [runparallel]

                drive = driver.doe_generators.ListGenerator()

                _data = widgets.Text(
                    value="[]",
                    description="List of collections of name :",
                    style=style,
                    disabled=False,
                )

                def list_generator():

                    self.vboxdoedriver.children[0].children = [_data, runparallel]
                    self.vboxdoedriver.children[1].children = [procspermodel]


                _filename = widgets.Text(
                    description="File name  :",
                )

                def csv_generator():

                    self.vboxdoedriver.children[0].children = [_filename, runparallel]
                    self.vboxdoedriver.children[1].children = [procspermodel]

                drive = driver.doe_generators.UniformGenerator()

                _num_samples = widgets.BoundedIntText(
                    value=drive.__dict__["_num_samples"],
                    min=0,
                    max=100,
                    description="Number of samples :",
                    style=style,
                    disabled=False,
                )

                _seed = widgets.BoundedIntText(
                    value=drive.__dict__["_seed"],
                    min=0,
                    max=100,
                    description="Seed  :",
                    disabled=False,
                )

                def uniform_generator():

                    self.vboxdoedriver.children[0].children = [_num_samples, procspermodel]
                    self.vboxdoedriver.children[1].children = [_seed, runparallel]


                drive = driver.doe_generators._pyDOE_Generator()

                def onchangelevels(change):

                    if generator.v_model == '_pyDOE_Generator':
                        drive = drive = driver.doe_generators._pyDOE_Generator()

                        if change["new"] == "Int":

                            _levelspydoe = widgets.BoundedIntText(
                                value=drive.__dict__["_levels"],
                                description="Levels  :",
                                min=0,
                                max=1000,
                                disabled=False,
                            )

                        elif change["new"] == "Dict":

                            _levelspydoe = widgets.Text(
                                value="[]", description="Levels  :", disabled=False
                            )

                        self.vboxdoedriver.children[1].children = [_levelspydoe, procspermodel]

                    elif generator.v_model == 'FullFactorialGenerator':
                        drive = driver.doe_generators.FullFactorialGenerator()

                        if change["new"] == "Int":

                            _levelsfull = widgets.BoundedIntText(
                                value=drive.__dict__["_levels"],
                                description="Levels  :",
                                min=0,
                                max=1000,
                                disabled=False,
                            )

                        elif change["new"] == "Dict":

                            _levelsfull = widgets.Text(
                                value="[]", description="Levels  :", disabled=False
                            )

                        self.vboxdoedriver.children[1].children = [_levelsfull, procspermodel]

                    elif generator.v_model == 'PlackettBurmanGenerator':
                        drive = driver.doe_generators.PlackettBurmanGenerator()

                        if change["new"] == "Int":

                            _levelsplackett = widgets.BoundedIntText(
                                value=drive.__dict__["_levels"],
                                description="Levels  :",
                                min=0,
                                max=1000,
                                disabled=False,
                            )

                        elif change["new"] == "Dict":

                            _levelsplackett = widgets.Text(
                                value="[]", description="Levels  :", disabled=False
                            )

                        self.vboxdoedriver.children[1].children = [_levelsplackett, procspermodel]

                    elif generator.v_model == 'BoxBehnkenGenerator':
                        drive = driver.doe_generators.BoxBehnkenGenerator()

                        if change["new"] == "Int":

                            _levelsbox = widgets.BoundedIntText(
                                value=drive.__dict__["_levels"],
                                description="Levels  :",
                                min=0,
                                max=1000,
                                disabled=False,
                            )

                        elif change["new"] == "Dict":

                            _levelsbox = widgets.Text(
                                value="[]", description="Levels  :", disabled=False
                            )

                        self.vboxdoedriver.children[1].children = [_levelsbox, procspermodel]


                selectlevels = widgets.RadioButtons(
                    options=["Int", "Dict"],
                    value="Int",
                    description="Levels type  :",
                    disabled=False,
                )

                selectlevels.observe(onchangelevels, names="value")


                _levelspydoe = widgets.BoundedIntText(
                    value=drive.__dict__["_levels"],
                    description="Levels  :",
                    min=0,
                    max=1000,
                    disabled=False,
                )

                _sizes = widgets.BoundedIntText(
                    value=drive.__dict__["_sizes"],
                    min=0,
                    max=100,
                    description="Sizes  :",
                    disabled=False,
                )

                def pydoe_generator():

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizes, runparallel]
                    self.vboxdoedriver.children[1].children = [_levelspydoe, procspermodel]


                drive = driver.doe_generators.FullFactorialGenerator()


                _levelsfull = widgets.BoundedIntText(
                    value=drive.__dict__["_levels"],
                    description="Levels  :",
                    min=0,
                    max=1000,
                    disabled=False,
                )

                _sizes = widgets.BoundedIntText(
                    value=drive.__dict__["_sizes"],
                    min=0,
                    max=100,
                    description="Sizes  :",
                    disabled=False,
                )

                def full_factorial_generator():

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizes, runparallel]
                    self.vboxdoedriver.children[1].children = [_levelsfull, procspermodel]


                def generalized_subset_generator():

                    self.vboxdoedriver.children[0].children = [procspermodel]
                    self.vboxdoedriver.children[1].children = [runparallel]

                drive = driver.doe_generators.PlackettBurmanGenerator()


                _levelsplackett = widgets.BoundedIntText(
                    value=drive.__dict__["_levels"],
                    description="Levels  :",
                    min=0,
                    max=1000,
                    disabled=False,
                )

                _sizes = widgets.BoundedIntText(
                    value=drive.__dict__["_sizes"],
                    min=0,
                    max=100,
                    description="Sizes  :",
                    disabled=False,
                )

                def plackett_burman_generator():

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizes, runparallel]
                    self.vboxdoedriver.children[1].children = [_levelsplackett, procspermodel]


                drive = driver.doe_generators.BoxBehnkenGenerator()

                _levelsbox = widgets.BoundedIntText(
                    value=drive.__dict__["_levels"],
                    description="Levels  :",
                    min=0,
                    max=1000,
                    disabled=False,
                )

                _sizes = widgets.BoundedIntText(
                    value=drive.__dict__["_sizes"],
                    min=0,
                    max=100,
                    description="Sizes  :",
                    disabled=False,
                )

                _center = widgets.BoundedIntText(
                    value=drive.__dict__["_center"],
                    min=0,
                    max=100,
                    description="Center  :",
                    disabled=False,
                )

                def box_behnken_generator():

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizes, procspermodel]
                    self.vboxdoedriver.children[1].children = [_levelsbox, _center, runparallel]


                drive = driver.doe_generators.LatinHypercubeGenerator()

                _samples = widgets.BoundedIntText(
                    value=drive.__dict__["_samples"],
                    min=0,
                    max=100,
                    description="Number of samples to generate :",
                    style=style,
                    disabled=False,
                )

                _criterion = v.Select(
                    items=["None", "center", "maximin", "centermaximin", "correlation"],
                    v_model=drive.__dict__["_criterion"],
                    label="Criterion :",
                    filled=True,
                    shaped=True,
                    style_="width:500px;",
                )

                _iterations = widgets.BoundedIntText(
                    value=drive.__dict__["_iterations"],
                    min=0,
                    max=100,
                    description="Iterations  :",
                    disabled=False,
                )

                _seed = widgets.BoundedIntText(
                    value=drive.__dict__["_seed"],
                    min=0,
                    max=100,
                    description="Seed :",
                    disabled=False,
                )

                def latin_hypercube_generator():

                    self.vboxdoedriver.children[0].children = [_samples, _iterations, procspermodel]
                    self.vboxdoedriver.children[1].children = [_criterion, _seed, runparallel]


                generator.on_event("change", onchangegenerator)
                doe_generator()
                self.generator.children[0].children = [generator]
                self.button.children[0].children = [btn]


            drive = driver.genetic_algorithm_driver.SimpleGADriver()

            style = {"description_width": "initial"}

            bits = widgets.Text(
                value="{}",
                description="Number of bits of resolution :",
                style=style,
                disabled=False,
            )

            elitism = widgets.Checkbox(
                value=drive.options.__dict__["_dict"]["elitism"].get("value"),
                description="Elitism",
                disabled=False,
            )

            gray = widgets.Checkbox(
                value=drive.options.__dict__["_dict"]["gray"].get("value"),
                description="Gray",
                disabled=False,
            )

            crossbits = widgets.Checkbox(
                value=drive.options.__dict__["_dict"]["cross_bits"].get("value"),
                description="Cross bits",
                disabled=False,
            )

            maxgen = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["max_gen"].get("value"),
                min=0,
                max=1000,
                description="Number of generations :",
                style=style,
                disabled=False,
            )

            popsize = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["pop_size"].get("value"),
                min=0,
                max=100,
                description="Number of points in the GA :",
                style=style,
                disabled=False,
            )

            runparallel = widgets.Checkbox(
                value=drive.options.__dict__["_dict"]["run_parallel"].get("value"),
                description="Run parallel",
                disabled=False,
            )

            procspermodel = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["procs_per_model"].get("value"),
                min=drive.options.__dict__["_dict"]["procs_per_model"].get("lower"),
                max=100,
                description="Processors per model :",
                style=style,
                disabled=False,
            )

            penaltyparameter = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["penalty_parameter"].get("value"),
                min=drive.options.__dict__["_dict"]["penalty_parameter"].get("lower"),
                max=100,
                description="Penalty parameter :",
                style=style,
                disabled=False,
            )

            penaltyexponent = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["penalty_exponent"].get("value"),
                min=0,
                max=100,
                description="Penalty exponent :",
                style=style,
                disabled=False,
            )

            cross_prob = widgets.BoundedFloatText(
                value=drive.options.__dict__["_dict"]["Pc"].get("value"),
                min=drive.options.__dict__["_dict"]["Pc"].get("lower"),
                max=drive.options.__dict__["_dict"]["Pc"].get("upper"),
                description="Crossover probability :",
                style=style,
                disabled=False,
            )

            mut_rate = widgets.BoundedFloatText(
                value=drive.options.__dict__["_dict"]["Pm"].get("value"),
                min=drive.options.__dict__["_dict"]["Pm"].get("lower"),
                max=drive.options.__dict__["_dict"]["Pm"].get("upper"),
                description="Mutation rate :",
                style=style,
                disabled=False,
            )

            multiobjweights = widgets.Text(
                value="{}", description="Multi objective weights :", style=style, disabled=False
            )

            multiobjexponent = widgets.BoundedIntText(
                value=drive.options.__dict__["_dict"]["multi_obj_exponent"].get("value"),
                min=drive.options.__dict__["_dict"]["multi_obj_exponent"].get("lower"),
                max=100,
                description="Multi-objective weighting exponent :",
                style=style,
                disabled=False,
            )

            computepareto = widgets.Checkbox(
                value=drive.options.__dict__["_dict"]["compute_pareto"].get("value"),
                description="Compute pareto",
                disabled=False,
            )

            def genetic_algorithm_driver_change():

                self.generator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vbox.children[0].children = [bits, gray, maxgen, runparallel, penaltyparameter, cross_prob, multiobjweights, computepareto]
                self.vbox.children[1].children = [elitism, crossbits, popsize, procspermodel, penaltyexponent, mut_rate, multiobjexponent]

            def pyoptsparse_driver_change():

                self.generator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vbox.children[0].children = []
                self.vbox.children[1].children = []


            def onchange(widget, event, data):

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

            select = v.Select(
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

            select.on_event("change", onchange)

            display(select)
            scipy_optimizer_change()
            display(self.vbox)
            display(self.generator)
            display(self.vboxdoedriver)
            button()
            display(self.button)

        title()
        inputoutput()
        drivers()

    def display(self):
        """
        Display the user interface
        :return the display object
        """
        clear_output(wait=True)
        self.read()
        self._initialize_widgets()
