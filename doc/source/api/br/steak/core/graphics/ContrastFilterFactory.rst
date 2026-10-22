ContrastFilterFactory
=====================

.. py:class:: br.steak.core.graphics.ContrastFilterFactory

   Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

.. py:currentmodule:: ContrastFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.ContrastFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.steak.core.graphics.ContrastFilterFactory.initialize_with_adjustment`
              - Initialize a new instance with the adjustment to contrast.


Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import ContrastFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> ContrastFilter
    :canonical: br.steak.core.graphics.ContrastFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~ContrastFilter`

.. py:method:: initialize_with_adjustment(self, adjustment: float) -> ContrastFilter
    :canonical: br.steak.core.graphics.ContrastFilterFactory.initialize_with_adjustment

    Initialize a new instance with the adjustment to contrast.

    :Parameters:

        **adjustment** : :obj:`~float`


    :Returns:

        :obj:`~ContrastFilter`

