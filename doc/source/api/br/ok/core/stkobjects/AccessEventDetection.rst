AccessEventDetection
====================

.. py:class:: br.ok.core.stkobjects.AccessEventDetection

   Define properties and methods to configure the event detection strategy used in access computations.

.. py:currentmodule:: AccessEventDetection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AccessEventDetection.is_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.AccessEventDetection.set_type`
              - Set the event detection type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AccessEventDetection.strategy`
              - Get the selected event detection strategy.
            * - :py:attr:`~br.ok.core.stkobjects.AccessEventDetection.supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.AccessEventDetection.type`
              - Get the type of event detection (e.g., with or without subsampling).



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AccessEventDetection


Property detail
---------------

.. py:property:: strategy
    :canonical: br.ok.core.stkobjects.AccessEventDetection.strategy
    :type: IEventDetectionStrategy

    Get the selected event detection strategy.

.. py:property:: supported_types
    :canonical: br.ok.core.stkobjects.AccessEventDetection.supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: type
    :canonical: br.ok.core.stkobjects.AccessEventDetection.type
    :type: EventDetection

    Get the type of event detection (e.g., with or without subsampling).


Method detail
-------------

.. py:method:: is_type_supported(self, event_detection: EventDetection) -> bool
    :canonical: br.ok.core.stkobjects.AccessEventDetection.is_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **event_detection** : :obj:`~EventDetection`


    :Returns:

        :obj:`~bool`

.. py:method:: set_type(self, event_detection: EventDetection) -> None
    :canonical: br.ok.core.stkobjects.AccessEventDetection.set_type

    Set the event detection type.

    :Parameters:

        **event_detection** : :obj:`~EventDetection`


    :Returns:

        :obj:`~None`




