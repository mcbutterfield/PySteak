LaunchVehicleGraphics
=====================

.. py:class:: br.ok.core.stkobjects.LaunchVehicleGraphics

   2D Graphics for a launch vehicle.

.. py:currentmodule:: LaunchVehicleGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.set_attributes_type`
              - Set the 2D Graphics attributes type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.attributes`
              - Get the launch vehicle's 2D Graphics attributes.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.attributes_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.attributes_type`
              - Get the 2D Graphics attributes type: basic, access intervals, custom intervals, or real time.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.elevation_contours`
              - Get the launch vehicle's 2D elevation contour properties.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.ground_ellipses`
              - Get the launch vehicle's 2D ground ellipses properties.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.label_name`
              - The user-specified name to use as a label for the launch vehicle.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.lighting`
              - Get the launch vehicle's 2D lighting properties.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.pass_data`
              - Get the launch vehicle's 2D trajectory properties.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.range_contours`
              - Get the launch vehicle's 2D range contour properties.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.resolution`
              - Get the launch vehicle's 2D resolution properties.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.saa`
              - Get the vehicle's South Atlantic Anomaly Contour properties.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.show_graphics`
              - Specify whether graphics attributes of the launch vehicle are visible.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.swath`
              - Get the launch vehicle's 2D swath properties.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.use_instance_name`
              - Opt whether to use the instance name as the label.
            * - :py:attr:`~br.ok.core.stkobjects.LaunchVehicleGraphics.use_instance_name_label`
              - Specify whether to use the name of the launch vehicle (as shown in the Object Browser) as its label.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import LaunchVehicleGraphics


Property detail
---------------

.. py:property:: attributes
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.attributes
    :type: IVehicleGraphics2DAttributes

    Get the launch vehicle's 2D Graphics attributes.

.. py:property:: attributes_supported_types
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.attributes_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attributes_type
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.attributes_type
    :type: VehicleGraphics2DAttributeType

    Get the 2D Graphics attributes type: basic, access intervals, custom intervals, or real time.

.. py:property:: elevation_contours
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.elevation_contours
    :type: VehicleGraphics2DElevationContours

    Get the launch vehicle's 2D elevation contour properties.

.. py:property:: ground_ellipses
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.ground_ellipses
    :type: VehicleGraphics2DGroundEllipsesCollection

    Get the launch vehicle's 2D ground ellipses properties.

.. py:property:: label_name
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.label_name
    :type: str

    The user-specified name to use as a label for the launch vehicle.

.. py:property:: label_notes
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: lighting
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.lighting
    :type: VehicleGraphics2DLighting

    Get the launch vehicle's 2D lighting properties.

.. py:property:: pass_data
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.pass_data
    :type: VehicleGraphics2DTrajectoryPassData

    Get the launch vehicle's 2D trajectory properties.

.. py:property:: radar_cross_section
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Get the radar cross section graphics interface.

.. py:property:: range_contours
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.range_contours
    :type: Graphics2DRangeContours

    Get the launch vehicle's 2D range contour properties.

.. py:property:: resolution
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.resolution
    :type: VehicleGraphics2DTrajectoryResolution

    Get the launch vehicle's 2D resolution properties.

.. py:property:: saa
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.saa
    :type: VehicleGraphics2DSAA

    Get the vehicle's South Atlantic Anomaly Contour properties.

.. py:property:: show_graphics
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the launch vehicle are visible.

.. py:property:: swath
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.swath
    :type: VehicleGraphics2DSwath

    Get the launch vehicle's 2D swath properties.

.. py:property:: use_instance_name
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.use_instance_name
    :type: bool

    Opt whether to use the instance name as the label.

.. py:property:: use_instance_name_label
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.use_instance_name_label
    :type: bool

    Specify whether to use the name of the launch vehicle (as shown in the Object Browser) as its label.


Method detail
-------------






.. py:method:: is_attributes_type_supported(self, attributes: VehicleGraphics2DAttributeType) -> bool
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics2DAttributeType`


    :Returns:

        :obj:`~bool`












.. py:method:: set_attributes_type(self, attributes: VehicleGraphics2DAttributeType) -> None
    :canonical: br.ok.core.stkobjects.LaunchVehicleGraphics.set_attributes_type

    Set the 2D Graphics attributes type.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics2DAttributeType`


    :Returns:

        :obj:`~None`






