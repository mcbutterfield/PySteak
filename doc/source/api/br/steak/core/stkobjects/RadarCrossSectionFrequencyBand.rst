RadarCrossSectionFrequencyBand
==============================

.. py:class:: br.steak.core.stkobjects.RadarCrossSectionFrequencyBand

   Class defining a inheritable radar cross section frequency band.

.. py:currentmodule:: RadarCrossSectionFrequencyBand

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.set_compute_strategy`
              - Set the current compute strategy by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.compute_strategy`
              - Get the current compute strategy.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.maximum_frequency`
              - Get or set the frequency band maximum frequency.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.minimum_frequency`
              - Get or set the frequency band minimum frequency.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.supported_compute_strategies`
              - Get an array of supported compute strategy names.
            * - :py:attr:`~br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.swerling_case`
              - Get or set the band Swerling case.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RadarCrossSectionFrequencyBand


Property detail
---------------

.. py:property:: compute_strategy
    :canonical: br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.compute_strategy
    :type: IRadarCrossSectionComputeStrategy

    Get the current compute strategy.

.. py:property:: maximum_frequency
    :canonical: br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.maximum_frequency
    :type: float

    Get or set the frequency band maximum frequency.

.. py:property:: minimum_frequency
    :canonical: br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.minimum_frequency
    :type: float

    Get or set the frequency band minimum frequency.

.. py:property:: supported_compute_strategies
    :canonical: br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.supported_compute_strategies
    :type: list

    Get an array of supported compute strategy names.

.. py:property:: swerling_case
    :canonical: br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.swerling_case
    :type: RadarSwerlingCase

    Get or set the band Swerling case.


Method detail
-------------





.. py:method:: set_compute_strategy(self, compute_strategy_name: str) -> None
    :canonical: br.steak.core.stkobjects.RadarCrossSectionFrequencyBand.set_compute_strategy

    Set the current compute strategy by name.

    :Parameters:

        **compute_strategy_name** : :obj:`~str`


    :Returns:

        :obj:`~None`




