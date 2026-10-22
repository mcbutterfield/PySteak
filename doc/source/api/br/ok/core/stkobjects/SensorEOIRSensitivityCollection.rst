SensorEOIRSensitivityCollection
===============================

.. py:class:: br.ok.core.stkobjects.SensorEOIRSensitivityCollection

   Class defining the Sensitivities collection for an EOIR Sensor.

.. py:currentmodule:: SensorEOIRSensitivityCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SensorEOIRSensitivityCollection.add`
              - Add a radiometric pair.
            * - :py:attr:`~br.ok.core.stkobjects.SensorEOIRSensitivityCollection.item`
              - Given an index, returns an SensorEOIRRadiometricPair interface.
            * - :py:attr:`~br.ok.core.stkobjects.SensorEOIRSensitivityCollection.remove_at`
              - Remove a radiometric pair given an index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SensorEOIRSensitivityCollection._new_enum`
              - Enumerates through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.SensorEOIRSensitivityCollection.count`
              - The number of items in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import SensorEOIRSensitivityCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.SensorEOIRSensitivityCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.SensorEOIRSensitivityCollection.count
    :type: int

    The number of items in the collection.


Method detail
-------------

.. py:method:: add(self) -> SensorEOIRRadiometricPair
    :canonical: br.ok.core.stkobjects.SensorEOIRSensitivityCollection.add

    Add a radiometric pair.

    :Returns:

        :obj:`~SensorEOIRRadiometricPair`


.. py:method:: item(self, index: int) -> SensorEOIRRadiometricPair
    :canonical: br.ok.core.stkobjects.SensorEOIRSensitivityCollection.item

    Given an index, returns an SensorEOIRRadiometricPair interface.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SensorEOIRRadiometricPair`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.ok.core.stkobjects.SensorEOIRSensitivityCollection.remove_at

    Remove a radiometric pair given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


