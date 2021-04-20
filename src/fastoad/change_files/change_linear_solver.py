from IPython.display import display
from IPython.display import clear_output
import ipywidgets as widgets
from ruamel.yaml import YAML
import openmdao.solvers.linear as solvers


def direct_change():
    drive = solvers.direct.DirectSolver()

    # print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.DirectSolver(err_on_singular=' + str(err_on_singular.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    err_on_singular = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['err_on_singular'].get('value'),
        description='Raise an error if LU decomposition is singular',
        style=style,
        disabled=False,
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(err_on_singular, button)
    button.on_click(save)


def linear_block_gs_change():
    drive = solvers.linear_block_gs.LinearBlockGS()

    # print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.LinearBlockGS(use_aitken=' + str(
                use_aitken.value) + ',aitken_min_factor='
            doc['model']['linear_solver'] += str(aitken_min_factor.value) + ',aitken_max_factor=' + str(
                aitken_max_factor.value)
            doc['model']['linear_solver'] += ',aitken_initial_factor=' + str(
                aitken_initial_factor.value) + ',maxiter=' + str(maxiter.value)
            doc['model']['linear_solver'] += ',atol=' + str(atol.value) + ',rtol=' + str(rtol.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    use_aitken = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['use_aitken'].get('value'),
        description='Set to True to use Aitken relaxation',
        style=style,
        disabled=False,
    )

    aitken_min_factor = widgets.FloatText(
        value=drive.options.__dict__['_dict']['aitken_min_factor'].get('value'),
        description='Lower limit for Aitken relaxation factor :',
        style=style,
        disabled=False
    )

    aitken_max_factor = widgets.FloatText(
        value=drive.options.__dict__['_dict']['aitken_max_factor'].get('value'),
        description='Upper limit for Aitken relaxation factor :',
        style=style,
        disabled=False
    )

    aitken_initial_factor = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['aitken_initial_factor'].get('value'),
        description='Initial value for Aitken relaxation factor :',
        style=style,
        disabled=False
    )

    maxiter = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['maxiter'].get('value'),
        min=1,
        max=10000,
        description='Maxiter:',
        style=style,
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['atol'].get('value'),
        min=10e-12,
        max=1,
        description='aTol:',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['rtol'].get('value'),
        min=10e-12,
        max=1,
        description='rTol:',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(use_aitken, aitken_min_factor, aitken_max_factor, aitken_initial_factor, maxiter, atol, rtol, button)
    button.on_click(save)


def linear_block_jac_change():
    drive = solvers.linear_block_jac.LinearBlockJac()

    # print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.LinearBlockJac(maxiter=' + str(maxiter.value) + ',atol=' + str(
                atol.value) + ',rtol='
            doc['model']['linear_solver'] += str(rtol.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['maxiter'].get('value'),
        min=1,
        max=10000,
        description='Maxiter:',
        style=style,
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['atol'].get('value'),
        min=1e-20,
        max=1,
        description='aTol:',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['rtol'].get('value'),
        min=10e-12,
        max=1,
        description='rTol:',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(maxiter, atol, rtol, button)
    button.on_click(save)


def linear_runonce_change():
    drive = solvers.linear_runonce.LinearRunOnce()

    # print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.LinearRunOnce(use_aitken=' + str(
                use_aitken.value) + ',aitken_min_factor='
            doc['model']['linear_solver'] += str(aitken_min_factor.value) + ',aitken_max_factor=' + str(
                aitken_max_factor.value)
            doc['model']['linear_solver'] += ',aitken_initial_factor=' + str(aitken_initial_factor.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    use_aitken = widgets.Checkbox(
        value=drive.options.__dict__['_dict']['use_aitken'].get('value'),
        description='Set to True to use Aitken relaxation',
        style=style,
        disabled=False,
    )

    aitken_min_factor = widgets.FloatText(
        value=drive.options.__dict__['_dict']['aitken_min_factor'].get('value'),
        description='Lower limit for Aitken relaxation factor :',
        style=style,
        disabled=False
    )

    aitken_max_factor = widgets.FloatText(
        value=drive.options.__dict__['_dict']['aitken_max_factor'].get('value'),
        description='Upper limit for Aitken relaxation factor :',
        style=style,
        disabled=False
    )

    aitken_initial_factor = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['aitken_initial_factor'].get('value'),
        description='Initial value for Aitken relaxation factor :',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(use_aitken, aitken_min_factor, aitken_max_factor, aitken_initial_factor, button)
    button.on_click(save)


def petsc_ksp_change():
    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.PETScKrylov()'
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


def scipy_iter_solver_change():
    drive = solvers.scipy_iter_solver.ScipyKrylov()

    # print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.ScipyKrylov(maxiter=' + str(maxiter.value) + ',atol=' + str(
                atol.value) + ',rtol='
            doc['model']['linear_solver'] += str(rtol.value) + ',restart=' + str(restart.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['maxiter'].get('value'),
        min=1,
        max=10000,
        description='Maxiter:',
        style=style,
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['atol'].get('value'),
        min=1e-20,
        max=1,
        description='aTol:',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['rtol'].get('value'),
        min=10e-12,
        max=1,
        description='rTol:',
        style=style,
        disabled=False
    )

    restart = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['restart'].get('value'),
        min=0,
        max=1000,
        description='Restart:',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(maxiter, atol, rtol, restart, button)
    button.on_click(save)


def user_defined_change():
    drive = solvers.user_defined.LinearUserDefined()

    # print(drive.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.LinearUserDefined(maxiter=' + str(maxiter.value) + ',atol=' + str(
                atol.value) + ',rtol='
            doc['model']['linear_solver'] += str(rtol.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=drive.options.__dict__['_dict']['maxiter'].get('value'),
        min=1,
        max=10000,
        description='Maxiter:',
        style=style,
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['atol'].get('value'),
        min=1e-20,
        max=1,
        description='aTol:',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=drive.options.__dict__['_dict']['rtol'].get('value'),
        min=10e-12,
        max=1,
        description='rTol:',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(maxiter, atol, rtol, button)
    button.on_click(save)


def onchange(change):
    clear_output(wait=True)
    display(select)
    if change['new'] == 'direct':
        clear_output(wait=True)
        display(select)
        direct_change()
    elif change['new'] == 'linear_block_gs':
        clear_output(wait=True)
        display(select)
        linear_block_gs_change()
    elif change['new'] == 'linear_block_jac':
        clear_output(wait=True)
        display(select)
        linear_block_jac_change()
    elif change['new'] == 'linear_runonce':
        clear_output(wait=True)
        display(select)
        linear_runonce_change()
    elif change['new'] == 'petsc_ksp':
        clear_output(wait=True)
        display(select)
        petsc_ksp_change()
    elif change['new'] == 'scipy_iter_solver':
        clear_output(wait=True)
        display(select)
        scipy_iter_solver_change()
    elif change['new'] == 'user_defined':
        clear_output(wait=True)
        display(select)
        user_defined_change()


style = {'description_width': 'initial'}

select = widgets.Dropdown(
    options=['direct', 'linear_block_gs', 'linear_block_jac', 'linear_runonce',
             'petsc_ksp', 'scipy_iter_solver', 'user_defined'],
    value='direct',
    style=style,
    description='Linear solvers :',
)

select.observe(onchange, names='value')
display(select)
direct_change()