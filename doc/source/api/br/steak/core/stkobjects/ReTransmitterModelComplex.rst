ReTransmitterModelComplex
=========================

.. py:class:: br.steak.core.stkobjects.ReTransmitterModelComplex

   Bases: :py:class:`~br.steak.core.stkobjects.IReTransmitterModel`, :py:class:`~br.steak.core.stkobjects.ITransmitterModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a complex re-transmitter model.

.. py:currentmodule:: ReTransmitterModelComplex

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ReTransmitterModelComplex.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ReTransmitterModelComplex.antenna_control`
              - Get the receiver antenna control.
            * - :py:attr:`~br.steak.core.stkobjects.ReTransmitterModelComplex.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~br.steak.core.stkobjects.ReTransmitterModelComplex.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~br.steak.core.stkobjects.ReTransmitterModelComplex.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.
            * - :py:attr:`~br.steak.core.stkobjects.ReTransmitterModelComplex.polarization`
              - Get the polarization.
            * - :py:attr:`~br.steak.core.stkobjects.ReTransmitterModelComplex.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~br.steak.core.stkobjects.ReTransmitterModelComplex.saturated_power`
              - Get or set the saturated power.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ReTransmitterModelComplex


Property detail
---------------

.. py:property:: antenna_control
    :canonical: br.steak.core.stkobjects.ReTransmitterModelComplex.antenna_control
    :type: AntennaControl

    Get the receiver antenna control.

.. py:property:: enable_filter
    :canonical: br.steak.core.stkobjects.ReTransmitterModelComplex.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: enable_polarization
    :canonical: br.steak.core.stkobjects.ReTransmitterModelComplex.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: filter_component_linking
    :canonical: br.steak.core.stkobjects.ReTransmitterModelComplex.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.

.. py:property:: polarization
    :canonical: br.steak.core.stkobjects.ReTransmitterModelComplex.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: br.steak.core.stkobjects.ReTransmitterModelComplex.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: saturated_power
    :canonical: br.steak.core.stkobjects.ReTransmitterModelComplex.saturated_power
    :type: float

    Get or set the saturated power.


Method detail
-------------











.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: br.steak.core.stkobjects.ReTransmitterModelComplex.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`

