VehicleGroundEllipsesCollection
===============================

.. py:class:: br.ok.core.stkobjects.VehicleGroundEllipsesCollection

   List of Ground Ellipses.

.. py:currentmodule:: VehicleGroundEllipsesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection.get_ellipse_set`
              - Get an element from the collection using the Ellipse Set name.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection.remove_ellipse_set`
              - Remove an element from the collection using the Ellipse Set name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGroundEllipsesCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.VehicleGroundEllipsesCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.VehicleGroundEllipsesCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self, name: str) -> VehicleGroundEllipseElement
    :canonical: br.ok.core.stkobjects.VehicleGroundEllipsesCollection.add

    Add a new element to the collection.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~VehicleGroundEllipseElement`


.. py:method:: get_ellipse_set(self, ellipse_set_name: str) -> VehicleGroundEllipseElement
    :canonical: br.ok.core.stkobjects.VehicleGroundEllipsesCollection.get_ellipse_set

    Get an element from the collection using the Ellipse Set name.

    :Parameters:

        **ellipse_set_name** : :obj:`~str`


    :Returns:

        :obj:`~VehicleGroundEllipseElement`

.. py:method:: item(self, index: int) -> VehicleGroundEllipseElement
    :canonical: br.ok.core.stkobjects.VehicleGroundEllipsesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VehicleGroundEllipseElement`

.. py:method:: remove_all(self) -> None
    :canonical: br.ok.core.stkobjects.VehicleGroundEllipsesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.ok.core.stkobjects.VehicleGroundEllipsesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_ellipse_set(self, ellipse_set_name: str) -> None
    :canonical: br.ok.core.stkobjects.VehicleGroundEllipsesCollection.remove_ellipse_set

    Remove an element from the collection using the Ellipse Set name.

    :Parameters:

        **ellipse_set_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


