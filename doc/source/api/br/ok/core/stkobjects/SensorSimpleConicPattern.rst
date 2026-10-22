SensorSimpleConicPattern
========================

.. py:class:: br.ok.core.stkobjects.SensorSimpleConicPattern

   Bases: :py:class:`~br.ok.core.stkobjects.ISensorPattern`

   Class defining the simple conic pattern for a Sensor.

.. py:currentmodule:: SensorSimpleConicPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SensorSimpleConicPattern.angular_resolution`
              - Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...
            * - :py:attr:`~br.ok.core.stkobjects.SensorSimpleConicPattern.cone_angle`
              - Simple cone angle defining the sensor pattern. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import SensorSimpleConicPattern


Property detail
---------------

.. py:property:: angular_resolution
    :canonical: br.ok.core.stkobjects.SensorSimpleConicPattern.angular_resolution
    :type: typing.Any

    Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...

.. py:property:: cone_angle
    :canonical: br.ok.core.stkobjects.SensorSimpleConicPattern.cone_angle
    :type: typing.Any

    Simple cone angle defining the sensor pattern. Uses Angle Dimension.


