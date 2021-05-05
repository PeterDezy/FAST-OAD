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

        def title():

            title = v.TextField(
                v_model=self.title,
                label="Title :",
                outlined=True,
                clearable=True,
                style_="margin-top:20px",
            )

            display(title)

        def inputoutput():

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

            display(input, output)

        def button():

            button = v.Btn(
                color="blue",
                elevation=4,
                style_="width:150px;margin:auto",
                outlined=True,
                children=[v.Icon(children=["get_app"]), "Save"],
            )

            def on_save_button_clicked(widget, event, data):
                self.save()

            button.on_event("click", on_save_button_clicked)

            display(button)

        def drivers():
            def scipy_optimizer_change():

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

                vbox = v.Html(
                    tag="div",
                    class_="d-flex justify-center mb-6",
                    children=[
                        v.Html(
                            tag="div", children=[optimizers, maxiter]
                        ),
                        v.Html(tag="div", children=[tol, disp]),
                    ],
                )

                display(vbox)
                button()

            def differential_evolution_driver_change():

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

                left_box = widgets.VBox(
                    [maxgen, runparallel, penaltyparameter, cross_prob, multiobjweights]
                )
                right_box = widgets.VBox(
                    [popsize, procspermodel, penaltyexponent, diff_rate, multiobjexponent]
                )
                vbox = widgets.HBox([left_box, right_box])

                display(vbox)
                button()

            def doe_driver_change():

                drive = driver.doe_driver.DOEDriver()

                style = {"description_width": "initial"}

                def onchangegenerator(widget, event, data):

                    clear_output(wait=True)
                    title()
                    inputoutput()
                    display(select)

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
                    filled=True,
                    shaped=True,
                    style_="width:500px;",
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

                def doe_generator():

                    drive = driver.doe_generators.DOEGenerator()

                    left_box = widgets.VBox([procspermodel])
                    right_box = widgets.VBox([runparallel])
                    vbox = widgets.HBox([left_box, right_box])

                    display(vbox)
                    button()

                def list_generator():

                    drive = driver.doe_generators.ListGenerator()

                    _data = widgets.Text(
                        value="[]",
                        description="List of collections of name :",
                        style=style,
                        disabled=False,
                    )

                    left_box = widgets.VBox([_data, runparallel])
                    right_box = widgets.VBox([procspermodel])
                    vbox = widgets.HBox([left_box, right_box])

                    display(vbox)
                    button()

                def csv_generator():

                    _filename = widgets.Text(description="File name  :", disabled=False)

                    left_box = widgets.VBox([_filename, runparallel])
                    right_box = widgets.VBox([procspermodel])
                    vbox = widgets.HBox([left_box, right_box])

                    display(vbox)
                    button()

                def uniform_generator():

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

                    left_box = widgets.VBox([_num_samples, procspermodel])
                    right_box = widgets.VBox([_seed, runparallel])
                    vbox = widgets.HBox([left_box, right_box])

                    display(vbox)
                    button()

                def pydoe_generator():

                    drive = driver.doe_generators._pyDOE_Generator()

                    def onchangelevels(change):

                        if change["new"] == "Int":

                            _levels = widgets.BoundedIntText(
                                value=drive.__dict__["_levels"],
                                description="Levels  :",
                                min=0,
                                max=1000,
                                disabled=False,
                            )

                        elif change["new"] == "Dict":

                            _levels = widgets.Text(
                                value="[]", description="Levels  :", disabled=False
                            )

                        clear_output(wait=True)
                        title()
                        inputoutput()
                        display(select)

                        left_box = widgets.VBox([selectlevels, _sizes, runparallel])
                        right_box = widgets.VBox([_levels, procspermodel])
                        vbox = widgets.HBox([left_box, right_box])

                        display(select, generator, vbox)
                        button()

                    selectlevels = widgets.RadioButtons(
                        options=["Int", "Dict"],
                        value="Int",
                        description="Levels type  :",
                        disabled=False,
                    )

                    _levels = widgets.BoundedIntText(
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

                    left_box = widgets.VBox([selectlevels, _sizes, runparallel])
                    right_box = widgets.VBox([_levels, procspermodel])
                    vbox = widgets.HBox([left_box, right_box])

                    selectlevels.observe(onchangelevels, names="value")
                    display(vbox)
                    button()

                def full_factorial_generator():

                    drive = driver.doe_generators.FullFactorialGenerator()

                    def onchangelevels(change):

                        if change["new"] == "Int":

                            _levels = widgets.BoundedIntText(
                                value=drive.__dict__["_levels"],
                                description="Levels  :",
                                min=0,
                                max=1000,
                                disabled=False,
                            )

                        elif change["new"] == "Dict":

                            _levels = widgets.Text(
                                value="[]", description="Levels  :", disabled=False
                            )

                        clear_output(wait=True)
                        title()
                        inputoutput()
                        display(select)

                        left_box = widgets.VBox([selectlevels, _sizes, runparallel])
                        right_box = widgets.VBox([_levels, procspermodel])
                        vbox = widgets.HBox([left_box, right_box])

                        display(select, generator, vbox)

                    selectlevels = widgets.RadioButtons(
                        options=["Int", "Dict"],
                        value="Int",
                        description="Levels type  :",
                        disabled=False,
                    )

                    _levels = widgets.BoundedIntText(
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

                    left_box = widgets.VBox([selectlevels, _sizes, runparallel])
                    right_box = widgets.VBox([_levels, procspermodel])
                    vbox = widgets.HBox([left_box, right_box])

                    selectlevels.observe(onchangelevels, names="value")
                    display(vbox)
                    button()

                def generalized_subset_generator():

                    left_box = widgets.VBox([procspermodel])
                    right_box = widgets.VBox([runparallel])
                    vbox = widgets.HBox([left_box, right_box])

                    display(vbox)
                    button()

                def plackett_burman_generator():

                    drive = driver.doe_generators.PlackettBurmanGenerator()

                    def onchangelevels(change):

                        if change["new"] == "Int":

                            _levels = widgets.BoundedIntText(
                                value=drive.__dict__["_levels"],
                                description="Levels  :",
                                min=0,
                                max=1000,
                                disabled=False,
                            )

                        elif change["new"] == "Dict":

                            _levels = widgets.Text(
                                value="[]", description="Levels  :", disabled=False
                            )

                        clear_output(wait=True)
                        title()
                        inputoutput()
                        display(select)

                        left_box = widgets.VBox([selectlevels, _sizes, runparallel])
                        right_box = widgets.VBox([_levels, procspermodel])
                        vbox = widgets.HBox([left_box, right_box])

                        display(select, generator, vbox)

                    selectlevels = widgets.RadioButtons(
                        options=["Int", "Dict"],
                        value="Int",
                        description="Levels type  :",
                        disabled=False,
                    )

                    _levels = widgets.BoundedIntText(
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

                    left_box = widgets.VBox([selectlevels, _sizes, runparallel])
                    right_box = widgets.VBox([_levels, procspermodel])
                    vbox = widgets.HBox([left_box, right_box])

                    selectlevels.observe(onchangelevels, names="value")
                    display(vbox)
                    button()

                def box_behnken_generator():

                    drive = driver.doe_generators.BoxBehnkenGenerator()

                    def onchangelevels(change):

                        if change["new"] == "Int":

                            _levels = widgets.BoundedIntText(
                                value=drive.__dict__["_levels"],
                                description="Levels  :",
                                min=0,
                                max=1000,
                                disabled=False,
                            )

                        elif change["new"] == "Dict":

                            _levels = widgets.Text(
                                value="[]", description="Levels  :", disabled=False
                            )

                        clear_output(wait=True)
                        title()
                        inputoutput()
                        display(select)

                        left_box = widgets.VBox([selectlevels, _sizes, procspermodel])
                        right_box = widgets.VBox([_levels, _center, runparallel])
                        vbox = widgets.HBox([left_box, right_box])

                        display(select, generator, vbox)

                    selectlevels = widgets.RadioButtons(
                        options=["Int", "Dict"],
                        value="Int",
                        description="Levels type  :",
                        disabled=False,
                    )

                    _levels = widgets.BoundedIntText(
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

                    left_box = widgets.VBox([selectlevels, _sizes, procspermodel])
                    right_box = widgets.VBox([_levels, _center, runparallel])
                    vbox = widgets.HBox([left_box, right_box])

                    selectlevels.observe(onchangelevels, names="value")
                    display(vbox)
                    button()

                def latin_hypercube_generator():

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

                    left_box = widgets.VBox([_samples, _iterations, procspermodel])
                    right_box = widgets.VBox([_criterion, _seed, runparallel])
                    vbox = widgets.HBox([left_box, right_box])

                    display(vbox)
                    button()

                generator.on_event("change", onchangegenerator)
                display(generator)
                doe_generator()

            def genetic_algorithm_driver_change():

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

                left_box = widgets.VBox(
                    [
                        bits,
                        gray,
                        maxgen,
                        runparallel,
                        penaltyparameter,
                        cross_prob,
                        multiobjweights,
                        computepareto,
                    ]
                )
                right_box = widgets.VBox(
                    [
                        elitism,
                        crossbits,
                        popsize,
                        procspermodel,
                        penaltyexponent,
                        mut_rate,
                        multiobjexponent,
                    ]
                )
                vbox = widgets.HBox([left_box, right_box])

                display(vbox)
                button()

            def pyoptsparse_driver_change():

                button()

            def onchange(widget, event, data):

                clear_output(wait=True)
                title()
                inputoutput()
                display(select)
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
