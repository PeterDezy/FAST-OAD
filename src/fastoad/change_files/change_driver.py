"""
Change the driver in the configuration file
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

from IPython.display import clear_output, display, HTML
import ipywidgets as widgets
import ipyvuetify as v
import openmdao.drivers as driver
from ruamel.yaml import YAML


class ChangeDriver:
    """
    A class to change the driver in the configuration file
    """
    def __init__(self):
        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()

        # Css
        self.css = "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;} "
        self.css += ".green {background-color: lightgreen;} </style>"
        self.html = HTML(self.css)


    def scipy_optimizer_change(self):

        drive = driver.scipy_optimizer.ScipyOptimizeDriver()

        self.optimizers = widgets.Dropdown(
            options=drive.options.__dict__['_dict']['optimizer'].get('values'),
            value=drive.options.__dict__['_dict']['optimizer'].get('value'),
            description='Optimizers :',
        )

        self.tol = widgets.BoundedFloatText(
            value=drive.options.__dict__['_dict']['tol'].get('value'),
            min=drive.options.__dict__['_dict']['tol'].get('lower'),
            max=1,
            description='Tol :',
            disabled=False
        )

        self.maxiter = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['maxiter'].get('value'),
            min=drive.options.__dict__['_dict']['maxiter'].get('lower'),
            max=1000,
            description='Maxiter :',
            disabled=False
        )

        self.disp = widgets.Checkbox(
            value=drive.options.__dict__['_dict']['disp'].get('value'),
            description='Disp',
            disabled=False,
            indent=True
        )

        left_box = widgets.VBox([self.optimizers, self.maxiter])
        right_box = widgets.VBox([self.tol, self.disp])
        self.vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        self.maxiter.add_class("top")

        # Right Widgets
        self.disp.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")
        self.vbox.add_class("top")

        display(self.vbox)

    def differential_evolution_driver_change(self):

        drive = driver.differential_evolution_driver.DifferentialEvolutionDriver()

        style = {'description_width': 'initial'}

        self.maxgen = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['max_gen'].get('value'),
            min=0,
            max=1000,
            description='Max generations :',
            style=style,
            disabled=False
        )

        self.popsize = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['pop_size'].get('value'),
            min=0,
            max=100,
            description='Number of points in the GA :',
            style=style,
            disabled=False
        )

        self.runparallel = widgets.Checkbox(
            value=drive.options.__dict__['_dict']['run_parallel'].get('value'),
            description='Run parallel',
            disabled=False,
        )

        self.procspermodel = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['procs_per_model'].get('value'),
            min=drive.options.__dict__['_dict']['procs_per_model'].get('lower'),
            max=100,
            description='Processors per model :',
            style=style,
            disabled=False
        )

        self.penaltyparameter = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['penalty_parameter'].get('value'),
            min=drive.options.__dict__['_dict']['penalty_parameter'].get('lower'),
            max=100,
            description='Penalty parameter :',
            style=style,
            disabled=False
        )

        self.penaltyexponent = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['penalty_exponent'].get('value'),
            min=0,
            max=100,
            description='Penalty exponent :',
            style=style,
            disabled=False
        )

        self.pc = widgets.BoundedFloatText(
            value=drive.options.__dict__['_dict']['Pc'].get('value'),
            min=drive.options.__dict__['_dict']['Pc'].get('lower'),
            max=drive.options.__dict__['_dict']['Pc'].get('upper'),
            description='Crossover probability :',
            style=style,
            disabled=False
        )

        self.dr = widgets.BoundedFloatText(
            value=drive.options.__dict__['_dict']['F'].get('value'),
            min=drive.options.__dict__['_dict']['F'].get('lower'),
            max=drive.options.__dict__['_dict']['F'].get('upper'),
            description='Differential rate :',
            style=style,
            disabled=False
        )

        self.multiobjweights = widgets.Text(
            value='{}',
            description='Multi objective weights :',
            style=style,
            disabled=False
        )

        self.multiobjexponent = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['multi_obj_exponent'].get('value'),
            min=drive.options.__dict__['_dict']['multi_obj_exponent'].get('lower'),
            max=100,
            description='Multi-objective weighting exponent :',
            style=style,
            disabled=False
        )

        left_box = widgets.VBox([self.maxgen, self.runparallel, self.penaltyparameter, self.pc, self.multiobjweights])
        right_box = widgets.VBox([self.popsize, self.procspermodel, self.penaltyexponent, self.dr, self.multiobjexponent])
        self.vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        self.runparallel.add_class("top")
        self.penaltyparameter.add_class("top")
        self.pc.add_class("top")
        self.multiobjweights.add_class("top")

        # Right Widgets
        self.procspermodel.add_class("top")
        self.penaltyexponent.add_class("top")
        self.dr.add_class("top")
        self.multiobjexponent.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        self.vbox.add_class("top")

        display(self.vbox)

    def doe_driver_change(self):

        drive = driver.doe_driver.DOEDriver()

        style = {'description_width': 'initial'}

        def onchangegenerator(change):

            clear_output(wait=True)
            display(self.select, self.generator, self.html)

            if change['new'] == 'DOEGenerator':
                DOEGenerator(self)
            elif change['new'] == 'ListGenerator':
                ListGenerator(self)
            elif change['new'] == 'CSVGenerator':
                CSVGenerator(self)
            elif change['new'] == 'UniformGenerator':
                UniformGenerator(self)
            elif change['new'] == '_pyDOE_Generator':
                _pyDOE_Generator(self)
            elif change['new'] == 'FullFactorialGenerator':
                FullFactorialGenerator(self)
            elif change['new'] == 'GeneralizedSubsetGenerator':
                GeneralizedSubsetGenerator(self)
            elif change['new'] == 'PlackettBurmanGenerator':
                PlackettBurmanGenerator(self)
            elif change['new'] == 'BoxBehnkenGenerator':
                BoxBehnkenGenerator(self)
            elif change['new'] == 'LatinHypercubeGenerator':
                LatinHypercubeGenerator(self)

        self.generator = widgets.Dropdown(
            options=['DOEGenerator', 'ListGenerator', 'CSVGenerator', 'UniformGenerator', '_pyDOE_Generator',
                     'FullFactorialGenerator',
                     'GeneralizedSubsetGenerator', 'PlackettBurmanGenerator', 'BoxBehnkenGenerator',
                     'LatinHypercubeGenerator'],
            value='DOEGenerator',
            description='Generator :',
        )

        self.procspermodel = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['procs_per_model'].get('value'),
            min=drive.options.__dict__['_dict']['procs_per_model'].get('lower'),
            max=100,
            description='Processors per model :',
            style=style,
            disabled=False
        )

        self.runparallel = widgets.Checkbox(
            value=drive.options.__dict__['_dict']['run_parallel'].get('value'),
            description='Run parallel',
            disabled=False,
        )

        def DOEGenerator(self):

            drive = driver.doe_generators.DOEGenerator()

            left_box = widgets.VBox([self.procspermodel])
            right_box = widgets.VBox([self.runparallel])
            self.vbox = widgets.HBox([left_box, right_box])

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            display(self.vbox)

        def ListGenerator(self):

            drive = driver.doe_generators.ListGenerator()

            self._data = widgets.Text(
                value='[]',
                description='List of collections of name :',
                style=style,
                disabled=False
            )

            left_box = widgets.VBox([self._data, self.runparallel])
            right_box = widgets.VBox([self.procspermodel])
            self.vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            self.runparallel.add_class("top")

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            display(self.vbox)

        def CSVGenerator(self):

            self._filename = widgets.Text(
                description='File name  :',
                disabled=False
            )

            left_box = widgets.VBox([self._filename, self.runparallel])
            right_box = widgets.VBox([self.procspermodel])
            self.vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            self.runparallel.add_class("top")

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            display(self.vbox)

        def UniformGenerator(self):

            drive = driver.doe_generators.UniformGenerator()

            self._num_samples = widgets.BoundedIntText(
                value=drive.__dict__['_num_samples'],
                min=0,
                max=100,
                description='Number of samples :',
                style=style,
                disabled=False
            )

            self._seed = widgets.BoundedIntText(
                value=drive.__dict__['_seed'],
                min=0,
                max=100,
                description='Seed  :',
                disabled=False
            )

            left_box = widgets.VBox([self._num_samples, self.procspermodel])
            right_box = widgets.VBox([self._seed, self.runparallel])
            self.vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            self.procspermodel.add_class("top")

            # Right Widgets
            self.runparallel.add_class("top")

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            display(self.vbox)

        def _pyDOE_Generator(self):

            drive = driver.doe_generators._pyDOE_Generator()

            def onchangelevels(change):

                if change['new'] == 'Int':

                    self._levels = widgets.BoundedIntText(
                        value=drive.__dict__['_levels'],
                        description='Levels  :',
                        min=0,
                        max=1000,
                        disabled=False
                    )

                elif change['new'] == 'Dict':

                    self._levels = widgets.Text(
                        value='[]',
                        description='Levels  :',
                        disabled=False
                    )

                clear_output(wait=True)

                left_box = widgets.VBox([self.selectlevels, self._sizes, self.runparallel])
                right_box = widgets.VBox([self._levels, self.procspermodel])
                self.vbox = widgets.HBox([left_box, right_box])

                # left Widgets
                self._sizes.add_class("top")
                self.runparallel.add_class("top")

                # Right Widgets
                self.procspermodel.add_class("top")

                # VBox & Button Widgets
                self.vbox.add_class("top")
                left_box.add_class("left")
                left_box.add_class("right")
                self.vbox.add_class("top")

                display(self.select, self.generator, self.vbox, self.html)

            self.selectlevels = widgets.RadioButtons(
                options=['Int', 'Dict'],
                value='Int',
                description='Levels type  :',
                disabled=False
            )

            self._levels = widgets.BoundedIntText(
                value=drive.__dict__['_levels'],
                description='Levels  :',
                min=0,
                max=1000,
                disabled=False
            )

            self._sizes = widgets.BoundedIntText(
                value=drive.__dict__['_sizes'],
                min=0,
                max=100,
                description='Sizes  :',
                disabled=False
            )

            left_box = widgets.VBox([self.selectlevels, self._sizes, self.runparallel])
            right_box = widgets.VBox([self._levels, self.procspermodel])
            self.vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            self._sizes.add_class("top")
            self.runparallel.add_class("top")

            # Right Widgets
            self.procspermodel.add_class("top")

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            self.selectlevels.observe(onchangelevels, names='value')
            display(self.vbox)

        def FullFactorialGenerator(self):

            drive = driver.doe_generators.FullFactorialGenerator()

            def onchangelevels(change):

                if change['new'] == 'Int':

                    self._levels = widgets.BoundedIntText(
                        value=drive.__dict__['_levels'],
                        description='Levels  :',
                        min=0,
                        max=1000,
                        disabled=False
                    )

                elif change['new'] == 'Dict':

                    self._levels = widgets.Text(
                        value='[]',
                        description='Levels  :',
                        disabled=False
                    )

                clear_output(wait=True)

                left_box = widgets.VBox([self.selectlevels, self._sizes, self.runparallel])
                right_box = widgets.VBox([self._levels, self.procspermodel])
                self.vbox = widgets.HBox([left_box, right_box])

                # left Widgets
                self._sizes.add_class("top")
                self.runparallel.add_class("top")

                # Right Widgets
                self.procspermodel.add_class("top")

                # VBox & Button Widgets
                self.vbox.add_class("top")
                left_box.add_class("left")
                left_box.add_class("right")
                self.vbox.add_class("top")

                display(self.select, self.generator, self.vbox, self.html)

            self.selectlevels = widgets.RadioButtons(
                options=['Int', 'Dict'],
                value='Int',
                description='Levels type  :',
                disabled=False
            )

            self._levels = widgets.BoundedIntText(
                value=drive.__dict__['_levels'],
                description='Levels  :',
                min=0,
                max=1000,
                disabled=False
            )

            self._sizes = widgets.BoundedIntText(
                value=drive.__dict__['_sizes'],
                min=0,
                max=100,
                description='Sizes  :',
                disabled=False
            )

            left_box = widgets.VBox([self.selectlevels, self._sizes, self.runparallel])
            right_box = widgets.VBox([self._levels, self.procspermodel])
            self.vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            self._sizes.add_class("top")
            self.runparallel.add_class("top")

            # Right Widgets
            self.procspermodel.add_class("top")

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            self.selectlevels.observe(onchangelevels, names='value')
            display(self.vbox)

        def GeneralizedSubsetGenerator(self):

            print("Not finished")

            left_box = widgets.VBox([self.procspermodel])
            right_box = widgets.VBox([self.runparallel])
            self.vbox = widgets.HBox([left_box, right_box])

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            display(self.vbox)

        def PlackettBurmanGenerator(self):

            drive = driver.doe_generators.PlackettBurmanGenerator()

            def onchangelevels(change):

                if change['new'] == 'Int':

                    self._levels = widgets.BoundedIntText(
                        value=drive.__dict__['_levels'],
                        description='Levels  :',
                        min=0,
                        max=1000,
                        disabled=False
                    )

                elif change['new'] == 'Dict':

                    self._levels = widgets.Text(
                        value='[]',
                        description='Levels  :',
                        disabled=False
                    )

                clear_output(wait=True)

                left_box = widgets.VBox([self.selectlevels, self._sizes, self.runparallel])
                right_box = widgets.VBox([self._levels, self.procspermodel])
                self.vbox = widgets.HBox([left_box, right_box])

                # left Widgets
                self._sizes.add_class("top")
                self.runparallel.add_class("top")

                # Right Widgets
                self.procspermodel.add_class("top")

                # VBox & Button Widgets
                self.vbox.add_class("top")
                left_box.add_class("left")
                left_box.add_class("right")
                self.vbox.add_class("top")

                display(self.select, self.generator, self.vbox, self.html)

            self.selectlevels = widgets.RadioButtons(
                options=['Int', 'Dict'],
                value='Int',
                description='Levels type  :',
                disabled=False
            )

            self._levels = widgets.BoundedIntText(
                value=drive.__dict__['_levels'],
                description='Levels  :',
                min=0,
                max=1000,
                disabled=False
            )

            self._sizes = widgets.BoundedIntText(
                value=drive.__dict__['_sizes'],
                min=0,
                max=100,
                description='Sizes  :',
                disabled=False
            )

            left_box = widgets.VBox([self.selectlevels, self._sizes, self.runparallel])
            right_box = widgets.VBox([self._levels, self.procspermodel])
            self.vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            self._sizes.add_class("top")
            self.runparallel.add_class("top")

            # Right Widgets
            self.procspermodel.add_class("top")

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            self.selectlevels.observe(onchangelevels, names='value')
            display(self.vbox)

        def BoxBehnkenGenerator(self):

            drive = driver.doe_generators.BoxBehnkenGenerator()

            def onchangelevels(change):

                if change['new'] == 'Int':

                    self._levels = widgets.BoundedIntText(
                        value=drive.__dict__['_levels'],
                        description='Levels  :',
                        min=0,
                        max=1000,
                        disabled=False
                    )

                elif change['new'] == 'Dict':

                    self._levels = widgets.Text(
                        value='[]',
                        description='Levels  :',
                        disabled=False
                    )

                clear_output(wait=True)

                left_box = widgets.VBox([self.selectlevels, self._sizes, self.procspermodel])
                right_box = widgets.VBox([self._levels, self._center, self.runparallel])
                self.vbox = widgets.HBox([left_box, right_box])

                # left Widgets
                self._sizes.add_class("top")
                self.procspermodel.add_class("top")

                # Right Widgets
                self._center.add_class("top")
                self.runparallel.add_class("top")

                # VBox & Button Widgets
                self.vbox.add_class("top")
                left_box.add_class("left")
                left_box.add_class("right")
                self.vbox.add_class("top")

                display(self.select, self.generator, self.vbox, self.html)

            self.selectlevels = widgets.RadioButtons(
                options=['Int', 'Dict'],
                value='Int',
                description='Levels type  :',
                disabled=False
            )

            self._levels = widgets.BoundedIntText(
                value=drive.__dict__['_levels'],
                description='Levels  :',
                min=0,
                max=1000,
                disabled=False
            )

            self._sizes = widgets.BoundedIntText(
                value=drive.__dict__['_sizes'],
                min=0,
                max=100,
                description='Sizes  :',
                disabled=False
            )

            self._center = widgets.BoundedIntText(
                value=drive.__dict__['_center'],
                min=0,
                max=100,
                description='Center  :',
                disabled=False
            )

            left_box = widgets.VBox([self.selectlevels, self._sizes, self.procspermodel])
            right_box = widgets.VBox([self._levels, self._center, self.runparallel])
            self.vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            self._sizes.add_class("top")
            self.procspermodel.add_class("top")

            # Right Widgets
            self._center.add_class("top")
            self.runparallel.add_class("top")

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            self.selectlevels.observe(onchangelevels, names='value')
            display(self.vbox)

        def LatinHypercubeGenerator(self):

            drive = driver.doe_generators.LatinHypercubeGenerator()

            self._samples = widgets.BoundedIntText(
                value=drive.__dict__['_samples'],
                min=0,
                max=100,
                description='Number of samples to generate :',
                style=style,
                disabled=False
            )

            self._criterion = widgets.Dropdown(
                options=['None', 'center', 'maximin', 'centermaximin', 'correlation'],
                value=drive.__dict__['_criterion'],
                description='Criterion :',
            )

            self._iterations = widgets.BoundedIntText(
                value=drive.__dict__['_iterations'],
                min=0,
                max=100,
                description='Iterations  :',
                disabled=False
            )

            self._seed = widgets.BoundedIntText(
                value=drive.__dict__['_seed'],
                min=0,
                max=100,
                description='Seed :',
                disabled=False
            )

            left_box = widgets.VBox([self._samples, self._iterations, self.procspermodel])
            right_box = widgets.VBox([self._criterion, self._seed, self.runparallel])
            self.vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            self._iterations.add_class("top")
            self.procspermodel.add_class("top")

            # Right Widgets
            self._seed.add_class("top")
            self.runparallel.add_class("top")

            # VBox & Button Widgets
            self.vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            self.vbox.add_class("top")

            display(self.vbox)

        self.generator.observe(onchangegenerator, names='value')
        display(self.generator)
        DOEGenerator(self)

    def genetic_algorithm_driver_change(self):

        drive = driver.genetic_algorithm_driver.SimpleGADriver()

        style = {'description_width': 'initial'}

        self.bits = widgets.Text(
            value='{}',
            description='Number of bits of resolution :',
            style=style,
            disabled=False
        )

        self.elitism = widgets.Checkbox(
            value=drive.options.__dict__['_dict']['elitism'].get('value'),
            description='Elitism',
            disabled=False,
        )

        self.gray = widgets.Checkbox(
            value=drive.options.__dict__['_dict']['gray'].get('value'),
            description='Gray',
            disabled=False,
        )

        self.crossbits = widgets.Checkbox(
            value=drive.options.__dict__['_dict']['cross_bits'].get('value'),
            description='Cross bits',
            disabled=False,
        )

        self.maxgen = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['max_gen'].get('value'),
            min=0,
            max=1000,
            description='Number of generations :',
            style=style,
            disabled=False
        )

        self.popsize = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['pop_size'].get('value'),
            min=0,
            max=100,
            description='Number of points in the GA :',
            style=style,
            disabled=False
        )

        self.runparallel = widgets.Checkbox(
            value=drive.options.__dict__['_dict']['run_parallel'].get('value'),
            description='Run parallel',
            disabled=False,
        )

        self.procspermodel = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['procs_per_model'].get('value'),
            min=drive.options.__dict__['_dict']['procs_per_model'].get('lower'),
            max=100,
            description='Processors per model :',
            style=style,
            disabled=False
        )

        self.penaltyparameter = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['penalty_parameter'].get('value'),
            min=drive.options.__dict__['_dict']['penalty_parameter'].get('lower'),
            max=100,
            description='Penalty parameter :',
            style=style,
            disabled=False
        )

        self.penaltyexponent = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['penalty_exponent'].get('value'),
            min=0,
            max=100,
            description='Penalty exponent :',
            style=style,
            disabled=False
        )

        self.pc = widgets.BoundedFloatText(
            value=drive.options.__dict__['_dict']['Pc'].get('value'),
            min=drive.options.__dict__['_dict']['Pc'].get('lower'),
            max=drive.options.__dict__['_dict']['Pc'].get('upper'),
            description='Crossover probability :',
            style=style,
            disabled=False
        )

        self.pm = widgets.BoundedFloatText(
            value=drive.options.__dict__['_dict']['Pm'].get('value'),
            min=drive.options.__dict__['_dict']['Pm'].get('lower'),
            max=drive.options.__dict__['_dict']['Pm'].get('upper'),
            description='Mutation rate :',
            style=style,
            disabled=False
        )

        self.multiobjweights = widgets.Text(
            value='{}',
            description='Multi objective weights :',
            style=style,
            disabled=False
        )

        self.multiobjexponent = widgets.BoundedIntText(
            value=drive.options.__dict__['_dict']['multi_obj_exponent'].get('value'),
            min=drive.options.__dict__['_dict']['multi_obj_exponent'].get('lower'),
            max=100,
            description='Multi-objective weighting exponent :',
            style=style,
            disabled=False
        )

        self.computepareto = widgets.Checkbox(
            value=drive.options.__dict__['_dict']['compute_pareto'].get('value'),
            description='Compute pareto',
            disabled=False,
        )

        self.button = widgets.Button(
            description='Save',
            tooltip='Save',
            icon='save'
        )

        left_box = widgets.VBox([self.bits, self.gray, self.maxgen, self.runparallel, self.penaltyparameter, self.pc, self.multiobjweights, self.computepareto])
        right_box = widgets.VBox([self.elitism,self.crossbits, self.popsize, self.procspermodel,self.penaltyexponent, self.pm, self.multiobjexponent])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        self.gray.add_class("top")
        self.maxgen.add_class("top")
        self.runparallel.add_class("top")
        self.penaltyparameter.add_class("top")
        self.pc.add_class("top")
        self.multiobjweights.add_class("top")
        self.computepareto.add_class("top")

        # Right Widgets
        self.crossbits.add_class("top")
        self.popsize.add_class("top")
        self.procspermodel.add_class("top")
        self.penaltyexponent.add_class("top")
        self.pm.add_class("top")
        self.multiobjexponent.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        self.vbox.add_class("top")

        display(self.vbox)

    def pyoptsparse_driver_change(self):

        print("not finished")

    def changedriver(self):

        def onchange(change):


            display(self.select,self.html)

            if change['new'] == 'scipy_optimizer':
                self.scipy_optimizer_change()
            elif change['new'] == 'differential_evolution_driver':
                self.differential_evolution_driver_change()
            elif change['new'] == 'doe_driver':
                self.doe_driver_change()
            elif change['new'] == 'genetic_algorithm_driver':
                self.genetic_algorithm_driver_change()
            elif change['new'] == 'pyoptsparse_driver':
                self.pyoptsparse_driver_change()

        self.select = widgets.Dropdown(
            options=['differential_evolution_driver', 'doe_driver', 'genetic_algorithm_driver',
                     'pyoptsparse_driver', 'scipy_optimizer'],
            value='scipy_optimizer',
            description='Driver :',
        )

        self.select.observe(onchange, names='value')

        clear_output(wait=True)
        display(self.html)
        self.scipy_optimizer_change()

    def display(self, change=None) -> display:
        """
        Display the user interface
        :return the display object
        """
        clear_output(wait=True)
        self.changedriver()
        ui = widgets.VBox(
            [self.select]
        )
        return ui
