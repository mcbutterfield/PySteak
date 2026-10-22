IGreatArcGraphics
=================

.. py:class:: br.ok.core.stkobjects.IGreatArcGraphics

   2D Graphics common for all Great Arc Vehicles.

.. py:currentmodule:: IGreatArcGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.set_attributes_type`
              - Set the 2D Graphics attributes type for the vehicle.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.attributes`
              - Get the vehicle's 2D Graphics attributes.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.attributes_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.attributes_type`
              - Get the 2D Graphics attributes type for the vehicle: basic, access intervals, custom intervals, or real time.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.ground_ellipses`
              - Get the vehicle's 2D ground ellipses graphics.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.label_name`
              - The user-specified name to use as a label for the vehicle.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.lighting`
              - Get the vehicle's 2D lighting graphics.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.pass_data`
              - Get the vehicle's 2D route graphics.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.range_contours`
              - Get the vehicle's 2D range contour graphics.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.resolution`
              - Get the vehicle's 2D resolution graphics.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.show_graphics`
              - Specify whether graphics attributes of the vehicle are visible.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.use_instance_name_label`
              - Specify whether to use the name of the vehicle (as shown in the Object Browser) as its label.
            * - :py:attr:`~br.ok.core.stkobjects.IGreatArcGraphics.waypoint_marker`
              - Get the vehicle's 2D waypoint marker graphics.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IGreatArcGraphics


Property detail
---------------

.. py:property:: attributes
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.attributes
    :type: IVehicleGraphics2DAttributes

    Get the vehicle's 2D Graphics attributes.

.. py:property:: attributes_supported_types
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.attributes_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attributes_type
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.attributes_type
    :type: VehicleGraphics2DAttributeType

    Get the 2D Graphics attributes type for the vehicle: basic, access intervals, custom intervals, or real time.

.. py:property:: ground_ellipses
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.ground_ellipses
    :type: VehicleGraphics2DGroundEllipsesCollection

    Get the vehicle's 2D ground ellipses graphics.

.. py:property:: label_name
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.label_name
    :type: str

    The user-specified name to use as a label for the vehicle.

.. py:property:: label_notes
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: lighting
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.lighting
    :type: VehicleGraphics2DLighting

    Get the vehicle's 2D lighting graphics.

.. py:property:: pass_data
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.pass_data
    :type: VehicleGraphics2DRoutePassData

    Get the vehicle's 2D route graphics.

.. py:property:: range_contours
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.range_contours
    :type: Graphics2DRangeContours

    Get the vehicle's 2D range contour graphics.

.. py:property:: resolution
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.resolution
    :type: VehicleGraphics2DRouteResolution

    Get the vehicle's 2D resolution graphics.

.. py:property:: show_graphics
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the vehicle are visible.

.. py:property:: use_instance_name_label
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.use_instance_name_label
    :type: bool

    Specify whether to use the name of the vehicle (as shown in the Object Browser) as its label.

.. py:property:: waypoint_marker
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.waypoint_marker
    :type: VehicleGraphics2DWaypointMarker

    Get the vehicle's 2D waypoint marker graphics.


Method detail
-------------





.. py:method:: is_attributes_type_supported(self, attributes: VehicleGraphics2DAttributeType) -> bool
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics2DAttributeType`


    :Returns:

        :obj:`~bool`










.. py:method:: set_attributes_type(self, attributes: VehicleGraphics2DAttributeType) -> None
    :canonical: br.ok.core.stkobjects.IGreatArcGraphics.set_attributes_type

    Set the 2D Graphics attributes type for the vehicle.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics2DAttributeType`


    :Returns:

        :obj:`~None`




