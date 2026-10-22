RadarModelMultifunction
=======================

.. py:class:: br.ok.core.stkobjects.RadarModelMultifunction

   Bases: :py:class:`~br.ok.core.stkobjects.IRadarModel`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a multifunction radar model.

.. py:currentmodule:: RadarModelMultifunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.set_pointing_strategy_type`
              - Set the current pointing strategy type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.antenna_beams`
              - Get the antenna beams collection.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.clutter`
              - Get the radar clutter settings.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.detection_processing`
              - Get the radar detection processing object.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.jamming`
              - Get the radar jamming.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.location`
              - Get the radar location object.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.pointing_strategy`
              - Get the pointing strategy.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.receiver`
              - Get the radar receiver.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.transmitter`
              - Get the radar transmitter.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMultifunction.waveform_strategy_settings`
              - Get the waveform selection strategy settings.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarModelMultifunction


Property detail
---------------

.. py:property:: antenna_beams
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.antenna_beams
    :type: RadarAntennaBeamCollection

    Get the antenna beams collection.

.. py:property:: clutter
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.clutter
    :type: RadarClutter

    Get the radar clutter settings.

.. py:property:: detection_processing
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.detection_processing
    :type: RadarMultifunctionDetectionProcessing

    Get the radar detection processing object.

.. py:property:: jamming
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.jamming
    :type: RadarJamming

    Get the radar jamming.

.. py:property:: location
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.location
    :type: CommRadCartesianLocation

    Get the radar location object.

.. py:property:: pointing_strategy
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.pointing_strategy
    :type: IPointingStrategy

    Get the pointing strategy.

.. py:property:: receiver
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.receiver
    :type: RadarReceiver

    Get the radar receiver.

.. py:property:: transmitter
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.transmitter
    :type: RadarTransmitterMultifunction

    Get the radar transmitter.

.. py:property:: waveform_strategy_settings
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.waveform_strategy_settings
    :type: RadarMultifunctionWaveformStrategySettings

    Get the waveform selection strategy settings.


Method detail
-------------








.. py:method:: set_pointing_strategy_type(self, value: PointingStrategyType) -> None
    :canonical: br.ok.core.stkobjects.RadarModelMultifunction.set_pointing_strategy_type

    Set the current pointing strategy type.

    :Parameters:

        **value** : :obj:`~PointingStrategyType`


    :Returns:

        :obj:`~None`



