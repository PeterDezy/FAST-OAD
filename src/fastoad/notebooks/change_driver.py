from IPython.display import display
from IPython.display import clear_output
import ipywidgets as widgets
from ruamel.yaml import YAML
from fastoad.io.configuration.configuration import _YAMLSerializer
import openmdao.drivers as driver


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

    display(optimizers, tol, maxiter, disp, button)
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

    display(maxgen, popsize, runparallel, procspermodel, penaltyparameter, penaltyexponent, pc, dr, multiobjweights,
            multiobjexponent, button)
    button.on_click(save)


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
            doc['driver'] += '(procs_per_model=' + str(procspermodel.value) + ',run_parallel=' + str(
                runparallel.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    style = {'description_width': 'initial'}

    doe_generators_change()

    generator = widgets.Dropdown(
        options=['ListGenerator', 'CSVGenerator', 'UniformGenerator', '_pyDOE_Generator', 'FullFactorialGenerator',
                 'GeneralizedSubsetGenerator', 'PlackettBurmanGenerator', 'BoxBehnkenGenerator',
                 'LatinHypercubeGenerator'],
        value='ListGenerator',
        description='Generator :',
    )

    def onchangegenerator(change):

        if change['new'] == 'ListGenerator':
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

    select.observe(onchangegenerator, names='value')
    display(generator, procspermodel, runparallel, button)
    button.on_click(save)


def DOEGenerator():
    drive = driver.doe_generators.DOEGenerator()

    print(drive.options.__dict__)


def ListGenerator():
    drive = driver.doe_generators.ListGenerator()

    print(drive.options.__dict__)


def CSVGenerator():
    drive = driver.doe_generators.CSVGenerator()

    print(drive.options.__dict__)


def UniformGenerator():
    drive = driver.doe_generators.UniformGenerator()

    print(drive.options.__dict__)


def _pyDOE_Generator():
    drive = driver.doe_generators._pyDOE_Generator()

    print(drive.options.__dict__)


def FullFactorialGenerator():
    drive = driver.doe_generators.FullFactorialGenerator()

    print(drive.options.__dict__)


def GeneralizedSubsetGenerator():
    drive = driver.doe_generators.GeneralizedSubsetGenerator()

    print(drive.options.__dict__)


def PlackettBurmanGenerator():
    drive = driver.doe_generators.PlackettBurmanGenerator()

    print(drive.options.__dict__)


def BoxBehnkenGenerator():
    drive = driver.doe_generators.BoxBehnkenGenerator()

    print(drive.options.__dict__)


def LatinHypercubeGenerator():
    drive = driver.doe_generators.LatinHypercubeGenerator()

    print(drive.options.__dict__)


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

    display(bits, elitism, gray, crossbits, maxgen, popsize, runparallel, procspermodel, penaltyparameter,
            penaltyexponent, pc, pm, multiobjweights, multiobjexponent, computepareto, button)
    button.on_click(save)


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

    display(button)
    button.on_click(save)


def onchange(change):
    clear_output(wait=True)
    display(select, button)
    if change['new'] == 'scipy_optimizer':
        clear_output(wait=True)
        display(select)
        scipy_optimizer_change()
    elif change['new'] == 'differential_evolution_driver':
        clear_output(wait=True)
        display(select)
        differential_evolution_driver_change()
    elif change['new'] == 'doe_driver':
        clear_output(wait=True)
        display(select)
        doe_driver_change()
    elif change['new'] == 'genetic_algorithm_driver':
        clear_output(wait=True)
        display(select)
        genetic_algorithm_driver_change()
    elif change['new'] == 'pyoptsparse_driver':
        clear_output(wait=True)
        display(select)
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