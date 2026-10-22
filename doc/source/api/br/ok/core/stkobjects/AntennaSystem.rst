AntennaSystem
=============

.. py:class:: br.ok.core.stkobjects.AntennaSystem

   Class defining an antenna system.

.. py:currentmodule:: AntennaSystem

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AntennaSystem.set_beam_selection_strategy_type`
              - Set the beam selection strategy type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AntennaSystem.antenna_beams`
              - Get the antenna beam collection.
            * - :py:attr:`~br.ok.core.stkobjects.AntennaSystem.beam_selection_strategy`
              - Get the beam selection strategy.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AntennaSystem


Property detail
---------------

.. py:property:: antenna_beams
    :canonical: br.ok.core.stkobjects.AntennaSystem.antenna_beams
    :type: AntennaBeamCollection

    Get the antenna beam collection.

.. py:property:: beam_selection_strategy
    :canonical: br.ok.core.stkobjects.AntennaSystem.beam_selection_strategy
    :type: IAntennaBeamSelectionStrategy

    Get the beam selection strategy.


Method detail
-------------



.. py:method:: set_beam_selection_strategy_type(self, value: BeamSelectionStrategyType) -> None
    :canonical: br.ok.core.stkobjects.AntennaSystem.set_beam_selection_strategy_type

    Set the beam selection strategy type.

    :Parameters:

        **value** : :obj:`~BeamSelectionStrategyType`


    :Returns:

        :obj:`~None`

