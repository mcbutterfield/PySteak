ReTransmitterModelSimple
========================

.. py:class:: br.ok.core.stkobjects.ReTransmitterModelSimple

   Bases: :py:class:`~br.ok.core.stkobjects.IReTransmitterModel`, :py:class:`~br.ok.core.stkobjects.ITransmitterModel`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a simple re-transmitter model.

.. py:currentmodule:: ReTransmitterModelSimple

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ReTransmitterModelSimple.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ReTransmitterModelSimple.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~br.ok.core.stkobjects.ReTransmitterModelSimple.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~br.ok.core.stkobjects.ReTransmitterModelSimple.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.
            * - :py:attr:`~br.ok.core.stkobjects.ReTransmitterModelSimple.polarization`
              - Get the polarization.
            * - :py:attr:`~br.ok.core.stkobjects.ReTransmitterModelSimple.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~br.ok.core.stkobjects.ReTransmitterModelSimple.saturated_eirp`
              - Get or set the saturated eirp.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ReTransmitterModelSimple


Property detail
---------------

.. py:property:: enable_filter
    :canonical: br.ok.core.stkobjects.ReTransmitterModelSimple.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: enable_polarization
    :canonical: br.ok.core.stkobjects.ReTransmitterModelSimple.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: filter_component_linking
    :canonical: br.ok.core.stkobjects.ReTransmitterModelSimple.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.

.. py:property:: polarization
    :canonical: br.ok.core.stkobjects.ReTransmitterModelSimple.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: br.ok.core.stkobjects.ReTransmitterModelSimple.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: saturated_eirp
    :canonical: br.ok.core.stkobjects.ReTransmitterModelSimple.saturated_eirp
    :type: float

    Get or set the saturated eirp.


Method detail
-------------










.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: br.ok.core.stkobjects.ReTransmitterModelSimple.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`

