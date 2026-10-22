VehicleSpatialInformation
=========================

.. py:class:: br.ok.core.stkobjects.VehicleSpatialInformation

   Represents a spatial information of the vehicle.

.. py:currentmodule:: VehicleSpatialInformation

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleSpatialInformation.get_available_times`
              - Return a collection of available intervals.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleSpatialInformation.get_state`
              - Return a spatial state of the vehicle at specified time.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleSpatialInformation.recycle`
              - Control whether to reuse the same spatial state object in subsequent calls to GetState.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleSpatialInformation


Property detail
---------------

.. py:property:: recycle
    :canonical: br.ok.core.stkobjects.VehicleSpatialInformation.recycle
    :type: bool

    Control whether to reuse the same spatial state object in subsequent calls to GetState.


Method detail
-------------

.. py:method:: get_available_times(self) -> TimeIntervalCollectionReadOnly
    :canonical: br.ok.core.stkobjects.VehicleSpatialInformation.get_available_times

    Return a collection of available intervals.

    :Returns:

        :obj:`~TimeIntervalCollectionReadOnly`

.. py:method:: get_state(self, time: typing.Any) -> SpatialState
    :canonical: br.ok.core.stkobjects.VehicleSpatialInformation.get_state

    Return a spatial state of the vehicle at specified time.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~SpatialState`


