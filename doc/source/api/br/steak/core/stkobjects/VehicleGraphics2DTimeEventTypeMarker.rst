VehicleGraphics2DTimeEventTypeMarker
====================================

.. py:class:: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker

   Bases: :py:class:`~br.steak.core.stkobjects.IVehicleGraphics2DTimeEventType`

   2D Graphics time event: marker type.

.. py:currentmodule:: VehicleGraphics2DTimeEventTypeMarker

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.color`
              - Marker color.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.event_interval`
              - Event interval.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.marker_style`
              - Marker style.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.unique_identifer`
              - Get or set the Unique ID is a unique identifier for each time event. The default is TimeEvent<number>. The unique ID is required when modifying time event data using the Graphics TimeEvent Connect command.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleGraphics2DTimeEventTypeMarker


Property detail
---------------

.. py:property:: color
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.color
    :type: Color

    Marker color.

.. py:property:: event_interval
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.event_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Event interval.

.. py:property:: marker_style
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.marker_style
    :type: str

    Marker style.

.. py:property:: unique_identifer
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.unique_identifer
    :type: str

    Get or set the Unique ID is a unique identifier for each time event. The default is TimeEvent<number>. The unique ID is required when modifying time event data using the Graphics TimeEvent Connect command.


