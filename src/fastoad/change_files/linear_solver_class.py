"""
Linear solver class
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
import openmdao.solvers.linear as solvers

class LinearSolver:

    def __init__(self):

        # Parameters config file
        self.solver = None

        self.select = None

        self.vboxlinearsolver = v.Html(
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

        self.vboxaitkenlinear = v.Html(
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
        Initialize widgets for linear solvers
        """

        solver = solvers.direct.DirectSolver()


        iprintdirect = v.TextField(
            v_model=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            label="Print the output :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        assemble_jacdirect = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            label="Assemble jacobian",
            style_='margin-left:50px;width:500px;',
        )

        err_on_singular = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["err_on_singular"].get("value"),
            label="Raise an error if LU decomposition is singular",
        )

        def direct_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this linear solver
            """

            self.vboxaitkenlinear.children[0].children = []
            self.vboxaitkenlinear.children[1].children = []
            self.vboxlinearsolver.children[0].children = [iprintdirect, err_on_singular]
            self.vboxlinearsolver.children[1].children = [assemble_jacdirect]


        solver = solvers.linear_block_gs.LinearBlockGS()


        maxitergs = v.TextField(
            v_model=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            label="Maxiter :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        atolgs = v.TextField(
            v_model=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            label="Absolute Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;margin-left:50px;',
        )

        rtolgs = v.TextField(
            v_model=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            label="Relative Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        iprintgs = v.TextField(
            v_model=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            label="Print the output :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        err_on_non_convergegs = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            label="Err on non converge",
            style_='margin-bottom:20px;',
        )

        assemble_jacgs = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            label="Assemble jacobian",
        )

        use_aitkengs = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["use_aitken"].get("value"),
            label="Use Aitken relaxation",
            style_='margin-left:50px;',
        )

        aitken_min_factorgs = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_min_factor"].get("value"),
            min=0,
            max=100,
            label="Aitken min factor :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        aitken_max_factorgs = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_max_factor"].get("value"),
            min=0,
            max=100,
            label="Aitken max factor :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;margin-top:5px;',
        )

        aitken_initial_factorgs = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_initial_factor"].get("value"),
            min=0,
            max=100,
            label="Aitken initial factor :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        def change_use_aitkengs(widget, event, data):
            """
            A function which display or not the aitken options widgets, dependent on if you use aitken
            """

            if data:
                self.vboxaitkenlinear.children[0].children = [aitken_min_factorgs, aitken_initial_factorgs]
                self.vboxaitkenlinear.children[1].children = [aitken_max_factorgs]
            else:
                self.vboxaitkenlinear.children[0].children = []
                self.vboxaitkenlinear.children[1].children = []

        use_aitkengs.on_event('change', change_use_aitkengs)

        def linear_block_gs_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this linear solver
            """

            use_aitkengs.v_model = False
            self.vboxaitkenlinear.children[0].children = []
            self.vboxaitkenlinear.children[1].children = []
            self.vboxlinearsolver.children[0].children = [maxitergs, rtolgs, err_on_non_convergegs, assemble_jacgs]
            self.vboxlinearsolver.children[1].children = [atolgs, iprintgs, use_aitkengs]


        solver = solvers.linear_block_jac.LinearBlockJac()


        maxiterjac = v.TextField(
            v_model=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            label="Maxiter :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        atoljac = v.TextField(
            v_model=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            label="Absolute Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;margin-top:5px;',
        )

        rtoljac = v.TextField(
            v_model=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            label="Relative Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        iprintjac = v.TextField(
            v_model=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            label="Print the output :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        err_on_non_convergejac = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            label="Err on non converge",
        )

        assemble_jacblockjac = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            label="Assemble jacobian",
            style_='margin-left:50px;',
        )

        def linear_block_jac_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this linear solver
            """

            self.vboxaitkenlinear.children[0].children = []
            self.vboxaitkenlinear.children[1].children = []
            self.vboxlinearsolver.children[0].children = [maxiterjac, rtoljac, err_on_non_convergejac]
            self.vboxlinearsolver.children[1].children = [atoljac, iprintjac, assemble_jacblockjac]


        solver = solvers.linear_runonce.LinearRunOnce()


        iprintrunonce = v.TextField(
            v_model=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            label="Print the output :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        assemble_jacrunonce = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            label="Assemble jacobian",
        )

        use_aitkenrunonce = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["use_aitken"].get("value"),
            label="Use Aitken relaxation",
            style_='margin-left:50px;width:500px;',
        )

        aitken_min_factorrunonce = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_min_factor"].get("value"),
            min=0,
            max=100,
            label="Aitken min factor :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        aitken_max_factorrunonce = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_max_factor"].get("value"),
            min=0,
            max=100,
            label="Aitken max factor :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;margin-top:5px;',
        )

        aitken_initial_factorrunonce = v.TextField(
            v_model=solver.options.__dict__["_dict"]["aitken_initial_factor"].get("value"),
            min=0,
            max=100,
            label="Aitken initial factor :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        def change_use_aitkenrunonce(widget, event, data):
            """
            A function which display or not the aitken options widgets, dependent on if you use aitken
            """

            if data:
                self.vboxaitkenlinear.children[0].children = [aitken_min_factorrunonce, aitken_initial_factorrunonce]
                self.vboxaitkenlinear.children[1].children = [aitken_max_factorrunonce]
            else:
                self.vboxaitkenlinear.children[0].children = []
                self.vboxaitkenlinear.children[1].children = []

        use_aitkenrunonce.on_event('change', change_use_aitkenrunonce)

        def linear_runonce_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this linear solver
            """

            use_aitkenrunonce.v_model = False
            self.vboxaitkenlinear.children[0].children = []
            self.vboxaitkenlinear.children[1].children = []
            self.vboxlinearsolver.children[0].children = [iprintrunonce, assemble_jacrunonce]
            self.vboxlinearsolver.children[1].children = [use_aitkenrunonce]


        def petsc_ksp_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this linear solver
            """

            self.vboxaitkenlinear.children[0].children = []
            self.vboxaitkenlinear.children[1].children = []
            self.vboxlinearsolver.children[0].children = []
            self.vboxlinearsolver.children[1].children = []


        solver = solvers.scipy_iter_solver.ScipyKrylov()


        maxiterspicy = v.TextField(
            v_model=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            label="Maxiter :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        atolspicy = v.TextField(
            v_model=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            label="Absolute Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;margin-left:50px;',
        )

        rtolspicy = v.TextField(
            v_model=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            label="Relative Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        iprintspicy = v.TextField(
            v_model=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            label="Print the output :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        err_on_non_convergespicy = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            label="Err on non converge",
            style_='margin-bottom:20px;',
        )

        assemble_jacspicy = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            label="Assemble jacobian",
        )

        restart = v.TextField(
            v_model=solver.options.__dict__["_dict"]["restart"].get("value"),
            min=0,
            max=1000,
            label="Restart :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        def scipy_iter_solver_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this linear solver
            """

            self.vboxaitkenlinear.children[0].children = []
            self.vboxaitkenlinear.children[1].children = []
            self.vboxlinearsolver.children[0].children = [maxiterspicy, rtolspicy, err_on_non_convergespicy, assemble_jacspicy]
            self.vboxlinearsolver.children[1].children = [atolspicy, iprintspicy, restart]


        solver = solvers.user_defined.LinearUserDefined()


        maxiteruser = v.TextField(
            v_model=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            label="Maxiter :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;',
        )

        atoluser = v.TextField(
            v_model=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            label="Absolute Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;margin-top:5px;margin-left:50px;',
        )

        rtoluser = v.TextField(
            v_model=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            label="Relative Error Tolerance :",
            type='number',
            outlined=True,
            style_='width:500px;',
        )

        iprintuser = v.TextField(
            v_model=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            label="Print the output :",
            type='number',
            outlined=True,
            style_='width:500px;margin-left:50px;',
        )

        err_on_non_convergeuser = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            label="Err on non converge",
        )

        assemble_jacuser = v.Checkbox(
            v_model=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            label="Assemble jacobian",
            style_='margin-left:50px;',
        )

        def user_defined_change():
            """
            Adapt widgets & vbox widgets to only display widgets you need in this linear solver
            """

            self.vboxaitkenlinear.children[0].children = []
            self.vboxaitkenlinear.children[1].children = []
            self.vboxlinearsolver.children[0].children = [maxiteruser, rtoluser, err_on_non_convergeuser]
            self.vboxlinearsolver.children[1].children = [atoluser, iprintuser, assemble_jacuser]


        def onchange(widget, event, data):
            """
            A function which start the function you need for your linear driver
            """

            if data == "direct":
                direct_change()
            elif data == "linear_block_gs":
                linear_block_gs_change()
            elif data == "linear_block_jac":
                linear_block_jac_change()
            elif data == "linear_runonce":
                linear_runonce_change()
            elif data == "petsc_ksp":
                petsc_ksp_change()
            elif data == "scipy_iter_solver":
                scipy_iter_solver_change()
            elif data == "user_defined":
                user_defined_change()

        self.select = v.Select(
            items=[
                "direct",
                "linear_block_gs",
                "linear_block_jac",
                "linear_runonce",
                "petsc_ksp",
                "scipy_iter_solver",
                "user_defined",
            ],
            v_model="direct",
            label="Linear solvers :",
            outlined=True,
            style_='margin-top:5px;',
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
        direct_change()
        display(self.vboxlinearsolver)
        display(self.vboxaitkenlinear)
        display(btn)

    def save(self):

        self.solver = "linear_solver: "
        if (self.select.v_model == "direct"):
            self.solver += "om.DirectSolver("
            self.solver += "iprint="+str(self.vboxlinearsolver.children[0].children[0].v_model)
            self.solver += ",assemble_jac="+str(self.vboxlinearsolver.children[1].children[0].v_model)
            self.solver += ",err_on_singular="+str(self.vboxlinearsolver.children[0].children[1].v_model)+")"
        elif (self.select.v_model == "linear_block_gs"):
            self.solver += "om.LinearBlockGS("
            self.solver += "maxiter="+str(self.vboxlinearsolver.children[0].children[0].v_model)
            self.solver += ",atol="+str(self.vboxlinearsolver.children[1].children[0].v_model)
            self.solver += ",rtol="+str(self.vboxlinearsolver.children[0].children[1].v_model)
            self.solver += ",iprint="+str(self.vboxlinearsolver.children[1].children[1].v_model)
            self.solver += ",err_on_non_converge="+str(self.vboxlinearsolver.children[0].children[2].v_model)
            self.solver += ",use_aitken="+str(self.vboxlinearsolver.children[1].children[2].v_model)
            self.solver += ",assemble_jac="+str(self.vboxlinearsolver.children[0].children[3].v_model)
            if(str(self.vboxlinearsolver.children[1].children[2].v_model)=="True"):
                self.solver += ",aitken_min_factor="+str(self.vboxaitkenlinear.children[0].children[0].v_model)
                self.solver += ",aitken_max_factor="+str(self.vboxaitkenlinear.children[1].children[0].v_model)
                self.solver += ",aitken_initial_factor="+str(self.vboxaitkenlinear.children[0].children[1].v_model)
            self.solver += ")"
        elif (self.select.v_model == "linear_block_jac"):
            self.solver += "om.LinearBlockJac("
            self.solver += "maxiter="+str(self.vboxlinearsolver.children[0].children[0].v_model)
            self.solver += ",atol="+str(self.vboxlinearsolver.children[1].children[0].v_model)
            self.solver += ",rtol="+str(self.vboxlinearsolver.children[0].children[1].v_model)
            self.solver += ",iprint="+str(self.vboxlinearsolver.children[1].children[1].v_model)
            self.solver += ",err_on_non_converge="+str(self.vboxlinearsolver.children[0].children[2].v_model)
            self.solver += ",assemble_jac="+str(self.vboxlinearsolver.children[1].children[2].v_model)+")"
        elif (self.select.v_model == "linear_runonce"):
            self.solver += "om.LinearRunOnce("
            self.solver += "iprint="+str(self.vboxlinearsolver.children[0].children[0].v_model)
            self.solver += ",use_aitken="+str(self.vboxlinearsolver.children[1].children[0].v_model)
            self.solver += ",assemble_jac="+str(self.vboxlinearsolver.children[0].children[1].v_model)
            if(str(self.vboxlinearsolver.children[1].children[0].v_model)=="True"):
                self.solver += ",aitken_min_factor="+str(self.vboxaitkenlinear.children[0].children[0].v_model)
                self.solver += ",aitken_max_factor="+str(self.vboxaitkenlinear.children[1].children[0].v_model)
                self.solver += ",aitken_initial_factor="+str(self.vboxaitkenlinear.children[0].children[1].v_model)
            self.solver += ")"
        elif (self.select.v_model == "petsc_ksp"):
            self.solver += "om.PETScKrylov()"
        elif (self.select.v_model == "scipy_iter_solver"):
            self.solver += "om.ScipyKrylov("
            self.solver += "maxiter="+str(self.vboxlinearsolver.children[0].children[0].v_model)
            self.solver += ",atol="+str(self.vboxlinearsolver.children[1].children[0].v_model)
            self.solver += ",rtol="+str(self.vboxlinearsolver.children[0].children[1].v_model)
            self.solver += ",iprint="+str(self.vboxlinearsolver.children[1].children[1].v_model)
            self.solver += ",err_on_non_converge="+str(self.vboxlinearsolver.children[0].children[2].v_model)
            self.solver += ",restart="+str(self.vboxlinearsolver.children[1].children[2].v_model)
            self.solver += ",assemble_jac="+str(self.vboxlinearsolver.children[0].children[3].v_model)+")"
        elif (self.select.v_model == "user_defined"):
            self.solver += "om.LinearUserDefined("
            self.solver += "maxiter="+str(self.vboxlinearsolver.children[0].children[0].v_model)
            self.solver += ",atol="+str(self.vboxlinearsolver.children[1].children[0].v_model)
            self.solver += ",rtol="+str(self.vboxlinearsolver.children[0].children[1].v_model)
            self.solver += ",iprint="+str(self.vboxlinearsolver.children[1].children[1].v_model)
            self.solver += ",err_on_non_converge="+str(self.vboxlinearsolver.children[0].children[2].v_model)
            self.solver += ",assemble_jac="+str(self.vboxlinearsolver.children[1].children[2].v_model) + ")"
        print(self.solver)

    def display(self):

        self.initialize()