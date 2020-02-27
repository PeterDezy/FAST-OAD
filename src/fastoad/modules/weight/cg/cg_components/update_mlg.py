"""
    Estimation of main landing gear center of gravity
"""

#  This file is part of FAST : A framework for rapid Overall Aircraft Design
#  Copyright (C) 2020  ONERA/ISAE
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

import numpy as np
import openmdao.api as om


class UpdateMLG(om.Group):
    """ Main landing gear center of gravity estimation """

    def setup(self):
        # This local group ensures quick resolution of the implicit component
        self.add_subsystem('mlg', _UpdateMLG(), promotes=['*'])

        self.nonlinear_solver = om.NewtonSolver()
        self.linear_solver = om.DirectSolver()


class _UpdateMLG(om.ImplicitComponent):
    # TODO: Document equations. Cite sources
    """ Main landing gear center of gravity estimation """

    def setup(self):
        self.add_input('data:geometry:wing:MAC:length', val=np.nan, units='m')
        self.add_input('data:geometry:wing:MAC:x', val=np.nan, units='m')
        self.add_input('data:weight:aircraft:CG:ratio', val=np.nan)
        self.add_input('data:weight:airframe:landing_gear:front:CG:x', units='m')

        self.add_output('data:weight:airframe:landing_gear:main:CG:x', units='m')

        self.declare_partials('data:weight:airframe:landing_gear:main:CG:x', '*', method='fd')

    def apply_nonlinear(self, inputs, outputs, residuals, discrete_inputs=None,
                        discrete_outputs=None):
        l0_wing = inputs['data:geometry:wing:MAC:length']
        fa_length = inputs['data:geometry:wing:MAC:x']
        cg_ratio = inputs['data:weight:aircraft:CG:ratio']
        cg_a51 = outputs['data:weight:airframe:landing_gear:main:CG:x']
        cg_a52 = inputs['data:weight:airframe:landing_gear:front:CG:x']
        delta_lg = cg_a51 - cg_a52

        x_cg = fa_length - 0.25 * l0_wing + cg_ratio * l0_wing

        new_cg_a51 = x_cg + 0.08 * delta_lg

        residuals['data:weight:airframe:landing_gear:main:CG:x'] = cg_a51 - new_cg_a51

    def guess_nonlinear(self, inputs, outputs, residuals,
                        discrete_inputs=None, discrete_outputs=None):
        outputs['data:weight:airframe:landing_gear:main:CG:x'] = inputs['data:geometry:wing:MAC:x']