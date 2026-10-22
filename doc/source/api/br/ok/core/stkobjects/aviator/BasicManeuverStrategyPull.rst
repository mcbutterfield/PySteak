BasicManeuverStrategyPull
=========================

.. py:class:: br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the pull strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyPull

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.active_angle`
              - Get or set the pull angle for the active mode.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.active_mode`
              - Get or set the pull mode for the pull basic maneuver strategy.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.override_pull_g`
              - Get or set the pull G override value. The pull G mode must be set to override to access this property.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.pull_g_mode`
              - Get or set the pull G mode for a pull basic maneuver strategy.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import BasicManeuverStrategyPull


Property detail
---------------

.. py:property:: active_angle
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.active_angle
    :type: typing.Any

    Get or set the pull angle for the active mode.

.. py:property:: active_mode
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.active_mode
    :type: PullMode

    Get or set the pull mode for the pull basic maneuver strategy.

.. py:property:: airspeed_options
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: override_pull_g
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.override_pull_g
    :type: float

    Get or set the pull G override value. The pull G mode must be set to override to access this property.

.. py:property:: pull_g_mode
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategyPull.pull_g_mode
    :type: PerformanceModelOverride

    Get or set the pull G mode for a pull basic maneuver strategy.


