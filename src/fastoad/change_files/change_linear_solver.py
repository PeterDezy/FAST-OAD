from IPython.display import display
from IPython.display import clear_output
import ipywidgets as widgets
from ruamel.yaml import YAML
import openmdao.solvers.linear as solvers


def direct_change():

    solver = solvers.direct.DirectSolver()

    # print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.DirectSolver(iprint='+str(iprint.value)+',assemble_jac=' + \
                                            str(assemble_jac.value)+',err_on_singular=' + \
                                            str(err_on_singular.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    iprint = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['iprint'].get('value'),
        min=0,
        max=1,
        description='Print the output :',
        style=style,
        disabled=False
    )

    assemble_jac = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['assemble_jac'].get('value'),
        description='Activates use of assembled jacobian by this solver',
        style=style,
        disabled=False,
    )

    err_on_singular = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['err_on_singular'].get('value'),
        description='Raise an error if LU decomposition is singular',
        style=style,
        disabled=False,
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(iprint,assemble_jac, err_on_singular, button)
    button.on_click(save)


def linear_block_gs_change():

    solver = solvers.linear_block_gs.LinearBlockGS()

    # print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.LinearBlockGS(maxiter=' + str(maxiter.value) + ',atol=' + \
                                            str(atol.value) + ',rtol='+str(rtol.value)+',iprint=' + \
                                            str(iprint.value)+',err_on_non_converge=' + \
                                            str(err_on_non_converge.value)+',assemble_jac=' + \
                                            str(assemble_jac.value) + ',use_aitken=' + str(use_aitken.value)
            if str(use_aitken.value) == 'True':
                doc['model']['linear_solver'] += ',aitken_min_factor=' + \
                                                 str(aitken_min_factor.value) + ',aitken_max_factor=' + \
                                                 str(aitken_max_factor.value) + ',aitken_initial_factor=' + \
                                                 str(aitken_initial_factor.value)

            doc['model']['linear_solver'] += ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['maxiter'].get('value'),
        min=1,
        max=10000,
        description='Maxiter :',
        style=style,
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['atol'].get('value'),
        min=1e-20,
        max=1,
        description='Absolute Error Tolerance :',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['rtol'].get('value'),
        min=10e-12,
        max=1,
        description='Relative Error Tolerance :',
        style=style,
        disabled=False
    )

    iprint = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['iprint'].get('value'),
        min=0,
        max=1,
        description='Print the output :',
        style=style,
        disabled=False
    )

    err_on_non_converge = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['err_on_non_converge'].get('value'),
        description='When True, AnalysisError will be raised if we don\'t converge',
        style=style,
        disabled=False,
    )

    assemble_jac = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['assemble_jac'].get('value'),
        description='Activates use of assembled jacobian by this solver',
        style=style,
        disabled=False,
    )

    use_aitken = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['use_aitken'].get('value'),
        description='Use Aitken relaxation',
        disabled=False,
    )

    aitken_min_factor = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['aitken_min_factor'].get('value'),
        min=0,
        max=100,
        description='Aitken min factor :',
        style=style,
        disabled=False
    )

    aitken_max_factor = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['aitken_max_factor'].get('value'),
        min=0,
        max=100,
        description='Aitken max factor :',
        style=style,
        disabled=False
    )

    aitken_initial_factor = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['aitken_initial_factor'].get('value'),
        min=0,
        max=100,
        description='Aitken initial factor :',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    vb = widgets.VBox(
        children=[]
    )

    def change_use_aitken(b):

        if b['new']:
            vb.children = [aitken_min_factor, aitken_max_factor, aitken_initial_factor]
        else:
            vb.children = []

    use_aitken.observe(change_use_aitken, names='value')

    display(maxiter, atol, rtol,iprint,err_on_non_converge,assemble_jac,use_aitken,vb, button)
    button.on_click(save)


def linear_block_jac_change():

    solver = solvers.linear_block_jac.LinearBlockJac()

    # print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.LinearBlockJac(maxiter=' + str(maxiter.value) + ',atol=' + \
                                            str(atol.value) + ',rtol='+str(rtol.value)+',iprint=' + \
                                            str(iprint.value)+',err_on_non_converge=' + \
                                            str(err_on_non_converge.value)+',assemble_jac=' + \
                                            str(assemble_jac.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['maxiter'].get('value'),
        min=1,
        max=10000,
        description='Maxiter :',
        style=style,
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['atol'].get('value'),
        min=1e-20,
        max=1,
        description='Absolute Error Tolerance :',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['rtol'].get('value'),
        min=10e-12,
        max=1,
        description='Relative Error Tolerance :',
        style=style,
        disabled=False
    )

    iprint = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['iprint'].get('value'),
        min=0,
        max=1,
        description='Print the output :',
        style=style,
        disabled=False
    )

    err_on_non_converge = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['err_on_non_converge'].get('value'),
        description='When True, AnalysisError will be raised if we don\'t converge',
        style=style,
        disabled=False,
    )

    assemble_jac = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['assemble_jac'].get('value'),
        description='Activates use of assembled jacobian by this solver',
        style=style,
        disabled=False,
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(maxiter, atol, rtol,iprint,err_on_non_converge,assemble_jac, button)
    button.on_click(save)


def linear_runonce_change():

    solver = solvers.linear_runonce.LinearRunOnce()

    # print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.LinearRunOnce(iprint='+str(iprint.value)+',assemble_jac=' + \
                                            str(assemble_jac.value) + ',use_aitken=' + str(use_aitken.value)
            if str(use_aitken.value) == 'True':
                doc['model']['linear_solver'] += ',aitken_min_factor=' + \
                                                 str(aitken_min_factor.value) + ',aitken_max_factor=' + \
                                                 str(aitken_max_factor.value) + ',aitken_initial_factor=' + \
                                                 str(aitken_initial_factor.value)

            doc['model']['linear_solver'] += ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")


    iprint = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['iprint'].get('value'),
        min=0,
        max=1,
        description='Print the output :',
        style=style,
        disabled=False
    )

    assemble_jac = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['assemble_jac'].get('value'),
        description='Activates use of assembled jacobian by this solver',
        style=style,
        disabled=False,
    )

    use_aitken = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['use_aitken'].get('value'),
        description='Use Aitken relaxation',
        disabled=False,
    )

    aitken_min_factor = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['aitken_min_factor'].get('value'),
        min=0,
        max=100,
        description='Aitken min factor :',
        style=style,
        disabled=False
    )

    aitken_max_factor = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['aitken_max_factor'].get('value'),
        min=0,
        max=100,
        description='Aitken max factor :',
        style=style,
        disabled=False
    )

    aitken_initial_factor = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['aitken_initial_factor'].get('value'),
        min=0,
        max=100,
        description='Aitken initial factor :',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    vb = widgets.VBox(
        children=[]
    )

    def change_use_aitken(b):

        if b['new']:
            vb.children = [aitken_min_factor, aitken_max_factor, aitken_initial_factor]
        else:
            vb.children = []

    use_aitken.observe(change_use_aitken, names='value')

    display(iprint,assemble_jac,use_aitken, vb, button)
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

    solver = solvers.scipy_iter_solver.ScipyKrylov()

    # print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.ScipyKrylov(maxiter=' + str(maxiter.value) + ',atol=' + \
                                            str(atol.value) + ',rtol='+str(rtol.value) + ',iprint=' + \
                                            str(iprint.value)+',err_on_non_converge=' + \
                                            str(err_on_non_converge.value)+',assemble_jac=' + \
                                            str(assemble_jac.value) + ',restart=' + str(restart.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['maxiter'].get('value'),
        min=1,
        max=10000,
        description='Maxiter :',
        style=style,
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['atol'].get('value'),
        min=1e-20,
        max=1,
        description='Absolute Error Tolerance :',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['rtol'].get('value'),
        min=10e-12,
        max=1,
        description='Relative Error Tolerance :',
        style=style,
        disabled=False
    )

    iprint = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['iprint'].get('value'),
        min=0,
        max=1,
        description='Print the output :',
        style=style,
        disabled=False
    )

    err_on_non_converge = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['err_on_non_converge'].get('value'),
        description='When True, AnalysisError will be raised if we don\'t converge',
        style=style,
        disabled=False,
    )

    assemble_jac = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['assemble_jac'].get('value'),
        description='Activates use of assembled jacobian by this solver',
        style=style,
        disabled=False,
    )

    restart = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['restart'].get('value'),
        min=0,
        max=1000,
        description='Restart :',
        style=style,
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(maxiter, atol, rtol,iprint,err_on_non_converge,assemble_jac, restart, button)
    button.on_click(save)


def user_defined_change():

    solver = solvers.user_defined.LinearUserDefined()

    # print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "./workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['linear_solver'] = 'om.LinearUserDefined(maxiter=' + str(maxiter.value) + ',atol=' + \
                                            str(atol.value) + ',rtol='+str(rtol.value)+',iprint=' + \
                                            str(iprint.value)+',err_on_non_converge=' + \
                                            str(err_on_non_converge.value)+',assemble_jac='+str(assemble_jac.value)+')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['maxiter'].get('value'),
        min=1,
        max=10000,
        description='Maxiter :',
        style=style,
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['atol'].get('value'),
        min=1e-20,
        max=1,
        description='Absolute Error Tolerance :',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['rtol'].get('value'),
        min=10e-12,
        max=1,
        description='Relative Error Tolerance :',
        style=style,
        disabled=False
    )

    iprint = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['iprint'].get('value'),
        min=0,
        max=1,
        description='Print the output :',
        style=style,
        disabled=False
    )

    err_on_non_converge = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['err_on_non_converge'].get('value'),
        description='When True, AnalysisError will be raised if we don\'t converge',
        style=style,
        disabled=False,
    )

    assemble_jac = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['assemble_jac'].get('value'),
        description='Activates use of assembled jacobian by this solver',
        style=style,
        disabled=False,
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(maxiter, atol, rtol,iprint,err_on_non_converge,assemble_jac, button)
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
