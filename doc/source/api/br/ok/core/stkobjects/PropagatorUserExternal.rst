PropagatorUserExternal
======================

.. py:class:: br.ok.core.stkobjects.PropagatorUserExternal

   Bases: :py:class:`~br.ok.core.stkobjects.IPropagator`

   Class defining the user-external propagator.

.. py:currentmodule:: PropagatorUserExternal

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.propagate`
              - Propagates the vehicle's path using the specified time interval.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.available_propagators`
              - Get available propagators.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.available_vehicle_identifiers`
              - Get available IDs.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.description`
              - Description.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.file`
              - Name of user-external file.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.propagator`
              - Propagator.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.start_time`
              - Get or set the start time of ephemeris interval. Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.stop_time`
              - Get or set the stop time of ephemeris interval. Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorUserExternal.vehicle_id`
              - Vehicle ID.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import PropagatorUserExternal


Property detail
---------------

.. py:property:: available_propagators
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.available_propagators
    :type: list

    Get available propagators.

.. py:property:: available_vehicle_identifiers
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.available_vehicle_identifiers
    :type: list

    Get available IDs.

.. py:property:: description
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.description
    :type: str

    Description.

.. py:property:: ephemeris_interval
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: file
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.file
    :type: str

    Name of user-external file.

.. py:property:: propagator
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.propagator
    :type: str

    Propagator.

.. py:property:: start_time
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.start_time
    :type: typing.Any

    Get or set the start time of ephemeris interval. Uses DateFormat Dimension.

.. py:property:: step
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: stop_time
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.stop_time
    :type: typing.Any

    Get or set the stop time of ephemeris interval. Uses DateFormat Dimension.

.. py:property:: vehicle_id
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.vehicle_id
    :type: str

    Vehicle ID.


Method detail
-------------







.. py:method:: propagate(self) -> None
    :canonical: br.ok.core.stkobjects.PropagatorUserExternal.propagate

    Propagates the vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`











