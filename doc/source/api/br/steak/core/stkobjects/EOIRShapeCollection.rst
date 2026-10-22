EOIRShapeCollection
===================

.. py:class:: br.steak.core.stkobjects.EOIRShapeCollection

   Collection of shapes.

.. py:currentmodule:: EOIRShapeCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.EOIRShapeCollection.add`
              - Add an element at the end of the collection.
            * - :py:attr:`~br.steak.core.stkobjects.EOIRShapeCollection.item`
              - Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:attr:`~br.steak.core.stkobjects.EOIRShapeCollection.remove_at`
              - Remove an element at the given index in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.EOIRShapeCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.EOIRShapeCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import EOIRShapeCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.EOIRShapeCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.EOIRShapeCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self) -> EOIRShape
    :canonical: br.steak.core.stkobjects.EOIRShapeCollection.add

    Add an element at the end of the collection.

    :Returns:

        :obj:`~EOIRShape`


.. py:method:: item(self, index: int) -> EOIRShape
    :canonical: br.steak.core.stkobjects.EOIRShapeCollection.item

    Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~EOIRShape`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.EOIRShapeCollection.remove_at

    Remove an element at the given index in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


