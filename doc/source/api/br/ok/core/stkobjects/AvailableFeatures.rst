AvailableFeatures
=================

.. py:class:: br.ok.core.stkobjects.AvailableFeatures

   Class is used to check the availability of the features such as Astrogator, etc.

.. py:currentmodule:: AvailableFeatures

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AvailableFeatures.is_object_type_available`
              - Return true if the specified STK object type is available.
            * - :py:attr:`~br.ok.core.stkobjects.AvailableFeatures.is_propagator_type_available`
              - Return true if the specified propagator is available.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AvailableFeatures



Method detail
-------------

.. py:method:: is_object_type_available(self, object_type: STKObjectType) -> bool
    :canonical: br.ok.core.stkobjects.AvailableFeatures.is_object_type_available

    Return true if the specified STK object type is available.

    :Parameters:

        **object_type** : :obj:`~STKObjectType`


    :Returns:

        :obj:`~bool`

.. py:method:: is_propagator_type_available(self, propagator_type: PropagatorType) -> bool
    :canonical: br.ok.core.stkobjects.AvailableFeatures.is_propagator_type_available

    Return true if the specified propagator is available.

    :Parameters:

        **propagator_type** : :obj:`~PropagatorType`


    :Returns:

        :obj:`~bool`

