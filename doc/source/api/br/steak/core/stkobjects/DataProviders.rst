DataProviders
=============

.. py:class:: br.steak.core.stkobjects.DataProviders

   Class defining data providers.

.. py:currentmodule:: DataProviders

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviders.contains`
              - Determine whether the collection contains a specific data provider.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviders.get_item_by_index`
              - Retrieve a data provider from the collection by index.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviders.get_item_by_name`
              - Retrieve a data provider from the collection by name.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviders.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviders._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviders.count`
              - Return an element in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import DataProviders


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.DataProviders._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.DataProviders.count
    :type: int

    Return an element in the collection.


Method detail
-------------

.. py:method:: contains(self, data_provider_name: str) -> bool
    :canonical: br.steak.core.stkobjects.DataProviders.contains

    Determine whether the collection contains a specific data provider.

    :Parameters:

        **data_provider_name** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: get_item_by_index(self, index: int) -> IDataProviderInfo
    :canonical: br.steak.core.stkobjects.DataProviders.get_item_by_index

    Retrieve a data provider from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_item_by_name(self, name: str) -> IDataProviderInfo
    :canonical: br.steak.core.stkobjects.DataProviders.get_item_by_name

    Retrieve a data provider from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: item(self, index_or_name: typing.Any) -> IDataProviderInfo
    :canonical: br.steak.core.stkobjects.DataProviders.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IDataProviderInfo`


