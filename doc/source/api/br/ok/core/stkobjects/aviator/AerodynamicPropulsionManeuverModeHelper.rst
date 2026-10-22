AerodynamicPropulsionManeuverModeHelper
=======================================

.. py:class:: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper

   Class defining the The calculation mode for the Aero/Prop maneuver mode helper. Helper for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AerodynamicPropulsionManeuverModeHelper

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.set_reference_airspeed`
              - Set the reference airspeed and reference airspeed type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.control_authority`
              - Get or set the control authority of how much to factor a turn over push/pull.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.estimated_ps`
              - Get the estimated specific excess power.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.flight_mode`
              - Get or set the performance flight mode.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.mode`
              - Get or set the calculation mode for the Aero/Prop maneuver mode helper.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed`
              - Get the reference airspeed.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed_type`
              - Get the reference airspeed type.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_altitude`
              - Get or set the reference altitude.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_load_factor`
              - Get or set the reference load factor.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_weight`
              - Get or set the reference weight.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.status_message`
              - Get the status message in the message window.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.use_afterburner`
              - Opt whether to use the afterburner if it is possible.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import AerodynamicPropulsionManeuverModeHelper


Property detail
---------------

.. py:property:: control_authority
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.control_authority
    :type: float

    Get or set the control authority of how much to factor a turn over push/pull.

.. py:property:: estimated_ps
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.estimated_ps
    :type: float

    Get the estimated specific excess power.

.. py:property:: flight_mode
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.flight_mode
    :type: AerodynamicPropulsionFlightMode

    Get or set the performance flight mode.

.. py:property:: mode
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.mode
    :type: AccelerationManeuverAerodynamicPropulsionMode

    Get or set the calculation mode for the Aero/Prop maneuver mode helper.

.. py:property:: reference_airspeed
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed
    :type: float

    Get the reference airspeed.

.. py:property:: reference_airspeed_type
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_airspeed_type
    :type: AirspeedType

    Get the reference airspeed type.

.. py:property:: reference_altitude
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_altitude
    :type: float

    Get or set the reference altitude.

.. py:property:: reference_load_factor
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_load_factor
    :type: float

    Get or set the reference load factor.

.. py:property:: reference_weight
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.reference_weight
    :type: float

    Get or set the reference weight.

.. py:property:: status_message
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.status_message
    :type: str

    Get the status message in the message window.

.. py:property:: use_afterburner
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.use_afterburner
    :type: bool

    Opt whether to use the afterburner if it is possible.


Method detail
-------------
















.. py:method:: set_reference_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: br.ok.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper.set_reference_airspeed

    Set the reference airspeed and reference airspeed type.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`




