PropagatorSimpleAscent
======================

.. py:class:: br.ok.core.stkobjects.PropagatorSimpleAscent

   Bases: :py:class:`~br.ok.core.stkobjects.IPropagator`

   Class defining the simple ascent propagator for a launch vehicle.

.. py:currentmodule:: PropagatorSimpleAscent

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorSimpleAscent.propagate`
              - Propagates the launch vehicle's path using the specified time interval.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorSimpleAscent.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorSimpleAscent.initial_state`
              - Get the initial state.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorSimpleAscent.step`
              - Step size. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import PropagatorSimpleAscent


Property detail
---------------

.. py:property:: ephemeris_interval
    :canonical: br.ok.core.stkobjects.PropagatorSimpleAscent.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: initial_state
    :canonical: br.ok.core.stkobjects.PropagatorSimpleAscent.initial_state
    :type: LaunchVehicleInitialState

    Get the initial state.

.. py:property:: step
    :canonical: br.ok.core.stkobjects.PropagatorSimpleAscent.step
    :type: float

    Step size. Uses Time Dimension.


Method detail
-------------



.. py:method:: propagate(self) -> None
    :canonical: br.ok.core.stkobjects.PropagatorSimpleAscent.propagate

    Propagates the launch vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`



