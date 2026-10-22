RadarTransmitter
================

.. py:class:: br.ok.core.stkobjects.RadarTransmitter

   Class defining the radar transmitter.

.. py:currentmodule:: RadarTransmitter

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.enable_orthogonal_polarization`
              - Get or set the option for enabling the orthogonal polarization.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.frequency`
              - Get or set the frequency.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.frequency_specification`
              - Get or set the frequency specification.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.polarization`
              - Get the polarization.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.power`
              - Get or set the power.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.power_amplifier_bandwidth`
              - Get or set the power amplifier bandwidth.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitter.wavelength`
              - Get or set the wavelength.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarTransmitter


Property detail
---------------

.. py:property:: enable_filter
    :canonical: br.ok.core.stkobjects.RadarTransmitter.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: enable_orthogonal_polarization
    :canonical: br.ok.core.stkobjects.RadarTransmitter.enable_orthogonal_polarization
    :type: bool

    Get or set the option for enabling the orthogonal polarization.

.. py:property:: enable_polarization
    :canonical: br.ok.core.stkobjects.RadarTransmitter.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: filter_component_linking
    :canonical: br.ok.core.stkobjects.RadarTransmitter.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.

.. py:property:: frequency
    :canonical: br.ok.core.stkobjects.RadarTransmitter.frequency
    :type: float

    Get or set the frequency.

.. py:property:: frequency_specification
    :canonical: br.ok.core.stkobjects.RadarTransmitter.frequency_specification
    :type: RadarFrequencySpecificationType

    Get or set the frequency specification.

.. py:property:: polarization
    :canonical: br.ok.core.stkobjects.RadarTransmitter.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: br.ok.core.stkobjects.RadarTransmitter.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: power
    :canonical: br.ok.core.stkobjects.RadarTransmitter.power
    :type: float

    Get or set the power.

.. py:property:: power_amplifier_bandwidth
    :canonical: br.ok.core.stkobjects.RadarTransmitter.power_amplifier_bandwidth
    :type: float

    Get or set the power amplifier bandwidth.

.. py:property:: wavelength
    :canonical: br.ok.core.stkobjects.RadarTransmitter.wavelength
    :type: float

    Get or set the wavelength.


Method detail
-------------


















.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: br.ok.core.stkobjects.RadarTransmitter.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`



