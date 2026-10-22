LevelsFilter
============

.. py:class:: br.ok.core.graphics.LevelsFilter

   Bases: :py:class:`~br.ok.core.graphics.IRasterFilter`

   Adjusts the band levels of the source raster linearly.

.. py:currentmodule:: LevelsFilter

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.LevelsFilter.clear_adjustments`
              - Clear the level adjustment values for all bands.
            * - :py:attr:`~br.ok.core.graphics.LevelsFilter.set_level_adjustment`
              - Set the linear level adjustment value for the given raster band. Both negative and positive values are accepted.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import LevelsFilter



Method detail
-------------

.. py:method:: clear_adjustments(self) -> None
    :canonical: br.ok.core.graphics.LevelsFilter.clear_adjustments

    Clear the level adjustment values for all bands.

    :Returns:

        :obj:`~None`

.. py:method:: set_level_adjustment(self, band: RasterBand, adjustment: int) -> None
    :canonical: br.ok.core.graphics.LevelsFilter.set_level_adjustment

    Set the linear level adjustment value for the given raster band. Both negative and positive values are accepted.

    :Parameters:

        **band** : :obj:`~RasterBand`

        **adjustment** : :obj:`~int`


    :Returns:

        :obj:`~None`

