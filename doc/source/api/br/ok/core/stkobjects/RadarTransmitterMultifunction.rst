RadarTransmitterMultifunction
=============================

.. py:class:: br.ok.core.stkobjects.RadarTransmitterMultifunction

   Class defining the multifunction radar transmitter.

.. py:currentmodule:: RadarTransmitterMultifunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.enable_orthogonal_polarization`
              - Get or set the option for enabling the orthogonal polarization.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.maximum_power_limit`
              - Get or set the power.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.polarization`
              - Get the polarization.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~br.ok.core.stkobjects.RadarTransmitterMultifunction.power_amplifier_bandwidth`
              - Get or set the power amplifier bandwidth.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarTransmitterMultifunction


Property detail
---------------

.. py:property:: enable_filter
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: enable_orthogonal_polarization
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.enable_orthogonal_polarization
    :type: bool

    Get or set the option for enabling the orthogonal polarization.

.. py:property:: enable_polarization
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: filter_component_linking
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.

.. py:property:: maximum_power_limit
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.maximum_power_limit
    :type: float

    Get or set the power.

.. py:property:: polarization
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: power_amplifier_bandwidth
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.power_amplifier_bandwidth
    :type: float

    Get or set the power amplifier bandwidth.


Method detail
-------------














.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: br.ok.core.stkobjects.RadarTransmitterMultifunction.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`

