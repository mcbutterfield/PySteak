AlphaFromRasterFilter
=====================

.. py:class:: br.ok.core.graphics.AlphaFromRasterFilter

   Bases: :py:class:`~br.ok.core.graphics.IRasterFilter`

   Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

.. py:currentmodule:: AlphaFromRasterFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.AlphaFromRasterFilter.raster`
              - Get or set the raster that the source raster will use to derive an alpha band.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import AlphaFromRasterFilter


Property detail
---------------

.. py:property:: raster
    :canonical: br.ok.core.graphics.AlphaFromRasterFilter.raster
    :type: IRaster

    Get or set the raster that the source raster will use to derive an alpha band.


