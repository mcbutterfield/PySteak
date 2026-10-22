VehicleGPSElementCollection
===========================

.. py:class:: br.steak.core.stkobjects.VehicleGPSElementCollection

   A collection of GPS elements.

.. py:currentmodule:: VehicleGPSElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSElementCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSElementCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSElementCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleGPSElementCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.VehicleGPSElementCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.VehicleGPSElementCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleGPSElement
    :canonical: br.steak.core.stkobjects.VehicleGPSElementCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VehicleGPSElement`


