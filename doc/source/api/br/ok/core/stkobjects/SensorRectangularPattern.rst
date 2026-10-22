SensorRectangularPattern
========================

.. py:class:: br.ok.core.stkobjects.SensorRectangularPattern

   Bases: :py:class:`~br.ok.core.stkobjects.ISensorPattern`

   Class defining the rectangular pattern for a Sensor.

.. py:currentmodule:: SensorRectangularPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SensorRectangularPattern.angular_resolution`
              - Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...
            * - :py:attr:`~br.ok.core.stkobjects.SensorRectangularPattern.horizontal_half_angle`
              - The angle from the boresight (Z) direction to the edge of the sensor in the XZ plane of the sensor's coordinate system. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.SensorRectangularPattern.vertical_half_angle`
              - The angle from the boresight (Z) direction to the edge of the sensor in the YZ plane of the sensor's coordinate system. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import SensorRectangularPattern


Property detail
---------------

.. py:property:: angular_resolution
    :canonical: br.ok.core.stkobjects.SensorRectangularPattern.angular_resolution
    :type: typing.Any

    Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...

.. py:property:: horizontal_half_angle
    :canonical: br.ok.core.stkobjects.SensorRectangularPattern.horizontal_half_angle
    :type: typing.Any

    The angle from the boresight (Z) direction to the edge of the sensor in the XZ plane of the sensor's coordinate system. Uses Angle Dimension.

.. py:property:: vertical_half_angle
    :canonical: br.ok.core.stkobjects.SensorRectangularPattern.vertical_half_angle
    :type: typing.Any

    The angle from the boresight (Z) direction to the edge of the sensor in the YZ plane of the sensor's coordinate system. Uses Angle Dimension.


