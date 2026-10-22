PropagatorTwoBody
=================

.. py:class:: br.ok.core.stkobjects.PropagatorTwoBody

   Bases: :py:class:`~br.ok.core.stkobjects.IPropagator`

   Class defining the two body propagator.

.. py:currentmodule:: PropagatorTwoBody

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorTwoBody.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorTwoBody.display_coordinate_type`
              - The propagator's display coordinate type.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorTwoBody.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorTwoBody.initial_state`
              - Get the initial state.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorTwoBody.propagation_frame`
              - Get or set the propagation frame.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorTwoBody.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorTwoBody.supported_propagation_frames`
              - Return supported propagation frames.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import PropagatorTwoBody


Property detail
---------------

.. py:property:: display_coordinate_type
    :canonical: br.ok.core.stkobjects.PropagatorTwoBody.display_coordinate_type
    :type: PropagatorDisplayCoordinateType

    The propagator's display coordinate type.

.. py:property:: ephemeris_interval
    :canonical: br.ok.core.stkobjects.PropagatorTwoBody.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: initial_state
    :canonical: br.ok.core.stkobjects.PropagatorTwoBody.initial_state
    :type: VehicleInitialState

    Get the initial state.

.. py:property:: propagation_frame
    :canonical: br.ok.core.stkobjects.PropagatorTwoBody.propagation_frame
    :type: VehiclePropagationFrame

    Get or set the propagation frame.

.. py:property:: step
    :canonical: br.ok.core.stkobjects.PropagatorTwoBody.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: supported_propagation_frames
    :canonical: br.ok.core.stkobjects.PropagatorTwoBody.supported_propagation_frames
    :type: list

    Return supported propagation frames.


Method detail
-------------





.. py:method:: propagate(self) -> None
    :canonical: br.ok.core.stkobjects.PropagatorTwoBody.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`






