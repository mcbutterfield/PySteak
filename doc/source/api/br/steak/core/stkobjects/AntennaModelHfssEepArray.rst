AntennaModelHfssEepArray
========================

.. py:class:: br.steak.core.stkobjects.AntennaModelHfssEepArray

   Bases: :py:class:`~br.steak.core.stkobjects.IAntennaModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining an HFSS EEP array antenna model.

.. py:currentmodule:: AntennaModelHfssEepArray

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.beam_direction_provider`
              - Get the beam direction provider.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.beam_direction_provider_type`
              - Get or set the beam direction provider type.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.beamformer`
              - Get the beamformer.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.beamformer_type`
              - Get or set beamformer type.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.element_configuration`
              - Get the element configuration.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.elements`
              - Get the collection of elements.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.height`
              - Get the array height.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.number_of_elements`
              - Get the number of array elements.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.supported_beam_direction_provider_types`
              - Get an array of valid beam direction provider types.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaModelHfssEepArray.width`
              - Get the array width.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AntennaModelHfssEepArray


Property detail
---------------

.. py:property:: beam_direction_provider
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.beam_direction_provider
    :type: IDirectionProvider

    Get the beam direction provider.

.. py:property:: beam_direction_provider_type
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.beam_direction_provider_type
    :type: DirectionProviderType

    Get or set the beam direction provider type.

.. py:property:: beamformer
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.beamformer
    :type: IBeamformer

    Get the beamformer.

.. py:property:: beamformer_type
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.beamformer_type
    :type: BeamformerType

    Get or set beamformer type.

.. py:property:: element_configuration
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.element_configuration
    :type: ElementConfigurationHfssEepFile

    Get the element configuration.

.. py:property:: elements
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.elements
    :type: ElementCollection

    Get the collection of elements.

.. py:property:: height
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.height
    :type: float

    Get the array height.

.. py:property:: number_of_elements
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.number_of_elements
    :type: int

    Get the number of array elements.

.. py:property:: supported_beam_direction_provider_types
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.supported_beam_direction_provider_types
    :type: list

    Get an array of valid beam direction provider types.

.. py:property:: width
    :canonical: br.steak.core.stkobjects.AntennaModelHfssEepArray.width
    :type: float

    Get the array width.


