AccessGraphics
==============

.. py:class:: br.ok.core.stkobjects.AccessGraphics

   Class defining 2D Graphics for Access.

.. py:currentmodule:: AccessGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AccessGraphics.color_mode`
              - Color mode for access graphics, either use the object colors or a single, custom color.
            * - :py:attr:`~br.ok.core.stkobjects.AccessGraphics.custom_color`
              - Color for all access graphics, used when color mode is set to custom.
            * - :py:attr:`~br.ok.core.stkobjects.AccessGraphics.inherit`
              - Specify whether the Access graphics inherit from the Scenario. Otherwise they can be set locally for this object.
            * - :py:attr:`~br.ok.core.stkobjects.AccessGraphics.line_style`
              - Line style of lines between objects during access periods in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.ok.core.stkobjects.AccessGraphics.line_width`
              - Line width of lines between objects during access periods in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.ok.core.stkobjects.AccessGraphics.show_animation_highlight_graphics_2d`
              - Specify whether an Animate Highlight appears in the 2D Graphics window during access periods. The Animate Highlight is a box drawn around each object participating in the access.
            * - :py:attr:`~br.ok.core.stkobjects.AccessGraphics.show_line`
              - Specify whether a line appears between objects during access periods in the 2D and 3D Graphics windows.
            * - :py:attr:`~br.ok.core.stkobjects.AccessGraphics.static_graphics_2d`
              - Specify whether a Static Highlight appears in the 2D Graphics window. The Static Highlight is a thick line overlaying portions of a vehicle's ground track during access periods.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AccessGraphics


Property detail
---------------

.. py:property:: color_mode
    :canonical: br.ok.core.stkobjects.AccessGraphics.color_mode
    :type: IvColorMode

    Color mode for access graphics, either use the object colors or a single, custom color.

.. py:property:: custom_color
    :canonical: br.ok.core.stkobjects.AccessGraphics.custom_color
    :type: Color

    Color for all access graphics, used when color mode is set to custom.

.. py:property:: inherit
    :canonical: br.ok.core.stkobjects.AccessGraphics.inherit
    :type: bool

    Specify whether the Access graphics inherit from the Scenario. Otherwise they can be set locally for this object.

.. py:property:: line_style
    :canonical: br.ok.core.stkobjects.AccessGraphics.line_style
    :type: str

    Line style of lines between objects during access periods in the 2D and 3D Graphics windows.

.. py:property:: line_width
    :canonical: br.ok.core.stkobjects.AccessGraphics.line_width
    :type: int

    Line width of lines between objects during access periods in the 2D and 3D Graphics windows.

.. py:property:: show_animation_highlight_graphics_2d
    :canonical: br.ok.core.stkobjects.AccessGraphics.show_animation_highlight_graphics_2d
    :type: bool

    Specify whether an Animate Highlight appears in the 2D Graphics window during access periods. The Animate Highlight is a box drawn around each object participating in the access.

.. py:property:: show_line
    :canonical: br.ok.core.stkobjects.AccessGraphics.show_line
    :type: bool

    Specify whether a line appears between objects during access periods in the 2D and 3D Graphics windows.

.. py:property:: static_graphics_2d
    :canonical: br.ok.core.stkobjects.AccessGraphics.static_graphics_2d
    :type: bool

    Specify whether a Static Highlight appears in the 2D Graphics window. The Static Highlight is a thick line overlaying portions of a vehicle's ground track during access periods.


