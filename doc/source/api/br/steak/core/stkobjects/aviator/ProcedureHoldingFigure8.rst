ProcedureHoldingFigure8
=======================

.. py:class:: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8

   Bases: :py:class:`~br.steak.core.stkobjects.aviator.IProcedure`

   Class defining a holding figure 8 procedure.

.. py:currentmodule:: ProcedureHoldingFigure8

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.get_minimum_width`
              - Get the minimum allowable width based on the aircraft's minimum diameter at this altitude.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.bearing`
              - Get or set the bearing of the holding point from the site.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.enroute_turn_direction_options`
              - Get the enroute turn direction options.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.hold_cruise_airspeed_options`
              - Get the hold cruise airspeed options.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.length`
              - Get or set the distance between the centers of the pattern's arcs.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.level_off_mode`
              - Get or set the mode for the level off maneuver.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.profile_mode`
              - Get or set the mode defines how the aircraft will perform the holding pattern.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.range`
              - Get or set the distance to the holding point from the site.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.refuel_dump_mode`
              - Get or set the mode that defines when the aircraft will leave the holding pattern for a Refuel/Dump operation.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.turns`
              - Get or set the number of full turns.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.use_alternate_entry_points`
              - Get or set the option to enter the holding pattern from an alternate point.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.use_magnetic_heading`
              - Get or set the option to use a magnetic heading.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.width`
              - Get or set the width of the holding pattern.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.aviator import ProcedureHoldingFigure8


Property detail
---------------

.. py:property:: altitude_options
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.altitude_options
    :type: AltitudeMSLOptions

    Get the altitude options.

.. py:property:: bearing
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.bearing
    :type: typing.Any

    Get or set the bearing of the holding point from the site.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.enroute_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_options
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_turn_direction_options
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.enroute_turn_direction_options
    :type: EnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: hold_cruise_airspeed_options
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.hold_cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the hold cruise airspeed options.

.. py:property:: length
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.length
    :type: float

    Get or set the distance between the centers of the pattern's arcs.

.. py:property:: level_off_mode
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.level_off_mode
    :type: AltitudeConstraintManeuverMode

    Get or set the mode for the level off maneuver.

.. py:property:: profile_mode
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.profile_mode
    :type: HoldingProfileMode

    Get or set the mode defines how the aircraft will perform the holding pattern.

.. py:property:: range
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.range
    :type: float

    Get or set the distance to the holding point from the site.

.. py:property:: refuel_dump_mode
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.refuel_dump_mode
    :type: HoldRefuelDumpMode

    Get or set the mode that defines when the aircraft will leave the holding pattern for a Refuel/Dump operation.

.. py:property:: turns
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.turns
    :type: int

    Get or set the number of full turns.

.. py:property:: use_alternate_entry_points
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.use_alternate_entry_points
    :type: bool

    Get or set the option to enter the holding pattern from an alternate point.

.. py:property:: use_magnetic_heading
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.use_magnetic_heading
    :type: bool

    Get or set the option to use a magnetic heading.

.. py:property:: width
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.width
    :type: float

    Get or set the width of the holding pattern.


Method detail
-------------







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

.. py:method:: get_minimum_width(self) -> float
    :canonical: br.steak.core.stkobjects.aviator.ProcedureHoldingFigure8.get_minimum_width

    Get the minimum allowable width based on the aircraft's minimum diameter at this altitude.

    :Returns:

        :obj:`~float`




















