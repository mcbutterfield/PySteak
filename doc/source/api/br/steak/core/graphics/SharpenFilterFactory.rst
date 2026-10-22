SharpenFilterFactory
====================

.. py:class:: br.steak.core.graphics.SharpenFilterFactory

   Apply a convolution filter to increase the sharpness of the source raster.

.. py:currentmodule:: SharpenFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.SharpenFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.steak.core.graphics.SharpenFilterFactory.initialize_with_method`
              - Initialize a new instance with the specified sharpen method.


Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import SharpenFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> SharpenFilter
    :canonical: br.steak.core.graphics.SharpenFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~SharpenFilter`

.. py:method:: initialize_with_method(self, method: RasterSharpenMethod) -> SharpenFilter
    :canonical: br.steak.core.graphics.SharpenFilterFactory.initialize_with_method

    Initialize a new instance with the specified sharpen method.

    :Parameters:

        **method** : :obj:`~RasterSharpenMethod`


    :Returns:

        :obj:`~SharpenFilter`

