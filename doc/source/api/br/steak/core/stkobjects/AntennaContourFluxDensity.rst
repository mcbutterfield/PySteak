AntennaContourFluxDensity
=========================

.. py:class:: br.steak.core.stkobjects.AntennaContourFluxDensity

   Bases: :py:class:`~br.steak.core.stkobjects.IAntennaContour`

   Class defining an antenna flux density contour properties.

.. py:currentmodule:: AntennaContourFluxDensity

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AntennaContourFluxDensity.set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AntennaContourFluxDensity.azimuth_resolution`
              - Get the azimuth resolution.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaContourFluxDensity.elevation_resolution`
              - Get the elevation resolution.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaContourFluxDensity.maximum_elevation_angle`
              - Get the maximum elevation.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AntennaContourFluxDensity


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: br.steak.core.stkobjects.AntennaContourFluxDensity.azimuth_resolution
    :type: typing.Any

    Get the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: br.steak.core.stkobjects.AntennaContourFluxDensity.elevation_resolution
    :type: typing.Any

    Get the elevation resolution.

.. py:property:: maximum_elevation_angle
    :canonical: br.steak.core.stkobjects.AntennaContourFluxDensity.maximum_elevation_angle
    :type: typing.Any

    Get the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuth_resolution: float, elevation_resolution: float, max_elevation: float) -> None
    :canonical: br.steak.core.stkobjects.AntennaContourFluxDensity.set_resolution

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

        **azimuth_resolution** : :obj:`~float`

        **elevation_resolution** : :obj:`~float`

        **max_elevation** : :obj:`~float`


    :Returns:

        :obj:`~None`

