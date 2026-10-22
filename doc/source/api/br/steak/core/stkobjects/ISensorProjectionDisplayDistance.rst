ISensorProjectionDisplayDistance
================================

.. py:class:: br.steak.core.stkobjects.ISensorProjectionDisplayDistance

   ISensorProjectionDisplayDistance Interface for setting projection altitude options for a sensor.

.. py:currentmodule:: ISensorProjectionDisplayDistance

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ISensorProjectionDisplayDistance.altitude_crossing_sides`
              - Indicate which crossings are computed and displayed in the 2D Graphics window.
            * - :py:attr:`~br.steak.core.stkobjects.ISensorProjectionDisplayDistance.direction`
              - Indicate the direction in which the sensor's field of view crosses the specified altitude.
            * - :py:attr:`~br.steak.core.stkobjects.ISensorProjectionDisplayDistance.maximum`
              - Maximum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.ISensorProjectionDisplayDistance.minimum`
              - Minimum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.ISensorProjectionDisplayDistance.number_of_steps`
              - Step count. Determines the interval between sensor projections. For a specified min/max altitude: the step count determines the number and altitude of projections to be displayed. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.ISensorProjectionDisplayDistance.projects_thru_crossing`
              - Specify whether the sensor's field-of-view will extend beyond specified crossings.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ISensorProjectionDisplayDistance


Property detail
---------------

.. py:property:: altitude_crossing_sides
    :canonical: br.steak.core.stkobjects.ISensorProjectionDisplayDistance.altitude_crossing_sides
    :type: SensorAltitudeCrossingSideType

    Indicate which crossings are computed and displayed in the 2D Graphics window.

.. py:property:: direction
    :canonical: br.steak.core.stkobjects.ISensorProjectionDisplayDistance.direction
    :type: SensorAltitudeCrossingDirection

    Indicate the direction in which the sensor's field of view crosses the specified altitude.

.. py:property:: maximum
    :canonical: br.steak.core.stkobjects.ISensorProjectionDisplayDistance.maximum
    :type: float

    Maximum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.

.. py:property:: minimum
    :canonical: br.steak.core.stkobjects.ISensorProjectionDisplayDistance.minimum
    :type: float

    Minimum altitude above the facility, place or target from which the sensor projects. Uses Distance Dimension.

.. py:property:: number_of_steps
    :canonical: br.steak.core.stkobjects.ISensorProjectionDisplayDistance.number_of_steps
    :type: int

    Step count. Determines the interval between sensor projections. For a specified min/max altitude: the step count determines the number and altitude of projections to be displayed. Dimensionless.

.. py:property:: projects_thru_crossing
    :canonical: br.steak.core.stkobjects.ISensorProjectionDisplayDistance.projects_thru_crossing
    :type: bool

    Specify whether the sensor's field-of-view will extend beyond specified crossings.


