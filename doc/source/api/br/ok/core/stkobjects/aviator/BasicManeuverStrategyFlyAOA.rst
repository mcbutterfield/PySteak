BasicManeuverStrategyFlyAOA
===========================

.. py:class:: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the fly AOA strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyFlyAOA

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.aoa`
              - Get or set the angle of attack.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.control_roll_angle`
              - Get or set the option to define a goal value for the aircraft's roll angle.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.override_roll_rate`
              - Get or set the roll rate override value for the Fly AOA basic maneuver strategy. The roll rate mode must be set to override to access this property.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.roll_angle`
              - Get or set the goal value for the roll angle.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.roll_rate_dot`
              - Get or set the rate of change of the roll rate.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.roll_rate_mode`
              - Get or set the roll rate mode for a Fly AOA basic maneuver strategy.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.stop_on_roll_angle`
              - Get or set the option to stop the maneuver if the specified roll angle is achieved.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.turn_direction`
              - Get or set the roll turn direction for a Fly AOA basic maneuver strategy.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import BasicManeuverStrategyFlyAOA


Property detail
---------------

.. py:property:: airspeed_options
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: aoa
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.aoa
    :type: typing.Any

    Get or set the angle of attack.

.. py:property:: control_roll_angle
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.control_roll_angle
    :type: bool

    Get or set the option to define a goal value for the aircraft's roll angle.

.. py:property:: override_roll_rate
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.override_roll_rate
    :type: typing.Any

    Get or set the roll rate override value for the Fly AOA basic maneuver strategy. The roll rate mode must be set to override to access this property.

.. py:property:: roll_angle
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.roll_angle
    :type: typing.Any

    Get or set the goal value for the roll angle.

.. py:property:: roll_rate_dot
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.roll_rate_dot
    :type: typing.Any

    Get or set the rate of change of the roll rate.

.. py:property:: roll_rate_mode
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.roll_rate_mode
    :type: PerformanceModelOverride

    Get or set the roll rate mode for a Fly AOA basic maneuver strategy.

.. py:property:: stop_on_roll_angle
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.stop_on_roll_angle
    :type: bool

    Get or set the option to stop the maneuver if the specified roll angle is achieved.

.. py:property:: turn_direction
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA.turn_direction
    :type: FlyAOALeftRight

    Get or set the roll turn direction for a Fly AOA basic maneuver strategy.


