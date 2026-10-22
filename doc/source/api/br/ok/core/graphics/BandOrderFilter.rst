BandOrderFilter
===============

.. py:class:: br.ok.core.graphics.BandOrderFilter

   Bases: :py:class:`~br.ok.core.graphics.IRasterFilter`

   Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

.. py:currentmodule:: BandOrderFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.BandOrderFilter.band_order`
              - Get or set the raster format indicating the desired order of the bands in the source raster.
            * - :py:attr:`~br.ok.core.graphics.BandOrderFilter.maintain_raster_format`
              - Get or set a value indicating whether to maintain the source raster's format after the filter is applied. When true, the source raster's format is maintained after swizzling.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import BandOrderFilter


Property detail
---------------

.. py:property:: band_order
    :canonical: br.ok.core.graphics.BandOrderFilter.band_order
    :type: RasterFormat

    Get or set the raster format indicating the desired order of the bands in the source raster.

.. py:property:: maintain_raster_format
    :canonical: br.ok.core.graphics.BandOrderFilter.maintain_raster_format
    :type: bool

    Get or set a value indicating whether to maintain the source raster's format after the filter is applied. When true, the source raster's format is maintained after swizzling.


