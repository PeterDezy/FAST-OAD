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


def linearsolvers():

    """
    A class to change the linear solver in the configuration file
    """


    def direct_change():

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

        iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        err_on_singular = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_singular"].get("value"),
            description="Raise an error if LU decomposition is singular",
            style=style,
            disabled=False,
        )

        left_box = widgets.VBox([iprint])
        right_box = widgets.VBox([assemble_jac, err_on_singular])
        vbox = widgets.HBox([left_box, right_box])

        # Left Widgets

        # Right Widgets
        err_on_singular.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(vbox)

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

        maxiter = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            description="Maxiter :",
            style=style,
            disabled=False,
        )

        atol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            description="Absolute Error Tolerance :",
            style=style,
            disabled=False,
        )

        rtol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            description="Relative Error Tolerance :",
            style=style,
            disabled=False,
        )

        iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        err_on_non_converge = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            description="When True, AnalysisError will be raised if we don't converge",
            style=style,
            disabled=False,
        )

        assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        use_aitken = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["use_aitken"].get("value"),
            description="Use Aitken relaxation",
            disabled=False,
        )

        aitken_min_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_min_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken min factor :",
            style=style,
            disabled=False,
        )

        aitken_max_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_max_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken max factor :",
            style=style,
            disabled=False,
        )

        aitken_initial_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_initial_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken initial factor :",
            style=style,
            disabled=False,
        )

        vb = widgets.VBox(children=[])

        def change_use_aitken(b):

            if b["new"]:
                vb.children = [
                    aitken_min_factor,
                    aitken_max_factor,
                    aitken_initial_factor,
                ]
            else:
                vb.children = []

        use_aitken.observe(change_use_aitken, names="value")

        left_box = widgets.VBox(
            [maxiter, rtol, err_on_non_converge, assemble_jac]
        )
        right_box = widgets.VBox([atol, iprint, use_aitken, vb])
        vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        rtol.add_class("top")
        err_on_non_converge.add_class("top")
        assemble_jac.add_class("top")

        # Right Widgets
        iprint.add_class("top")
        use_aitken.add_class("top")
        vb.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")

        display(vbox)

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

        maxiter = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            description="Maxiter :",
            style=style,
            disabled=False,
        )

        atol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            description="Absolute Error Tolerance :",
            style=style,
            disabled=False,
        )

        rtol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            description="Relative Error Tolerance :",
            style=style,
            disabled=False,
        )

        iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        err_on_non_converge = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            description="When True, AnalysisError will be raised if we don't converge",
            style=style,
            disabled=False,
        )

        assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        left_box = widgets.VBox([maxiter, rtol, err_on_non_converge])
        right_box = widgets.VBox([atol, iprint, assemble_jac])
        vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        rtol.add_class("top")
        err_on_non_converge.add_class("top")

        # Right Widgets
        iprint.add_class("top")
        assemble_jac.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(vbox)

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

        iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        use_aitken = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["use_aitken"].get("value"),
            description="Use Aitken relaxation",
            disabled=False,
        )

        aitken_min_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_min_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken min factor :",
            style=style,
            disabled=False,
        )

        aitken_max_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_max_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken max factor :",
            style=style,
            disabled=False,
        )

        aitken_initial_factor = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["aitken_initial_factor"].get("value"),
            min=0,
            max=100,
            description="Aitken initial factor :",
            style=style,
            disabled=False,
        )

        vb = widgets.VBox(children=[])

        def change_use_aitken(b):

            if b["new"]:
                vb.children = [
                    aitken_min_factor,
                    aitken_max_factor,
                    aitken_initial_factor,
                ]
            else:
                vb.children = []

        use_aitken.observe(change_use_aitken, names="value")

        left_box = widgets.VBox([iprint, assemble_jac])
        right_box = widgets.VBox([use_aitken, vb])
        vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        assemble_jac.add_class("top")

        # Right Widgets
        vb.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(vbox)

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

        maxiter = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            description="Maxiter :",
            style=style,
            disabled=False,
        )

        atol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            description="Absolute Error Tolerance :",
            style=style,
            disabled=False,
        )

        rtol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            description="Relative Error Tolerance :",
            style=style,
            disabled=False,
        )

        iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        err_on_non_converge = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            description="When True, AnalysisError will be raised if we don't converge",
            style=style,
            disabled=False,
        )

        assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        restart = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["restart"].get("value"),
            min=0,
            max=1000,
            description="Restart :",
            style=style,
            disabled=False,
        )

        left_box = widgets.VBox(
            [maxiter, rtol, err_on_non_converge, assemble_jac]
        )
        right_box = widgets.VBox([atol, iprint, restart])
        vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        rtol.add_class("top")
        err_on_non_converge.add_class("top")
        assemble_jac.add_class("top")

        # Right Widgets
        iprint.add_class("top")
        restart.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(vbox)

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

        maxiter = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["maxiter"].get("value"),
            min=1,
            max=10000,
            description="Maxiter :",
            style=style,
            disabled=False,
        )

        atol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["atol"].get("value"),
            min=1e-20,
            max=1,
            description="Absolute Error Tolerance :",
            style=style,
            disabled=False,
        )

        rtol = widgets.BoundedFloatText(
            value=solver.options.__dict__["_dict"]["rtol"].get("value"),
            min=10e-12,
            max=1,
            description="Relative Error Tolerance :",
            style=style,
            disabled=False,
        )

        iprint = widgets.BoundedIntText(
            value=solver.options.__dict__["_dict"]["iprint"].get("value"),
            min=0,
            max=1,
            description="Print the output :",
            style=style,
            disabled=False,
        )

        err_on_non_converge = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["err_on_non_converge"].get("value"),
            description="When True, AnalysisError will be raised if we don't converge",
            style=style,
            disabled=False,
        )

        assemble_jac = widgets.Checkbox(
            value=solver.options.__dict__["_dict"]["assemble_jac"].get("value"),
            description="Activates use of assembled jacobian by this solver",
            style=style,
            disabled=False,
        )

        left_box = widgets.VBox(
            [maxiter, rtol, err_on_non_converge, assemble_jac]
        )
        right_box = widgets.VBox([atol, iprint])
        vbox = widgets.HBox([left_box, right_box])

        # Left Widgets
        rtol.add_class("top")
        err_on_non_converge.add_class("top")
        assemble_jac.add_class("top")

        # Right Widgets
        iprint.add_class("top")

        # VBox & Button Widgets
        vbox.add_class("top")
        left_box.add_class("left")
        left_box.add_class("right")

        display(vbox)

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

    select = widgets.Dropdown(
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

    select.observe(onchange, names="value")
    display(select)
    direct_change()
