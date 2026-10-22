VehicleGraphics3DGeoBox
=======================

.. py:class:: br.steak.core.stkobjects.VehicleGraphics3DGeoBox

   Geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

.. py:currentmodule:: VehicleGraphics3DGeoBox

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DGeoBox.reposition`
              - Reposition the geostationary box.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DGeoBox.color`
              - Color of the lines defining the plane.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DGeoBox.east_west`
              - Angular length of the plane from East to West. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DGeoBox.longitude`
              - Center longitude of the plane at the initial condition of the satellite at epoch. Uses Longitude Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DGeoBox.north_south`
              - Angular length of the plane from North to South. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DGeoBox.radius`
              - Get or set the radius from the center of the Earth to the center of the plane. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DGeoBox.show_graphics`
              - Opt whether to show the plane.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleGraphics3DGeoBox


Property detail
---------------

.. py:property:: color
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DGeoBox.color
    :type: Color

    Color of the lines defining the plane.

.. py:property:: east_west
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DGeoBox.east_west
    :type: float

    Angular length of the plane from East to West. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DGeoBox.longitude
    :type: float

    Center longitude of the plane at the initial condition of the satellite at epoch. Uses Longitude Dimension.

.. py:property:: north_south
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DGeoBox.north_south
    :type: float

    Angular length of the plane from North to South. Uses Angle Dimension.

.. py:property:: radius
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DGeoBox.radius
    :type: float

    Get or set the radius from the center of the Earth to the center of the plane. Uses Distance Dimension.

.. py:property:: show_graphics
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DGeoBox.show_graphics
    :type: bool

    Opt whether to show the plane.


Method detail
-------------













.. py:method:: reposition(self) -> None
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DGeoBox.reposition

    Reposition the geostationary box.

    :Returns:

        :obj:`~None`

