DataProviderResultInterval
==========================

.. py:class:: br.steak.core.stkobjects.DataProviderResultInterval

   Represents a interval in the collection of intervals returned by the data providers.

.. py:currentmodule:: DataProviderResultInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultInterval.multiple_threshold_crossings`
              - Return an array of two-dimensional arrays.  Each two-dimensional array contains start and stop times based on the boundaries passed in. The DataSets property must contain the Time dataset for this method to work correctly.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultInterval.threshold_crossings`
              - Return a two-dimensional array containing time and direction data (negative for decreasing). The DataSets property must contain the Time dataset for this method to work correctly.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultInterval.data_sets`
              - Return a collection of data sets within the interval.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultInterval.start_time`
              - Return the start time of the interval. Uses DateFormat Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultInterval.stop_time`
              - Return the stop time of the interval. Uses DateFormat Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import DataProviderResultInterval


Property detail
---------------

.. py:property:: data_sets
    :canonical: br.steak.core.stkobjects.DataProviderResultInterval.data_sets
    :type: DataProviderResultDataSetCollection

    Return a collection of data sets within the interval.

.. py:property:: start_time
    :canonical: br.steak.core.stkobjects.DataProviderResultInterval.start_time
    :type: typing.Any

    Return the start time of the interval. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: br.steak.core.stkobjects.DataProviderResultInterval.stop_time
    :type: typing.Any

    Return the stop time of the interval. Uses DateFormat Dimension.


Method detail
-------------


.. py:method:: multiple_threshold_crossings(self, elem_name: str, thresholds: list) -> list
    :canonical: br.steak.core.stkobjects.DataProviderResultInterval.multiple_threshold_crossings

    Return an array of two-dimensional arrays.  Each two-dimensional array contains start and stop times based on the boundaries passed in. The DataSets property must contain the Time dataset for this method to work correctly.

    :Parameters:

        **elem_name** : :obj:`~str`

        **thresholds** : :obj:`~list`


    :Returns:

        :obj:`~list`



.. py:method:: threshold_crossings(self, elem_name: str, threshold: typing.Any) -> list
    :canonical: br.steak.core.stkobjects.DataProviderResultInterval.threshold_crossings

    Return a two-dimensional array containing time and direction data (negative for decreasing). The DataSets property must contain the Time dataset for this method to work correctly.

    :Parameters:

        **elem_name** : :obj:`~str`

        **threshold** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

