BlurFilter
==========

.. py:class:: br.steak.core.graphics.BlurFilter

   Bases: :py:class:`~br.steak.core.graphics.IConvolutionFilter`, :py:class:`~br.steak.core.graphics.IRasterFilter`

   Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

.. py:currentmodule:: BlurFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.BlurFilter.method`
              - Get or set the method used to blur the source raster.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import BlurFilter


Property detail
---------------

.. py:property:: method
    :canonical: br.steak.core.graphics.BlurFilter.method
    :type: BlurMethod

    Get or set the method used to blur the source raster.


