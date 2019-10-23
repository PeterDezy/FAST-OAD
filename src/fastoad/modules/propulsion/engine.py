"""
Base module for engine models
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

from abc import ABC, abstractmethod
from typing import Union, Sequence, Optional, Tuple, TypeVar

import numpy as np
import openmdao.api as om

from fastoad.constants import FlightPhase

IEngineSubclass = TypeVar('IEngineSubclass', bound='IEngine')


class IEngine(ABC):
    """
    Interface for Engine models
    """

    # pylint: disable=too-few-public-methods  # that is the needed interface

    # pylint: disable=too-many-arguments  # they define the trajectory
    @abstractmethod
    def compute_flight_points(self,
                              mach: Union[float, Sequence],
                              altitude: Union[float, Sequence],
                              phase: Union[FlightPhase, Sequence],
                              use_thrust_rate: Optional[Union[bool, Sequence]] = None,
                              thrust_rate: Optional[Union[float, Sequence]] = None,
                              thrust: Optional[Union[float, Sequence]] = None) \
            -> Tuple[Union[float, Sequence],
                     Union[float, Sequence],
                     Union[float, Sequence]]:
        """
        Computes Specific Fuel Consumption according to provided conditions.

        Each input can be a float, a list or an array.
        Inputs that are not floats must all have the same shape (numpy speaking).

        About use_thrust_rate, thrust_rate and thrust
        ---------------------------------------------

            *use_thrust_rate* tells if a flight point should be computed using *thrust_rate*
            or *thrust* as input.

            - if *use_thrust_rate* is None, the considered input will be the provided one
            between *thrust_rate* and *thrust* (if both are provided, *thrust_rate* will be used)

            - if *use_thrust_rate* is True or False (i.e., not a sequence), the considered input
            will be taken accordingly, and should of course not be None.

            - if *use_thrust_rate* is a sequence or array, *thrust_rate* and *thrust* should be
            provided and have the same shape as *use_thrust_rate*. The method will consider for
            each element which input will be used according to *use_thrust_rate*


        :param mach: Mach number
        :param altitude: (unit=m) altitude w.r.t. to sea level
        :param phase: flight phase
        :param use_thrust_rate: tells if thrust_rate or thrust should be used (works element-wise)
        :param thrust_rate: thrust rate (unit=none)
        :param thrust: required thrust (unit=N)
        :return: SFC (in kg/s/N), thrust rate, thrust (in N)
        """


class OMIEngine(om.ExplicitComponent, ABC):
    """
    Base class for OpenMDAO wrapping of subclasses of :class`IEngine`.

    Classes that implements this interface should add their own inputs in setup()
    and implement :meth:`get_engine`.
    """

    def initialize(self):
        self.options.declare('flight_point_count', 1, types=(int, tuple))

    def setup(self):
        shape = self.options['flight_point_count']
        self.add_input('mach', np.nan, shape=shape)
        self.add_input('altitude', np.nan, shape=shape, units='m')
        self.add_input('phase', np.nan, shape=shape)
        self.add_input('use_thrust_rate', np.nan, shape=shape)
        self.add_input('required_thrust_rate', np.nan, shape=shape)
        self.add_input('required_thrust', np.nan, shape=shape, units='N')

        self.add_output('SFC', shape=shape, units='kg/s/N')
        self.add_output('thrust_rate', shape=shape, units='kg/s/N')
        self.add_output('thrust', shape=shape, units='kg/s/N')
        self.declare_partials('SFC', '*', method='fd')
        self.declare_partials('thrust_rate', '*', method='fd')
        self.declare_partials('thrust', '*', method='fd')

    def compute(self, inputs, outputs, discrete_inputs=None, discrete_outputs=None):
        engine = self.get_engine(inputs)
        sfc, thrust_rate, thrust = engine.compute_flight_points(inputs['mach'], inputs['altitude'],
                                                                inputs['phase'],
                                                                inputs['use_thrust_rate'],
                                                                inputs['required_thrust_rate'],
                                                                inputs['required_thrust'])
        outputs['SFC'] = sfc
        outputs['thrust_rate'] = thrust_rate
        outputs['thrust'] = thrust

    @staticmethod
    @abstractmethod
    def get_engine(inputs) -> IEngineSubclass:
        """

        :param inputs: input parameters that define the engine
        :return: a :class`IEngineSubclass` instance
        """