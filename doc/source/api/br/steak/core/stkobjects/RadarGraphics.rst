RadarGraphics
=============

.. py:class:: br.steak.core.stkobjects.RadarGraphics

   Class defining 2D Graphics properties of a Radar.

.. py:currentmodule:: RadarGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarGraphics.access`
              - Get the radar's access graphics interface.
            * - :py:attr:`~br.steak.core.stkobjects.RadarGraphics.boresight_color`
              - The color in which boresight graphics display.
            * - :py:attr:`~br.steak.core.stkobjects.RadarGraphics.boresight_marker_style`
              - The marker style used to represent the boresight graphically.
            * - :py:attr:`~br.steak.core.stkobjects.RadarGraphics.contour_graphics`
              - Get the radar's antenna contour graphics interface.
            * - :py:attr:`~br.steak.core.stkobjects.RadarGraphics.multipath`
              - Get the radar's multipath graphics interface.
            * - :py:attr:`~br.steak.core.stkobjects.RadarGraphics.show`
              - Opt whether to display graphics for the radar object.
            * - :py:attr:`~br.steak.core.stkobjects.RadarGraphics.show_boresight`
              - Opt whether to display boresight graphics for the radar's antenna.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RadarGraphics


Property detail
---------------

.. py:property:: access
    :canonical: br.steak.core.stkobjects.RadarGraphics.access
    :type: RadarAccessGraphics

    Get the radar's access graphics interface.

.. py:property:: boresight_color
    :canonical: br.steak.core.stkobjects.RadarGraphics.boresight_color
    :type: Color

    The color in which boresight graphics display.

.. py:property:: boresight_marker_style
    :canonical: br.steak.core.stkobjects.RadarGraphics.boresight_marker_style
    :type: str

    The marker style used to represent the boresight graphically.

.. py:property:: contour_graphics
    :canonical: br.steak.core.stkobjects.RadarGraphics.contour_graphics
    :type: AntennaContourGraphics

    Get the radar's antenna contour graphics interface.

.. py:property:: multipath
    :canonical: br.steak.core.stkobjects.RadarGraphics.multipath
    :type: RadarMultipathGraphics

    Get the radar's multipath graphics interface.

.. py:property:: show
    :canonical: br.steak.core.stkobjects.RadarGraphics.show
    :type: bool

    Opt whether to display graphics for the radar object.

.. py:property:: show_boresight
    :canonical: br.steak.core.stkobjects.RadarGraphics.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the radar's antenna.


