RotateFilterFactory
===================

.. py:class:: br.ok.core.graphics.RotateFilterFactory

   Rotate the source raster clockwise by the specified angle.

.. py:currentmodule:: RotateFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.RotateFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~br.ok.core.graphics.RotateFilterFactory.initialize_with_angle`
              - Initialize a new instance with a counterclockwise rotation angle.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import RotateFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> RotateFilter
    :canonical: br.ok.core.graphics.RotateFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~RotateFilter`

.. py:method:: initialize_with_angle(self, rotate_angle: float) -> RotateFilter
    :canonical: br.ok.core.graphics.RotateFilterFactory.initialize_with_angle

    Initialize a new instance with a counterclockwise rotation angle.

    :Parameters:

        **rotate_angle** : :obj:`~float`


    :Returns:

        :obj:`~RotateFilter`

