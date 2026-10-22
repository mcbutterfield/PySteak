IOverlay
========

.. py:class:: br.steak.core.graphics.IOverlay

   A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

.. py:currentmodule:: IOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.IOverlay.bring_to_front`
              - Brings the overlay to the front of the z-order, so it is on top of all other overlays with the same parent.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.control_to_overlay`
              - Transform a given position, specified relative to the overall globe control, into coordinates relative to this overlay...
            * - :py:attr:`~br.steak.core.graphics.IOverlay.overlay_to_control`
              - Transform a given position, specified relative to the overlay, into coordinates relative to the overall globe control...
            * - :py:attr:`~br.steak.core.graphics.IOverlay.send_to_back`
              - Send the overlay to the back of the z-order, so it is underneath all other overlays with the same parent.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.IOverlay.border_color`
              - Get or set the overlay's border color. By default, the border color is white. However, also by default, the overlay has a border size of 0.0 so the border is not displayed.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.border_size`
              - Get or set the size of the overlay's border. By default, this is 0.0 so the border is not displayed.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.border_translucency`
              - Get or set the translucency of the overlay border. Translucency is a value between 0.0 and 1.0, where 0.0 is completely opaque and 1.0 is completely transparent.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.bounds`
              - Get the bounds of the overlay relative to its parent. The array contains the properties defining the bounds in the order left x location, top y location, width, height.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.clip_to_parent`
              - Get or set a value indicating whether or not the overlay will be clipped by the bounds of its parent. If this property is <see langword='false' />, part of this overlay may be visible outside of its parent's bounds.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.color`
              - Get or set the overlay's color. By default, the overlay is white.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.control_bounds`
              - Get the bounds of the overlay in coordinates relative to the overall globe control. The array contains the properties defining the bounds in the order left x location, top y location, width, height.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.control_position`
              - Get the position of the overlay in coordinates relative to the overall globe control. The array represents the position of the overlay and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.control_size`
              - Get the size of the overlay in coordinates relative to the overall globe control. The elements are in the order width, height, width screen overlay unit, height screen overlay unit.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.display`
              - Get or set if this overlay and the collection of overlays that are contained within this overlay should be rendered.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.display_condition`
              - Get or set the display condition that determines if the overlay should be rendered. Both this and display must evaluate to true for the overlay to be rendered.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.flip_x`
              - Get or set whether the overlay will be flipped along its X axis.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.flip_y`
              - Get or set whether the overlay will be flipped along its Y axis.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.height`
              - Get or set the height of the overlay. The unit in which the height is defined is specified by the height unit property.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.height_unit`
              - Get or set the unit of the height property.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.maximum_size`
              - Get or set the maximum size of the overlay. The overlay will never be larger than this size, even if the overlay's size is specified as a percentage of its parent and its parent is very large...
            * - :py:attr:`~br.steak.core.graphics.IOverlay.minimum_size`
              - Get or set the minimum size of the overlay. The overlay will never be smaller than this size, even if the overlay's size is specified as a percentage of its parent and its parent is very small...
            * - :py:attr:`~br.steak.core.graphics.IOverlay.origin`
              - Get or set the origin from which the overlay's position is defined. By default, the value of this property is bottom left...
            * - :py:attr:`~br.steak.core.graphics.IOverlay.overlays`
              - Get the collection of overlays that are contained within this overlay.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.padding`
              - Get or set the padding surrounding the overlays that are contained within this overlay. The array contains the components of the padding arranged in the order left, top, right, bottom.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.parent`
              - Get the overlay's parent. This may be another overlay if this overlay was added to that overlay's overlays collection. Or, it may be the screen overlay manager if this overlay was added to the scene manager's screen overlays collection.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.picking_enabled`
              - Get or set a value indicating whether or not picking on the overlay is enabled. If picking is disabled, this overlay will never show up in the result of PickScreenOverlay, even if it occupies the specified pick position.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.pinning_origin`
              - Get or set the origin of the pinning position property, relative to the overlay...
            * - :py:attr:`~br.steak.core.graphics.IOverlay.pinning_position`
              - Get or set the pinning position of the overlay, relative to the overlay, which determines the point on the overlay that corresponds to the position property. The array represents the pinning position of the overlay and has a size of 4...
            * - :py:attr:`~br.steak.core.graphics.IOverlay.position`
              - Get or set the position of the overlay relative to its parent. The array represents the position of the overlay and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.rotation_angle`
              - Get or set the counter-clockwise rotation of the overlay. The overlay is rotated around the point specified by the rotation point property.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.rotation_point`
              - Get or set the point that the overlay is rotated around when the rotation angle property has a value other than 0.0. The array contains seven elements defining the properties of the rotation point...
            * - :py:attr:`~br.steak.core.graphics.IOverlay.scale`
              - Get or set the fractional value used to scale the overlay's size property. A value greater than 1.0 will make the overlay larger while a value less than 1.0 will make it smaller.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.size`
              - Get or set the size of the overlay. The array elements represent the size of the overlay in the order width, height, width screen overlay unit, height screen overlay unit.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.tag`
              - Get or set custom value associated with this primitive.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.translation_x`
              - Get or set the value with which the overlay will be translated from the X value of the position property.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.translation_y`
              - Get or set the value with which the overlay will be translated from the Y value of the position property.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.translucency`
              - Get or set the overlay's translucency. Translucency is a value between 0.0 and 1.0, where 0.0 is completely opaque and 1.0 is completely transparent.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.width`
              - Get or set the width of the overlay. The unit in which the width is defined is specified by the width unit property.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.width_unit`
              - Get or set the unit of the width property.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.x`
              - Get or set the X position of the overlay relative to its parent. The unit in which the position is defined is specified by the x unit property. The position is measured horizontally from the origin, which is, by default, the lower-left corner.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.x_unit`
              - Get or set the unit of the x property.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.y`
              - Get or set the Y position of the overlay relative to its parent. The unit in which the position is defined is specified by the y unit property. The position is measured vertically from the origin, which is, by default, the lower-left corner.
            * - :py:attr:`~br.steak.core.graphics.IOverlay.y_unit`
              - Get or set the unit of the y property.


Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import IOverlay


Property detail
---------------

.. py:property:: border_color
    :canonical: br.steak.core.graphics.IOverlay.border_color
    :type: Color

    Get or set the overlay's border color. By default, the border color is white. However, also by default, the overlay has a border size of 0.0 so the border is not displayed.

.. py:property:: border_size
    :canonical: br.steak.core.graphics.IOverlay.border_size
    :type: int

    Get or set the size of the overlay's border. By default, this is 0.0 so the border is not displayed.

.. py:property:: border_translucency
    :canonical: br.steak.core.graphics.IOverlay.border_translucency
    :type: float

    Get or set the translucency of the overlay border. Translucency is a value between 0.0 and 1.0, where 0.0 is completely opaque and 1.0 is completely transparent.

.. py:property:: bounds
    :canonical: br.steak.core.graphics.IOverlay.bounds
    :type: list

    Get the bounds of the overlay relative to its parent. The array contains the properties defining the bounds in the order left x location, top y location, width, height.

.. py:property:: clip_to_parent
    :canonical: br.steak.core.graphics.IOverlay.clip_to_parent
    :type: bool

    Get or set a value indicating whether or not the overlay will be clipped by the bounds of its parent. If this property is <see langword='false' />, part of this overlay may be visible outside of its parent's bounds.

.. py:property:: color
    :canonical: br.steak.core.graphics.IOverlay.color
    :type: Color

    Get or set the overlay's color. By default, the overlay is white.

.. py:property:: control_bounds
    :canonical: br.steak.core.graphics.IOverlay.control_bounds
    :type: list

    Get the bounds of the overlay in coordinates relative to the overall globe control. The array contains the properties defining the bounds in the order left x location, top y location, width, height.

.. py:property:: control_position
    :canonical: br.steak.core.graphics.IOverlay.control_position
    :type: list

    Get the position of the overlay in coordinates relative to the overall globe control. The array represents the position of the overlay and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.

.. py:property:: control_size
    :canonical: br.steak.core.graphics.IOverlay.control_size
    :type: list

    Get the size of the overlay in coordinates relative to the overall globe control. The elements are in the order width, height, width screen overlay unit, height screen overlay unit.

.. py:property:: display
    :canonical: br.steak.core.graphics.IOverlay.display
    :type: bool

    Get or set if this overlay and the collection of overlays that are contained within this overlay should be rendered.

.. py:property:: display_condition
    :canonical: br.steak.core.graphics.IOverlay.display_condition
    :type: IDisplayCondition

    Get or set the display condition that determines if the overlay should be rendered. Both this and display must evaluate to true for the overlay to be rendered.

.. py:property:: flip_x
    :canonical: br.steak.core.graphics.IOverlay.flip_x
    :type: bool

    Get or set whether the overlay will be flipped along its X axis.

.. py:property:: flip_y
    :canonical: br.steak.core.graphics.IOverlay.flip_y
    :type: bool

    Get or set whether the overlay will be flipped along its Y axis.

.. py:property:: height
    :canonical: br.steak.core.graphics.IOverlay.height
    :type: float

    Get or set the height of the overlay. The unit in which the height is defined is specified by the height unit property.

.. py:property:: height_unit
    :canonical: br.steak.core.graphics.IOverlay.height_unit
    :type: ScreenOverlayUnit

    Get or set the unit of the height property.

.. py:property:: maximum_size
    :canonical: br.steak.core.graphics.IOverlay.maximum_size
    :type: list

    Get or set the maximum size of the overlay. The overlay will never be larger than this size, even if the overlay's size is specified as a percentage of its parent and its parent is very large...

.. py:property:: minimum_size
    :canonical: br.steak.core.graphics.IOverlay.minimum_size
    :type: list

    Get or set the minimum size of the overlay. The overlay will never be smaller than this size, even if the overlay's size is specified as a percentage of its parent and its parent is very small...

.. py:property:: origin
    :canonical: br.steak.core.graphics.IOverlay.origin
    :type: ScreenOverlayOrigin

    Get or set the origin from which the overlay's position is defined. By default, the value of this property is bottom left...

.. py:property:: overlays
    :canonical: br.steak.core.graphics.IOverlay.overlays
    :type: ScreenOverlayCollection

    Get the collection of overlays that are contained within this overlay.

.. py:property:: padding
    :canonical: br.steak.core.graphics.IOverlay.padding
    :type: list

    Get or set the padding surrounding the overlays that are contained within this overlay. The array contains the components of the padding arranged in the order left, top, right, bottom.

.. py:property:: parent
    :canonical: br.steak.core.graphics.IOverlay.parent
    :type: IScreenOverlayContainer

    Get the overlay's parent. This may be another overlay if this overlay was added to that overlay's overlays collection. Or, it may be the screen overlay manager if this overlay was added to the scene manager's screen overlays collection.

.. py:property:: picking_enabled
    :canonical: br.steak.core.graphics.IOverlay.picking_enabled
    :type: bool

    Get or set a value indicating whether or not picking on the overlay is enabled. If picking is disabled, this overlay will never show up in the result of PickScreenOverlay, even if it occupies the specified pick position.

.. py:property:: pinning_origin
    :canonical: br.steak.core.graphics.IOverlay.pinning_origin
    :type: ScreenOverlayPinningOrigin

    Get or set the origin of the pinning position property, relative to the overlay...

.. py:property:: pinning_position
    :canonical: br.steak.core.graphics.IOverlay.pinning_position
    :type: list

    Get or set the pinning position of the overlay, relative to the overlay, which determines the point on the overlay that corresponds to the position property. The array represents the pinning position of the overlay and has a size of 4...

.. py:property:: position
    :canonical: br.steak.core.graphics.IOverlay.position
    :type: list

    Get or set the position of the overlay relative to its parent. The array represents the position of the overlay and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.

.. py:property:: rotation_angle
    :canonical: br.steak.core.graphics.IOverlay.rotation_angle
    :type: float

    Get or set the counter-clockwise rotation of the overlay. The overlay is rotated around the point specified by the rotation point property.

.. py:property:: rotation_point
    :canonical: br.steak.core.graphics.IOverlay.rotation_point
    :type: list

    Get or set the point that the overlay is rotated around when the rotation angle property has a value other than 0.0. The array contains seven elements defining the properties of the rotation point...

.. py:property:: scale
    :canonical: br.steak.core.graphics.IOverlay.scale
    :type: float

    Get or set the fractional value used to scale the overlay's size property. A value greater than 1.0 will make the overlay larger while a value less than 1.0 will make it smaller.

.. py:property:: size
    :canonical: br.steak.core.graphics.IOverlay.size
    :type: list

    Get or set the size of the overlay. The array elements represent the size of the overlay in the order width, height, width screen overlay unit, height screen overlay unit.

.. py:property:: tag
    :canonical: br.steak.core.graphics.IOverlay.tag
    :type: typing.Any

    Get or set custom value associated with this primitive.

.. py:property:: translation_x
    :canonical: br.steak.core.graphics.IOverlay.translation_x
    :type: float

    Get or set the value with which the overlay will be translated from the X value of the position property.

.. py:property:: translation_y
    :canonical: br.steak.core.graphics.IOverlay.translation_y
    :type: float

    Get or set the value with which the overlay will be translated from the Y value of the position property.

.. py:property:: translucency
    :canonical: br.steak.core.graphics.IOverlay.translucency
    :type: float

    Get or set the overlay's translucency. Translucency is a value between 0.0 and 1.0, where 0.0 is completely opaque and 1.0 is completely transparent.

.. py:property:: width
    :canonical: br.steak.core.graphics.IOverlay.width
    :type: float

    Get or set the width of the overlay. The unit in which the width is defined is specified by the width unit property.

.. py:property:: width_unit
    :canonical: br.steak.core.graphics.IOverlay.width_unit
    :type: ScreenOverlayUnit

    Get or set the unit of the width property.

.. py:property:: x
    :canonical: br.steak.core.graphics.IOverlay.x
    :type: float

    Get or set the X position of the overlay relative to its parent. The unit in which the position is defined is specified by the x unit property. The position is measured horizontally from the origin, which is, by default, the lower-left corner.

.. py:property:: x_unit
    :canonical: br.steak.core.graphics.IOverlay.x_unit
    :type: ScreenOverlayUnit

    Get or set the unit of the x property.

.. py:property:: y
    :canonical: br.steak.core.graphics.IOverlay.y
    :type: float

    Get or set the Y position of the overlay relative to its parent. The unit in which the position is defined is specified by the y unit property. The position is measured vertically from the origin, which is, by default, the lower-left corner.

.. py:property:: y_unit
    :canonical: br.steak.core.graphics.IOverlay.y_unit
    :type: ScreenOverlayUnit

    Get or set the unit of the y property.


Method detail
-------------








.. py:method:: bring_to_front(self) -> None
    :canonical: br.steak.core.graphics.IOverlay.bring_to_front

    Brings the overlay to the front of the z-order, so it is on top of all other overlays with the same parent.

    :Returns:

        :obj:`~None`








.. py:method:: control_to_overlay(self, x: float, y: float) -> list
    :canonical: br.steak.core.graphics.IOverlay.control_to_overlay

    Transform a given position, specified relative to the overall globe control, into coordinates relative to this overlay...

    :Parameters:

        **x** : :obj:`~float`

        **y** : :obj:`~float`


    :Returns:

        :obj:`~list`



















.. py:method:: overlay_to_control(self, x: float, y: float) -> list
    :canonical: br.steak.core.graphics.IOverlay.overlay_to_control

    Transform a given position, specified relative to the overlay, into coordinates relative to the overall globe control...

    :Parameters:

        **x** : :obj:`~float`

        **y** : :obj:`~float`


    :Returns:

        :obj:`~list`



















.. py:method:: send_to_back(self) -> None
    :canonical: br.steak.core.graphics.IOverlay.send_to_back

    Send the overlay to the back of the z-order, so it is underneath all other overlays with the same parent.

    :Returns:

        :obj:`~None`























