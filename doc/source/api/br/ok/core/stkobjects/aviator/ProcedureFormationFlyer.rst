ProcedureFormationFlyer
=======================

.. py:class:: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.IProcedure`

   Class defining an formationflyer procedure.

.. py:currentmodule:: ProcedureFormationFlyer

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.cross_range_close_rate`
              - Get Cross Range close rate.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.initial_close_max_speed_advantage`
              - Get Initial Close Max Speed Advantage.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.max_time_step`
              - Get Max time Step.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.min_time_step`
              - Get Min time Step.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_condition`
              - Get Stop condition.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_down_range`
              - Get stop downrange.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_fuel_state`
              - Get stop fuel state.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_on_hover`
              - Set Stop on hover mode.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_time`
              - Get stop time.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import ProcedureFormationFlyer


Property detail
---------------

.. py:property:: cross_range_close_rate
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.cross_range_close_rate
    :type: float

    Get Cross Range close rate.

.. py:property:: initial_close_max_speed_advantage
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.initial_close_max_speed_advantage
    :type: float

    Get Initial Close Max Speed Advantage.

.. py:property:: max_time_step
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.max_time_step
    :type: float

    Get Max time Step.

.. py:property:: min_time_step
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.min_time_step
    :type: float

    Get Min time Step.

.. py:property:: stop_condition
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_condition
    :type: FormationFlyerStopCondition

    Get Stop condition.

.. py:property:: stop_down_range
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_down_range
    :type: float

    Get stop downrange.

.. py:property:: stop_fuel_state
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_fuel_state
    :type: float

    Get stop fuel state.

.. py:property:: stop_on_hover
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_on_hover
    :type: None

    Set Stop on hover mode.

.. py:property:: stop_time
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.stop_time
    :type: float

    Get stop time.


Method detail
-------------



.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: br.ok.core.stkobjects.aviator.ProcedureFormationFlyer.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

















