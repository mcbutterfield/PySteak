SensorHalfPowerPattern
======================

.. py:class:: br.steak.core.stkobjects.SensorHalfPowerPattern

   Bases: :py:class:`~br.steak.core.stkobjects.ISensorPattern`

   Class defining the half-power pattern for a Sensor.

.. py:currentmodule:: SensorHalfPowerPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SensorHalfPowerPattern.angular_resolution`
              - Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...
            * - :py:attr:`~br.steak.core.stkobjects.SensorHalfPowerPattern.antenna_diameter`
              - The diameter of the antenna dish. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.SensorHalfPowerPattern.frequency`
              - The antenna's frequency in GHz. Uses Frequency Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.SensorHalfPowerPattern.half_angle`
              - Get the half angle of the cone for, calculated on the basis of the Frequency and AntennaDiameter properties. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import SensorHalfPowerPattern


Property detail
---------------

.. py:property:: angular_resolution
    :canonical: br.steak.core.stkobjects.SensorHalfPowerPattern.angular_resolution
    :type: typing.Any

    Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...

.. py:property:: antenna_diameter
    :canonical: br.steak.core.stkobjects.SensorHalfPowerPattern.antenna_diameter
    :type: float

    The diameter of the antenna dish. Uses SmallDistanceUnit Dimension.

.. py:property:: frequency
    :canonical: br.steak.core.stkobjects.SensorHalfPowerPattern.frequency
    :type: float

    The antenna's frequency in GHz. Uses Frequency Dimension.

.. py:property:: half_angle
    :canonical: br.steak.core.stkobjects.SensorHalfPowerPattern.half_angle
    :type: typing.Any

    Get the half angle of the cone for, calculated on the basis of the Frequency and AntennaDiameter properties. Uses Angle Dimension.


