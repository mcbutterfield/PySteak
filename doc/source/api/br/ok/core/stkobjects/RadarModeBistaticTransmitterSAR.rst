RadarModeBistaticTransmitterSAR
===============================

.. py:class:: br.ok.core.stkobjects.RadarModeBistaticTransmitterSAR

   Bases: :py:class:`~br.ok.core.stkobjects.IRadarModeBistaticTransmitter`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a bistatic transmitter sar radar mode.

.. py:currentmodule:: RadarModeBistaticTransmitterSAR

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModeBistaticTransmitterSAR.modulator`
              - Get the interface for setting the modulator parameters.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModeBistaticTransmitterSAR.pulse_definition`
              - Get the interface for configuring the SAR waveform pulse definition.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarModeBistaticTransmitterSAR


Property detail
---------------

.. py:property:: modulator
    :canonical: br.ok.core.stkobjects.RadarModeBistaticTransmitterSAR.modulator
    :type: RadarModulator

    Get the interface for setting the modulator parameters.

.. py:property:: pulse_definition
    :canonical: br.ok.core.stkobjects.RadarModeBistaticTransmitterSAR.pulse_definition
    :type: RadarWaveformSarPulseDefinition

    Get the interface for configuring the SAR waveform pulse definition.


