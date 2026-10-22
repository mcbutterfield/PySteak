VehicleWaypointAltitudeReferenceTerrain
=======================================

.. py:class:: br.steak.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain

   Bases: :py:class:`~br.steak.core.stkobjects.IVehicleWaypointAltitudeReference`

   Terrain altitude reference.

.. py:currentmodule:: VehicleWaypointAltitudeReferenceTerrain

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain.granularity`
              - Define the distance between sampling points along a vehicle route, used when waypoint altitudes are referenced to terrain. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain.interpolation_method`
              - Get or set the terrain interpolation method to be used to define the height of the vehicle with respect to terrain data.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleWaypointAltitudeReferenceTerrain


Property detail
---------------

.. py:property:: granularity
    :canonical: br.steak.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain.granularity
    :type: float

    Define the distance between sampling points along a vehicle route, used when waypoint altitudes are referenced to terrain. Uses Distance Dimension.

.. py:property:: interpolation_method
    :canonical: br.steak.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain.interpolation_method
    :type: VehicleWaypointInterpolationMethod

    Get or set the terrain interpolation method to be used to define the height of the vehicle with respect to terrain data.


