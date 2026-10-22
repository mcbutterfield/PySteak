IWaveform
=========

.. py:class:: br.ok.core.stkobjects.IWaveform

   Provide access to the properties and methods defining an antenna model.

.. py:currentmodule:: IWaveform

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IWaveform.frequency`
              - Get or set the frequency.
            * - :py:attr:`~br.ok.core.stkobjects.IWaveform.frequency_specification`
              - Get or set the frequency specification.
            * - :py:attr:`~br.ok.core.stkobjects.IWaveform.name`
              - Get the waveform name.
            * - :py:attr:`~br.ok.core.stkobjects.IWaveform.power`
              - Get the power.
            * - :py:attr:`~br.ok.core.stkobjects.IWaveform.type`
              - Get the waveform type enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.IWaveform.wavelength`
              - Get or set the wavelength.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IWaveform


Property detail
---------------

.. py:property:: frequency
    :canonical: br.ok.core.stkobjects.IWaveform.frequency
    :type: float

    Get or set the frequency.

.. py:property:: frequency_specification
    :canonical: br.ok.core.stkobjects.IWaveform.frequency_specification
    :type: FrequencySpecificationType

    Get or set the frequency specification.

.. py:property:: name
    :canonical: br.ok.core.stkobjects.IWaveform.name
    :type: str

    Get the waveform name.

.. py:property:: power
    :canonical: br.ok.core.stkobjects.IWaveform.power
    :type: float

    Get the power.

.. py:property:: type
    :canonical: br.ok.core.stkobjects.IWaveform.type
    :type: WaveformType

    Get the waveform type enumeration.

.. py:property:: wavelength
    :canonical: br.ok.core.stkobjects.IWaveform.wavelength
    :type: float

    Get or set the wavelength.


