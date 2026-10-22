DataProviderResultDataSet
=========================

.. py:class:: br.ok.core.stkobjects.DataProviderResultDataSet

   Represents a dataset in the collection of datasets returned by the data providers.

.. py:currentmodule:: DataProviderResultDataSet

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResultDataSet.get_internal_units_values`
              - Get the Internal Unit Values of the Data.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResultDataSet.get_values`
              - Retrieve an array of values of the elements in the dataset.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResultDataSet.get_values_subset`
              - Retrieve a subset of an array of values of the elements in the dataset beginning at a given zero-indexed position and containing a specified number of values.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResultDataSet.count`
              - Return a number of elements in the dataset. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResultDataSet.dimension_name`
              - Return the dimension of elements of the dataset.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResultDataSet.element_name`
              - Return a name of the dataset.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResultDataSet.element_type`
              - Return a type of elements of the dataset. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResultDataSet.statistics`
              - Return an interface for computing statistics on the results.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import DataProviderResultDataSet


Property detail
---------------

.. py:property:: count
    :canonical: br.ok.core.stkobjects.DataProviderResultDataSet.count
    :type: int

    Return a number of elements in the dataset. Dimensionless.

.. py:property:: dimension_name
    :canonical: br.ok.core.stkobjects.DataProviderResultDataSet.dimension_name
    :type: str

    Return the dimension of elements of the dataset.

.. py:property:: element_name
    :canonical: br.ok.core.stkobjects.DataProviderResultDataSet.element_name
    :type: str

    Return a name of the dataset.

.. py:property:: element_type
    :canonical: br.ok.core.stkobjects.DataProviderResultDataSet.element_type
    :type: int

    Return a type of elements of the dataset. Dimensionless.

.. py:property:: statistics
    :canonical: br.ok.core.stkobjects.DataProviderResultDataSet.statistics
    :type: DataProviderResultStatistics

    Return an interface for computing statistics on the results.


Method detail
-------------





.. py:method:: get_internal_units_values(self) -> list
    :canonical: br.ok.core.stkobjects.DataProviderResultDataSet.get_internal_units_values

    Get the Internal Unit Values of the Data.

    :Returns:

        :obj:`~list`

.. py:method:: get_values(self) -> list
    :canonical: br.ok.core.stkobjects.DataProviderResultDataSet.get_values

    Retrieve an array of values of the elements in the dataset.

    :Returns:

        :obj:`~list`

.. py:method:: get_values_subset(self, index: int, count: int) -> list
    :canonical: br.ok.core.stkobjects.DataProviderResultDataSet.get_values_subset

    Retrieve a subset of an array of values of the elements in the dataset beginning at a given zero-indexed position and containing a specified number of values.

    :Parameters:

        **index** : :obj:`~int`

        **count** : :obj:`~int`


    :Returns:

        :obj:`~list`


