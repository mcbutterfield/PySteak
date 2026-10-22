AlphaFromRasterFilterFactory
============================

.. py:class:: br.steak.core.graphics.AlphaFromRasterFilterFactory

   Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

.. py:currentmodule:: AlphaFromRasterFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.AlphaFromRasterFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.steak.core.graphics.AlphaFromRasterFilterFactory.initialize_with_raster`
              - Initialize a new instance with the raster that the source raster will use to derive an alpha band.


Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import AlphaFromRasterFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> AlphaFromRasterFilter
    :canonical: br.steak.core.graphics.AlphaFromRasterFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~AlphaFromRasterFilter`

.. py:method:: initialize_with_raster(self, raster: IRaster) -> AlphaFromRasterFilter
    :canonical: br.steak.core.graphics.AlphaFromRasterFilterFactory.initialize_with_raster

    Initialize a new instance with the raster that the source raster will use to derive an alpha band.

    :Parameters:

        **raster** : :obj:`~IRaster`


    :Returns:

        :obj:`~AlphaFromRasterFilter`

