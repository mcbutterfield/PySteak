DataProviderResultIntervalCollection
====================================

.. py:class:: br.steak.core.stkobjects.DataProviderResultIntervalCollection

   Represents a collection of intervals returned by the data providers.

.. py:currentmodule:: DataProviderResultIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultIntervalCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultIntervalCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultIntervalCollection.count`
              - Return a number of elements in collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import DataProviderResultIntervalCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.DataProviderResultIntervalCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.DataProviderResultIntervalCollection.count
    :type: int

    Return a number of elements in collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> DataProviderResultInterval
    :canonical: br.steak.core.stkobjects.DataProviderResultIntervalCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~DataProviderResultInterval`


