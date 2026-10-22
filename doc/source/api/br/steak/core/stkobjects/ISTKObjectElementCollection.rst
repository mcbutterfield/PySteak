ISTKObjectElementCollection
===========================

.. py:class:: br.steak.core.stkobjects.ISTKObjectElementCollection

   Represents a collection of STK objects.

.. py:currentmodule:: ISTKObjectElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ISTKObjectElementCollection.contains`
              - Check whether an object with the given name exists.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObjectElementCollection.get_item_by_index`
              - Retrieve an Stk object element from the collection by index.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObjectElementCollection.get_item_by_name`
              - Retrieve an Stk object element from the collection by name.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObjectElementCollection.item`
              - Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ISTKObjectElementCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObjectElementCollection.count`
              - Return the number of elements in a collection.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ISTKObjectElementCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.ISTKObjectElementCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.ISTKObjectElementCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: contains(self, inst_name: str) -> bool
    :canonical: br.steak.core.stkobjects.ISTKObjectElementCollection.contains

    Check whether an object with the given name exists.

    :Parameters:

        **inst_name** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: get_item_by_index(self, index: int) -> ISTKObject
    :canonical: br.steak.core.stkobjects.ISTKObjectElementCollection.get_item_by_index

    Retrieve an Stk object element from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ISTKObject`

.. py:method:: get_item_by_name(self, name: str) -> ISTKObject
    :canonical: br.steak.core.stkobjects.ISTKObjectElementCollection.get_item_by_name

    Retrieve an Stk object element from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ISTKObject`

.. py:method:: item(self, index_or_name: typing.Any) -> ISTKObject
    :canonical: br.steak.core.stkobjects.ISTKObjectElementCollection.item

    Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ISTKObject`


