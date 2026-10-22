SolidTriangulatorResult
=======================

.. py:class:: br.steak.core.graphics.SolidTriangulatorResult

   Bases: :py:class:`~br.steak.core.graphics.ITriangulatorResult`

   The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

.. py:currentmodule:: SolidTriangulatorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.SolidTriangulatorResult.closed`
              - Get whether the solid is closed. For example, a box with six faces is closed. If one face is removed, the box is open.
            * - :py:attr:`~br.steak.core.graphics.SolidTriangulatorResult.outline_indices`
              - Get indices into positions that define the positions outlining the solid. The indices returned consider the three components of a position (x, y, and z) as a single array element...
            * - :py:attr:`~br.steak.core.graphics.SolidTriangulatorResult.outline_polyline_type`
              - Get the polyline type of outline indices and outline positions.
            * - :py:attr:`~br.steak.core.graphics.SolidTriangulatorResult.outline_positions`
              - Get the positions outlining the solid. Three array elements (in the order x, y, z) constitute one position.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import SolidTriangulatorResult


Property detail
---------------

.. py:property:: closed
    :canonical: br.steak.core.graphics.SolidTriangulatorResult.closed
    :type: bool

    Get whether the solid is closed. For example, a box with six faces is closed. If one face is removed, the box is open.

.. py:property:: outline_indices
    :canonical: br.steak.core.graphics.SolidTriangulatorResult.outline_indices
    :type: list

    Get indices into positions that define the positions outlining the solid. The indices returned consider the three components of a position (x, y, and z) as a single array element...

.. py:property:: outline_polyline_type
    :canonical: br.steak.core.graphics.SolidTriangulatorResult.outline_polyline_type
    :type: PolylineType

    Get the polyline type of outline indices and outline positions.

.. py:property:: outline_positions
    :canonical: br.steak.core.graphics.SolidTriangulatorResult.outline_positions
    :type: list

    Get the positions outlining the solid. Three array elements (in the order x, y, z) constitute one position.


