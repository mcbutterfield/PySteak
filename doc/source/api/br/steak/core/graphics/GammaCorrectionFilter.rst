GammaCorrectionFilter
=====================

.. py:class:: br.steak.core.graphics.GammaCorrectionFilter

   Bases: :py:class:`~br.steak.core.graphics.IRasterFilter`

   Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

.. py:currentmodule:: GammaCorrectionFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.GammaCorrectionFilter.gamma`
              - Get or set the gamma value for the filter. The value must be between .2 and 5. The default gamma value is 2.2.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import GammaCorrectionFilter


Property detail
---------------

.. py:property:: gamma
    :canonical: br.steak.core.graphics.GammaCorrectionFilter.gamma
    :type: float

    Get or set the gamma value for the filter. The value must be between .2 and 5. The default gamma value is 2.2.


