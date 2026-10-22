DataProviderInterval
====================

.. py:class:: br.ok.core.stkobjects.DataProviderInterval

   Bases: :py:class:`~br.ok.core.stkobjects.IDataProvider`, :py:class:`~br.ok.core.stkobjects.IDataProviderInfo`

   Support for interval data providers (e.g. Facility lighting times).

.. py:currentmodule:: DataProviderInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.DataProviderInterval.execute`
              - Compute the data; interval data providers require an interval or list of intervals. StartTime/StopTime use DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderInterval.execute_elements`
              - Compute the data and return just the indicated data elements; interval data providers require an interval or list of intervals. StartTime/StopTime use DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderInterval.execute_elements_event_array`
              - Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderInterval.execute_event_array`
              - Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import DataProviderInterval



Method detail
-------------

.. py:method:: execute(self, start_time: typing.Any, stop_time: typing.Any) -> DataProviderResult
    :canonical: br.ok.core.stkobjects.DataProviderInterval.execute

    Compute the data; interval data providers require an interval or list of intervals. StartTime/StopTime use DateFormat Dimension.

    :Parameters:

        **start_time** : :obj:`~typing.Any`

        **stop_time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_elements(self, start_time: typing.Any, stop_time: typing.Any, element_names: list) -> DataProviderResult
    :canonical: br.ok.core.stkobjects.DataProviderInterval.execute_elements

    Compute the data and return just the indicated data elements; interval data providers require an interval or list of intervals. StartTime/StopTime use DateFormat Dimension.

    :Parameters:

        **start_time** : :obj:`~typing.Any`

        **stop_time** : :obj:`~typing.Any`

        **element_names** : :obj:`~list`


    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_elements_event_array(self, event_array: ITimeToolTimeArray, start_time: typing.Any, stop_time: typing.Any, element_names: list) -> DataProviderResult
    :canonical: br.ok.core.stkobjects.DataProviderInterval.execute_elements_event_array

    Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.

    :Parameters:

        **event_array** : :obj:`~ITimeToolTimeArray`

        **start_time** : :obj:`~typing.Any`

        **stop_time** : :obj:`~typing.Any`

        **element_names** : :obj:`~list`


    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_event_array(self, event_array: ITimeToolTimeArray, start_time: typing.Any, stop_time: typing.Any) -> DataProviderResult
    :canonical: br.ok.core.stkobjects.DataProviderInterval.execute_event_array

    Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.

    :Parameters:

        **event_array** : :obj:`~ITimeToolTimeArray`

        **start_time** : :obj:`~typing.Any`

        **stop_time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~DataProviderResult`

