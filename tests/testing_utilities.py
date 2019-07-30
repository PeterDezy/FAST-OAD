"""
Convenience functions for helping tests
"""
#  This file is part of FAST : A framework for rapid Overall Aircraft Design
#  Copyright (C) 2019  ONERA/ISAE
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

import logging
from typing import TypeVar

from openmdao.core.indepvarcomp import IndepVarComp
from openmdao.core.problem import Problem
from openmdao.core.system import System

from fastoad.openmdao.checks import get_unconnected_inputs

SystemSubclass = TypeVar('SystemSubclass', bound=System)

# Logger for this module
_LOGGER = logging.getLogger(__name__)


def run_system(component: SystemSubclass, input_vars: IndepVarComp, setup_mode='auto'):
    """ Runs and returns an OpenMDAO problem with provided component and data"""
    problem = Problem()
    model = problem.model
    model.add_subsystem('inputs', input_vars, promotes=['*'])
    model.add_subsystem('component', component, promotes=['*'])

    problem.setup(mode=setup_mode)
    missing, _ = get_unconnected_inputs(problem, _LOGGER)
    assert not missing

    problem.run_model()

    return problem