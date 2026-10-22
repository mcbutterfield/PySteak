VehicleGraphics2DTimeEventTypeMarker
====================================

.. py:class:: br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker

   Bases: :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DTimeEventType`

   2D Graphics time event: marker type.

.. py:currentmodule:: VehicleGraphics2DTimeEventTypeMarker

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.color`
              - Marker color.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.event_interval`
              - Event interval.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.marker_style`
              - Marker style.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.unique_identifer`
              - Get or set the Unique ID is a unique identifier for each time event. The default is TimeEvent<number>. The unique ID is required when modifying time event data using the Graphics TimeEvent Connect command.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGraphics2DTimeEventTypeMarker


Property detail
---------------

.. py:property:: color
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.color
    :type: Color

    Marker color.

.. py:property:: event_interval
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.event_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Event interval.

.. py:property:: marker_style
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.marker_style
    :type: str

    Marker style.

.. py:property:: unique_identifer
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.unique_identifer
    :type: str

    Get or set the Unique ID is a unique identifier for each time event. The default is TimeEvent<number>. The unique ID is required when modifying time event data using the Graphics TimeEvent Connect command.


