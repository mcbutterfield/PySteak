BrightnessFilterFactory
=======================

.. py:class:: br.steak.core.graphics.BrightnessFilterFactory

   Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

.. py:currentmodule:: BrightnessFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.BrightnessFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.steak.core.graphics.BrightnessFilterFactory.initialize_with_adjustment`
              - Initialize a new instance with the adjustment to brightness.


Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import BrightnessFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> BrightnessFilter
    :canonical: br.steak.core.graphics.BrightnessFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~BrightnessFilter`

.. py:method:: initialize_with_adjustment(self, adjustment: float) -> BrightnessFilter
    :canonical: br.steak.core.graphics.BrightnessFilterFactory.initialize_with_adjustment

    Initialize a new instance with the adjustment to brightness.

    :Parameters:

        **adjustment** : :obj:`~float`


    :Returns:

        :obj:`~BrightnessFilter`

