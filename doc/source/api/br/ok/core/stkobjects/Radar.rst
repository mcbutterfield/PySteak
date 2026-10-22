Radar
=====

.. py:class:: br.ok.core.stkobjects.Radar

   Bases: :py:class:`~br.ok.core.stkobjects.ISTKObject`, :py:class:`~br.ok.core.stkobjects.ILifetimeInformation`

   Class defining the radar object.

.. py:currentmodule:: Radar

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Radar.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Radar.chain_analysis_options`
              - Get the radar's chain analysis options.
            * - :py:attr:`~br.ok.core.stkobjects.Radar.graphics`
              - Get the 2D Graphics properties for the radar.
            * - :py:attr:`~br.ok.core.stkobjects.Radar.graphics_3d`
              - Get the 3D Graphics properties for the radar.
            * - :py:attr:`~br.ok.core.stkobjects.Radar.model_component_linking`
              - Get the link/embed controller for managing the radar model component.
            * - :py:attr:`~br.ok.core.stkobjects.Radar.refraction`
              - Refraction method, a member of the SensorRefractionType enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.Radar.refraction_model`
              - Get a refraction model.
            * - :py:attr:`~br.ok.core.stkobjects.Radar.refraction_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.Radar.rf_environment`
              - Get the object RF Environment settings.
            * - :py:attr:`~br.ok.core.stkobjects.Radar.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Radar


Property detail
---------------

.. py:property:: chain_analysis_options
    :canonical: br.ok.core.stkobjects.Radar.chain_analysis_options
    :type: ChainAnalysisOptions

    Get the radar's chain analysis options.

.. py:property:: graphics
    :canonical: br.ok.core.stkobjects.Radar.graphics
    :type: RadarGraphics

    Get the 2D Graphics properties for the radar.

.. py:property:: graphics_3d
    :canonical: br.ok.core.stkobjects.Radar.graphics_3d
    :type: RadarGraphics3D

    Get the 3D Graphics properties for the radar.

.. py:property:: model_component_linking
    :canonical: br.ok.core.stkobjects.Radar.model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar model component.

.. py:property:: refraction
    :canonical: br.ok.core.stkobjects.Radar.refraction
    :type: SensorRefractionType

    Refraction method, a member of the SensorRefractionType enumeration.

.. py:property:: refraction_model
    :canonical: br.ok.core.stkobjects.Radar.refraction_model
    :type: IRefractionModelBase

    Get a refraction model.

.. py:property:: refraction_supported_types
    :canonical: br.ok.core.stkobjects.Radar.refraction_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: rf_environment
    :canonical: br.ok.core.stkobjects.Radar.rf_environment
    :type: ObjectRFEnvironment

    Get the object RF Environment settings.

.. py:property:: use_refraction_in_access
    :canonical: br.ok.core.stkobjects.Radar.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.


Method detail
-------------



.. py:method:: is_refraction_type_supported(self, model: SensorRefractionType) -> bool
    :canonical: br.ok.core.stkobjects.Radar.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **model** : :obj:`~SensorRefractionType`


    :Returns:

        :obj:`~bool`










