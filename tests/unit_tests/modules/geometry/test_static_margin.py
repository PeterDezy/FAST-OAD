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

import os.path as pth

import pytest

from fastoad.io.xml import OMXmlIO
from fastoad.modules.geometry.compute_static_margin import ComputeStaticMargin
from tests.testing_utilities import run_system

DATA_FOLDER_PATH = pth.join(pth.dirname(__file__), 'data')
RESULTS_FOLDER_PATH = pth.join(pth.dirname(__file__),
                               'results', pth.splitext(pth.basename(__file__))[0])


@pytest.fixture(scope="module")
def input_xml() -> OMXmlIO:
    """
    :return: access to the sample xml data
    """
    # TODO: have more consistency in input data (no need for the whole geometry_inputs_full.xml)
    return OMXmlIO(pth.join(pth.dirname(__file__), "data", "geometry_inputs_full.xml"))


def test_compute_static_margin(input_xml):
    """ Tests computation of static margin """

    input_list = [
        'data:geometry:wing:MAC:length',
        'data:geometry:wing:MAC:x'
    ]

    input_vars = input_xml.read(only=input_list)

    input_vars.add_output('data:weight:aircraft:CG:ratio', 0.388971)
    input_vars.add_output('data:aerodynamics:cruise:neutral_point:x', 0.537521)

    problem = run_system(ComputeStaticMargin(), input_vars)

    static_margin = problem['data:handling_qualities:static_margin']
    assert static_margin == pytest.approx(0.098550, abs=1e-6)
    cg_global = problem['data:weight:aircraft:CG:x']
    assert cg_global == pytest.approx(17.3, abs=1e-1)