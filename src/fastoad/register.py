"""
This module is for registering all internal OpenMDAO modules that we want
available through OpenMDAOSystemRegistry
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

from fastoad.module_management import OpenMDAOSystemRegistry
from fastoad.module_management.constants import ModelDomain
from fastoad.modules.aerodynamics.aerodynamics_high_speed import AerodynamicsHighSpeed
from fastoad.modules.aerodynamics.aerodynamics_landing import AerodynamicsLanding
from fastoad.modules.geometry import Geometry
from fastoad.modules.handling_qualities.tail_sizing.compute_tail_areas import ComputeTailAreas
from fastoad.modules.loops.compute_wing_area import ComputeWingArea
from fastoad.modules.performances import BreguetFromOWE
from fastoad.modules.propulsion.fuel_engine.rubber_engine import OMRubberEngine
from fastoad.modules.weight.weight import Weight


def register_openmdao_systems():
    """
    The place where to register FAST-OAD internal models.

    Warning: this function is effective only if called from a Python module that
    is a started bundle for iPOPO
    """
    # Aerodynamics ################################################################
    OpenMDAOSystemRegistry.register_system(AerodynamicsLanding,
                                           'fastoad.aerodynamics.landing.legacy',
                                           domain=ModelDomain.AERODYNAMICS)
    OpenMDAOSystemRegistry.register_system(AerodynamicsHighSpeed,
                                           'fastoad.aerodynamics.highspeed.legacy',
                                           domain=ModelDomain.AERODYNAMICS)

    # Geometry ####################################################################
    OpenMDAOSystemRegistry.register_system(Geometry,
                                           'fastoad.geometry.legacy',
                                           domain=ModelDomain.GEOMETRY
                                           )

    # handling qualities ##########################################################
    OpenMDAOSystemRegistry.register_system(ComputeTailAreas,
                                           'fastoad.handling_qualities.legacy',
                                           domain=ModelDomain.HANDLING_QUALITIES
                                           )

    # Loops #######################################################################
    OpenMDAOSystemRegistry.register_system(ComputeWingArea,
                                           'fastoad.loop.wing_area',
                                           domain=ModelDomain.OTHER
                                           )

    # Weight ######################################################################
    OpenMDAOSystemRegistry.register_system(Weight,
                                           'fastoad.weight.legacy',
                                           domain=ModelDomain.WEIGHT
                                           )
    # Performance #################################################################
    OpenMDAOSystemRegistry.register_system(BreguetFromOWE,
                                           'fastoad.performances.breguet',
                                           domain=ModelDomain.PERFORMANCE
                                           )

    # Propulsion ##################################################################
    rubber_engine_description = """
    Parametric engine model as OpenMDAO component.
    
    Implementation of E. Roux models for fuel consumption of low bypass ratio engines
    For more information, see RubberEngine class in FAST-OAD developer documentation.
    """

    OpenMDAOSystemRegistry.register_system(OMRubberEngine,
                                           'fastoad.propulsion.rubber_engine',
                                           domain=ModelDomain.PROPULSION,
                                           desc=rubber_engine_description
                                           )