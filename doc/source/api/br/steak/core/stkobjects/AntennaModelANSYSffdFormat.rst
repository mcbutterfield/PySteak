AntennaModelANSYSffdFormat
==========================

.. py:class:: br.steak.core.stkobjects.AntennaModelANSYSffdFormat

   Bases: :py:class:`~br.steak.core.stkobjects.IAntennaModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining an antenna pattern ANSYS ffd model.

.. py:currentmodule:: AntennaModelANSYSffdFormat

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelANSYSffdFormat.defined_frequencies`
              - Get the frequencies defined in the file.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelANSYSffdFormat.defined_power_value`
              - Get the Defined Power Value for the selected GainType.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelANSYSffdFormat.filename`
              - Get or set the user antenna data filename.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelANSYSffdFormat.gain_type`
              - Get or set the gain type.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelANSYSffdFormat.polarization_reference_axis`
              - Get or set the polarization reference axis.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelANSYSffdFormat.user_gain_factor`
              - Get or set the User Gain Factor.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AntennaModelANSYSffdFormat


Property detail
---------------

.. py:property:: defined_frequencies
    :canonical: br.steak.core.stkobjects.AntennaModelANSYSffdFormat.defined_frequencies
    :type: str

    Get the frequencies defined in the file.

.. py:property:: defined_power_value
    :canonical: br.steak.core.stkobjects.AntennaModelANSYSffdFormat.defined_power_value
    :type: float

    Get the Defined Power Value for the selected GainType.

.. py:property:: filename
    :canonical: br.steak.core.stkobjects.AntennaModelANSYSffdFormat.filename
    :type: str

    Get or set the user antenna data filename.

.. py:property:: gain_type
    :canonical: br.steak.core.stkobjects.AntennaModelANSYSffdFormat.gain_type
    :type: HFSSFarFieldDataGainType

    Get or set the gain type.

.. py:property:: polarization_reference_axis
    :canonical: br.steak.core.stkobjects.AntennaModelANSYSffdFormat.polarization_reference_axis
    :type: PolarizationReferenceAxis

    Get or set the polarization reference axis.

.. py:property:: user_gain_factor
    :canonical: br.steak.core.stkobjects.AntennaModelANSYSffdFormat.user_gain_factor
    :type: float

    Get or set the User Gain Factor.


