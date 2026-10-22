IDrawElementRect
================

.. py:class:: br.steak.core.stkx.IDrawElementRect

   Bases: IDrawElement

   Define a rectangle in control coordinates.

.. py:currentmodule:: IDrawElementRect

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkx.IDrawElementRect.set`
              - Set the rectangle coordinates.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkx.IDrawElementRect.bottom`
              - The y-coordinate of the bottom edge of this rectangle.
            * - :py:attr:`~br.steak.core.stkx.IDrawElementRect.color`
              - Color of the rectangle.
            * - :py:attr:`~br.steak.core.stkx.IDrawElementRect.left`
              - The x-coordinate of the left edge of this rectangle.
            * - :py:attr:`~br.steak.core.stkx.IDrawElementRect.line_style`
              - Specify the style of the line.
            * - :py:attr:`~br.steak.core.stkx.IDrawElementRect.line_width`
              - Specify the width of the line.
            * - :py:attr:`~br.steak.core.stkx.IDrawElementRect.right`
              - The x-coordinate of the right edge of this rectangle.
            * - :py:attr:`~br.steak.core.stkx.IDrawElementRect.top`
              - The y-coordinate of the top edge of this rectangle.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkx import IDrawElementRect


Property detail
---------------

.. py:property:: bottom
    :canonical: br.steak.core.stkx.IDrawElementRect.bottom
    :type: int

    The y-coordinate of the bottom edge of this rectangle.

.. py:property:: color
    :canonical: br.steak.core.stkx.IDrawElementRect.color
    :type: Color

    Color of the rectangle.

.. py:property:: left
    :canonical: br.steak.core.stkx.IDrawElementRect.left
    :type: int

    The x-coordinate of the left edge of this rectangle.

.. py:property:: line_style
    :canonical: br.steak.core.stkx.IDrawElementRect.line_style
    :type: LineStyle

    Specify the style of the line.

.. py:property:: line_width
    :canonical: br.steak.core.stkx.IDrawElementRect.line_width
    :type: float

    Specify the width of the line.

.. py:property:: right
    :canonical: br.steak.core.stkx.IDrawElementRect.right
    :type: int

    The x-coordinate of the right edge of this rectangle.

.. py:property:: top
    :canonical: br.steak.core.stkx.IDrawElementRect.top
    :type: int

    The y-coordinate of the top edge of this rectangle.


Method detail
-------------










.. py:method:: set(self, left: int, top: int, right: int, bottom: int) -> None
    :canonical: br.steak.core.stkx.IDrawElementRect.set

    Set the rectangle coordinates.

    :Parameters:

        **left** : :obj:`~int`

        **top** : :obj:`~int`

        **right** : :obj:`~int`

        **bottom** : :obj:`~int`


    :Returns:

        :obj:`~None`


