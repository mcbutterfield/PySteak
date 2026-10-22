VehicleGraphics3DIntervalsElement
=================================

.. py:class:: br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement

   Intervals graphics for covariance pointing contour.

.. py:currentmodule:: VehicleGraphics3DIntervalsElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.color`
              - Get or set the line color.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.line_width`
              - Get or set the line width.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.show_graphics`
              - Opt whether to display the object during the selected time using the selected graphics properties.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.start_time`
              - Time at which the interval begins and the selected graphics display in the 3D window. Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.stop_time`
              - Time at which the interval ends. Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.translucency`
              - Get or set the translucency. Dimensionless.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGraphics3DIntervalsElement


Property detail
---------------

.. py:property:: color
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.color
    :type: Color

    Get or set the line color.

.. py:property:: line_width
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.line_width
    :type: LineWidth

    Get or set the line width.

.. py:property:: show_graphics
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.show_graphics
    :type: bool

    Opt whether to display the object during the selected time using the selected graphics properties.

.. py:property:: start_time
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.start_time
    :type: typing.Any

    Time at which the interval begins and the selected graphics display in the 3D window. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.stop_time
    :type: typing.Any

    Time at which the interval ends. Uses DateFormat Dimension.

.. py:property:: translucency
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement.translucency
    :type: float

    Get or set the translucency. Dimensionless.


