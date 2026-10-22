AxesPrimitive
=============

.. py:class:: br.ok.core.graphics.AxesPrimitive

   Bases: :py:class:`~br.ok.core.graphics.IPrimitive`

   Render an axes in the 3D scene.

.. py:currentmodule:: AxesPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.display_label`
              - Get or set whether the axes' label is displayed.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.display_lines`
              - Get or set whether persistence lines are displayed.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.display_sweep`
              - Get or set whether the persistence sweep (triangles) is displayed.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.display_trace`
              - Get or set whether the persistence trace (points) is displayed.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.fade_persistence`
              - Get or set whether the persistence path should fade over time.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.label`
              - Get or set the axes label.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.length`
              - Get or set the axes' source-to-arrow-tip length.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.lighting`
              - Get or set whether the primitive is lit.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.persistence_duration`
              - Get or set the maximum duration of the persistence path.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.persistence_width`
              - Get or set persistence point/line width.
            * - :py:attr:`~br.ok.core.graphics.AxesPrimitive.width`
              - Get or set the width in pixels. As the camera distances changes from this primitive, the geometry will autoscale to maintain this thickness.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import AxesPrimitive


Property detail
---------------

.. py:property:: display_label
    :canonical: br.ok.core.graphics.AxesPrimitive.display_label
    :type: bool

    Get or set whether the axes' label is displayed.

.. py:property:: display_lines
    :canonical: br.ok.core.graphics.AxesPrimitive.display_lines
    :type: bool

    Get or set whether persistence lines are displayed.

.. py:property:: display_sweep
    :canonical: br.ok.core.graphics.AxesPrimitive.display_sweep
    :type: bool

    Get or set whether the persistence sweep (triangles) is displayed.

.. py:property:: display_trace
    :canonical: br.ok.core.graphics.AxesPrimitive.display_trace
    :type: bool

    Get or set whether the persistence trace (points) is displayed.

.. py:property:: fade_persistence
    :canonical: br.ok.core.graphics.AxesPrimitive.fade_persistence
    :type: bool

    Get or set whether the persistence path should fade over time.

.. py:property:: label
    :canonical: br.ok.core.graphics.AxesPrimitive.label
    :type: str

    Get or set the axes label.

.. py:property:: length
    :canonical: br.ok.core.graphics.AxesPrimitive.length
    :type: float

    Get or set the axes' source-to-arrow-tip length.

.. py:property:: lighting
    :canonical: br.ok.core.graphics.AxesPrimitive.lighting
    :type: bool

    Get or set whether the primitive is lit.

.. py:property:: persistence_duration
    :canonical: br.ok.core.graphics.AxesPrimitive.persistence_duration
    :type: float

    Get or set the maximum duration of the persistence path.

.. py:property:: persistence_width
    :canonical: br.ok.core.graphics.AxesPrimitive.persistence_width
    :type: float

    Get or set persistence point/line width.

.. py:property:: width
    :canonical: br.ok.core.graphics.AxesPrimitive.width
    :type: float

    Get or set the width in pixels. As the camera distances changes from this primitive, the geometry will autoscale to maintain this thickness.


