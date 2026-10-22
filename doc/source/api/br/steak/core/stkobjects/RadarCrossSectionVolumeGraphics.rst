RadarCrossSectionVolumeGraphics
===============================

.. py:class:: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics

   Class defining 3D Volume Graphics properties of radar cross section.

.. py:currentmodule:: RadarCrossSectionVolumeGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.set_number_of_points`
              - Set the azimuth/elevation ranges and number of points.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.set_resolution`
              - Set the azimuth/elevation ranges and resolution.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_number_of_points`
              - Get the number of azimuth points.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_resolution`
              - Get the azimuth resolution.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_start`
              - Get the azimuth start value.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_stop`
              - Get the azimuth stop value.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.color_method`
              - Color method for contours (color ramp or explicit).
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_number_of_points`
              - Get the number of elevation points.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_resolution`
              - Get the elevation resolution.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_start`
              - Get the elevation start value.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_stop`
              - Get the elevation stop value.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.levels`
              - Get the collection of volume levels.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.minimum_displayed_rcs`
              - Get or set the minimum displayed radar cross section value.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.relative_to_maximum`
              - Get or set the contours value represents the gain value relative to the maximum.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.scale`
              - Get or set the scale value.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.show`
              - Opt whether to display volume graphics for the radar cross section.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.start_color`
              - Get or set the color ramp start color.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.stop_color`
              - Get or set the color ramp stop color.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.wireframe`
              - Enable the ability to view the volume as a wireframe.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RadarCrossSectionVolumeGraphics


Property detail
---------------

.. py:property:: azimuth_number_of_points
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_number_of_points
    :type: int

    Get the number of azimuth points.

.. py:property:: azimuth_resolution
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_resolution
    :type: float

    Get the azimuth resolution.

.. py:property:: azimuth_start
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_start
    :type: float

    Get the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.azimuth_stop
    :type: float

    Get the azimuth stop value.

.. py:property:: color_method
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.color_method
    :type: FigureOfMeritGraphics2DColorMethod

    Color method for contours (color ramp or explicit).

.. py:property:: elevation_number_of_points
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_number_of_points
    :type: int

    Get the number of elevation points.

.. py:property:: elevation_resolution
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_resolution
    :type: float

    Get the elevation resolution.

.. py:property:: elevation_start
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_start
    :type: float

    Get the elevation start value.

.. py:property:: elevation_stop
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.elevation_stop
    :type: float

    Get the elevation stop value.

.. py:property:: levels
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.levels
    :type: RadarCrossSectionVolumeLevelCollection

    Get the collection of volume levels.

.. py:property:: minimum_displayed_rcs
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.minimum_displayed_rcs
    :type: float

    Get or set the minimum displayed radar cross section value.

.. py:property:: relative_to_maximum
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.relative_to_maximum
    :type: bool

    Get or set the contours value represents the gain value relative to the maximum.

.. py:property:: scale
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.scale
    :type: float

    Get or set the scale value.

.. py:property:: show
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.show
    :type: bool

    Opt whether to display volume graphics for the radar cross section.

.. py:property:: start_color
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.start_color
    :type: Color

    Get or set the color ramp start color.

.. py:property:: stop_color
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.stop_color
    :type: Color

    Get or set the color ramp stop color.

.. py:property:: wireframe
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.wireframe
    :type: bool

    Enable the ability to view the volume as a wireframe.


Method detail
-------------


















.. py:method:: set_number_of_points(self, azimuth_start: float, azimuth_stop: float, azimuth_num_points: int, elevation_start: float, elevation_stop: float, elevation_num_points: int) -> None
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.set_number_of_points

    Set the azimuth/elevation ranges and number of points.

    :Parameters:

        **azimuth_start** : :obj:`~float`

        **azimuth_stop** : :obj:`~float`

        **azimuth_num_points** : :obj:`~int`

        **elevation_start** : :obj:`~float`

        **elevation_stop** : :obj:`~float`

        **elevation_num_points** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: set_resolution(self, azimuth_start: float, azimuth_stop: float, azimuth_resolution: float, elevation_start: float, elevation_stop: float, elevation_resolution: float) -> None
    :canonical: br.steak.core.stkobjects.RadarCrossSectionVolumeGraphics.set_resolution

    Set the azimuth/elevation ranges and resolution.

    :Parameters:

        **azimuth_start** : :obj:`~float`

        **azimuth_stop** : :obj:`~float`

        **azimuth_resolution** : :obj:`~float`

        **elevation_start** : :obj:`~float`

        **elevation_stop** : :obj:`~float`

        **elevation_resolution** : :obj:`~float`


    :Returns:

        :obj:`~None`









