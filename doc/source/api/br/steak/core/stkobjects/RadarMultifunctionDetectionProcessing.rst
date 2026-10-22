RadarMultifunctionDetectionProcessing
=====================================

.. py:class:: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing

   Class defining multifunction radar detection processing.

.. py:currentmodule:: RadarMultifunctionDetectionProcessing

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.set_probability_of_detection`
              - Set the probability of detection algorithm by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.azimuth_resolution`
              - Get or set the overriding azimuth resolution value.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.enable_coherent_pulses`
              - Get or set the flag for modeling coherent pulses.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.enable_pulse_canceller`
              - Get or set the flag for enabling pulse cancellation.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.enable_resolution_override`
              - Get or set the flag for overriding the computed range and azimuth resolution values.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.number_of_pulses_to_cancel`
              - Get or set the number of pulses to cancel.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.probability_of_detection`
              - Get the interface for setting the probability of detection parameters.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.pulse_integration`
              - Get the interface for setting pulse integration parameters.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.pulse_integration_type`
              - Get or set the pulse integration type.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.range_cell_resolution`
              - Get or set the overriding range cell resolution value.
            * - :py:attr:`~br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.supported_probability_of_detection`
              - Get an array of supported model names.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RadarMultifunctionDetectionProcessing


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.azimuth_resolution
    :type: float

    Get or set the overriding azimuth resolution value.

.. py:property:: enable_coherent_pulses
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.enable_coherent_pulses
    :type: bool

    Get or set the flag for modeling coherent pulses.

.. py:property:: enable_pulse_canceller
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.enable_pulse_canceller
    :type: bool

    Get or set the flag for enabling pulse cancellation.

.. py:property:: enable_resolution_override
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.enable_resolution_override
    :type: bool

    Get or set the flag for overriding the computed range and azimuth resolution values.

.. py:property:: number_of_pulses_to_cancel
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.number_of_pulses_to_cancel
    :type: int

    Get or set the number of pulses to cancel.

.. py:property:: probability_of_detection
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.probability_of_detection
    :type: IRadarProbabilityOfDetection

    Get the interface for setting the probability of detection parameters.

.. py:property:: pulse_integration
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.pulse_integration
    :type: IRadarPulseIntegration

    Get the interface for setting pulse integration parameters.

.. py:property:: pulse_integration_type
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.pulse_integration_type
    :type: RadarPulseIntegrationType

    Get or set the pulse integration type.

.. py:property:: range_cell_resolution
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.range_cell_resolution
    :type: float

    Get or set the overriding range cell resolution value.

.. py:property:: supported_probability_of_detection
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.supported_probability_of_detection
    :type: list

    Get an array of supported model names.


Method detail
-------------

















.. py:method:: set_probability_of_detection(self, name: str) -> None
    :canonical: br.steak.core.stkobjects.RadarMultifunctionDetectionProcessing.set_probability_of_detection

    Set the probability of detection algorithm by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`


