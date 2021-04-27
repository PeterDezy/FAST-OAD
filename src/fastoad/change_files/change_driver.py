from IPython.display import display
from IPython.display import clear_output
from ruamel.yaml import YAML
from fastoad.io.configuration.configuration import _YAMLSerializer
import openmdao.drivers as driver
import ipywidgets as widgets

css = "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;} .green {background-color: lightgreen;} </style>"
html = HTML(css)
display(html)


def scipy_optimizer_change():
    drive = driver.scipy_optimizer.ScipyOptimizeDriver()

    # print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['driver'] = 'om.ScipyOptimizeDriver'
            doc['driver'] += '(optimizer=\'' + optimizers.value + '\',tol=' + str(tol.value) + ',maxiter=' + str(
                maxiter.value)
            doc['driver'] += ',disp=' + str(disp.value) + ')'

            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    optimizers = widgets.Dropdown(
        options=drive.options.__dict__['_dict']['optimizer'].get('values'),
        value=drive.options.__dict__['_dict']['optimizer'].get('value'),
        description='Optimizers :',
    )

    tol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['tol'].get('value'),
        min=drive.options.__dict__['_dict']['tol'].get('lower'),
        max=1,
        description='Tol :',
        disabled=False
    )

    maxiter = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['maxiter'].get('value'),
        min=drive.options.__dict__['_dict']['maxiter'].get('lower'),
        max=1000,
        description='Maxiter :',
        disabled=False
    )

    disp = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['disp'].get('value'),
        description='Disp',
        disabled=False,
        indent=True
    )

    left_box = widgets.VBox([optimizers, maxiter])
    right_box = widgets.VBox([tol, disp])
    vbox = widgets.HBox([left_box, right_box])

    # Left Widgets
    maxiter.add_class("top")

    # Right Widgets
    disp.add_class("top")

    # VBox & Button Widgets
    vbox.add_class("top")
    left_box.add_class("left")
    vbox.add_class("top")
    button.add_class("top")
    button.add_class("green")

    display(vbox, button)

    button.on_click(save)


def differential_evolution_driver_change():
    drive = driver.differential_evolution_driver.DifferentialEvolutionDriver()

    #     print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['driver'] = 'om.DifferentialEvolutionDriver'
            doc['driver'] += '(max_gen=' + str(maxgen.value) + ',pop_size=' + str(
                popsize.value) + ',run_parallel=' + str(runparallel.value) + ',procs_per_model=' + str(
                procspermodel.value)
            doc['driver'] += ',penalty_parameter=' + str(penaltyparameter.value) + ',penalty_exponent=' + str(
                penaltyexponent.value)
            doc['driver'] += ',Pc=' + str(pc.value) + ',F=' + str(dr.value) + ',multi_obj_weights=' + str(
                multiobjweights.value) + ',multi_obj_exponent=' + str(multiobjexponent.value) + ')'

            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    style = {'description_width': 'initial'}

    maxgen = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['max_gen'].get('value'),
        min=0,
        max=1000,
        description='Max generations :',
        style=style,
        disabled=False
    )

    popsize = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['pop_size'].get('value'),
        min=0,
        max=100,
        description='Number of points in the GA :',
        style=style,
        disabled=False
    )

    runparallel = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['run_parallel'].get('value'),
        description='Run parallel',
        disabled=False,
    )

    procspermodel = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['procs_per_model'].get('value'),
        min=drive.options.__dict__['_dict']['procs_per_model'].get('lower'),
        max=100,
        description='Processors per model :',
        style=style,
        disabled=False
    )

    penaltyparameter = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['penalty_parameter'].get('value'),
        min=drive.options.__dict__['_dict']['penalty_parameter'].get('lower'),
        max=100,
        description='Penalty parameter :',
        style=style,
        disabled=False
    )

    penaltyexponent = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['penalty_exponent'].get('value'),
        min=0,
        max=100,
        description='Penalty exponent :',
        style=style,
        disabled=False
    )

    pc = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['Pc'].get('value'),
        min=drive.options.__dict__['_dict']['Pc'].get('lower'),
        max=drive.options.__dict__['_dict']['Pc'].get('upper'),
        description='Crossover probability :',
        style=style,
        disabled=False
    )

    dr = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['F'].get('value'),
        min=drive.options.__dict__['_dict']['F'].get('lower'),
        max=drive.options.__dict__['_dict']['F'].get('upper'),
        description='Differential rate :',
        style=style,
        disabled=False
    )

    multiobjweights = widgets.Text(
        value='{}',
        description='Multi objective weights :',
        style=style,
        disabled=False
    )

    multiobjexponent = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['multi_obj_exponent'].get('value'),
        min=drive.options.__dict__['_dict']['multi_obj_exponent'].get('lower'),
        max=100,
        description='Multi-objective weighting exponent :',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    left_box = widgets.VBox([maxgen, runparallel, penaltyparameter, pc, multiobjweights])
    right_box = widgets.VBox([popsize, procspermodel, penaltyexponent, dr, multiobjexponent])
    vbox = widgets.HBox([left_box, right_box])

    # left Widgets
    runparallel.add_class("top")
    penaltyparameter.add_class("top")
    pc.add_class("top")
    multiobjweights.add_class("top")

    # Right Widgets
    procspermodel.add_class("top")
    penaltyexponent.add_class("top")
    dr.add_class("top")
    multiobjexponent.add_class("top")

    # VBox & Button Widgets
    vbox.add_class("top")
    left_box.add_class("left")
    left_box.add_class("right")
    vbox.add_class("top")
    button.add_class("top")
    button.add_class("green")

    display(vbox, button)


def doe_driver_change():
    drive = driver.doe_driver.DOEDriver()

    #     print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['driver'] = 'om.DOEDriver'

            if generator.value == 'DOEGenerator':
                doc['driver'] += '(generator=' + str(generator.value)
            if generator.value == 'ListGenerator':
                doc['driver'] += '(generator=' + str(generator.value) + ',_data=' + str(_data.value)
            if generator.value == 'CSVGenerator':
                doc['driver'] += '(generator=' + str(generator.value) + ',_filename=' + str(_filename.value)
            if generator.value == 'UniformGenerator':
                doc['driver'] += '(generator=' + str(generator.value) + ',_num_samples=' + str(
                    _num_samples.value) + ',_seed=' + str(_seed.value)
            if generator.value == '_pyDOE_Generator':
                doc['driver'] += '(generator=' + str(generator.value) + ',_levels=' + str(
                    _levels.value) + ',_sizes=' + str(_sizes.value)
            if generator.value == 'FullFactorialGenerator':
                doc['driver'] += '(generator=' + str(generator.value) + ',_levels=' + str(
                    _levels.value) + ',_sizes=' + str(_sizes.value)
            if generator.value == 'GeneralizedSubsetGenerator':
                doc['driver'] += '(generator=' + str(generator.value)
            if generator.value == 'PlackettBurmanGenerator':
                doc['driver'] += '(generator=' + str(generator.value) + ',_levels=' + str(
                    _levels.value) + ',_sizes=' + str(_sizes.value)
            if generator.value == 'BoxBehnkenGenerator':
                doc['driver'] += '(generator=' + str(generator.value) + ',_levels=' + str(
                    _levels.value) + ',_sizes=' + str(_sizes.value) + ',_center=' + str(_center.value)
            if generator.value == 'LatinHypercubeGenerator':
                doc['driver'] += '(generator=' + str(generator.value) + ',_samples=' + str(
                    _samples.value) + ',_criterion=' + str(_criterion.value) + ',_iterations=' + str(
                    _iterations.value) + ',_seed=' + str(_seed.value)

            doc['driver'] += ',procs_per_model=' + str(procspermodel.value) + ',run_parallel=' + str(
                runparallel.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    style = {'description_width': 'initial'}

    def onchangegenerator(change):

        clear_output(wait=True)
        display(select, generator, html)

        if change['new'] == 'DOEGenerator':
            DOEGenerator()
        elif change['new'] == 'ListGenerator':
            ListGenerator()
        elif change['new'] == 'CSVGenerator':
            CSVGenerator()
        elif change['new'] == 'UniformGenerator':
            UniformGenerator()
        elif change['new'] == '_pyDOE_Generator':
            _pyDOE_Generator()
        elif change['new'] == 'FullFactorialGenerator':
            FullFactorialGenerator()
        elif change['new'] == 'GeneralizedSubsetGenerator':
            GeneralizedSubsetGenerator()
        elif change['new'] == 'PlackettBurmanGenerator':
            PlackettBurmanGenerator()
        elif change['new'] == 'BoxBehnkenGenerator':
            BoxBehnkenGenerator()
        elif change['new'] == 'LatinHypercubeGenerator':
            LatinHypercubeGenerator()

    generator = widgets.Dropdown(
        options=['DOEGenerator', 'ListGenerator', 'CSVGenerator', 'UniformGenerator', '_pyDOE_Generator',
                 'FullFactorialGenerator',
                 'GeneralizedSubsetGenerator', 'PlackettBurmanGenerator', 'BoxBehnkenGenerator',
                 'LatinHypercubeGenerator'],
        value='DOEGenerator',
        description='Generator :',
    )

    procspermodel = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['procs_per_model'].get('value'),
        min=drive.options.__dict__['_dict']['procs_per_model'].get('lower'),
        max=100,
        description='Processors per model :',
        style=style,
        disabled=False
    )

    runparallel = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['run_parallel'].get('value'),
        description='Run parallel',
        disabled=False,
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    def DOEGenerator():

        drive = driver.doe_generators.DOEGenerator()

        #         print(drive.__dict__)

        left_box = widgets.VBox([procspermodel])
        right_box = widgets.VBox([runparallel])
        vbox = widgets.HBox([left_box, right_box])

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("save_28")
        button.add_class("top")
        button.add_class("green")

        display(vbox, button)
        button.on_click(save)

    def ListGenerator():

        drive = driver.doe_generators.ListGenerator()

        #         print(drive.__dict__)

        global _data

        _data = widgets.Text(
            value='[]',
            description='List of collections of name :',
            style=style,
            disabled=False
        )

        left_box = widgets.VBox([_data, runparallel])
        right_box = widgets.VBox([procspermodel])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        runparallel.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        display(vbox, button)
        button.on_click(save)

    def CSVGenerator():

        #         print(drive.__dict__)

        global _filename

        _filename = widgets.Text(
            description='File name  :',
            disabled=False
        )

        left_box = widgets.VBox([_filename, runparallel])
        right_box = widgets.VBox([procspermodel])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        runparallel.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        display(vbox, button)
        button.on_click(save)

    def UniformGenerator():

        drive = driver.doe_generators.UniformGenerator()

        #         print(drive.__dict__)

        global _num_samples

        _num_samples = widgets.BoundedIntText(
            value=drive.__dict__['_num_samples'],
            min=0,
            max=100,
            description='Number of samples :',
            style=style,
            disabled=False
        )

        global _seed

        _seed = widgets.BoundedIntText(
            value=drive.__dict__['_seed'],
            min=0,
            max=100,
            description='Seed  :',
            disabled=False
        )

        left_box = widgets.VBox([_num_samples, procspermodel])
        right_box = widgets.VBox([_seed, runparallel])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        procspermodel.add_class("top")

        # Right Widgets
        runparallel.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        display(vbox, button)
        button.on_click(save)

    def _pyDOE_Generator():

        drive = driver.doe_generators._pyDOE_Generator()

        #         print(drive.__dict__)

        global _levels

        def onchangelevels(change):

            global _levels

            if change['new'] == 'Int':

                _levels = widgets.BoundedIntText(
                    value=drive.__dict__['_levels'],
                    description='Levels  :',
                    min=0,
                    max=1000,
                    disabled=False
                )

            elif change['new'] == 'Dict':

                _levels = widgets.Text(
                    value='[]',
                    description='Levels  :',
                    disabled=False
                )

            clear_output(wait=True)

            left_box = widgets.VBox([selectlevels, _sizes, runparallel])
            right_box = widgets.VBox([_levels, procspermodel])
            vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            _sizes.add_class("top")
            runparallel.add_class("top")

            # Right Widgets
            procspermodel.add_class("top")

            # VBox & Button Widgets
            vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            vbox.add_class("top")
            button.add_class("top")
            button.add_class("green")

            display(select, generator, vbox, button, html)

        selectlevels = widgets.RadioButtons(
            options=['Int', 'Dict'],
            value='Int',
            description='Levels type  :',
            disabled=False
        )

        _levels = widgets.BoundedIntText(
            value=drive.__dict__['_levels'],
            description='Levels  :',
            min=0,
            max=1000,
            disabled=False
        )

        global _sizes

        _sizes = widgets.BoundedIntText(
            value=drive.__dict__['_sizes'],
            min=0,
            max=100,
            description='Sizes  :',
            disabled=False
        )

        left_box = widgets.VBox([selectlevels, _sizes, runparallel])
        right_box = widgets.VBox([_levels, procspermodel])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        _sizes.add_class("top")
        runparallel.add_class("top")

        # Right Widgets
        procspermodel.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        selectlevels.observe(onchangelevels, names='value')
        display(vbox, button)
        button.on_click(save)

    def FullFactorialGenerator():

        drive = driver.doe_generators.FullFactorialGenerator()

        #         print(drive.__dict__)

        global _levels

        def onchangelevels(change):

            global _levels

            if change['new'] == 'Int':

                _levels = widgets.BoundedIntText(
                    value=drive.__dict__['_levels'],
                    description='Levels  :',
                    min=0,
                    max=1000,
                    disabled=False
                )

            elif change['new'] == 'Dict':

                _levels = widgets.Text(
                    value='[]',
                    description='Levels  :',
                    disabled=False
                )

            clear_output(wait=True)

            left_box = widgets.VBox([selectlevels, _sizes, runparallel])
            right_box = widgets.VBox([_levels, procspermodel])
            vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            _sizes.add_class("top")
            runparallel.add_class("top")

            # Right Widgets
            procspermodel.add_class("top")

            # VBox & Button Widgets
            vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            vbox.add_class("top")
            button.add_class("top")
            button.add_class("green")

            display(select, generator, vbox, button, html)

        selectlevels = widgets.RadioButtons(
            options=['Int', 'Dict'],
            value='Int',
            description='Levels type  :',
            disabled=False
        )

        _levels = widgets.BoundedIntText(
            value=drive.__dict__['_levels'],
            description='Levels  :',
            min=0,
            max=1000,
            disabled=False
        )

        global _sizes

        _sizes = widgets.BoundedIntText(
            value=drive.__dict__['_sizes'],
            min=0,
            max=100,
            description='Sizes  :',
            disabled=False
        )

        left_box = widgets.VBox([selectlevels, _sizes, runparallel])
        right_box = widgets.VBox([_levels, procspermodel])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        _sizes.add_class("top")
        runparallel.add_class("top")

        # Right Widgets
        procspermodel.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        selectlevels.observe(onchangelevels, names='value')
        display(vbox, button)
        button.on_click(save)

    def GeneralizedSubsetGenerator():

        print("Not finished")

        #         drive = driver.doe_generators.GeneralizedSubsetGenerator()

        #         print(drive.__dict__)

        left_box = widgets.VBox([procspermodel])
        right_box = widgets.VBox([runparallel])
        vbox = widgets.HBox([left_box, right_box])

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        display(vbox, button)
        button.on_click(save)

    def PlackettBurmanGenerator():

        drive = driver.doe_generators.PlackettBurmanGenerator()

        #         print(drive.__dict__)

        global _levels

        def onchangelevels(change):

            global _levels

            if change['new'] == 'Int':

                _levels = widgets.BoundedIntText(
                    value=drive.__dict__['_levels'],
                    description='Levels  :',
                    min=0,
                    max=1000,
                    disabled=False
                )

            elif change['new'] == 'Dict':

                _levels = widgets.Text(
                    value='[]',
                    description='Levels  :',
                    disabled=False
                )

            clear_output(wait=True)

            left_box = widgets.VBox([selectlevels, _sizes, runparallel])
            right_box = widgets.VBox([_levels, procspermodel])
            vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            _sizes.add_class("top")
            runparallel.add_class("top")

            # Right Widgets
            procspermodel.add_class("top")

            # VBox & Button Widgets
            vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            vbox.add_class("top")
            button.add_class("top")
            button.add_class("green")

            display(select, generator, vbox, button, html)

        selectlevels = widgets.RadioButtons(
            options=['Int', 'Dict'],
            value='Int',
            description='Levels type  :',
            disabled=False
        )

        _levels = widgets.BoundedIntText(
            value=drive.__dict__['_levels'],
            description='Levels  :',
            min=0,
            max=1000,
            disabled=False
        )

        global _sizes

        _sizes = widgets.BoundedIntText(
            value=drive.__dict__['_sizes'],
            min=0,
            max=100,
            description='Sizes  :',
            disabled=False
        )

        left_box = widgets.VBox([selectlevels, _sizes, runparallel])
        right_box = widgets.VBox([_levels, procspermodel])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        _sizes.add_class("top")
        runparallel.add_class("top")

        # Right Widgets
        procspermodel.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        selectlevels.observe(onchangelevels, names='value')
        display(vbox, button)
        button.on_click(save)

    def BoxBehnkenGenerator():

        drive = driver.doe_generators.BoxBehnkenGenerator()

        #         print(drive.__dict__)

        global _levels

        def onchangelevels(change):

            global _levels

            if change['new'] == 'Int':

                _levels = widgets.BoundedIntText(
                    value=drive.__dict__['_levels'],
                    description='Levels  :',
                    min=0,
                    max=1000,
                    disabled=False
                )

            elif change['new'] == 'Dict':

                _levels = widgets.Text(
                    value='[]',
                    description='Levels  :',
                    disabled=False
                )

            clear_output(wait=True)

            left_box = widgets.VBox([selectlevels, _sizes, procspermodel])
            right_box = widgets.VBox([_levels, _center, runparallel])
            vbox = widgets.HBox([left_box, right_box])

            # left Widgets
            _sizes.add_class("top")
            procspermodel.add_class("top")

            # Right Widgets
            _center.add_class("top")
            runparallel.add_class("top")

            # VBox & Button Widgets
            vbox.add_class("top")
            left_box.add_class("left")
            left_box.add_class("right")
            vbox.add_class("top")
            button.add_class("top")
            button.add_class("green")

            display(select, generator, vbox, button, html)

        selectlevels = widgets.RadioButtons(
            options=['Int', 'Dict'],
            value='Int',
            description='Levels type  :',
            disabled=False
        )

        _levels = widgets.BoundedIntText(
            value=drive.__dict__['_levels'],
            description='Levels  :',
            min=0,
            max=1000,
            disabled=False
        )

        global _sizes

        _sizes = widgets.BoundedIntText(
            value=drive.__dict__['_sizes'],
            min=0,
            max=100,
            description='Sizes  :',
            disabled=False
        )

        global _center

        _center = widgets.BoundedIntText(
            value=drive.__dict__['_center'],
            min=0,
            max=100,
            description='Center  :',
            disabled=False
        )

        left_box = widgets.VBox([selectlevels, _sizes, procspermodel])
        right_box = widgets.VBox([_levels, _center, runparallel])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        _sizes.add_class("top")
        procspermodel.add_class("top")

        # Right Widgets
        _center.add_class("top")
        runparallel.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        selectlevels.observe(onchangelevels, names='value')
        display(vbox, button)
        button.on_click(save)

    def LatinHypercubeGenerator():

        drive = driver.doe_generators.LatinHypercubeGenerator()

        #         print(drive.__dict__)

        global _samples

        _samples = widgets.BoundedIntText(
            value=drive.__dict__['_samples'],
            min=0,
            max=100,
            description='Number of samples to generate :',
            style=style,
            disabled=False
        )

        global _criterion

        _criterion = widgets.Dropdown(
            options=['None', 'center', 'maximin', 'centermaximin', 'correlation'],
            value=drive.__dict__['_criterion'],
            description='Criterion :',
        )

        global _iterations

        _iterations = widgets.BoundedIntText(
            value=drive.__dict__['_iterations'],
            min=0,
            max=100,
            description='Iterations  :',
            disabled=False
        )

        global _seed

        _seed = widgets.BoundedIntText(
            value=drive.__dict__['_seed'],
            min=0,
            max=100,
            description='Seed :',
            disabled=False
        )

        left_box = widgets.VBox([_samples, _iterations, procspermodel])
        right_box = widgets.VBox([_criterion, _seed, runparallel])
        vbox = widgets.HBox([left_box, right_box])

        # left Widgets
        _iterations.add_class("top")
        procspermodel.add_class("top")

        # Right Widgets
        _seed.add_class("top")
        runparallel.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")
        vbox.add_class("top")
        button.add_class("top")
        button.add_class("green")

        display(vbox, button)
        button.on_click(save)

    generator.observe(onchangegenerator, names='value')
    display(generator)
    DOEGenerator()


def genetic_algorithm_driver_change():
    drive = driver.genetic_algorithm_driver.SimpleGADriver()

    #     print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['driver'] = 'om.SimpleGADriver'
            doc['driver'] += '(bits=' + str(bits.value) + ',elitism=' + str(elitism.value) + ',gray=' + str(
                gray.value) + ',cross_bits=' + str(crossbits.value) + ',max_gen=' + str(
                maxgen.value) + ',pop_size=' + str(popsize.value)
            doc['driver'] += ',run_parallel=' + str(runparallel.value) + ',procs_per_model=' + str(
                procspermodel.value) + ',penalty_parameter=' + str(penaltyparameter.value)
            doc['driver'] += ',penalty_exponent=' + str(penaltyexponent.value) + ',Pc=' + str(pc.value) + ',Pm=' + str(
                pm.value) + ',multi_obj_weights=' + str(multiobjweights.value)
            doc['driver'] += ',multi_obj_exponent=' + str(multiobjexponent.value) + ',compute_pareto=' + str(
                computepareto.value) + ')'

            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    style = {'description_width': 'initial'}

    bits = widgets.Text(
        value='{}',
        description='Number of bits of resolution :',
        style=style,
        disabled=False
    )

    elitism = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['elitism'].get('value'),
        description='Elitism',
        disabled=False,
    )

    gray = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['gray'].get('value'),
        description='Gray',
        disabled=False,
    )

    crossbits = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['cross_bits'].get('value'),
        description='Cross bits',
        disabled=False,
    )

    maxgen = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['max_gen'].get('value'),
        min=0,
        max=1000,
        description='Number of generations :',
        style=style,
        disabled=False
    )

    popsize = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['pop_size'].get('value'),
        min=0,
        max=100,
        description='Number of points in the GA :',
        style=style,
        disabled=False
    )

    runparallel = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['run_parallel'].get('value'),
        description='Run parallel',
        disabled=False,
    )

    procspermodel = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['procs_per_model'].get('value'),
        min=drive.options.__dict__['_dict']['procs_per_model'].get('lower'),
        max=100,
        description='Processors per model :',
        style=style,
        disabled=False
    )

    penaltyparameter = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['penalty_parameter'].get('value'),
        min=drive.options.__dict__['_dict']['penalty_parameter'].get('lower'),
        max=100,
        description='Penalty parameter :',
        style=style,
        disabled=False
    )

    penaltyexponent = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['penalty_exponent'].get('value'),
        min=0,
        max=100,
        description='Penalty exponent :',
        style=style,
        disabled=False
    )

    pc = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['Pc'].get('value'),
        min=drive.options.__dict__['_dict']['Pc'].get('lower'),
        max=drive.options.__dict__['_dict']['Pc'].get('upper'),
        description='Crossover probability :',
        style=style,
        disabled=False
    )

    pm = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['Pm'].get('value'),
        min=drive.options.__dict__['_dict']['Pm'].get('lower'),
        max=drive.options.__dict__['_dict']['Pm'].get('upper'),
        description='Mutation rate :',
        style=style,
        disabled=False
    )

    multiobjweights = widgets.Text(
        value='{}',
        description='Multi objective weights :',
        style=style,
        disabled=False
    )

    multiobjexponent = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['multi_obj_exponent'].get('value'),
        min=drive.options.__dict__['_dict']['multi_obj_exponent'].get('lower'),
        max=100,
        description='Multi-objective weighting exponent :',
        style=style,
        disabled=False
    )

    computepareto = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['compute_pareto'].get('value'),
        description='Compute pareto',
        disabled=False,
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    left_box = widgets.VBox([bits, gray, maxgen, runparallel, penaltyparameter, pc, multiobjweights, computepareto])
    right_box = widgets.VBox([elitism, crossbits, popsize, procspermodel, penaltyexponent, pm, multiobjexponent])
    vbox = widgets.HBox([left_box, right_box])

    # left Widgets
    gray.add_class("top")
    maxgen.add_class("top")
    runparallel.add_class("top")
    penaltyparameter.add_class("top")
    pc.add_class("top")
    multiobjweights.add_class("top")
    computepareto.add_class("top")

    # Right Widgets
    crossbits.add_class("top")
    popsize.add_class("top")
    procspermodel.add_class("top")
    penaltyexponent.add_class("top")
    pm.add_class("top")
    multiobjexponent.add_class("top")

    # VBox & Button Widgets
    vbox.add_class("top")
    left_box.add_class("left")
    left_box.add_class("right")
    vbox.add_class("top")
    button.add_class("top")
    button.add_class("green")

    display(vbox, button)


def pyoptsparse_driver_change():
    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['driver'] = 'om.pyOptSparseDriver()'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    button.add_class("top")
    button.add_class("green")

    display(button)
    button.on_click(save)


def onchange(change):
    clear_output(wait=True)
    display(select, html)

    if change['new'] == 'scipy_optimizer':
        scipy_optimizer_change()
    elif change['new'] == 'differential_evolution_driver':
        differential_evolution_driver_change()
    elif change['new'] == 'doe_driver':
        doe_driver_change()
    elif change['new'] == 'genetic_algorithm_driver':
        genetic_algorithm_driver_change()
    elif change['new'] == 'pyoptsparse_driver':
        pyoptsparse_driver_change()


select = widgets.Dropdown(
    options=['differential_evolution_driver', 'doe_driver', 'genetic_algorithm_driver',
             'pyoptsparse_driver', 'scipy_optimizer'],
    value='scipy_optimizer',
    description='Driver :',
)

button = widgets.Button(
    description='Save',
    tooltip='Save',
    icon='save'
)

select.observe(onchange, names='value')
display(select)
scipy_optimizer_change()