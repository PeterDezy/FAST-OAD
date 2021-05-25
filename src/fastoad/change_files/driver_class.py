"""
Driver class
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
import openmdao.drivers as driver

class Driver:
    """
    A class which display the driver widgets
    """

    def __init__(self):

        # Text to return in the yaml file
        self.driver = None

        # Ipyvuetify widgets
        self.select = None

        self.generator = None

        self.selectDriver = None

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

        self.vboxgenerator = v.Html(
            tag="div",
            children=[
                v.Html(
                    tag="div", children=[]
                ),
            ],
        )

    def initialize(self):
        """
        All ipyvuetify widgets to display for the driver
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


    def save(self) -> str :
        """
        Return the text to write in the yaml file for the driver
        """

        self.driver = "# Definition of problem driver assuming the OpenMDAO convention \"import openmdao.api as om\"\n"
        self.driver += "driver: "
        if (self.selectDriver.v_model == "differential_evolution_driver"):
            self.driver += "om.DifferentialEvolutionDriver("
            self.driver += "max_gen=" + str(self.vboxdriver.children[0].children[0].v_model)
            self.driver += ",pop_size=" + str(self.vboxdriver.children[1].children[0].v_model)
            self.driver += ",run_parallel=" + str(self.vboxdriver.children[0].children[1].v_model)
            self.driver += ",procs_per_model=" + str(self.vboxdriver.children[1].children[1].v_model)
            self.driver += ",penalty_parameter=" + str(self.vboxdriver.children[0].children[2].v_model)
            self.driver += ",penalty_exponent=" + str(self.vboxdriver.children[1].children[2].v_model)
            self.driver += ",Pc=" + str(self.vboxdriver.children[0].children[3].v_model)
            self.driver += ",F=" + str(self.vboxdriver.children[1].children[3].v_model)
            self.driver += ",multi_obj_weights=" + str(self.vboxdriver.children[0].children[4].v_model)
            self.driver += ",multi_obj_exponent=" + str(self.vboxdriver.children[1].children[4].v_model) + ")"
        elif (self.selectDriver.v_model == "doe_driver"):
            if (self.generator.v_model == "DOEGenerator"):
                self.driver += ""
            elif (self.generator.v_model == "ListGenerator"):
                self.driver += ""
            elif (self.generator.v_model == "CSVGenerator"):
                self.driver += ""
            elif (self.generator.v_model == "UniformGenerator"):
                self.driver += ""
            elif (self.generator.v_model == "_pyDOE_Generator"):
                self.driver += ""
            elif (self.generator.v_model == "FullFactorialGenerator"):
                self.driver += ""
            elif (self.generator.v_model == "GeneralizedSubsetGenerator"):
                self.driver += ""
            elif (self.generator.v_model == "PlackettBurmanGenerator"):
                self.driver += ""
            elif (self.generator.v_model == "BoxBehnkenGenerator"):
                self.driver += ""
            elif (self.generator.v_model == "LatinHypercubeGenerator"):
                self.driver += ""
        elif (self.selectDriver.v_model == "genetic_algorithm_driver"):
            self.driver += "om.SimpleGADriver("
            self.driver += "bits=" + str(self.vboxdriver.children[0].children[0].v_model)
            self.driver += ",elitism=" + str(self.vboxdriver.children[1].children[0].v_model)
            self.driver += ",gray=" + str(self.vboxdriver.children[0].children[1].v_model)
            self.driver += ",cross_bits=" + str(self.vboxdriver.children[1].children[1].v_model)
            self.driver += ",max_gen=" + str(self.vboxdriver.children[0].children[2].v_model)
            self.driver += ",pop_size=" + str(self.vboxdriver.children[1].children[2].v_model)
            self.driver += ",run_parallel=" + str(self.vboxdriver.children[0].children[3].v_model)
            self.driver += ",procs_per_model=" + str(self.vboxdriver.children[1].children[3].v_model)
            self.driver += ",penalty_parameter=" + str(self.vboxdriver.children[0].children[4].v_model)
            self.driver += ",penalty_exponent=" + str(self.vboxdriver.children[1].children[4].v_model)
            self.driver += ",Pc=" + str(self.vboxdriver.children[0].children[5].v_model)
            self.driver += ",Pm=" + str(self.vboxdriver.children[1].children[5].v_model)
            self.driver += ",multi_obj_weights=" + str(self.vboxdriver.children[0].children[6].v_model)
            self.driver += ",multi_obj_exponent=" + str(self.vboxdriver.children[1].children[6].v_model)
            self.driver += ",compute_parato=" + str(self.vboxdriver.children[0].children[7].v_model) + ")"
        elif (self.selectDriver.v_model == "pyoptsparse_driver"):
            self.driver += "om.pyOptSparseDriver()"
        elif (self.selectDriver.v_model == "scipy_optimizer"):
            self.driver += "om.ScipyOptimizeDriver("
            self.driver += "optimizer=\'" + self.vboxdriver.children[0].children[0].v_model + "\'"
            self.driver += ",tol=" + str(self.vboxdriver.children[1].children[0].v_model)
            self.driver += ",maxiter=" + str(self.vboxdriver.children[0].children[1].v_model)
            self.driver += ",disp=" + str(self.vboxdriver.children[1].children[1].v_model) + ")"
        self.driver += "\n\n"
        self.driver += "# Definition of OpenMDAO model\n"
        self.driver += "# Although \"model\" is a mandatory name for the top level of the model, its\n"
        self.driver += "# sub-components can be freely named by user\n"
        return self.driver

    def display(self):
        """
        Call the necessary functions to display the widgets
        """

        self.initialize()