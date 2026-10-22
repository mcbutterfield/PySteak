TerrainNormalSlopeAzimuth
=========================

.. py:class:: br.ok.core.stkobjects.TerrainNormalSlopeAzimuth

   Bases: :py:class:`~br.ok.core.stkobjects.ITerrainNormData`

   Class defining Slope/Azimuth data for the TerrainNormal.

.. py:currentmodule:: TerrainNormalSlopeAzimuth

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.TerrainNormalSlopeAzimuth.azimuth`
              - Specify the Azimuth (measured in an easterly sense from local north) of the normal to local terrain. This may also be thought of as the azimuth of the downhill direction. Uses Longitude Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.TerrainNormalSlopeAzimuth.slope`
              - Specify the Slope of the local terrain, defined as the angle between the normal to the local terrain and local surface normal, where the local surface normal is defined by the reference shape of the globe. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import TerrainNormalSlopeAzimuth


Property detail
---------------

.. py:property:: azimuth
    :canonical: br.ok.core.stkobjects.TerrainNormalSlopeAzimuth.azimuth
    :type: typing.Any

    Specify the Azimuth (measured in an easterly sense from local north) of the normal to local terrain. This may also be thought of as the azimuth of the downhill direction. Uses Longitude Dimension.

.. py:property:: slope
    :canonical: br.ok.core.stkobjects.TerrainNormalSlopeAzimuth.slope
    :type: typing.Any

    Specify the Slope of the local terrain, defined as the angle between the normal to the local terrain and local surface normal, where the local surface normal is defined by the reference shape of the globe. Uses Angle Dimension.


