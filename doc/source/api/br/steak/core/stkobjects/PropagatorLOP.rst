PropagatorLOP
=============

.. py:class:: br.steak.core.stkobjects.PropagatorLOP

   Bases: :py:class:`~br.steak.core.stkobjects.IPropagator`

   Class defining the Long-term Orbit Predictor (LOP).

.. py:currentmodule:: PropagatorLOP

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.PropagatorLOP.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.PropagatorLOP.display_coordinate_type`
              - The propagator's display coordinate type.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorLOP.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorLOP.force_model`
              - Get the force model parameters.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorLOP.initial_state`
              - Get the initial state.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorLOP.step`
              - Step size. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import PropagatorLOP


Property detail
---------------

.. py:property:: display_coordinate_type
    :canonical: br.steak.core.stkobjects.PropagatorLOP.display_coordinate_type
    :type: PropagatorDisplayCoordinateType

    The propagator's display coordinate type.

.. py:property:: ephemeris_interval
    :canonical: br.steak.core.stkobjects.PropagatorLOP.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: force_model
    :canonical: br.steak.core.stkobjects.PropagatorLOP.force_model
    :type: VehicleLOPForceModel

    Get the force model parameters.

.. py:property:: initial_state
    :canonical: br.steak.core.stkobjects.PropagatorLOP.initial_state
    :type: VehicleInitialState

    Get the initial state.

.. py:property:: step
    :canonical: br.steak.core.stkobjects.PropagatorLOP.step
    :type: float

    Step size. Uses Time Dimension.


Method detail
-------------






.. py:method:: propagate(self) -> None
    :canonical: br.steak.core.stkobjects.PropagatorLOP.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`



