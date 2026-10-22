Graphics3DReferenceAxes
=======================

.. py:class:: br.ok.core.stkobjects.Graphics3DReferenceAxes

   Bases: :py:class:`~br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`, :py:class:`~br.ok.core.stkobjects.IDisplayTime`

   Class defining a set of reference axes (3D Graphics, Vector Geometry Tool).

.. py:currentmodule:: Graphics3DReferenceAxes

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.available_axes`
              - Return an array of available Axes.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.available_points`
              - Return a safearray of available points.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.axes`
              - The name of the axes or system used to define the coordinate frame associated with the selected vector or axis.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.connect`
              - Specify the method used for connecting geometric elements.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.draw_at_central_body`
              - Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.draw_at_point`
              - If selected, the geometric element is drawn at the selected point.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.duration`
              - The length of time during which the geometric element is visible. Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.point`
              - Displays a point at the current animation time.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.show_persistence`
              - Successively displays geometric elements over the specified duration.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.thickness`
              - Thickness of line.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DReferenceAxes.transparent`
              - If selected, earlier occurrences of a geometric element display fade over time so that it is drawn as completely filled at the most recent animation time and fades as the animation moves forward.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Graphics3DReferenceAxes


Property detail
---------------

.. py:property:: available_axes
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.available_axes
    :type: list

    Return an array of available Axes.

.. py:property:: available_points
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.available_points
    :type: list

    Return a safearray of available points.

.. py:property:: axes
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.axes
    :type: str

    The name of the axes or system used to define the coordinate frame associated with the selected vector or axis.

.. py:property:: connect
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.connect
    :type: VectorAxesConnectType

    Specify the method used for connecting geometric elements.

.. py:property:: draw_at_central_body
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.draw_at_central_body
    :type: bool

    Only available for geometric elements relating to objects. If selected, the geometric element is drawn at the central body or object.

.. py:property:: draw_at_point
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.draw_at_point
    :type: bool

    If selected, the geometric element is drawn at the selected point.

.. py:property:: duration
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.duration
    :type: float

    The length of time during which the geometric element is visible. Uses Time Dimension.

.. py:property:: point
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.point
    :type: str

    Displays a point at the current animation time.

.. py:property:: show_persistence
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.show_persistence
    :type: bool

    Successively displays geometric elements over the specified duration.

.. py:property:: thickness
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.thickness
    :type: float

    Thickness of line.

.. py:property:: transparent
    :canonical: br.ok.core.stkobjects.Graphics3DReferenceAxes.transparent
    :type: bool

    If selected, earlier occurrences of a geometric element display fade over time so that it is drawn as completely filled at the most recent animation time and fades as the animation moves forward.


