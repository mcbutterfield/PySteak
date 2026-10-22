VehiclePositionVelocityCollection
=================================

.. py:class:: br.ok.core.stkobjects.VehiclePositionVelocityCollection

   Collection of position and velocity elements for HPOP covariance.

.. py:currentmodule:: VehiclePositionVelocityCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehiclePositionVelocityCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehiclePositionVelocityCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.VehiclePositionVelocityCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehiclePositionVelocityCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.VehiclePositionVelocityCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.VehiclePositionVelocityCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehiclePositionVelocityElement
    :canonical: br.ok.core.stkobjects.VehiclePositionVelocityCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VehiclePositionVelocityElement`


