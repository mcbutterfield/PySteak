RasterAttributes
================

.. py:class:: br.ok.core.graphics.RasterAttributes

   The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

.. py:currentmodule:: RasterAttributes

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.has_band`
              - Get whether the raster contains the given band.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.byte_length`
              - Get the size of the raster data in bytes.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.format`
              - Get the raster format associated with the attributes.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.height`
              - Get the height of the raster in pixels.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.number_of_bands`
              - Get the number of bands comprising the raster.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.orientation`
              - Get the raster orientation associated with the attributes.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.pixel_aspect_ratio`
              - Get the pixel aspect ratio of the raster.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.row_alignment`
              - Get the row alignment of the raster data in bytes.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.row_stride`
              - Get the stride or scan/row width in bytes of the raster data.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.type`
              - Get the raster type associated with the attributes.
            * - :py:attr:`~br.ok.core.graphics.RasterAttributes.width`
              - Get the width of the raster in pixels.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import RasterAttributes


Property detail
---------------

.. py:property:: byte_length
    :canonical: br.ok.core.graphics.RasterAttributes.byte_length
    :type: int

    Get the size of the raster data in bytes.

.. py:property:: format
    :canonical: br.ok.core.graphics.RasterAttributes.format
    :type: RasterFormat

    Get the raster format associated with the attributes.

.. py:property:: height
    :canonical: br.ok.core.graphics.RasterAttributes.height
    :type: int

    Get the height of the raster in pixels.

.. py:property:: number_of_bands
    :canonical: br.ok.core.graphics.RasterAttributes.number_of_bands
    :type: int

    Get the number of bands comprising the raster.

.. py:property:: orientation
    :canonical: br.ok.core.graphics.RasterAttributes.orientation
    :type: RasterOrientation

    Get the raster orientation associated with the attributes.

.. py:property:: pixel_aspect_ratio
    :canonical: br.ok.core.graphics.RasterAttributes.pixel_aspect_ratio
    :type: float

    Get the pixel aspect ratio of the raster.

.. py:property:: row_alignment
    :canonical: br.ok.core.graphics.RasterAttributes.row_alignment
    :type: int

    Get the row alignment of the raster data in bytes.

.. py:property:: row_stride
    :canonical: br.ok.core.graphics.RasterAttributes.row_stride
    :type: int

    Get the stride or scan/row width in bytes of the raster data.

.. py:property:: type
    :canonical: br.ok.core.graphics.RasterAttributes.type
    :type: RasterType

    Get the raster type associated with the attributes.

.. py:property:: width
    :canonical: br.ok.core.graphics.RasterAttributes.width
    :type: int

    Get the width of the raster in pixels.


Method detail
-------------



.. py:method:: has_band(self, band: RasterBand) -> bool
    :canonical: br.ok.core.graphics.RasterAttributes.has_band

    Get whether the raster contains the given band.

    :Parameters:

        **band** : :obj:`~RasterBand`


    :Returns:

        :obj:`~bool`









