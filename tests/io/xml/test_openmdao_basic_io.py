"""
Tests basic XML serializer for OpenMDAO variables
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
import os.path as pth
import shutil
from typing import List

import numpy as np
from lxml import etree
from openmdao.core.indepvarcomp import IndepVarComp
from openmdao.core.problem import Problem
from openmdao.drivers.scipy_optimizer import ScipyOptimizeDriver
from pytest import approx

from fastoad.io.xml import OpenMdaoXmlIO
from fastoad.io.xml import XPathReader
from tests.sellar_example.sellar import Sellar
from tests.io.xml.data.mass_breakdown.mass_breakdown import MassBreakdown

from fastoad.openmdao.types import Variable


def _check_basic_ivc(ivc: IndepVarComp):
    """ Checks that provided IndepVarComp instance matches content of data/basic.xml file """

    outputs: List[Variable] = []
    for (name, value, attributes) in ivc._indep_external:  # pylint: disable=protected-access
        outputs.append(Variable(name, value, attributes['units']))

    assert len(outputs) == 9

    # Using pytest.approx for numerical reason, but also because it works even if sequence types
    # are different (lists, tuples, numpy arrays)
    assert outputs[0].name == 'geometry/total_surface'
    assert outputs[0].value == approx([780.3])
    assert outputs[0].units == 'm**2'

    assert outputs[1].name == 'geometry/wing/span'
    assert outputs[1].value == approx([42])
    assert outputs[1].units == 'm'

    assert outputs[2].name == 'geometry/wing/aspect_ratio'
    assert outputs[2].value == approx([9.8])
    assert outputs[2].units is None

    assert outputs[3].name == 'geometry/fuselage/length'
    assert outputs[3].value == approx([40.])
    assert outputs[3].units == 'm'

    assert outputs[4].name == 'constants/k1'
    assert outputs[4].value == approx([1., 2., 3.])
    assert outputs[4].units == 'kg'

    assert outputs[5].name == 'constants/k2'
    assert outputs[5].value == approx([10., 20.])
    assert outputs[5].units is None

    assert outputs[6].name == 'constants/k3'
    assert outputs[6].value == approx([100., 200., 300., 400.])
    assert outputs[6].units == 'm/s'

    assert outputs[7].name == 'constants/k4'
    assert outputs[7].value == approx([-1, -2, -3])
    assert outputs[7].units is None

    assert outputs[8].name == 'constants/k5'
    assert outputs[8].value == approx([100, 200, 400, 500, 600])
    assert outputs[8].units is None

def _compare_xml(xml_1, xml_2):
    """ Checks that both xml files are the same """
    xml_1_read = OpenMdaoXmlIO(xml_1)
    ivc_1 = xml_1_read.read()
    xml_2_read = OpenMdaoXmlIO(xml_2)
    ivc_2 = xml_2_read.read()
    are_same = _compare_ivc(ivc_1, ivc_2)
    return are_same
    
def _compare_ivc(ivc_1, ivc_2):
    """ Checks that both ivc are the same """
    are_same = True

    outputs_1 = {}
    for (name, value, attributes) in ivc_1._indep_external:
        outputs_1[name] = Variable(name, value, attributes['units'])
    outputs_2 = {}
    for (name, value, attributes) in ivc_2._indep_external:
        outputs_2[name] = Variable(name, value, attributes['units'])
    # Check
    for i, (key, value) in enumerate(outputs_1.items()):
        if are_same:
            if key in outputs_2.keys():
                var_1 = outputs_1[key]
                var_2 = outputs_2[key]
                are_same = (var_1.name == var_2.name) and \
                    (str(var_1.value) == str(var_2.value)) and \
                        (var_1.units == var_2.units)
            else:
                are_same = False

    return are_same

def test_basic_xml_read_and_write_from_indepvarcomp():
    """
    Tests the creation of an XML file from an IndepVarComp instance
    """
    data_folder = pth.join(pth.dirname(__file__), 'data')
    result_folder = pth.join(pth.dirname(__file__), 'results', 'basic_xml')
    if pth.exists(result_folder):
        shutil.rmtree(result_folder)

    # Check write hand-made component
    ivc = IndepVarComp()
    ivc.add_output('geometry/total_surface', val=[780.3], units='m**2')
    ivc.add_output('geometry/wing/span', val=42.0, units='m')
    ivc.add_output('geometry/wing/aspect_ratio', val=[9.8])
    ivc.add_output('geometry/fuselage/length', val=40.0, units='m')
    ivc.add_output('constants/k1', val=[1.0, 2.0, 3.0], units='kg')
    ivc.add_output('constants/k2', val=[10.0, 20.0])
    ivc.add_output('constants/k3', val=np.array([100.0, 200.0, 300.0, 400.0]), units='m/s')
    ivc.add_output('constants/k4', val=[-1.0, -2.0, -3.0])
    ivc.add_output('constants/k5', val=[100.0, 200.0, 400.0, 500.0, 600.0])
    # Try writing with non-existing folder
    if pth.exists(result_folder):
        shutil.rmtree(result_folder)
    filename = pth.join(result_folder, 'handmade.xml')
    xml_write = OpenMdaoXmlIO(filename)
    xml_write.write(ivc)

    # check (read another IndepVarComp instance from  xml)
    xml_check = OpenMdaoXmlIO(filename)
    new_ivc = xml_check.read()
    _check_basic_ivc(new_ivc)

    # Check reading hand-made XML (with some format twists)
    filename = pth.join(data_folder, 'basic.xml')
    xml_read = OpenMdaoXmlIO(filename)
    ivc = xml_read.read()
    _check_basic_ivc(ivc)

    # write it (with existing destination folder)
    new_filename = pth.join(result_folder, 'basic.xml')
    xml_write = OpenMdaoXmlIO(new_filename)
    xml_write.write(ivc)

    # check (read another IndepVarComp instance from new xml)
    xml_check = OpenMdaoXmlIO(new_filename)
    new_ivc = xml_check.read()
    _check_basic_ivc(new_ivc)


def test_basic_xml_partial_read_and_write_from_indepvarcomp():
    data_folder = pth.join(pth.dirname(__file__), 'data')
    result_folder = pth.join(pth.dirname(__file__), 'results', 'basic_partial_xml')
    if pth.exists(result_folder):
        shutil.rmtree(result_folder)

    # Read full IndepVarComp
    filename = pth.join(data_folder, 'basic.xml')
    xml_read = OpenMdaoXmlIO(filename)
    ivc = xml_read.read(ignore=['does_not_exist'])
    _check_basic_ivc(ivc)

    # Add something to ignore and write it
    ivc.add_output('should_be_ignored/pointless', val=0.0)
    ivc.add_output('should_also_be_ignored', val=-10.0)

    badvar_filename = pth.join(result_folder, 'with_bad_var.xml')
    xml_write = OpenMdaoXmlIO(badvar_filename)
    xml_write.write(ivc, ignore=['does_not_exist'])  # Check with non-existent var in ignore list

    reader = XPathReader(badvar_filename)
    assert reader.get_float('should_be_ignored/pointless') == 0.0
    assert reader.get_float('should_also_be_ignored') == -10.0

    # Check partial reading with 'ignore'
    xml_read = OpenMdaoXmlIO(badvar_filename)
    new_ivc = xml_read.read(ignore=['should_be_ignored/pointless', 'should_also_be_ignored'])
    _check_basic_ivc(new_ivc)

    # Check partial reading with 'only'
    ok_vars = ['geometry/total_surface',
               'geometry/wing/span',
               'geometry/wing/aspect_ratio',
               'geometry/fuselage/length',
               'constants/k1',
               'constants/k2',
               'constants/k3',
               'constants/k4',
               'constants/k5'
               ]
    new_ivc2 = xml_read.read(only=ok_vars)
    _check_basic_ivc(new_ivc2)

    # Check partial writing with 'ignore'
    varok_filename = pth.join(result_folder, 'with_bad_var.xml')
    xml_write = OpenMdaoXmlIO(varok_filename)
    xml_write.write(ivc, ignore=['should_be_ignored/pointless', 'should_also_be_ignored'])

    xml_read = OpenMdaoXmlIO(varok_filename)
    new_ivc = xml_read.read()
    _check_basic_ivc(new_ivc)

    # Check partial writing with 'only'
    varok2_filename = pth.join(result_folder, 'with_bad_var.xml')
    xml_write = OpenMdaoXmlIO(varok2_filename)
    xml_write.write(ivc, only=ok_vars)

    xml_read = OpenMdaoXmlIO(varok2_filename)
    new_ivc = xml_read.read()
    _check_basic_ivc(new_ivc)


def test_basic_xml_write_from_problem():
    """
    Tests the creation of an XML file from OpenMDAO components
    """
    result_folder = pth.join(pth.dirname(__file__), 'results', 'sellar')
    if pth.exists(result_folder):
        shutil.rmtree(result_folder)

    # Create and run the problem
    problem = Problem()
    problem.model = Sellar()

    problem.driver = ScipyOptimizeDriver()

    problem.driver.options['optimizer'] = 'SLSQP'
    #
    problem.model.approx_totals()
    problem.model.add_design_var('x', lower=0, upper=10)
    problem.model.add_design_var('z', lower=0, upper=10)

    problem.model.add_objective('f')

    problem.model.add_constraint('g1', upper=0.)
    problem.model.add_constraint('g2', upper=0.)

    problem.setup()
    problem.run_driver()

    # Write the XML file
    filename = pth.join(result_folder, 'sellar.xml')
    xml_write = OpenMdaoXmlIO(filename)
    xml_write.use_promoted_names = False
    xml_write.path_separator = '.'
    xml_write.write(problem.model)

    # Check
    tree = etree.parse(filename)
    assert len(tree.xpath('/aircraft/indeps/x')) == 1
    assert len(tree.xpath('/aircraft/indeps/z')) == 2
    assert len(tree.xpath('/aircraft/Disc1/y1')) == 1
    assert len(tree.xpath('/aircraft/Disc2/y2')) == 1
    assert len(tree.xpath('/aircraft/Functions/f')) == 1
    assert len(tree.xpath('/aircraft/Functions/g1')) == 1
    assert len(tree.xpath('/aircraft/Functions/g2')) == 1

    # Write the XML file using promoted names
    filename = pth.join(result_folder, 'sellar.xml')
    xml_write = OpenMdaoXmlIO(filename)
    xml_write.use_promoted_names = True
    xml_write.path_separator = '.'
    xml_write.write(problem.model)

    # Check
    tree = etree.parse(filename)
    assert len(tree.xpath('/aircraft/x')) == 1
    assert len(tree.xpath('/aircraft/z')) == 2
    assert len(tree.xpath('/aircraft/y1')) == 1
    assert len(tree.xpath('/aircraft/y2')) == 1
    assert len(tree.xpath('/aircraft/f')) == 1
    assert len(tree.xpath('/aircraft/g1')) == 1
    assert len(tree.xpath('/aircraft/g2')) == 1

def test_write_xml_from_indepvarcomp_system_inputs():
    data_folder = pth.join(pth.dirname(__file__), 'data')
    result_folder = pth.join(pth.dirname(__file__), 'results', 'xml_system_inputs')
    if pth.exists(result_folder):
        shutil.rmtree(result_folder)

    # Read full IndepVarComp
    filename = pth.join(result_folder, 'xml_system_inputs.xml')
    xml_read = OpenMdaoXmlIO(filename)
    xml_read.path_separator = ':'

    system = MassBreakdown()

    problem = Problem()
    problem.model = system
    problem.setup()

    xml_read.write_inputs(problem, optional_inputs=True)
    ref_file = pth.join(data_folder, 'xml_mass_breakdown_inputs_ref.xml')

    assert _compare_xml(filename, ref_file)

    filename = pth.join(result_folder, 'xml_system_inputs_no_opt.xml')
    xml_read = OpenMdaoXmlIO(filename)
    xml_read.path_separator = ':'

    xml_read.write_inputs(problem, optional_inputs=False)
    ref_file = pth.join(data_folder, 'xml_mass_breakdown_inputs_no_opt_ref.xml')

    assert _compare_xml(filename, ref_file)