SensorEOIRSaturationCollection
==============================

.. py:class:: br.steak.core.stkobjects.SensorEOIRSaturationCollection

   Class defining the Saturations collection for an EOIR Sensor.

.. py:currentmodule:: SensorEOIRSaturationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SensorEOIRSaturationCollection.add`
              - Add a radiometric pair.
            * - :py:attr:`~br.steak.core.stkobjects.SensorEOIRSaturationCollection.item`
              - Given an index, returns an SensorEOIRRadiometricPair interface.
            * - :py:attr:`~br.steak.core.stkobjects.SensorEOIRSaturationCollection.remove_at`
              - Remove a radiometric pair given an index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SensorEOIRSaturationCollection._new_enum`
              - Enumerates through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.SensorEOIRSaturationCollection.count`
              - The number of items in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import SensorEOIRSaturationCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.SensorEOIRSaturationCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.SensorEOIRSaturationCollection.count
    :type: int

    The number of items in the collection.


Method detail
-------------

.. py:method:: add(self) -> SensorEOIRRadiometricPair
    :canonical: br.steak.core.stkobjects.SensorEOIRSaturationCollection.add

    Add a radiometric pair.

    :Returns:

        :obj:`~SensorEOIRRadiometricPair`


.. py:method:: item(self, index: int) -> SensorEOIRRadiometricPair
    :canonical: br.steak.core.stkobjects.SensorEOIRSaturationCollection.item

    Given an index, returns an SensorEOIRRadiometricPair interface.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SensorEOIRRadiometricPair`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.SensorEOIRSaturationCollection.remove_at

    Remove a radiometric pair given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


