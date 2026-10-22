IRaster
=======

.. py:class:: br.ok.core.graphics.IRaster

   A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

.. py:currentmodule:: IRaster

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.IRaster.apply`
              - Apply a raster filter to the raster and returns a new raster with the results of the filtering. The current raster is not modified.
            * - :py:attr:`~br.ok.core.graphics.IRaster.apply_in_place`
              - Apply a raster filter to the raster. The current raster will contain the results of the filtering.
            * - :py:attr:`~br.ok.core.graphics.IRaster.copy_from_raster`
              - Copy the data associated with the given raster into this raster.
            * - :py:attr:`~br.ok.core.graphics.IRaster.extract_band`
              - Extract the band of raster data associated with the given raster band.
            * - :py:attr:`~br.ok.core.graphics.IRaster.extract_band_from_raster_format`
              - Extract the bands of raster data associated with the given raster format.
            * - :py:attr:`~br.ok.core.graphics.IRaster.flip`
              - Flips the raster along the given axis.
            * - :py:attr:`~br.ok.core.graphics.IRaster.rotate`
              - Rotate the raster by the given angle.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.IRaster.attributes`
              - Get the raster attributes that define the raster data.
            * - :py:attr:`~br.ok.core.graphics.IRaster.height`
              - Get the height of the raster in pixels.
            * - :py:attr:`~br.ok.core.graphics.IRaster.width`
              - Get the width of the raster in pixels.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import IRaster


Property detail
---------------

.. py:property:: attributes
    :canonical: br.ok.core.graphics.IRaster.attributes
    :type: RasterAttributes

    Get the raster attributes that define the raster data.

.. py:property:: height
    :canonical: br.ok.core.graphics.IRaster.height
    :type: int

    Get the height of the raster in pixels.

.. py:property:: width
    :canonical: br.ok.core.graphics.IRaster.width
    :type: int

    Get the width of the raster in pixels.


Method detail
-------------

.. py:method:: apply(self, filter: IRasterFilter) -> IRaster
    :canonical: br.ok.core.graphics.IRaster.apply

    Apply a raster filter to the raster and returns a new raster with the results of the filtering. The current raster is not modified.

    :Parameters:

        **filter** : :obj:`~IRasterFilter`


    :Returns:

        :obj:`~IRaster`

.. py:method:: apply_in_place(self, filter: IRasterFilter) -> None
    :canonical: br.ok.core.graphics.IRaster.apply_in_place

    Apply a raster filter to the raster. The current raster will contain the results of the filtering.

    :Parameters:

        **filter** : :obj:`~IRasterFilter`


    :Returns:

        :obj:`~None`


.. py:method:: copy_from_raster(self, raster: IRaster) -> None
    :canonical: br.ok.core.graphics.IRaster.copy_from_raster

    Copy the data associated with the given raster into this raster.

    :Parameters:

        **raster** : :obj:`~IRaster`


    :Returns:

        :obj:`~None`

.. py:method:: extract_band(self, band: RasterBand) -> IRaster
    :canonical: br.ok.core.graphics.IRaster.extract_band

    Extract the band of raster data associated with the given raster band.

    :Parameters:

        **band** : :obj:`~RasterBand`


    :Returns:

        :obj:`~IRaster`

.. py:method:: extract_band_from_raster_format(self, format: RasterFormat) -> IRaster
    :canonical: br.ok.core.graphics.IRaster.extract_band_from_raster_format

    Extract the bands of raster data associated with the given raster format.

    :Parameters:

        **format** : :obj:`~RasterFormat`


    :Returns:

        :obj:`~IRaster`

.. py:method:: flip(self, axis: RasterFlipAxis) -> None
    :canonical: br.ok.core.graphics.IRaster.flip

    Flips the raster along the given axis.

    :Parameters:

        **axis** : :obj:`~RasterFlipAxis`


    :Returns:

        :obj:`~None`


.. py:method:: rotate(self, angle: float) -> None
    :canonical: br.ok.core.graphics.IRaster.rotate

    Rotate the raster by the given angle.

    :Parameters:

        **angle** : :obj:`~float`


    :Returns:

        :obj:`~None`


