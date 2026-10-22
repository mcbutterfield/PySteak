SensorGraphics3DTargetProjectionCollection
==========================================

.. py:class:: br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection

   Time Dependent Target Projection List.

.. py:currentmodule:: SensorGraphics3DTargetProjectionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.remove_at`
              - Remove an element from the collection using specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import SensorGraphics3DTargetProjectionCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self) -> SensorGraphics3DProjectionElement
    :canonical: br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~SensorGraphics3DProjectionElement`


.. py:method:: item(self, index: int) -> SensorGraphics3DProjectionElement
    :canonical: br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SensorGraphics3DProjectionElement`

.. py:method:: remove_all(self) -> None
    :canonical: br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.SensorGraphics3DTargetProjectionCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


