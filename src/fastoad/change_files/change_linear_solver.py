"""
Change the linear solver in the configuration file
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

from IPython.display import clear_output, HTML, display
import ipywidgets as widgets
from ruamel.yaml import YAML
import openmdao.solvers.linear as solvers


css = "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;} .green {background-color: lightgreen;} </style>"
html = HTML(css)
display(html)


def ChangeLinearSolver():

    """
    A class to change the linear solver in the configuration file
    """

    def __init__(self):
        # The file name
        self.file_name = "./workdir/oad_process.yml"

        # Ruamel yaml
        self.yaml = YAML()

        # Css
        self.css = (
            "<style> .left {margin-left: 9%;} .right {margin-right: 10%;} .top {margin-top: 20px;} "
        )
        self.css += ".green {background-color: lightgreen;} </style>"
        self.html = HTML(self.css)

    def direct_change(self):

        solver = solvers.direct.DirectSolver()

        # print(solver.options.__dict__)

        def save(b):
            yaml = YAML()
            file_name = "./workdir/oad_process.yml"
            with open(file_name, "r") as f:
                doc = yaml.load(f)

            try:
                doc["model"]["linear_solver"] = (
                    "om.DirectSolver(iprint="
                    + str(iprint.value)
                    + ",assemble_jac="
                    + str(assemble_jac.value)
                    + ",err_on_singular="
                    + str(err_on_singular.value)
                    + ")"
                )
                with open(file_name, "w") as f:
                    yaml.dump(doc, f)
                print("Successfully changed options.\n")

            except:
                raise ValueError("Error while modifying.\n")

        self.iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        self.assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        self.err_on_singular = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_singular"].get("value"),
            description="Raise an error if LU decomposition is singular",
            style=style,
            disabled=False,
        )

        left_box = widgets.VBox([self.iprint])
        right_box = widgets.VBox([self.assemble_jac, self.err_on_singular])
        self.vbox = widgets.HBox([left_box, right_box])

        # Left Widgets

        # Right Widgets
        self.err_on_singular.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(self.vbox)

    def linear_block_gs_change():

        solver = solvers.linear_block_gs.LinearBlockGS()

        # print(solver.options.__dict__)

        def save(b):
            yaml = YAML()
            file_name = "./workdir/oad_process.yml"
            with open(file_name, "r") as f:
                doc = yaml.load(f)

            try:
                doc["model"]["linear_solver"] = (
                    "om.LinearBlockGS(maxiter="
                    + str(maxiter.value)
                    + ",atol="
                    + str(atol.value)
                    + ",rtol="
                    + str(rtol.value)
                    + ",iprint="
                    + str(iprint.value)
                    + ",err_on_non_converge="
                    + str(err_on_non_converge.value)
                    + ",assemble_jac="
                    + str(assemble_jac.value)
                    + ",use_aitken="
                    + str(use_aitken.value)
                )
                if str(use_aitken.value) == "True":
                    doc["model"]["linear_solver"] += (
                        ",aitken_min_factor="
                        + str(aitken_min_factor.value)
                        + ",aitken_max_factor="
                        + str(aitken_max_factor.value)
                        + ",aitken_initial_factor="
                        + str(aitken_initial_factor.value)
                    )

                doc["model"]["linear_solver"] += ")"
                with open(file_name, "w") as f:
                    yaml.dump(doc, f)
                print("Successfully changed options.\n")

            except:
                raise ValueError("Error while modifying.\n")

        self.maxiter = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            description="Maxiter :",
            style=style,
            disabled=False,
        )

        self.atol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            description="Absolute Error Tolerance :",
            style=style,
            disabled=False,
        )

        self.rtol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            description="Relative Error Tolerance :",
            style=style,
            disabled=False,
        )

        self.iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        self.err_on_non_converge = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            description="When True, AnalysisError will be raised if we don't converge",
            style=style,
            disabled=False,
        )

        self.assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        self.use_aitken = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["use_aitken"].get("value"),
            description="Use Aitken relaxation",
            disabled=False,
        )

        self.aitken_min_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_min_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken min factor :",
            style=style,
            disabled=False,
        )

        self.aitken_max_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_max_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken max factor :",
            style=style,
            disabled=False,
        )

        self.aitken_initial_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_initial_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken initial factor :",
            style=style,
            disabled=False,
        )

        self.vb = widgets.VBox(children=[])

        def change_use_aitken(b):

            if b["new"]:
                vb.children = [
                    self.aitken_min_factor,
                    self.aitken_max_factor,
                    self.aitken_initial_factor,
                ]
            else:
                vb.children = []

        use_aitken.observe(change_use_aitken, names="value")

        left_box = widgets.VBox(
            [self.maxiter, self.rtol, self.err_on_non_converge, self.assemble_jac]
        )
        right_box = widgets.VBox([self.atol, self.iprint, self.use_aitken, self.vb])
        self.vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        self.rtol.add_class("top")
        self.err_on_non_converge.add_class("top")
        self.assemble_jac.add_class("top")

        # Right Widgets
        self.iprint.add_class("top")
        self.use_aitken.add_class("top")
        self.vb.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")

        display(self.vbox)

    def linear_block_jac_change():

        solver = solvers.linear_block_jac.LinearBlockJac()

        # print(solver.options.__dict__)

        def save(b):
            yaml = YAML()
            file_name = "./workdir/oad_process.yml"
            with open(file_name, "r") as f:
                doc = yaml.load(f)

            try:
                doc["model"]["linear_solver"] = (
                    "om.LinearBlockJac(maxiter="
                    + str(maxiter.value)
                    + ",atol="
                    + str(atol.value)
                    + ",rtol="
                    + str(rtol.value)
                    + ",iprint="
                    + str(iprint.value)
                    + ",err_on_non_converge="
                    + str(err_on_non_converge.value)
                    + ",assemble_jac="
                    + str(assemble_jac.value)
                    + ")"
                )
                with open(file_name, "w") as f:
                    yaml.dump(doc, f)
                print("Successfully changed options.\n")

            except:
                raise ValueError("Error while modifying.\n")

        self.maxiter = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            description="Maxiter :",
            style=style,
            disabled=False,
        )

        self.atol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            description="Absolute Error Tolerance :",
            style=style,
            disabled=False,
        )

        self.rtol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            description="Relative Error Tolerance :",
            style=style,
            disabled=False,
        )

        self.iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        self.err_on_non_converge = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            description="When True, AnalysisError will be raised if we don't converge",
            style=style,
            disabled=False,
        )

        self.assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        left_box = widgets.VBox([self.maxiter, self.rtol, self.err_on_non_converge])
        right_box = widgets.VBox([self.atol, self.iprint, self.assemble_jac])
        self.vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        self.rtol.add_class("top")
        self.err_on_non_converge.add_class("top")

        # Right Widgets
        self.iprint.add_class("top")
        self.assemble_jac.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(self.vbox)

    def linear_runonce_change():

        solver = solvers.linear_runonce.LinearRunOnce()

        # print(solver.options.__dict__)

        def save(b):
            yaml = YAML()
            file_name = "./workdir/oad_process.yml"
            with open(file_name, "r") as f:
                doc = yaml.load(f)

            try:
                doc["model"]["linear_solver"] = (
                    "om.LinearRunOnce(iprint="
                    + str(iprint.value)
                    + ",assemble_jac="
                    + str(assemble_jac.value)
                    + ",use_aitken="
                    + str(use_aitken.value)
                )
                if str(use_aitken.value) == "True":
                    doc["model"]["linear_solver"] += (
                        ",aitken_min_factor="
                        + str(aitken_min_factor.value)
                        + ",aitken_max_factor="
                        + str(aitken_max_factor.value)
                        + ",aitken_initial_factor="
                        + str(aitken_initial_factor.value)
                    )

                doc["model"]["linear_solver"] += ")"
                with open(file_name, "w") as f:
                    yaml.dump(doc, f)
                print("Successfully changed options.\n")

            except:
                raise ValueError("Error while modifying.\n")

        self.iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        self.assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        self.use_aitken = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["use_aitken"].get("value"),
            description="Use Aitken relaxation",
            disabled=False,
        )

        self.aitken_min_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_min_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken min factor :",
            style=style,
            disabled=False,
        )

        self.aitken_max_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_max_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken max factor :",
            style=style,
            disabled=False,
        )

        self.aitken_initial_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_initial_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken initial factor :",
            style=style,
            disabled=False,
        )

        self.vb = widgets.VBox(children=[])

        def change_use_aitken(b):

            if b["new"]:
                vb.children = [
                    self.aitken_min_factor,
                    self.aitken_max_factor,
                    self.aitken_initial_factor,
                ]
            else:
                vb.children = []

        use_aitken.observe(change_use_aitken, names="value")

        left_box = widgets.VBox([self.iprint, self.assemble_jac])
        right_box = widgets.VBox([self.use_aitken, self.vb])
        self.vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        self.assemble_jac.add_class("top")

        # Right Widgets
        self.vb.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(self.vbox)

    def petsc_ksp_change():  # basique sans option celui là
        def save(b):
            yaml = YAML()
            file_name = "./workdir/oad_process.yml"
            with open(file_name, "r") as f:
                doc = yaml.load(f)

            try:
                doc["model"]["linear_solver"] = "om.PETScKrylov()"
                with open(file_name, "w") as f:
                    yaml.dump(doc, f)
                print("Successfully changed options.\n")

            except:
                raise ValueError("Error while modifying.\n")

    def scipy_iter_solver_change():

        solver = solvers.scipy_iter_solver.ScipyKrylov()

        # print(solver.options.__dict__)

        def save(b):
            yaml = YAML()
            file_name = "./workdir/oad_process.yml"
            with open(file_name, "r") as f:
                doc = yaml.load(f)

            try:
                doc["model"]["linear_solver"] = (
                    "om.ScipyKrylov(maxiter="
                    + str(maxiter.value)
                    + ",atol="
                    + str(atol.value)
                    + ",rtol="
                    + str(rtol.value)
                    + ",iprint="
                    + str(iprint.value)
                    + ",err_on_non_converge="
                    + str(err_on_non_converge.value)
                    + ",assemble_jac="
                    + str(assemble_jac.value)
                    + ",restart="
                    + str(restart.value)
                    + ")"
                )
                with open(file_name, "w") as f:
                    yaml.dump(doc, f)
                print("Successfully changed options.\n")

            except:
                raise ValueError("Error while modifying.\n")

        self.maxiter = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            description="Maxiter :",
            style=style,
            disabled=False,
        )

        self.atol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            description="Absolute Error Tolerance :",
            style=style,
            disabled=False,
        )

        self.rtol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            description="Relative Error Tolerance :",
            style=style,
            disabled=False,
        )

        self.iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        self.err_on_non_converge = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            description="When True, AnalysisError will be raised if we don't converge",
            style=style,
            disabled=False,
        )

        self.assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        self.restart = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["restart"].get("value"),
            min=0,
            max=1000,
            description="Restart :",
            style=style,
            disabled=False,
        )

        left_box = widgets.VBox(
            [self.maxiter, self.rtol, self.err_on_non_converge, self.assemble_jac]
        )
        right_box = widgets.VBox([self.atol, self.iprint, self.restart])
        self.vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        self.rtol.add_class("top")
        self.err_on_non_converge.add_class("top")
        self.assemble_jac.add_class("top")

        # Right Widgets
        self.iprint.add_class("top")
        self.restart.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(self.vbox)

    def user_defined_change():

        solver = solvers.user_defined.LinearUserDefined()

        # print(solver.options.__dict__)

        def save(b):
            yaml = YAML()
            file_name = "./workdir/oad_process.yml"
            with open(file_name, "r") as f:
                doc = yaml.load(f)

            try:
                doc["model"]["linear_solver"] = (
                    "om.LinearUserDefined(maxiter="
                    + str(maxiter.value)
                    + ",atol="
                    + str(atol.value)
                    + ",rtol="
                    + str(rtol.value)
                    + ",iprint="
                    + str(iprint.value)
                    + ",err_on_non_converge="
                    + str(err_on_non_converge.value)
                    + ",assemble_jac="
                    + str(assemble_jac.value)
                    + ")"
                )
                with open(file_name, "w") as f:
                    yaml.dump(doc, f)
                print("Successfully changed options.\n")

            except:
                raise ValueError("Error while modifying.\n")

        self.maxiter = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            description="Maxiter :",
            style=style,
            disabled=False,
        )

        self.atol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            description="Absolute Error Tolerance :",
            style=style,
            disabled=False,
        )

        self.rtol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            description="Relative Error Tolerance :",
            style=style,
            disabled=False,
        )

        self.iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        self.err_on_non_converge = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            description="When True, AnalysisError will be raised if we don't converge",
            style=style,
            disabled=False,
        )

        self.assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        left_box = widgets.VBox(
            [self.maxiter, self.rtol, self.err_on_non_converge, self.assemble_jac]
        )
        right_box = widgets.VBox([self.atol, self.iprint])
        self.vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        self.rtol.add_class("top")
        self.err_on_non_converge.add_class("top")
        self.assemble_jac.add_class("top")

        # Right Widgets
        self.iprint.add_class("top")

        # VBox & Button Widgets
        self.vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(self.vbox)

    def onchange(change):
        clear_output(wait=True)
        display(select)
        if change["new"] == "direct":
            clear_output(wait=True)
            display(select)
            direct_change()
        elif change["new"] == "linear_block_gs":
            clear_output(wait=True)
            display(select)
            linear_block_gs_change()
        elif change["new"] == "linear_block_jac":
            clear_output(wait=True)
            display(select)
            linear_block_jac_change()
        elif change["new"] == "linear_runonce":
            clear_output(wait=True)
            display(select)
            linear_runonce_change()
        elif change["new"] == "petsc_ksp":
            clear_output(wait=True)
            display(select)
            petsc_ksp_change()
        elif change["new"] == "scipy_iter_solver":
            clear_output(wait=True)
            display(select)
            scipy_iter_solver_change()
        elif change["new"] == "user_defined":
            clear_output(wait=True)
            display(select)
            user_defined_change()

    style = {"description_width": "initial"}

    self.select = widgets.Dropdown(
        options=[
            "direct",
            "linear_block_gs",
            "linear_block_jac",
            "linear_runonce",
            "petsc_ksp",
            "scipy_iter_solver",
            "user_defined",
        ],
        value="direct",
        style=style,
        description="Linear solvers :",
    )

    self.select.observe(onchange, names="value")
    display(self.select)
    direct_change()
