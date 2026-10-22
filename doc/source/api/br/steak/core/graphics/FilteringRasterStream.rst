FilteringRasterStream
=====================

.. py:class:: br.steak.core.graphics.FilteringRasterStream

   Bases: :py:class:`~br.steak.core.graphics.IRasterStream`, :py:class:`~br.steak.core.graphics.IRaster`

   A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

.. py:currentmodule:: FilteringRasterStream

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.FilteringRasterStream.filter`
              - Get the raster filter that will be applied to the raster stream on each update.
            * - :py:attr:`~br.steak.core.graphics.FilteringRasterStream.stream`
              - Get the raster stream that will have the raster filter applied on each update.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import FilteringRasterStream


Property detail
---------------

.. py:property:: filter
    :canonical: br.steak.core.graphics.FilteringRasterStream.filter
    :type: IRasterFilter

    Get the raster filter that will be applied to the raster stream on each update.

.. py:property:: stream
    :canonical: br.steak.core.graphics.FilteringRasterStream.stream
    :type: IRasterStream

    Get the raster stream that will have the raster filter applied on each update.


