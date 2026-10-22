SpaceEnvironmentRadiationDoseRateCollection
===========================================

.. py:class:: br.steak.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection

   Collection of dose rate elements computed for a shielding thickness.

.. py:currentmodule:: SpaceEnvironmentRadiationDoseRateCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import SpaceEnvironmentRadiationDoseRateCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> SpaceEnvironmentRadiationDoseRateElement
    :canonical: br.steak.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SpaceEnvironmentRadiationDoseRateElement`


