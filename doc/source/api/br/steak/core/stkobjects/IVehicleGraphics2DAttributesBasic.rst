IVehicleGraphics2DAttributesBasic
=================================

.. py:class:: br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic

   Bases: IVehicleGraphics2DAttributes

   Basic 2D Graphics Attributes for a vehicle.

.. py:currentmodule:: IVehicleGraphics2DAttributesBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.color`
              - Color in which vehicle marker, label and tracks are displayed.
            * - :py:attr:`~br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.inherit`
              - Inherit certain 2D graphics settings from the scenario level.
            * - :py:attr:`~br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.line`
              - Get the line display properties for the vehicle.
            * - :py:attr:`~br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.marker_style`
              - Style of marker used to represent vehicle.
            * - :py:attr:`~br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.show_graphics`
              - Show 2D Graphics for the vehicle.
            * - :py:attr:`~br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.show_label`
              - Opt whether to display the vehicle's label.


Examples
--------

Set 2D Graphics display properties

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Change the line width, style, color and marker

    graphics = satellite.graphics
    graphics.set_attributes_type(VehicleGraphics2DAttributeType.BASIC)
    attributes = graphics.attributes
    attributes.inherit = False
    attributes.line.width = LineWidth.WIDTH4
    attributes.line.style = LineStyle.LONG_DASH
    attributes.color = Colors.Lime
    if os.name == "nt":
        installPath = r"C:\Program Files\AGI\STK_ODTK 13"
    else:
        installPath = os.environ["STK_INSTALL_DIR"]
    attributes.marker_style = os.path.join(installPath, "STKData", "Pixmaps", "MarkersWin", "m010Satellite.bmp")


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import IVehicleGraphics2DAttributesBasic


Property detail
---------------

.. py:property:: color
    :canonical: br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.color
    :type: Color

    Color in which vehicle marker, label and tracks are displayed.

.. py:property:: inherit
    :canonical: br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.inherit
    :type: bool

    Inherit certain 2D graphics settings from the scenario level.

.. py:property:: line
    :canonical: br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.line
    :type: VehicleGraphics2DLine

    Get the line display properties for the vehicle.

.. py:property:: marker_style
    :canonical: br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.marker_style
    :type: str

    Style of marker used to represent vehicle.

.. py:property:: show_graphics
    :canonical: br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.show_graphics
    :type: bool

    Show 2D Graphics for the vehicle.

.. py:property:: show_label
    :canonical: br.steak.core.stkobjects.IVehicleGraphics2DAttributesBasic.show_label
    :type: bool

    Opt whether to display the vehicle's label.


