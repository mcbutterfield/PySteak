BasicManeuverStrategySimpleTurn
===============================

.. py:class:: br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the simple turn strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategySimpleTurn

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn.reference_frame`
              - Get or set the reference frame for the simple turn.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn.turn_angle`
              - Get or set the turn angle for the simple turn.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn.turn_radius_factor`
              - Get or set the turn radius factor for the simple turn.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import BasicManeuverStrategySimpleTurn


Property detail
---------------

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: reference_frame
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn.reference_frame
    :type: BasicManeuverReferenceFrame

    Get or set the reference frame for the simple turn.

.. py:property:: turn_angle
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn.turn_angle
    :type: typing.Any

    Get or set the turn angle for the simple turn.

.. py:property:: turn_radius_factor
    :canonical: br.ok.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn.turn_radius_factor
    :type: float

    Get or set the turn radius factor for the simple turn.


