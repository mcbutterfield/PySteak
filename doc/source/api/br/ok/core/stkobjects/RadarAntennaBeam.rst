RadarAntennaBeam
================

.. py:class:: br.ok.core.stkobjects.RadarAntennaBeam

   Class defining a radar antenna beam.

.. py:currentmodule:: RadarAntennaBeam

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.set_activity_type`
              - Set the activity type.
            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.set_pointing_strategy_type`
              - Set the current pointing strategy type.
            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.set_waveform_selection_strategy`
              - Set the current waveform selection strategy.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.activity`
              - Get the activity.
            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.beamwidth`
              - Get or set the antenna beamwidth.
            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.gain`
              - Get or set the antenna mainlobe gain.
            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.identifier`
              - Get or set the antenna beam identifier.
            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.pointing_strategy`
              - Get the pointing strategy.
            * - :py:attr:`~br.ok.core.stkobjects.RadarAntennaBeam.waveform_selection_strategy`
              - Get the waveform selection strategy.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarAntennaBeam


Property detail
---------------

.. py:property:: activity
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.activity
    :type: IRadarActivity

    Get the activity.

.. py:property:: beamwidth
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.beamwidth
    :type: float

    Get or set the antenna beamwidth.

.. py:property:: gain
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.gain
    :type: float

    Get or set the antenna mainlobe gain.

.. py:property:: identifier
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.identifier
    :type: str

    Get or set the antenna beam identifier.

.. py:property:: pointing_strategy
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.pointing_strategy
    :type: IPointingStrategy

    Get the pointing strategy.

.. py:property:: waveform_selection_strategy
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.waveform_selection_strategy
    :type: IWaveformSelectionStrategy

    Get the waveform selection strategy.


Method detail
-------------









.. py:method:: set_activity_type(self, activity_type: RadarActivityType) -> None
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.set_activity_type

    Set the activity type.

    :Parameters:

        **activity_type** : :obj:`~RadarActivityType`


    :Returns:

        :obj:`~None`

.. py:method:: set_pointing_strategy_type(self, value: PointingStrategyType) -> None
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.set_pointing_strategy_type

    Set the current pointing strategy type.

    :Parameters:

        **value** : :obj:`~PointingStrategyType`


    :Returns:

        :obj:`~None`

.. py:method:: set_waveform_selection_strategy(self, value: WaveformSelectionStrategyType) -> None
    :canonical: br.ok.core.stkobjects.RadarAntennaBeam.set_waveform_selection_strategy

    Set the current waveform selection strategy.

    :Parameters:

        **value** : :obj:`~WaveformSelectionStrategyType`


    :Returns:

        :obj:`~None`


