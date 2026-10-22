VehicleEllipseDataCollection
============================

.. py:class:: br.ok.core.stkobjects.VehicleEllipseDataCollection

   Ellipse Data Collection.

.. py:currentmodule:: VehicleEllipseDataCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleEllipseDataCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleEllipseDataCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleEllipseDataCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleEllipseDataCollection.remove_at`
              - Remove an element from the collection using specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleEllipseDataCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleEllipseDataCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleEllipseDataCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.VehicleEllipseDataCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.VehicleEllipseDataCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self) -> VehicleEllipseDataElement
    :canonical: br.ok.core.stkobjects.VehicleEllipseDataCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~VehicleEllipseDataElement`


.. py:method:: item(self, index: int) -> VehicleEllipseDataElement
    :canonical: br.ok.core.stkobjects.VehicleEllipseDataCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VehicleEllipseDataElement`

.. py:method:: remove_all(self) -> None
    :canonical: br.ok.core.stkobjects.VehicleEllipseDataCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.ok.core.stkobjects.VehicleEllipseDataCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


