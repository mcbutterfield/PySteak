RadarModeMonostaticSAR
======================

.. py:class:: br.steak.core.stkobjects.RadarModeMonostaticSAR

   Bases: :py:class:`~br.steak.core.stkobjects.IRadarModeMonostatic`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a monostatic sar radar mode.

.. py:currentmodule:: RadarModeMonostaticSAR

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarModeMonostaticSAR.modulator`
              - Get the interface for setting the modulator parameters.
            * - :py:attr:`~br.steak.core.stkobjects.RadarModeMonostaticSAR.pulse_definition`
              - Get the interface for configuring the SAR waveform pulse definition.
            * - :py:attr:`~br.steak.core.stkobjects.RadarModeMonostaticSAR.pulse_integration`
              - Get the interface for configuring the SAR waveform pulse integration.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RadarModeMonostaticSAR


Property detail
---------------

.. py:property:: modulator
    :canonical: br.steak.core.stkobjects.RadarModeMonostaticSAR.modulator
    :type: RadarModulator

    Get the interface for setting the modulator parameters.

.. py:property:: pulse_definition
    :canonical: br.steak.core.stkobjects.RadarModeMonostaticSAR.pulse_definition
    :type: RadarWaveformSarPulseDefinition

    Get the interface for configuring the SAR waveform pulse definition.

.. py:property:: pulse_integration
    :canonical: br.steak.core.stkobjects.RadarModeMonostaticSAR.pulse_integration
    :type: RadarWaveformSarPulseIntegration

    Get the interface for configuring the SAR waveform pulse integration.


