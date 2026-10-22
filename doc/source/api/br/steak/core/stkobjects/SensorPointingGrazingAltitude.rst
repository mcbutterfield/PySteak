SensorPointingGrazingAltitude
=============================

.. py:class:: br.steak.core.stkobjects.SensorPointingGrazingAltitude

   Bases: :py:class:`~br.steak.core.stkobjects.ISensorPointing`

   Class defining Grazing Altitude pointing type for a Sensor.

.. py:currentmodule:: SensorPointingGrazingAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SensorPointingGrazingAltitude.azimuth_offset`
              - The azimuth offset, defining the plane in the parent object's body-fixed frame in which the sensor boresight lies. It is the angle between the X axis and the azimuth vector in the XY plane. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.SensorPointingGrazingAltitude.grazing_altitude`
              - The altitude at which the boresight vector grazes the central body. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import SensorPointingGrazingAltitude


Property detail
---------------

.. py:property:: azimuth_offset
    :canonical: br.steak.core.stkobjects.SensorPointingGrazingAltitude.azimuth_offset
    :type: typing.Any

    The azimuth offset, defining the plane in the parent object's body-fixed frame in which the sensor boresight lies. It is the angle between the X axis and the azimuth vector in the XY plane. Uses Angle Dimension.

.. py:property:: grazing_altitude
    :canonical: br.steak.core.stkobjects.SensorPointingGrazingAltitude.grazing_altitude
    :type: float

    The altitude at which the boresight vector grazes the central body. Uses Distance Dimension.


