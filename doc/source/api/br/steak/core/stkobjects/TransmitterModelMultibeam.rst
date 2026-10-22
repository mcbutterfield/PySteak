TransmitterModelMultibeam
=========================

.. py:class:: br.steak.core.stkobjects.TransmitterModelMultibeam

   Bases: :py:class:`~br.steak.core.stkobjects.ITransmitterModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a multibeam transmitter model.

.. py:currentmodule:: TransmitterModelMultibeam

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.TransmitterModelMultibeam.set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.TransmitterModelMultibeam.antenna_system`
              - Get the antenna system.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterModelMultibeam.data_rate`
              - Get or set the data rate.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterModelMultibeam.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterModelMultibeam.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterModelMultibeam.modulator`
              - Get the current modulator model.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterModelMultibeam.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterModelMultibeam.supported_modulators`
              - Get an array of supported modulator model names.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import TransmitterModelMultibeam


Property detail
---------------

.. py:property:: antenna_system
    :canonical: br.steak.core.stkobjects.TransmitterModelMultibeam.antenna_system
    :type: AntennaSystem

    Get the antenna system.

.. py:property:: data_rate
    :canonical: br.steak.core.stkobjects.TransmitterModelMultibeam.data_rate
    :type: float

    Get or set the data rate.

.. py:property:: enable_filter
    :canonical: br.steak.core.stkobjects.TransmitterModelMultibeam.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: filter_component_linking
    :canonical: br.steak.core.stkobjects.TransmitterModelMultibeam.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.

.. py:property:: modulator
    :canonical: br.steak.core.stkobjects.TransmitterModelMultibeam.modulator
    :type: IModulatorModel

    Get the current modulator model.

.. py:property:: post_transmit_gains_losses
    :canonical: br.steak.core.stkobjects.TransmitterModelMultibeam.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: supported_modulators
    :canonical: br.steak.core.stkobjects.TransmitterModelMultibeam.supported_modulators
    :type: list

    Get an array of supported modulator model names.


Method detail
-------------









.. py:method:: set_modulator(self, name: str) -> None
    :canonical: br.steak.core.stkobjects.TransmitterModelMultibeam.set_modulator

    Set the current modulator model by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`


