TargetGraphics
==============

.. py:class:: br.steak.core.stkobjects.TargetGraphics

   Bases: :py:class:`~br.steak.core.stkobjects.IGroundLocationGraphics`

   Class defining 2D Graphics for a Target object.

.. py:currentmodule:: TargetGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.az_el_mask`
              - The graphics az-el mask properties for the facility, place or target.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.color`
              - The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.contours`
              - The range contours properties for the facility, place or target.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.inherit_from_scenario`
              - Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility, place or target.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.label_color`
              - The color in which the label for the object is displayed.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.label_name`
              - Use a user-specified name as the label for the facility, place or target. This does not have to correspond to the name of the object in the Object Browser.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.marker_color`
              - The color in which the marker for the object is displayed.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.marker_style`
              - The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.show_graphics`
              - Specify whether graphics attributes of the target are visible.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.show_label`
              - Display the label for the facility, place or target.
            * - :py:attr:`~br.steak.core.stkobjects.TargetGraphics.use_instance_name_label`
              - Use the name of the object as the label for the facility, place or target.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import TargetGraphics


Property detail
---------------

.. py:property:: az_el_mask
    :canonical: br.steak.core.stkobjects.TargetGraphics.az_el_mask
    :type: BasicAzElMask

    The graphics az-el mask properties for the facility, place or target.

.. py:property:: color
    :canonical: br.steak.core.stkobjects.TargetGraphics.color
    :type: Color

    The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.

.. py:property:: contours
    :canonical: br.steak.core.stkobjects.TargetGraphics.contours
    :type: Graphics2DRangeContours

    The range contours properties for the facility, place or target.

.. py:property:: inherit_from_scenario
    :canonical: br.steak.core.stkobjects.TargetGraphics.inherit_from_scenario
    :type: bool

    Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility, place or target.

.. py:property:: label_color
    :canonical: br.steak.core.stkobjects.TargetGraphics.label_color
    :type: Color

    The color in which the label for the object is displayed.

.. py:property:: label_name
    :canonical: br.steak.core.stkobjects.TargetGraphics.label_name
    :type: str

    Use a user-specified name as the label for the facility, place or target. This does not have to correspond to the name of the object in the Object Browser.

.. py:property:: label_notes
    :canonical: br.steak.core.stkobjects.TargetGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_color
    :canonical: br.steak.core.stkobjects.TargetGraphics.marker_color
    :type: Color

    The color in which the marker for the object is displayed.

.. py:property:: marker_style
    :canonical: br.steak.core.stkobjects.TargetGraphics.marker_style
    :type: str

    The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.

.. py:property:: radar_cross_section
    :canonical: br.steak.core.stkobjects.TargetGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Get the radar cross section graphics interface.

.. py:property:: show_graphics
    :canonical: br.steak.core.stkobjects.TargetGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the target are visible.

.. py:property:: show_label
    :canonical: br.steak.core.stkobjects.TargetGraphics.show_label
    :type: bool

    Display the label for the facility, place or target.

.. py:property:: use_instance_name_label
    :canonical: br.steak.core.stkobjects.TargetGraphics.use_instance_name_label
    :type: bool

    Use the name of the object as the label for the facility, place or target.


