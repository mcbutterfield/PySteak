RadarModeMonostaticSAR
======================

.. py:class:: br.ok.core.stkobjects.RadarModeMonostaticSAR

   Bases: :py:class:`~br.ok.core.stkobjects.IRadarModeMonostatic`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a monostatic sar radar mode.

.. py:currentmodule:: RadarModeMonostaticSAR

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModeMonostaticSAR.modulator`
              - Get the interface for setting the modulator parameters.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModeMonostaticSAR.pulse_definition`
              - Get the interface for configuring the SAR waveform pulse definition.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModeMonostaticSAR.pulse_integration`
              - Get the interface for configuring the SAR waveform pulse integration.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarModeMonostaticSAR


Property detail
---------------

.. py:property:: modulator
    :canonical: br.ok.core.stkobjects.RadarModeMonostaticSAR.modulator
    :type: RadarModulator

    Get the interface for setting the modulator parameters.

.. py:property:: pulse_definition
    :canonical: br.ok.core.stkobjects.RadarModeMonostaticSAR.pulse_definition
    :type: RadarWaveformSarPulseDefinition

    Get the interface for configuring the SAR waveform pulse definition.

.. py:property:: pulse_integration
    :canonical: br.ok.core.stkobjects.RadarModeMonostaticSAR.pulse_integration
    :type: RadarWaveformSarPulseIntegration

    Get the interface for configuring the SAR waveform pulse integration.


