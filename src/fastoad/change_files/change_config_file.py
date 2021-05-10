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

                self.generator.children[0].children = []
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

                self.generator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vboxdriver.children[0].children = [maxgendiff, runparalleldiff, penaltyparameterdiff, cross_probdiff, multiobjweightsdiff]
                self.vboxdriver.children[1].children = [popsizediff, procspermodeldiff, penaltyexponentdiff, diff_rate, multiobjexponentdiff]

            def doe_driver_change():

                self.vboxdriver.children[0].children = []
                self.vboxdriver.children[1].children = []
                self.button.children[0].children = []

                drive = driver.doe_driver.DOEDriver()

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

                    self.vboxdoedriver.children[0].children = [_data, runparalleldoe]
                    self.vboxdoedriver.children[1].children = [procspermodeldoe]


                _filename = v.TextField(
                    label="File name  :",
                    outlined=True,
                    style_='width:500px;margin-top:5px'
                )

                def csv_generator():

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

                    self.vboxdoedriver.children[0].children = [_num_samples, procspermodeldoe]
                    self.vboxdoedriver.children[1].children = [_seeduniform, runparalleldoe]


                drive = driver.doe_generators._pyDOE_Generator()

                def onchangelevels(widget, event, data):

                    if generator.v_model == '_pyDOE_Generator':
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

                    elif generator.v_model == 'FullFactorialGenerator':
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

                    elif generator.v_model == 'PlackettBurmanGenerator':
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

                    elif generator.v_model == 'BoxBehnkenGenerator':
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

                    self.vboxdoedriver.children[0].children = [selectlevels, _sizesfull, runparalleldoe]
                    self.vboxdoedriver.children[1].children = [_levelsfull, procspermodeldoe]


                def generalized_subset_generator():

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

                    self.vboxdoedriver.children[0].children = [_samples, _iterations, procspermodeldoe]
                    self.vboxdoedriver.children[1].children = [_criterion, _seedlatin, runparalleldoe]


                generator.on_event("change", onchangegenerator)
                doe_generator()
                self.generator.children[0].children = [generator]
                self.button.children[0].children = [btn]


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

                self.generator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vboxdriver.children[0].children = [bits, gray, maxgengenetic, runparallelgenetic, penaltyparametergenetic, cross_probgenetic, multiobjweightsgenetic, computepareto]
                self.vboxdriver.children[1].children = [elitism, crossbits, popsizegenetic, procspermodelgenetic, penaltyexponentgenetic, mut_rate, multiobjexponentgenetic]

            def pyoptsparse_driver_change():

                self.generator.children[0].children = []
                self.vboxdoedriver.children[0].children = []
                self.vboxdoedriver.children[1].children = []
                self.vboxdriver.children[0].children = []
                self.vboxdriver.children[1].children = []


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
            display(self.vboxdriver)
            display(self.generator)
            display(self.vboxdoedriver)


    def display(self):
        """
        Display the user interface
        :return the display object
        """
        clear_output(wait=True)
        self.read()
        self._initialize_widgets()
