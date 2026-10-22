GradientDetectFilterFactory
===========================

.. py:class:: br.ok.core.graphics.GradientDetectFilterFactory

   Apply a convolution filter to detect gradients in the source raster.

.. py:currentmodule:: GradientDetectFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.GradientDetectFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.ok.core.graphics.GradientDetectFilterFactory.initialize_with_method`
              - Initialize a new instance with specified gradient detect method.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import GradientDetectFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> GradientDetectFilter
    :canonical: br.ok.core.graphics.GradientDetectFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~GradientDetectFilter`

.. py:method:: initialize_with_method(self, method: GradientDetectMethod) -> GradientDetectFilter
    :canonical: br.ok.core.graphics.GradientDetectFilterFactory.initialize_with_method

    Initialize a new instance with specified gradient detect method.

    :Parameters:

        **method** : :obj:`~GradientDetectMethod`


    :Returns:

        :obj:`~GradientDetectFilter`

