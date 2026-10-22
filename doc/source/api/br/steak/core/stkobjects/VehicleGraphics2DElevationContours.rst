VehicleGraphics2DElevationContours
==================================

.. py:class:: br.steak.core.stkobjects.VehicleGraphics2DElevationContours

   General settings regarding display of elevation contours.

.. py:currentmodule:: VehicleGraphics2DElevationContours

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DElevationContours.elevations`
              - Collection of Levels.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DElevationContours.fill_style`
              - Get or set the type of fill to display.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DElevationContours.fill_translucency`
              - Specify the fill translucency percentage of the area within the contours. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DElevationContours.number_of_decimal_digits`
              - Number of decimal digits. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DElevationContours.show_filled_contours`
              - Opt whether to display a fill over the area within the contours.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics2DElevationContours.show_graphics`
              - Opt whether to display elevation contours.



Examples
--------

Set 2D/3D Elevation Contours

.. code-block:: python

    # Satellite satellite: Satellite object
    # Set the contours in the 2D properties
    contours = satellite.graphics.elevation_contours
    contours.show_graphics = True
    contours.number_of_decimal_digits = 0
    contours.elevations.add_level_range(0, 90, 10)  # Min, Max, Step
    # Turn the contours on in the 3D properties
    satellite.graphics_3d.elevation_contours.show_graphics = True


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleGraphics2DElevationContours


Property detail
---------------

.. py:property:: elevations
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DElevationContours.elevations
    :type: VehicleGraphics2DElevationsCollection

    Collection of Levels.

.. py:property:: fill_style
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DElevationContours.fill_style
    :type: FillStyle

    Get or set the type of fill to display.

.. py:property:: fill_translucency
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DElevationContours.fill_translucency
    :type: float

    Specify the fill translucency percentage of the area within the contours. Translucency ranges from 0 to 100 percent, where 100 percent is invisible.

.. py:property:: number_of_decimal_digits
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DElevationContours.number_of_decimal_digits
    :type: int

    Number of decimal digits. Dimensionless.

.. py:property:: show_filled_contours
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DElevationContours.show_filled_contours
    :type: bool

    Opt whether to display a fill over the area within the contours.

.. py:property:: show_graphics
    :canonical: br.steak.core.stkobjects.VehicleGraphics2DElevationContours.show_graphics
    :type: bool

    Opt whether to display elevation contours.


