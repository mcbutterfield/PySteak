MagnificationFilter
===================

.. py:class:: br.ok.core.graphics.MagnificationFilter

   IntEnum


.. py:currentmodule:: MagnificationFilter

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NEAREST`
              - Use the texel that is closest to the center of the pixel being textured. This usually faster than Linear but can produce images with sharper edges.

            * - :py:attr:`~LINEAR`
              - Use the weighted average of the four texels that are closest to the center of the pixel being textured.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import MagnificationFilter


