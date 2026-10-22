PixelSizeDisplayCondition
=========================

.. py:class:: br.ok.core.graphics.PixelSizeDisplayCondition

   Bases: :py:class:`~br.ok.core.graphics.IDisplayCondition`

   Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

.. py:currentmodule:: PixelSizeDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.PixelSizeDisplayCondition.maximum_pixel_size`
              - Get or set the maximum pixel size of the inclusive distance interval. Use Int32.MaxValue to ignore checking the maximum distance.
            * - :py:attr:`~br.ok.core.graphics.PixelSizeDisplayCondition.minimum_pixel_size`
              - Get or set the minimum pixel size of the inclusive distance interval.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import PixelSizeDisplayCondition


Property detail
---------------

.. py:property:: maximum_pixel_size
    :canonical: br.ok.core.graphics.PixelSizeDisplayCondition.maximum_pixel_size
    :type: int

    Get or set the maximum pixel size of the inclusive distance interval. Use Int32.MaxValue to ignore checking the maximum distance.

.. py:property:: minimum_pixel_size
    :canonical: br.ok.core.graphics.PixelSizeDisplayCondition.minimum_pixel_size
    :type: int

    Get or set the minimum pixel size of the inclusive distance interval.


