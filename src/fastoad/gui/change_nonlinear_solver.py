from IPython.display import display
from IPython.display import clear_output
import ipywidgets as widgets
from ruamel.yaml import YAML
from fastoad.io.configuration.configuration import _YAMLSerializer
import openmdao.solvers.nonlinear as solversnonlinear


def broyden_change():
    solver = solversnonlinear.broyden.BroydenSolver()

    #     print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "../notebooks/workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['nonlinear_solver'] = 'om.BroydenSolver'
            doc['model']['nonlinear_solver'] += '(maxiter=' + str(maxiter.value) + ',atol=' + str(
                atol.value) + ',rtol=' + str(rtol.value) + ',iprint=' + str(
                iprint.value) + ',err_on_non_converge=' + str(err_on_non_converge.value)
            doc['model']['nonlinear_solver'] += ',debug_print=' + str(debug_print.value) + ',stall_limit=' + str(
                stall_limit.value) + ',stall_tol=' + str(stall_tol.value) + ',alpha=' + str(alpha.value)
            doc['model']['nonlinear_solver'] += ',compute_jacobian=' + str(
                compute_jacobian.value) + ',converge_limit=' + str(converge_limit.value) + ',cs_reconverge=' + str(
                cs_reconverge.value)
            doc['model']['nonlinear_solver'] += ',diverge_limit=' + str(
                diverge_limit.value) + ',max_converge_failures=' + str(
                max_converge_failures.value) + ',max_jacobians=' + str(max_jacobians.value)
            doc['model']['nonlinear_solver'] += ',state_vars=' + str(state_vars.value) + ',update_broyden=' + str(
                update_broyden.value) + ',reraise_child_analysiserror=' + str(reraise_child_analysiserror.value) + ')'

            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['maxiter'].get('value'),
        min=0,
        max=10000,
        description='Maxiter :',
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['atol'].get('value'),
        min=0,
        max=1,
        description='Absolute Error Tolerance :',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['rtol'].get('value'),
        min=0,
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
        description='Err on non converge',
        disabled=False,
    )

    debug_print = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['debug_print'].get('value'),
        description='Debug Print',
        disabled=False,
    )

    stall_limit = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['stall_limit'].get('value'),
        min=0,
        max=100,
        description='Stall Limit :',
        disabled=False
    )

    stall_tol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['stall_tol'].get('value'),
        min=0,
        max=1,
        description='Stall tol :',
        disabled=False
    )

    alpha = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['alpha'].get('value'),
        min=0,
        max=10,
        description='Alpha :',
        disabled=False
    )

    compute_jacobian = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['compute_jacobian'].get('value'),
        description='Compute Jacobian',
        disabled=False,
    )

    converge_limit = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['converge_limit'].get('value'),
        min=0,
        max=100,
        description='Compute limit :',
        style=style,
        disabled=False
    )

    cs_reconverge = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['cs_reconverge'].get('value'),
        description='Cs reconverge',
        disabled=False,
    )

    diverge_limit = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['diverge_limit'].get('value'),
        min=0,
        max=100,
        description='Diverge Limit :',
        style=style,
        disabled=False
    )

    max_converge_failures = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['max_converge_failures'].get('value'),
        min=0,
        max=100,
        description='Max Converge Failures :',
        style=style,
        disabled=False
    )

    max_jacobians = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['max_jacobians'].get('value'),
        min=0,
        max=100,
        description='Max Jacobians :',
        style=style,
        disabled=False
    )

    state_vars = widgets.Text(
        value='[]',
        description='State Vars :',
        disabled=False
    )

    update_broyden = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['update_broyden'].get('value'),
        description='Update Broyden',
        disabled=False,
    )

    reraise_child_analysiserror = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['reraise_child_analysiserror'].get('value'),
        description='Reraise child Analysiserror',
        disabled=False,
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(maxiter, atol, rtol, iprint, err_on_non_converge, debug_print, stall_limit, stall_tol, alpha,
            compute_jacobian, converge_limit,
            cs_reconverge, diverge_limit, max_converge_failures, max_jacobians, state_vars, update_broyden,
            reraise_child_analysiserror, button)
    button.on_click(save)


def newton_change():
    solver = solversnonlinear.newton.NewtonSolver()

    #     print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "../notebooks/workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['nonlinear_solver'] = 'om.NewtonSolver'
            doc['model']['nonlinear_solver'] += '(maxiter=' + str(maxiter.value) + ',atol=' + str(
                atol.value) + ',rtol=' + str(rtol.value) + ',iprint=' + str(
                iprint.value) + ',err_on_non_converge=' + str(err_on_non_converge.value)
            doc['model']['nonlinear_solver'] += ',debug_print=' + str(debug_print.value) + ',stall_limit=' + str(
                stall_limit.value) + ',stall_tol=' + str(stall_tol.value) + ',solve_subsystems=' + str(
                solve_subsystems.value)
            if str(solve_subsystems.value) == 'True':
                doc['model']['nonlinear_solver'] += ',max_sub_solves=' + str(max_sub_solves.value)
            doc['model']['nonlinear_solver'] += ',cs_reconverge=' + str(
                cs_reconverge.value) + ',reraise_child_analysiserror=' + str(reraise_child_analysiserror.value) + ')'

            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['maxiter'].get('value'),
        min=0,
        max=10000,
        description='Maxiter :',
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['atol'].get('value'),
        min=0,
        max=1,
        description='Absolute Error Tolerance :',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['rtol'].get('value'),
        min=0,
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
        description='Err on non converge',
        disabled=False,
    )

    debug_print = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['debug_print'].get('value'),
        description='Debug Print',
        disabled=False,
    )

    stall_limit = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['stall_limit'].get('value'),
        min=0,
        max=100,
        description='Stall Limit :',
        disabled=False
    )

    stall_tol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['stall_tol'].get('value'),
        min=0,
        max=1,
        description='Stall tol :',
        disabled=False
    )

    solve_subsystems = widgets.Checkbox(
        value=False,
        description='Solve Subsystems',
        disabled=False,
    )

    max_sub_solves = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['max_sub_solves'].get('value'),
        min=0,
        max=100,
        description='Max Sub Solves :',
        style=style,
        disabled=False
    )

    cs_reconverge = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['cs_reconverge'].get('value'),
        description='Cs reconverge',
        disabled=False,
    )

    reraise_child_analysiserror = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['reraise_child_analysiserror'].get('value'),
        description='Reraise child Analysiserror',
        disabled=False,
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    vb = widgets.VBox(
        children=[]
    )

    def change_use_solve_subsystems(b):

        if b['new']:
            vb.children = [max_sub_solves]
        else:
            vb.children = []

    solve_subsystems.observe(change_use_solve_subsystems, names='value')

    display(maxiter, atol, rtol, iprint, err_on_non_converge, debug_print, stall_limit, stall_tol, solve_subsystems, vb,
            cs_reconverge, reraise_child_analysiserror, button)
    button.on_click(save)


def nonlinear_block_gs_change():
    solver = solversnonlinear.nonlinear_block_gs.NonlinearBlockGS()

    #     print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "../notebooks/workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['nonlinear_solver'] = 'om.NonlinearBlockGS'
            doc['model']['nonlinear_solver'] += '(maxiter=' + str(maxiter.value) + ',atol=' + str(
                atol.value) + ',rtol=' + str(rtol.value) + ',iprint=' + str(
                iprint.value) + ',err_on_non_converge=' + str(err_on_non_converge.value)
            doc['model']['nonlinear_solver'] += ',debug_print=' + str(debug_print.value) + ',stall_limit=' + str(
                stall_limit.value) + ',stall_tol=' + str(stall_tol.value) + ',use_aitken=' + str(use_aitken.value)
            if str(use_aitken.value) == 'True':
                doc['model']['nonlinear_solver'] += ',aitken_min_factor=' + str(
                    aitken_min_factor.value) + ',aitken_max_factor=' + str(
                    aitken_max_factor.value) + ',aitken_initial_factor=' + str(aitken_initial_factor.value)

            doc['model']['nonlinear_solver'] += ',cs_reconverge=' + str(
                cs_reconverge.value) + ',use_apply_nonlinear=' + str(
                use_apply_nonlinear.value) + ',reraise_child_analysiserror=' + str(
                reraise_child_analysiserror.value) + ')'
            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['maxiter'].get('value'),
        min=0,
        max=10000,
        description='Maxiter :',
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['atol'].get('value'),
        min=0,
        max=1,
        description='Absolute Error Tolerance :',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['rtol'].get('value'),
        min=0,
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
        description='Err on non converge',
        disabled=False,
    )

    debug_print = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['debug_print'].get('value'),
        description='Debug Print',
        disabled=False,
    )

    stall_limit = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['stall_limit'].get('value'),
        min=0,
        max=100,
        description='Stall Limit :',
        disabled=False
    )

    stall_tol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['stall_tol'].get('value'),
        min=0,
        max=1,
        description='Stall tol :',
        disabled=False
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
        max=1,
        description='Aitken initial factor :',
        style=style,
        disabled=False
    )

    cs_reconverge = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['cs_reconverge'].get('value'),
        description='Cs reconverge',
        disabled=False,
    )

    use_apply_nonlinear = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['use_apply_nonlinear'].get('value'),
        description='Use apply nonlinear',
        disabled=False,
    )

    reraise_child_analysiserror = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['reraise_child_analysiserror'].get('value'),
        description='Reraise child Analysiserror',
        disabled=False,
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

    display(maxiter, atol, rtol, iprint, err_on_non_converge, debug_print, stall_limit, stall_tol, use_aitken, vb,
            cs_reconverge, use_apply_nonlinear, reraise_child_analysiserror, button)
    button.on_click(save)


def nonlinear_block_jac_change():
    solver = solversnonlinear.nonlinear_block_jac.NonlinearBlockJac()

    #     print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "../notebooks/workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['nonlinear_solver'] = 'om.NonlinearBlockJac'
            doc['model']['nonlinear_solver'] += '(maxiter=' + str(maxiter.value) + ',atol=' + str(
                atol.value) + ',rtol=' + str(rtol.value) + ',iprint=' + str(
                iprint.value) + ',err_on_non_converge=' + str(err_on_non_converge.value)
            doc['model']['nonlinear_solver'] += ',debug_print=' + str(debug_print.value) + ',stall_limit=' + str(
                stall_limit.value) + ',stall_tol=' + str(stall_tol.value) + ')'

            with open(file_name, 'w') as f:
                yaml.dump(doc, f)
            print("Successfully changed options.\n")

        except:
            raise ValueError("Error while modifying.\n")

    maxiter = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['maxiter'].get('value'),
        min=0,
        max=10000,
        description='Maxiter :',
        disabled=False
    )

    atol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['atol'].get('value'),
        min=0,
        max=1,
        description='Absolute Error Tolerance :',
        style=style,
        disabled=False
    )

    rtol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['rtol'].get('value'),
        min=0,
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
        description='Err on non converge',
        disabled=False,
    )

    debug_print = widgets.Checkbox(
        value=solver.options.__dict__['_dict']['debug_print'].get('value'),
        description='Debug Print',
        disabled=False,
    )

    stall_limit = widgets.BoundedIntText(
        value=solver.options.__dict__['_dict']['stall_limit'].get('value'),
        min=0,
        max=100,
        description='Stall Limit :',
        disabled=False
    )

    stall_tol = widgets.BoundedFloatText(
        value=solver.options.__dict__['_dict']['stall_tol'].get('value'),
        min=0,
        max=1,
        description='Stall tol :',
        disabled=False
    )

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(maxiter, atol, rtol, iprint, err_on_non_converge, debug_print, stall_limit, stall_tol, button)
    button.on_click(save)


def nonlinear_runonce_change():
    solver = solversnonlinear.nonlinear_runonce.NonlinearRunOnce()

    #     print(solver.options.__dict__)

    def save(b):
        yaml = YAML()
        file_name = "../notebooks/workdir/oad_process.yml"
        with open(file_name, 'r') as f:
            doc = yaml.load(f)

        try:
            doc['model']['nonlinear_solver'] = 'om.NonlinearRunOnce'
            doc['model']['nonlinear_solver'] += '(iprint=' + str(iprint.value) + ')'

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

    button = widgets.Button(
        description='Save',
        tooltip='Save',
        icon='save'
    )

    display(iprint, button)
    button.on_click(save)


style = {'description_width': 'initial'}


def onchange(change):
    clear_output(wait=True)
    display(select, button)
    if change['new'] == 'broyden':
        clear_output(wait=True)
        display(select)
        broyden_change()
    elif change['new'] == 'newton':
        clear_output(wait=True)
        display(select)
        newton_change()
    elif change['new'] == 'nonlinear_block_gs':
        clear_output(wait=True)
        display(select)
        nonlinear_block_gs_change()
    elif change['new'] == 'nonlinear_block_jac':
        clear_output(wait=True)
        display(select)
        nonlinear_block_jac_change()
    elif change['new'] == 'nonlinear_runonce':
        clear_output(wait=True)
        display(select)
        nonlinear_runonce_change()


select = widgets.Dropdown(
    options=['broyden', 'newton', 'nonlinear_block_gs', 'nonlinear_block_jac',
             'nonlinear_runonce'],
    value='nonlinear_block_gs',
    description='Nonlinear solver :',
    style=style,
)

select.observe(onchange, names='value')
display(select)
nonlinear_block_gs_change()