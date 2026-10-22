VectorPrimitive
===============

.. py:class:: br.ok.core.graphics.VectorPrimitive

   Bases: :py:class:`~br.ok.core.graphics.IPrimitive`

   Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

.. py:currentmodule:: VectorPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.display_label`
              - Get or set whether the vector's label is displayed.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.display_lines`
              - Get or set whether persistence lines are displayed.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.display_magnitude`
              - Get or set whether the vector's magnitude is displayed.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.display_ra_dec`
              - Get or set whether the vector's RA-Dec is displayed.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.display_sweep`
              - Get or set whether the persistence sweep (triangles) is displayed.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.display_trace`
              - Get or set whether the persistence trace (points) is displayed.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.fade_persistence`
              - Get or set whether the persistence path should fade over time.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.label`
              - Get or set the user-defined label.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.length`
              - Get or set the vector's source-to-arrow-tip length.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.lighting`
              - Get or set whether the primitive is lit.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.persistence_duration`
              - Get or set the maximum duration of the persistence path.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.persistence_width`
              - Get or set persistence point/line width.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.true_scale`
              - Get or set whether vector's 'true scale' length (based on how the primitive was created) should be used.
            * - :py:attr:`~br.ok.core.graphics.VectorPrimitive.width`
              - Get or set the vector's width in pixels. As the camera distances changes from this primitive, the geometry will autoscale to maintain this thickness.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import VectorPrimitive


Property detail
---------------

.. py:property:: display_label
    :canonical: br.ok.core.graphics.VectorPrimitive.display_label
    :type: bool

    Get or set whether the vector's label is displayed.

.. py:property:: display_lines
    :canonical: br.ok.core.graphics.VectorPrimitive.display_lines
    :type: bool

    Get or set whether persistence lines are displayed.

.. py:property:: display_magnitude
    :canonical: br.ok.core.graphics.VectorPrimitive.display_magnitude
    :type: bool

    Get or set whether the vector's magnitude is displayed.

.. py:property:: display_ra_dec
    :canonical: br.ok.core.graphics.VectorPrimitive.display_ra_dec
    :type: bool

    Get or set whether the vector's RA-Dec is displayed.

.. py:property:: display_sweep
    :canonical: br.ok.core.graphics.VectorPrimitive.display_sweep
    :type: bool

    Get or set whether the persistence sweep (triangles) is displayed.

.. py:property:: display_trace
    :canonical: br.ok.core.graphics.VectorPrimitive.display_trace
    :type: bool

    Get or set whether the persistence trace (points) is displayed.

.. py:property:: fade_persistence
    :canonical: br.ok.core.graphics.VectorPrimitive.fade_persistence
    :type: bool

    Get or set whether the persistence path should fade over time.

.. py:property:: label
    :canonical: br.ok.core.graphics.VectorPrimitive.label
    :type: str

    Get or set the user-defined label.

.. py:property:: length
    :canonical: br.ok.core.graphics.VectorPrimitive.length
    :type: float

    Get or set the vector's source-to-arrow-tip length.

.. py:property:: lighting
    :canonical: br.ok.core.graphics.VectorPrimitive.lighting
    :type: bool

    Get or set whether the primitive is lit.

.. py:property:: persistence_duration
    :canonical: br.ok.core.graphics.VectorPrimitive.persistence_duration
    :type: float

    Get or set the maximum duration of the persistence path.

.. py:property:: persistence_width
    :canonical: br.ok.core.graphics.VectorPrimitive.persistence_width
    :type: float

    Get or set persistence point/line width.

.. py:property:: true_scale
    :canonical: br.ok.core.graphics.VectorPrimitive.true_scale
    :type: bool

    Get or set whether vector's 'true scale' length (based on how the primitive was created) should be used.

.. py:property:: width
    :canonical: br.ok.core.graphics.VectorPrimitive.width
    :type: float

    Get or set the vector's width in pixels. As the camera distances changes from this primitive, the geometry will autoscale to maintain this thickness.


