VehicleGraphics2DTimeEventTypeText
==================================

.. py:class:: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText

   Bases: :py:class:`~br.steak.core.stkobjects.IVehicleGraphics2DTimeEventType`

   2D Graphics time event: text type.

.. py:currentmodule:: VehicleGraphics2DTimeEventTypeText

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.is_offset_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.set_offset_type`
              - Offset direction: left or right.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.color`
              - Text color.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.event_interval`
              - Event interval.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_pixels`
              - Offsets the position of the text to the right or the left of the ground track.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_type`
              - Offset direction: left or right.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.text`
              - Text.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.unique_identifer`
              - User-defined unique ID.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleGraphics2DTimeEventTypeText


Property detail
---------------

.. py:property:: color
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.color
    :type: Color

    Text color.

.. py:property:: event_interval
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.event_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Event interval.

.. py:property:: offset_pixels
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_pixels
    :type: int

    Offsets the position of the text to the right or the left of the ground track.

.. py:property:: offset_supported_types
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: offset_type
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_type
    :type: VehicleGraphics2DOffset

    Offset direction: left or right.

.. py:property:: text
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.text
    :type: str

    Text.

.. py:property:: unique_identifer
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.unique_identifer
    :type: str

    User-defined unique ID.


Method detail
-------------




.. py:method:: is_offset_type_supported(self, offset: VehicleGraphics2DOffset) -> bool
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.is_offset_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **offset** : :obj:`~VehicleGraphics2DOffset`


    :Returns:

        :obj:`~bool`





.. py:method:: set_offset_type(self, offset: VehicleGraphics2DOffset) -> None
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeText.set_offset_type

    Offset direction: left or right.

    :Parameters:

        **offset** : :obj:`~VehicleGraphics2DOffset`


    :Returns:

        :obj:`~None`





