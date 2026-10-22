DoublesCollection
=================

.. py:class:: br.steak.core.stkutil.DoublesCollection

   A collection of doubles.

.. py:currentmodule:: DoublesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.DoublesCollection.add`
              - Add a value to the collection of doubles.
            * - :py:attr:`~br.steak.core.stkutil.DoublesCollection.item`
              - Return a double at a specified position.
            * - :py:attr:`~br.steak.core.stkutil.DoublesCollection.remove_all`
              - Clear the collection.
            * - :py:attr:`~br.steak.core.stkutil.DoublesCollection.remove_at`
              - Remove an element from the collection at a specified position.
            * - :py:attr:`~br.steak.core.stkutil.DoublesCollection.set_at`
              - Update an element in the collection at a specified position.
            * - :py:attr:`~br.steak.core.stkutil.DoublesCollection.to_array`
              - Return an array of the elements in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.DoublesCollection._new_enum`
              - Return a collection enumerator.
            * - :py:attr:`~br.steak.core.stkutil.DoublesCollection.count`
              - Return the number of items in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkutil import DoublesCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkutil.DoublesCollection._new_enum
    :type: EnumeratorProxy

    Return a collection enumerator.

.. py:property:: count
    :canonical: br.steak.core.stkutil.DoublesCollection.count
    :type: int

    Return the number of items in the collection.


Method detail
-------------

.. py:method:: add(self, value: float) -> None
    :canonical: br.steak.core.stkutil.DoublesCollection.add

    Add a value to the collection of doubles.

    :Parameters:

        **value** : :obj:`~float`


    :Returns:

        :obj:`~None`


.. py:method:: item(self, index: int) -> float
    :canonical: br.steak.core.stkutil.DoublesCollection.item

    Return a double at a specified position.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~float`

.. py:method:: remove_all(self) -> None
    :canonical: br.steak.core.stkutil.DoublesCollection.remove_all

    Clear the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkutil.DoublesCollection.remove_at

    Remove an element from the collection at a specified position.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: set_at(self, index: int, value: float) -> None
    :canonical: br.steak.core.stkutil.DoublesCollection.set_at

    Update an element in the collection at a specified position.

    :Parameters:

        **index** : :obj:`~int`

        **value** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: to_array(self) -> list
    :canonical: br.steak.core.stkutil.DoublesCollection.to_array

    Return an array of the elements in the collection.

    :Returns:

        :obj:`~list`


