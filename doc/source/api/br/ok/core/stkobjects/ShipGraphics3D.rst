ShipGraphics3D
==============

.. py:class:: br.ok.core.stkobjects.ShipGraphics3D

   Bases: :py:class:`~br.ok.core.stkobjects.IGreatArcGraphics3D`

   3D Graphics attributes for a ship.

.. py:currentmodule:: ShipGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ShipGraphics3D.drop_lines`
              - Return an interface allowing to configure vehicle's drop lines.
            * - :py:attr:`~br.ok.core.stkobjects.ShipGraphics3D.proximity`
              - Get the ship's 3D proximity properties.
            * - :py:attr:`~br.ok.core.stkobjects.ShipGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~br.ok.core.stkobjects.ShipGraphics3D.vapor_trail`
              - Vapor trail attributes.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ShipGraphics3D


Property detail
---------------

.. py:property:: drop_lines
    :canonical: br.ok.core.stkobjects.ShipGraphics3D.drop_lines
    :type: VehicleGraphics3DRouteDropLines

    Return an interface allowing to configure vehicle's drop lines.

.. py:property:: proximity
    :canonical: br.ok.core.stkobjects.ShipGraphics3D.proximity
    :type: VehicleGraphics3DRouteProximity

    Get the ship's 3D proximity properties.

.. py:property:: radar_cross_section
    :canonical: br.ok.core.stkobjects.ShipGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.

.. py:property:: vapor_trail
    :canonical: br.ok.core.stkobjects.ShipGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.


