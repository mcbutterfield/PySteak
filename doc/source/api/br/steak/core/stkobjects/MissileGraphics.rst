MissileGraphics
===============

.. py:class:: br.steak.core.stkobjects.MissileGraphics

   2D Graphics for missiles.

.. py:currentmodule:: MissileGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.set_attributes_type`
              - Set the type of display.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.attributes`
              - Get the 2D Graphics attributes.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.attributes_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.attributes_type`
              - Type of display: basic, during access intervals, during custom intervals, or real time.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.elevation_contours`
              - Get the elevation contours graphics.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.ground_ellipses`
              - Get the ground ellipses graphics.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.label_name`
              - The user-specified name to use as a label for the missile.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.lighting`
              - Get the lighting graphics.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.pass_data`
              - Get the 2D trajectory graphics.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.range_contours`
              - Get the range contour graphics.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.resolution`
              - Get the resolution graphics.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.saa`
              - Get the missile's South Atlantic Anomaly Contour properties.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.show_graphics`
              - Specify whether graphics attributes of the missile are visible.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.swath`
              - Get the swath graphics.
            * - :py:attr:`~br.steak.core.stkobjects.MissileGraphics.use_instance_name_label`
              - Specify whether to use the name of the missile (as shown in the Object Browser) as its label.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import MissileGraphics


Property detail
---------------

.. py:property:: attributes
    :canonical: br.steak.core.stkobjects.MissileGraphics.attributes
    :type: IVehicleGraphics2DAttributes

    Get the 2D Graphics attributes.

.. py:property:: attributes_supported_types
    :canonical: br.steak.core.stkobjects.MissileGraphics.attributes_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attributes_type
    :canonical: br.steak.core.stkobjects.MissileGraphics.attributes_type
    :type: VehicleGraphics2DAttributeType

    Type of display: basic, during access intervals, during custom intervals, or real time.

.. py:property:: elevation_contours
    :canonical: br.steak.core.stkobjects.MissileGraphics.elevation_contours
    :type: VehicleGraphics2DElevationContours

    Get the elevation contours graphics.

.. py:property:: ground_ellipses
    :canonical: br.steak.core.stkobjects.MissileGraphics.ground_ellipses
    :type: VehicleGraphics2DGroundEllipsesCollection

    Get the ground ellipses graphics.

.. py:property:: label_name
    :canonical: br.steak.core.stkobjects.MissileGraphics.label_name
    :type: str

    The user-specified name to use as a label for the missile.

.. py:property:: label_notes
    :canonical: br.steak.core.stkobjects.MissileGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: lighting
    :canonical: br.steak.core.stkobjects.MissileGraphics.lighting
    :type: VehicleGraphics2DLighting

    Get the lighting graphics.

.. py:property:: pass_data
    :canonical: br.steak.core.stkobjects.MissileGraphics.pass_data
    :type: VehicleGraphics2DTrajectoryPassData

    Get the 2D trajectory graphics.

.. py:property:: radar_cross_section
    :canonical: br.steak.core.stkobjects.MissileGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Get the radar cross section graphics interface.

.. py:property:: range_contours
    :canonical: br.steak.core.stkobjects.MissileGraphics.range_contours
    :type: Graphics2DRangeContours

    Get the range contour graphics.

.. py:property:: resolution
    :canonical: br.steak.core.stkobjects.MissileGraphics.resolution
    :type: VehicleGraphics2DTrajectoryResolution

    Get the resolution graphics.

.. py:property:: saa
    :canonical: br.steak.core.stkobjects.MissileGraphics.saa
    :type: VehicleGraphics2DSAA

    Get the missile's South Atlantic Anomaly Contour properties.

.. py:property:: show_graphics
    :canonical: br.steak.core.stkobjects.MissileGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the missile are visible.

.. py:property:: swath
    :canonical: br.steak.core.stkobjects.MissileGraphics.swath
    :type: VehicleGraphics2DSwath

    Get the swath graphics.

.. py:property:: use_instance_name_label
    :canonical: br.steak.core.stkobjects.MissileGraphics.use_instance_name_label
    :type: bool

    Specify whether to use the name of the missile (as shown in the Object Browser) as its label.


Method detail
-------------






.. py:method:: is_attributes_type_supported(self, attributes: VehicleGraphics2DAttributeType) -> bool
    :canonical: br.steak.core.stkobjects.MissileGraphics.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics2DAttributeType`


    :Returns:

        :obj:`~bool`












.. py:method:: set_attributes_type(self, attributes: VehicleGraphics2DAttributeType) -> None
    :canonical: br.steak.core.stkobjects.MissileGraphics.set_attributes_type

    Set the type of display.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics2DAttributeType`


    :Returns:

        :obj:`~None`




