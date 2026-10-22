UserVariableCollection
======================

.. py:class:: br.steak.core.stkobjects.astrogator.UserVariableCollection

   User Variable Initial Value Collection.

.. py:currentmodule:: UserVariableCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.UserVariableCollection.get_item_by_index`
              - Retrieve a user variable in the collection by index.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.UserVariableCollection.get_item_by_name`
              - Retrieve a user variable in the collection by name.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.UserVariableCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.UserVariableCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.UserVariableCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import UserVariableCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.astrogator.UserVariableCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.astrogator.UserVariableCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------


.. py:method:: get_item_by_index(self, index: int) -> UserVariable
    :canonical: br.steak.core.stkobjects.astrogator.UserVariableCollection.get_item_by_index

    Retrieve a user variable in the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~UserVariable`

.. py:method:: get_item_by_name(self, name: str) -> UserVariable
    :canonical: br.steak.core.stkobjects.astrogator.UserVariableCollection.get_item_by_name

    Retrieve a user variable in the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UserVariable`

.. py:method:: item(self, index_or_name: typing.Any) -> UserVariable
    :canonical: br.steak.core.stkobjects.astrogator.UserVariableCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~UserVariable`


