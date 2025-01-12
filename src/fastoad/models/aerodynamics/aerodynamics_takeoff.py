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

import openmdao.api as om

from fastoad.module_management.constants import ModelDomain
from fastoad.module_management.service_registry import RegisterOpenMDAOSystem
from .components.compute_polar import ComputePolar, PolarType
from .components.high_lift_aero import ComputeDeltaHighLift


@RegisterOpenMDAOSystem("fastoad.aerodynamics.takeoff.legacy", domain=ModelDomain.AERODYNAMICS)
class AerodynamicsTakeoff(om.Group):
    """
    Computes aerodynamic characteristics at takeoff.

    - Computes CL and CD increments due to high-lift devices at takeoff.
    """

    def setup(self):
        self.add_subsystem("delta_cl_cd", ComputeDeltaHighLift(landing_flag=False), promotes=["*"])
        self.add_subsystem("polar", ComputePolar(type=PolarType.TAKEOFF), promotes=["*"])
