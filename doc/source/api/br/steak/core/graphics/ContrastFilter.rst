ContrastFilter
==============

.. py:class:: br.steak.core.graphics.ContrastFilter

   Bases: :py:class:`~br.steak.core.graphics.IRasterFilter`

   Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

.. py:currentmodule:: ContrastFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.ContrastFilter.adjustment`
              - Get or set the contrast adjustment value for the filter. The value must be between -1 and 1, corresponding to least contrast to most contrast.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import ContrastFilter


Property detail
---------------

.. py:property:: adjustment
    :canonical: br.steak.core.graphics.ContrastFilter.adjustment
    :type: float

    Get or set the contrast adjustment value for the filter. The value must be between -1 and 1, corresponding to least contrast to most contrast.


