SurfaceTriangulatorResult
=========================

.. py:class:: br.steak.core.graphics.SurfaceTriangulatorResult

   Bases: :py:class:`~br.steak.core.graphics.ITriangulatorResult`

   The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

.. py:currentmodule:: SurfaceTriangulatorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.SurfaceTriangulatorResult.boundary_indices`
              - Get indices into positions that define the boundary positions that surround the mesh. The indices returned consider the three components of a position (x, y, and z) as a single array element...
            * - :py:attr:`~br.steak.core.graphics.SurfaceTriangulatorResult.boundary_polyline_type`
              - Get the polyline type of boundary positions.
            * - :py:attr:`~br.steak.core.graphics.SurfaceTriangulatorResult.boundary_positions`
              - Get the boundary positions that surround the mesh. Three array elements (in the order x, y, z) constitute one position.
            * - :py:attr:`~br.steak.core.graphics.SurfaceTriangulatorResult.boundary_positions_winding_order`
              - Get the winding order of boundary positions.
            * - :py:attr:`~br.steak.core.graphics.SurfaceTriangulatorResult.granularity`
              - Get the granularity used when the triangulation was computed. Lower granularities are more precise but create more triangles.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import SurfaceTriangulatorResult


Property detail
---------------

.. py:property:: boundary_indices
    :canonical: br.steak.core.graphics.SurfaceTriangulatorResult.boundary_indices
    :type: list

    Get indices into positions that define the boundary positions that surround the mesh. The indices returned consider the three components of a position (x, y, and z) as a single array element...

.. py:property:: boundary_polyline_type
    :canonical: br.steak.core.graphics.SurfaceTriangulatorResult.boundary_polyline_type
    :type: PolylineType

    Get the polyline type of boundary positions.

.. py:property:: boundary_positions
    :canonical: br.steak.core.graphics.SurfaceTriangulatorResult.boundary_positions
    :type: list

    Get the boundary positions that surround the mesh. Three array elements (in the order x, y, z) constitute one position.

.. py:property:: boundary_positions_winding_order
    :canonical: br.steak.core.graphics.SurfaceTriangulatorResult.boundary_positions_winding_order
    :type: WindingOrder

    Get the winding order of boundary positions.

.. py:property:: granularity
    :canonical: br.steak.core.graphics.SurfaceTriangulatorResult.granularity
    :type: float

    Get the granularity used when the triangulation was computed. Lower granularities are more precise but create more triangles.


