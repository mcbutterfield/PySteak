FlipFilterFactory
=================

.. py:class:: br.steak.core.graphics.FlipFilterFactory

   Flips the source raster along the given flip axis.

.. py:currentmodule:: FlipFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.FlipFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.steak.core.graphics.FlipFilterFactory.initialize_with_flip_axis`
              - Initialize a new instance with the specified flip axis.


Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import FlipFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> FlipFilter
    :canonical: br.steak.core.graphics.FlipFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~FlipFilter`

.. py:method:: initialize_with_flip_axis(self, flip_axis: RasterFlipAxis) -> FlipFilter
    :canonical: br.steak.core.graphics.FlipFilterFactory.initialize_with_flip_axis

    Initialize a new instance with the specified flip axis.

    :Parameters:

        **flip_axis** : :obj:`~RasterFlipAxis`


    :Returns:

        :obj:`~FlipFilter`

