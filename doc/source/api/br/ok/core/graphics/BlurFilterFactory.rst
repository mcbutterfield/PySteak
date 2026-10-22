BlurFilterFactory
=================

.. py:class:: br.ok.core.graphics.BlurFilterFactory

   Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

.. py:currentmodule:: BlurFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.BlurFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.ok.core.graphics.BlurFilterFactory.initialize_with_method`
              - Initialize a new instance with the specified blur method.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import BlurFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> BlurFilter
    :canonical: br.ok.core.graphics.BlurFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~BlurFilter`

.. py:method:: initialize_with_method(self, method: BlurMethod) -> BlurFilter
    :canonical: br.ok.core.graphics.BlurFilterFactory.initialize_with_method

    Initialize a new instance with the specified blur method.

    :Parameters:

        **method** : :obj:`~BlurMethod`


    :Returns:

        :obj:`~BlurFilter`

