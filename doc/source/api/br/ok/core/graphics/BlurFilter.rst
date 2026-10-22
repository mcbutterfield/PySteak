BlurFilter
==========

.. py:class:: br.ok.core.graphics.BlurFilter

   Bases: :py:class:`~br.ok.core.graphics.IConvolutionFilter`, :py:class:`~br.ok.core.graphics.IRasterFilter`

   Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

.. py:currentmodule:: BlurFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.BlurFilter.method`
              - Get or set the method used to blur the source raster.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import BlurFilter


Property detail
---------------

.. py:property:: method
    :canonical: br.ok.core.graphics.BlurFilter.method
    :type: BlurMethod

    Get or set the method used to blur the source raster.


