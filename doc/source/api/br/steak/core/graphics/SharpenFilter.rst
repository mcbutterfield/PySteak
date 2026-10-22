SharpenFilter
=============

.. py:class:: br.steak.core.graphics.SharpenFilter

   Bases: :py:class:`~br.steak.core.graphics.IConvolutionFilter`, :py:class:`~br.steak.core.graphics.IRasterFilter`

   Apply a convolution filter to increase the sharpness of the source raster.

.. py:currentmodule:: SharpenFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.SharpenFilter.method`
              - Get or set the method used to sharpen the source raster.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import SharpenFilter


Property detail
---------------

.. py:property:: method
    :canonical: br.steak.core.graphics.SharpenFilter.method
    :type: RasterSharpenMethod

    Get or set the method used to sharpen the source raster.


