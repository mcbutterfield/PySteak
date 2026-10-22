IModulatorModel
===============

.. py:class:: br.steak.core.stkobjects.IModulatorModel

   Provide access to the properties and methods defining a modulator model.

.. py:currentmodule:: IModulatorModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.bandwidth`
              - Get or set the filter bandwidth.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.chips_per_bit`
              - Get or set the chips per bit.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.enable_cdma_spread`
              - Get or set the option for modeling CDMA spread.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.enable_signal_psd`
              - Get or set the option for modeling signal PSD.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.lower_bandwidth_limit`
              - Get or set the lower bandwidth limit.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.name`
              - Get the modulator model name.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.psd_limit_multiplier`
              - Get or set the PSD limit multiplier.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.scale_bandwidth_automatically`
              - Get or set the option for auto scaling the bandwidth.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.spreading_gain`
              - Get the spreading gain.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.symmetric_bandwidth`
              - Get or set the option for specifying symmetric bandwidth.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.type`
              - Get the modulator model type enumeration.
            * - :py:attr:`~br.steak.core.stkobjects.IModulatorModel.upper_bandwidth_limit`
              - Get or set the upper bandwidth limit.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import IModulatorModel


Property detail
---------------

.. py:property:: bandwidth
    :canonical: br.steak.core.stkobjects.IModulatorModel.bandwidth
    :type: float

    Get or set the filter bandwidth.

.. py:property:: chips_per_bit
    :canonical: br.steak.core.stkobjects.IModulatorModel.chips_per_bit
    :type: int

    Get or set the chips per bit.

.. py:property:: enable_cdma_spread
    :canonical: br.steak.core.stkobjects.IModulatorModel.enable_cdma_spread
    :type: bool

    Get or set the option for modeling CDMA spread.

.. py:property:: enable_signal_psd
    :canonical: br.steak.core.stkobjects.IModulatorModel.enable_signal_psd
    :type: bool

    Get or set the option for modeling signal PSD.

.. py:property:: lower_bandwidth_limit
    :canonical: br.steak.core.stkobjects.IModulatorModel.lower_bandwidth_limit
    :type: float

    Get or set the lower bandwidth limit.

.. py:property:: name
    :canonical: br.steak.core.stkobjects.IModulatorModel.name
    :type: str

    Get the modulator model name.

.. py:property:: psd_limit_multiplier
    :canonical: br.steak.core.stkobjects.IModulatorModel.psd_limit_multiplier
    :type: int

    Get or set the PSD limit multiplier.

.. py:property:: scale_bandwidth_automatically
    :canonical: br.steak.core.stkobjects.IModulatorModel.scale_bandwidth_automatically
    :type: bool

    Get or set the option for auto scaling the bandwidth.

.. py:property:: spreading_gain
    :canonical: br.steak.core.stkobjects.IModulatorModel.spreading_gain
    :type: float

    Get the spreading gain.

.. py:property:: symmetric_bandwidth
    :canonical: br.steak.core.stkobjects.IModulatorModel.symmetric_bandwidth
    :type: bool

    Get or set the option for specifying symmetric bandwidth.

.. py:property:: type
    :canonical: br.steak.core.stkobjects.IModulatorModel.type
    :type: ModulatorModelType

    Get the modulator model type enumeration.

.. py:property:: upper_bandwidth_limit
    :canonical: br.steak.core.stkobjects.IModulatorModel.upper_bandwidth_limit
    :type: float

    Get or set the upper bandwidth limit.


