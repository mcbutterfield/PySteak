AutomaticSequenceCollection
===========================

.. py:class:: br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection

   Automatic Sequence Collection.

.. py:currentmodule:: AutomaticSequenceCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.add`
              - Create a new sequence.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.get_item_by_index`
              - Retrieve the given automatic sequence found by the index.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.get_item_by_name`
              - Retrieve the given automatic sequence found by the name.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.item`
              - Return the given automatic sequence.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.remove`
              - Remove a sequence.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.count`
              - Get the size of the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import AutomaticSequenceCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.count
    :type: int

    Get the size of the collection.


Method detail
-------------

.. py:method:: add(self, name: str) -> AutomaticSequence
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.add

    Create a new sequence.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AutomaticSequence`


.. py:method:: get_item_by_index(self, index: int) -> AutomaticSequence
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.get_item_by_index

    Retrieve the given automatic sequence found by the index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~AutomaticSequence`

.. py:method:: get_item_by_name(self, name: str) -> AutomaticSequence
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.get_item_by_name

    Retrieve the given automatic sequence found by the name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AutomaticSequence`

.. py:method:: item(self, index_or_name: typing.Any) -> AutomaticSequence
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.item

    Return the given automatic sequence.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~AutomaticSequence`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequenceCollection.remove

    Remove a sequence.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`


