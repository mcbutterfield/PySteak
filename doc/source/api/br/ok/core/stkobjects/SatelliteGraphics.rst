SatelliteGraphics
=================

.. py:class:: br.ok.core.stkobjects.SatelliteGraphics

   Satellite 2D Graphics properties.

.. py:currentmodule:: SatelliteGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.set_attributes_type`
              - Set the attributes type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.attributes`
              - Get the satellite's 2D Graphics Attributes.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.attributes_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.attributes_type`
              - Type of 2D Graphics attributes: basic, access intervals or custom intervals.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.elevation_contours`
              - Get the satellite's Elevation Contours properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.ground_ellipses`
              - Get the satellite's Ground Ellipses properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.ground_track_central_body_display`
              - Get the ground track display central bodies.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.label_name`
              - The user-specified name to use as a label for the satellite.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.lighting`
              - Get the satellite's Lighting properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.pass_data`
              - Get the leading/trailing ground track and orbit settings of the satellite's Pass properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.passes`
              - Get the pass display settings of the satellite's Pass properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.range_contours`
              - Get the satellite's Range Contours properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.resolution`
              - Get the path resolution settings of the satellite's Pass properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.saa`
              - Get the satellite's South Atlantic Anomaly Contour properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.show_graphics`
              - Specify whether graphics attributes of the satellite are visible.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.swath`
              - Get the satellite's Swath properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.time_events`
              - Get the satellite's TimeEvents properties.
            * - :py:attr:`~br.ok.core.stkobjects.SatelliteGraphics.use_instance_name_label`
              - Specify whether to use the name of the satellite (as shown in the Object Browser) as its label.



Examples
--------

Change the Display Label of the vehicle

.. code-block:: python

    # Satellite satellite: Satellite object
    satellite.graphics.use_instance_name_label = False
    satellite.graphics.label_name = "Python Satellite"


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import SatelliteGraphics


Property detail
---------------

.. py:property:: attributes
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.attributes
    :type: IVehicleGraphics2DAttributes

    Get the satellite's 2D Graphics Attributes.

.. py:property:: attributes_supported_types
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.attributes_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attributes_type
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.attributes_type
    :type: VehicleGraphics2DAttributeType

    Type of 2D Graphics attributes: basic, access intervals or custom intervals.

.. py:property:: elevation_contours
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.elevation_contours
    :type: VehicleGraphics2DElevationContours

    Get the satellite's Elevation Contours properties.

.. py:property:: ground_ellipses
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.ground_ellipses
    :type: VehicleGraphics2DGroundEllipsesCollection

    Get the satellite's Ground Ellipses properties.

.. py:property:: ground_track_central_body_display
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.ground_track_central_body_display
    :type: VehicleCentralBodies

    Get the ground track display central bodies.

.. py:property:: label_name
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.label_name
    :type: str

    The user-specified name to use as a label for the satellite.

.. py:property:: label_notes
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: lighting
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.lighting
    :type: VehicleGraphics2DLighting

    Get the satellite's Lighting properties.

.. py:property:: pass_data
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.pass_data
    :type: VehicleGraphics2DOrbitPassData

    Get the leading/trailing ground track and orbit settings of the satellite's Pass properties.

.. py:property:: passes
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.passes
    :type: VehicleGraphics2DPasses

    Get the pass display settings of the satellite's Pass properties.

.. py:property:: radar_cross_section
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Get the radar cross section graphics interface.

.. py:property:: range_contours
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.range_contours
    :type: Graphics2DRangeContours

    Get the satellite's Range Contours properties.

.. py:property:: resolution
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.resolution
    :type: VehicleGraphics2DPassResolution

    Get the path resolution settings of the satellite's Pass properties.

.. py:property:: saa
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.saa
    :type: VehicleGraphics2DSAA

    Get the satellite's South Atlantic Anomaly Contour properties.

.. py:property:: show_graphics
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the satellite are visible.

.. py:property:: swath
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.swath
    :type: VehicleGraphics2DSwath

    Get the satellite's Swath properties.

.. py:property:: time_events
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.time_events
    :type: VehicleGraphics2DTimeEventsCollection

    Get the satellite's TimeEvents properties.

.. py:property:: use_instance_name_label
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.use_instance_name_label
    :type: bool

    Specify whether to use the name of the satellite (as shown in the Object Browser) as its label.


Method detail
-------------







.. py:method:: is_attributes_type_supported(self, attributes: VehicleGraphics2DAttributeType) -> bool
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics2DAttributeType`


    :Returns:

        :obj:`~bool`













.. py:method:: set_attributes_type(self, attributes: VehicleGraphics2DAttributeType) -> None
    :canonical: br.ok.core.stkobjects.SatelliteGraphics.set_attributes_type

    Set the attributes type.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics2DAttributeType`


    :Returns:

        :obj:`~None`





