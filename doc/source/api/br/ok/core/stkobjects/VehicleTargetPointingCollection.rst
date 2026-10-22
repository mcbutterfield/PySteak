VehicleTargetPointingCollection
===============================

.. py:class:: br.ok.core.stkobjects.VehicleTargetPointingCollection

   List of Attitude Targets.

.. py:currentmodule:: VehicleTargetPointingCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.add_position_as_target`
              - Add the specified LLA position to the collection of targets. Latitude param uses Latitude Dimension, Longitude param uses Longitude Dimension. Alt param uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.contains`
              - Return true if the collection contains the specified target.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.remove`
              - Remove the element using the object path.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.remove_at`
              - Remove an element from the collection using specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.available_targets`
              - Return an array of available targets.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleTargetPointingCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: available_targets
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.available_targets
    :type: list

    Return an array of available targets.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self, short_path: str) -> VehicleTargetPointingElement
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.add

    Add a new element to the collection.

    :Parameters:

        **short_path** : :obj:`~str`


    :Returns:

        :obj:`~VehicleTargetPointingElement`

.. py:method:: add_position_as_target(self, latitude: float, longitude: float, altitude: float) -> VehicleTargetPointingElement
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.add_position_as_target

    Add the specified LLA position to the collection of targets. Latitude param uses Latitude Dimension, Longitude param uses Longitude Dimension. Alt param uses Distance Dimension.

    :Parameters:

        **latitude** : :obj:`~float`

        **longitude** : :obj:`~float`

        **altitude** : :obj:`~float`


    :Returns:

        :obj:`~VehicleTargetPointingElement`


.. py:method:: contains(self, path: str) -> bool
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.contains

    Return true if the collection contains the specified target.

    :Parameters:

        **path** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: item(self, index: int) -> VehicleTargetPointingElement
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VehicleTargetPointingElement`

.. py:method:: remove(self, path: str) -> None
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.remove

    Remove the element using the object path.

    :Parameters:

        **path** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


