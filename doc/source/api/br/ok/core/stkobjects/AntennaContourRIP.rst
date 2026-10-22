AntennaContourRIP
=================

.. py:class:: br.ok.core.stkobjects.AntennaContourRIP

   Bases: :py:class:`~br.ok.core.stkobjects.IAntennaContour`

   Class defining an antenna rip contour properties.

.. py:currentmodule:: AntennaContourRIP

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AntennaContourRIP.set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AntennaContourRIP.azimuth_resolution`
              - Get the azimuth resolution.
            * - :py:attr:`~br.ok.core.stkobjects.AntennaContourRIP.elevation_resolution`
              - Get the elevation resolution.
            * - :py:attr:`~br.ok.core.stkobjects.AntennaContourRIP.maximum_elevation_angle`
              - Get the maximum elevation.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AntennaContourRIP


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: br.ok.core.stkobjects.AntennaContourRIP.azimuth_resolution
    :type: typing.Any

    Get the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: br.ok.core.stkobjects.AntennaContourRIP.elevation_resolution
    :type: typing.Any

    Get the elevation resolution.

.. py:property:: maximum_elevation_angle
    :canonical: br.ok.core.stkobjects.AntennaContourRIP.maximum_elevation_angle
    :type: typing.Any

    Get the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuth_resolution: float, elevation_resolution: float, max_elevation: float) -> None
    :canonical: br.ok.core.stkobjects.AntennaContourRIP.set_resolution

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

        **azimuth_resolution** : :obj:`~float`

        **elevation_resolution** : :obj:`~float`

        **max_elevation** : :obj:`~float`


    :Returns:

        :obj:`~None`

