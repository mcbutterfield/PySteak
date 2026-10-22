ProcedureDelay
==============

.. py:class:: br.ok.core.stkobjects.aviator.ProcedureDelay

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.IProcedure`

   Class defining a delay procedure.

.. py:currentmodule:: ProcedureDelay

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureDelay.altitude`
              - Get or set the requested altitude of the procedure.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureDelay.altitude_mode`
              - Get or set the mode for handling the altitude of the aircraft.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureDelay.cruise_airspeed_options`
              - Get the interface for the cruise airspeed options.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureDelay.turn_direction`
              - Get or set the turn direction of the procedure.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureDelay.turn_radius_factor`
              - Get or set the turn radius factor.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import ProcedureDelay


Property detail
---------------

.. py:property:: altitude
    :canonical: br.ok.core.stkobjects.aviator.ProcedureDelay.altitude
    :type: float

    Get or set the requested altitude of the procedure.

.. py:property:: altitude_mode
    :canonical: br.ok.core.stkobjects.aviator.ProcedureDelay.altitude_mode
    :type: DelayAltitudeMode

    Get or set the mode for handling the altitude of the aircraft.

.. py:property:: cruise_airspeed_options
    :canonical: br.ok.core.stkobjects.aviator.ProcedureDelay.cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the interface for the cruise airspeed options.

.. py:property:: turn_direction
    :canonical: br.ok.core.stkobjects.aviator.ProcedureDelay.turn_direction
    :type: NavigatorTurnDirection

    Get or set the turn direction of the procedure.

.. py:property:: turn_radius_factor
    :canonical: br.ok.core.stkobjects.aviator.ProcedureDelay.turn_radius_factor
    :type: float

    Get or set the turn radius factor.


