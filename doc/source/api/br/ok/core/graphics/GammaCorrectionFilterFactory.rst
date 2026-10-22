GammaCorrectionFilterFactory
============================

.. py:class:: br.ok.core.graphics.GammaCorrectionFilterFactory

   Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

.. py:currentmodule:: GammaCorrectionFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.GammaCorrectionFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.ok.core.graphics.GammaCorrectionFilterFactory.initialize_with_gamma`
              - Initialize a new instance with the specified gamma.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import GammaCorrectionFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> GammaCorrectionFilter
    :canonical: br.ok.core.graphics.GammaCorrectionFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~GammaCorrectionFilter`

.. py:method:: initialize_with_gamma(self, gamma: float) -> GammaCorrectionFilter
    :canonical: br.ok.core.graphics.GammaCorrectionFilterFactory.initialize_with_gamma

    Initialize a new instance with the specified gamma.

    :Parameters:

        **gamma** : :obj:`~float`


    :Returns:

        :obj:`~GammaCorrectionFilter`

