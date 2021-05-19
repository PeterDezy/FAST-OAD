"""
Non Linear solver class
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
import ipyvuetify as v
import ipywidgets as widgets
import openmdao.solvers.nonlinear as solversnonlinear

class NonLinearSolver:

    def __init__(self):

        # Parameters config file
        self.solver = None

        self.select = None

        self.vboxnonlinearsolver = v.Html(
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

        self.vboxaitken = v.Html(
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

        self.vboxsubsolves = v.Html(
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

    def initialize(self):

        """
        Initialize widgets for non-linear solvers
        """

        solver = solversnonlinear.broyden.BroydenSolver()

        maxiter = v.TextField(
            v_model=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=0,
            max=10000,
            label="Maxiter :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        atol = v.TextField(
            v_model=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=0,
            max=1,
            label="Absolute Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;margin-left:50px;',
        )

        rtol = v.TextField(
            v_model=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=0,
            max=1,
            label="Relative Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        iprint = v.TextField(
            v_model=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            label="Print the output :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        err_on_non_converge = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            label="Err on non converge",
            style_='margin-bottom:20px;',
        )

        debug_print = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["debug_print"].get("value"),
            label="Debug Print",
            style_='margin-left:50px;margin-bottom:20px;',
        )

        stall_limit = v.TextField(
            v_model=solver.options.__dict__["_dict"]["stall_limit"].get("value"),
            min=0,
            max=100,
            label="Stall Limit :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        stall_tol = v.TextField(
            v_model=solver.options.__dict__["_dict"]["stall_tol"].get("value"),
            min=0,
            max=1,
            label="Stall tol :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        alpha = v.TextField(
            v_model=solver.options.__dict__["_dict"]["alpha"].get("value"),
            min=0,
            max=10,
            label="Alpha :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        compute_jacobian = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["compute_jacobian"].get("value"),
            label="Compute Jacobian",
            style_='margin-left:50px;margin-bottom:35px;',
        )

        converge_limit = v.TextField(
            v_model=solver.options.__dict__["_dict"]["converge_limit"].get("value"),
            min=0,
            max=100,
            label="Converge limit :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        cs_reconvergebroyden = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["cs_reconverge"].get("value"),
            label="Cs reconverge",
            style_='margin-left:50px;margin-bottom:20px;',
        )

        diverge_limit = v.TextField(
            v_model=solver.options.__dict__["_dict"]["diverge_limit"].get("value"),
            min=0,
            max=100,
            label="Diverge Limit :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        max_converge_failures = v.TextField(
            v_model=solver.options.__dict__["_dict"]["max_converge_failures"].get("value"),
            min=0,
            max=100,
            label="Max Converge Failures :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        max_jacobians = v.TextField(
            v_model=solver.options.__dict__["_dict"]["max_jacobians"].get("value"),
            min=0,
            max=100,
            label="Max Jacobians :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        state_vars = v.TextField(
            v_model="[]",
            label="State Vars :",
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        update_broyden = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["update_broyden"].get("value"),
            label="Update Broyden",
        )

        reraise_child_analysiserrorbroyden = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["reraise_child_analysiserror"].get("value"),
            label="Reraise child Analysis Error",
            style_='margin-left:50px;',
        )

        def broyden_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this non-linear solver
            """

            self.vboxsubsolves.children[0].children = []
            self.vboxaitken.children[0].children = []
            self.vboxaitken.children[1].children = []
            self.vboxnonlinearsolver.children[0].children = [maxiter, rtol, err_on_non_converge, stall_limit, alpha,
                                                             converge_limit, diverge_limit, max_jacobians,
                                                             update_broyden]
            self.vboxnonlinearsolver.children[1].children = [atol, iprint, debug_print, stall_tol, compute_jacobian,
                                                             cs_reconvergebroyden, max_converge_failures, state_vars,
                                                             reraise_child_analysiserrorbroyden]

        solver = solversnonlinear.newton.NewtonSolver()

        solve_subsystems = v.Checkbox(
            v_model=False,
            label="Solve Subsystems",
        )

        max_sub_solves = v.TextField(
            v_model=solver.options.__dict__["_dict"]["max_sub_solves"].get("value"),
            min=0,
            max=100,
            label="Max Sub Solves :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        cs_reconvergenewton = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["cs_reconverge"].get("value"),
            label="Cs reconverge",
        )

        reraise_child_analysiserrornewton = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["reraise_child_analysiserror"].get("value"),
            label="Reraise child Analysis Error",
            style_='margin-left:50px;'
        )

        def change_use_solve_subsystems(widget, event, data):
            """
            A function which display or not the 'max_sub_solves' widget, dependent on if you use solve subsystems
            """

            if data:
                self.vboxsubsolves.children[0].children = [max_sub_solves]
            else:
                self.vboxsubsolves.children[0].children = []

        solve_subsystems.on_event('change', change_use_solve_subsystems)

        def newton_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this non-linear solver
            """

            solve_subsystems.v_model = False
            self.vboxaitken.children[0].children = []
            self.vboxaitken.children[1].children = []
            self.vboxnonlinearsolver.children[0].children = [maxiter, rtol, err_on_non_converge, stall_limit,
                                                             solve_subsystems, cs_reconvergenewton]
            self.vboxnonlinearsolver.children[1].children = [atol, iprint, debug_print, stall_tol,
                                                             reraise_child_analysiserrornewton]

        solver = solversnonlinear.nonlinear_block_gs.NonlinearBlockGS()

        use_aitken = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["use_aitken"].get("value"),
            label="Use Aitken relaxation",
        )

        aitken_min_factor = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_min_factor"].get("value"),
            min=0,
            max=100,
            label="Aitken min factor :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        aitken_max_factor = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_max_factor"].get("value"),
            min=0,
            max=100,
            label="Aitken max factor :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;margin-left:50px;',
        )

        aitken_initial_factor = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_initial_factor"].get("value"),
            min=0,
            max=1,
            label="Aitken initial factor :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        cs_reconvergegs = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["cs_reconverge"].get("value"),
            label="Cs reconverge",
            style_='margin-left:50px;',
        )

        use_apply_nonlinear = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["use_apply_nonlinear"].get("value"),
            label="Use apply nonlinear",
            style_='width:500px;margin-left:50px;',
        )

        reraise_child_analysiserrorgs = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["reraise_child_analysiserror"].get("value"),
            label="Reraise child Analysis Error",
        )

        def change_use_aitken(widget, event, data):
            """
            A function which display or not the aitken options widgets, dependent on if you use aitken
            """

            if data:
                self.vboxaitken.children[0].children = [aitken_min_factor, aitken_initial_factor]
                self.vboxaitken.children[1].children = [aitken_max_factor]
            else:
                self.vboxaitken.children[0].children = []
                self.vboxaitken.children[1].children = []

        use_aitken.on_event('change', change_use_aitken)

        def nonlinear_block_gs_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this non-linear solver
            """

            self.vboxsubsolves.children[0].children = []
            use_aitken.v_model = False
            self.vboxnonlinearsolver.children[0].children = [maxiter, rtol, err_on_non_converge, stall_limit,
                                                             use_aitken, reraise_child_analysiserrorgs]
            self.vboxnonlinearsolver.children[1].children = [atol, iprint, debug_print, stall_tol, cs_reconvergegs,
                                                             use_apply_nonlinear]

        def nonlinear_block_jac_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this non-linear solver
            """

            self.vboxsubsolves.children[0].children = []
            self.vboxaitken.children[0].children = []
            self.vboxaitken.children[1].children = []
            self.vboxnonlinearsolver.children[0].children = [maxiter, rtol, err_on_non_converge, stall_limit]
            self.vboxnonlinearsolver.children[1].children = [atol, iprint, debug_print, stall_tol]

        iprintrunonce = v.TextField(
            v_model=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            label="Print the output :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        def nonlinear_runonce_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this non-linear solver
            """

            self.vboxsubsolves.children[0].children = []
            self.vboxnonlinearsolver.children[0].children = [iprintrunonce]
            self.vboxnonlinearsolver.children[1].children = []

        def onchange(widget, event, data):
            """
            A function which start the function you need for your non-linear driver
            """

            if data == "broyden":
                broyden_change()
            elif data == "newton":
                newton_change()
            elif data == "nonlinear_block_gs":
                nonlinear_block_gs_change()
            elif data == "nonlinear_block_jac":
                nonlinear_block_jac_change()
            elif data == "nonlinear_runonce":
                nonlinear_runonce_change()

        self.select = v.Select(
            items=["broyden", "newton", "nonlinear_block_gs", "nonlinear_block_jac", "nonlinear_runonce"],
            v_model="nonlinear_block_gs",
            label="Nonlinear solver :",
            outlined=True,
            style_="margin-top:5px;",
        )

        self.select.on_event('change', onchange)

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

        display(self.select)
        nonlinear_block_gs_change()
        display(self.vboxnonlinearsolver)
        display(self.vboxaitken)
        display(self.vboxsubsolves)
        display(btn)

    def save(self):

        self.solver = "nonlinear_solver: "
        if (self.select.v_model == "broyden"):
            self.solver += "om.BroydenSolver("
            self.solver += "maxiter="+str(self.vboxnonlinearsolver.children[0].children[0].v_model)
            self.solver += ",atol="+str(self.vboxnonlinearsolver.children[1].children[0].v_model)
            self.solver += ",rtol="+str(self.vboxnonlinearsolver.children[0].children[1].v_model)
            self.solver += ",iprint="+str(self.vboxnonlinearsolver.children[1].children[1].v_model)
            self.solver += ",err_on_non_converge="+str(self.vboxnonlinearsolver.children[0].children[2].v_model)
            self.solver += ",debug_print="+str(self.vboxnonlinearsolver.children[1].children[2].v_model)
            self.solver += ",stall_limit="+str(self.vboxnonlinearsolver.children[0].children[3].v_model)
            self.solver += ",stall_tol="+str(self.vboxnonlinearsolver.children[1].children[3].v_model)
            self.solver += ",alpha="+str(self.vboxnonlinearsolver.children[0].children[4].v_model)
            self.solver += ",compute_jacobian="+str(self.vboxnonlinearsolver.children[1].children[4].v_model)
            self.solver += ",converge_limit="+str(self.vboxnonlinearsolver.children[0].children[5].v_model)
            self.solver += ",cs_reconverge="+str(self.vboxnonlinearsolver.children[1].children[5].v_model)
            self.solver += ",diverge_limit="+str(self.vboxnonlinearsolver.children[0].children[6].v_model)
            self.solver += ",max_converge_failures="+str(self.vboxnonlinearsolver.children[1].children[6].v_model)
            self.solver += ",max_jacobians="+str(self.vboxnonlinearsolver.children[0].children[7].v_model)
            self.solver += ",state_vars="+str(self.vboxnonlinearsolver.children[1].children[7].v_model)
            self.solver += ",update_broyden="+str(self.vboxnonlinearsolver.children[0].children[8].v_model)
            self.solver += ",reraise_child_analysiserror="+str(self.vboxnonlinearsolver.children[1].children[8].v_model)
            self.solver += ")"
        elif (self.select.v_model == "newton"):
            self.solver += "om.NewtonSolver("
            self.solver += "maxiter="+str(self.vboxnonlinearsolver.children[0].children[0].v_model)
            self.solver += ",atol="+str(self.vboxnonlinearsolver.children[1].children[0].v_model)
            self.solver += ",rtol="+str(self.vboxnonlinearsolver.children[0].children[1].v_model)
            self.solver += ",iprint="+str(self.vboxnonlinearsolver.children[1].children[1].v_model)
            self.solver += ",err_on_non_converge="+str(self.vboxnonlinearsolver.children[0].children[2].v_model)
            self.solver += ",debug_print="+str(self.vboxnonlinearsolver.children[1].children[2].v_model)
            self.solver += ",stall_limit="+str(self.vboxnonlinearsolver.children[0].children[3].v_model)
            self.solver += ",stall_tol="+str(self.vboxnonlinearsolver.children[1].children[3].v_model)
            self.solver += ",solve_subsystems="+str(self.vboxnonlinearsolver.children[0].children[4].v_model)
            self.solver += ",cs_reconverge="+str(self.vboxnonlinearsolver.children[1].children[4].v_model)
            self.solver += ",reraise_child_analysiserror="+str(self.vboxnonlinearsolver.children[0].children[5].v_model)
            if (str(self.vboxnonlinearsolver.children[0].children[4].v_model) == "True"):
                self.solver += ",max_sub_solves="+str(self.vboxsubsolves.children[0].children[0].v_model)
            self.solver += ")"
        elif (self.select.v_model == "nonlinear_block_gs"):
            self.solver += "om.NonlinearBlockGS("
            self.solver += "maxiter="+str(self.vboxnonlinearsolver.children[0].children[0].v_model)
            self.solver += ",atol="+str(self.vboxnonlinearsolver.children[1].children[0].v_model)
            self.solver += ",rtol="+str(self.vboxnonlinearsolver.children[0].children[1].v_model)
            self.solver += ",iprint="+str(self.vboxnonlinearsolver.children[1].children[1].v_model)
            self.solver += ",err_on_non_converge="+str(self.vboxnonlinearsolver.children[0].children[2].v_model)
            self.solver += ",debug_print="+str(self.vboxnonlinearsolver.children[1].children[2].v_model)
            self.solver += ",stall_limit="+str(self.vboxnonlinearsolver.children[0].children[3].v_model)
            self.solver += ",stall_tol="+str(self.vboxnonlinearsolver.children[1].children[3].v_model)
            self.solver += ",use_aitken="+str(self.vboxnonlinearsolver.children[0].children[4].v_model)
            self.solver += ",cs_reconverge="+str(self.vboxnonlinearsolver.children[1].children[4].v_model)
            self.solver += ",use_apply_nonlinear="+str(self.vboxnonlinearsolver.children[0].children[5].v_model)
            self.solver += ",reraise_child_analysiserror="+str(self.vboxnonlinearsolver.children[1].children[5].v_model)
            if (str(self.vboxnonlinearsolver.children[0].children[4].v_model) == "True"):
                self.solver += ",aitken_min_factor="+str(self.vboxaitken.children[0].children[0].v_model)
                self.solver += ",aitken_max_factor="+str(self.vboxaitken.children[1].children[0].v_model)
                self.solver += ",aitken_initial_factor="+str(self.vboxaitken.children[0].children[1].v_model)
            self.solver += ")"
        elif (self.select.v_model == "nonlinear_block_jac"):
            self.solver += "om.NonlinearBlockJac("
            self.solver += "maxiter="+str(self.vboxnonlinearsolver.children[0].children[0].v_model)
            self.solver += ",atol="+str(self.vboxnonlinearsolver.children[1].children[0].v_model)
            self.solver += ",rtol="+str(self.vboxnonlinearsolver.children[0].children[1].v_model)
            self.solver += ",iprint="+str(self.vboxnonlinearsolver.children[1].children[1].v_model)
            self.solver += ",err_on_non_converge="+str(self.vboxnonlinearsolver.children[0].children[2].v_model)
            self.solver += ",debug_print="+str(self.vboxnonlinearsolver.children[1].children[2].v_model)
            self.solver += ",stall_limit="+str(self.vboxnonlinearsolver.children[0].children[3].v_model)
            self.solver += ",stall_tol="+str(self.vboxnonlinearsolver.children[1].children[3].v_model)+")"
        elif (self.select.v_model == "nonlinear_runonce"):
            self.solver += "om.NonlinearRunOnce("
            self.solver += "iprint="+str(self.vboxnonlinearsolver.children[0].children[0].v_model)+")"
        print(self.solver)

    def display(self):

        self.initialize()