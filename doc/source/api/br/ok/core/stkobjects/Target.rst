Target
======

.. py:class:: br.ok.core.stkobjects.Target

   Bases: :py:class:`~br.ok.core.stkobjects.ISTKObject`, :py:class:`~br.ok.core.stkobjects.IGroundLocation`, :py:class:`~br.ok.core.stkobjects.ILifetimeInformation`, :py:class:`~br.ok.core.stkobjects.IDisplayTime`

   Class defining the Target object.

.. py:currentmodule:: Target

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Target.get_az_el_mask`
              - Get the az-el mask. A member of the AzElMaskType enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.Target.get_az_el_mask_data`
              - Get az-el mask data.
            * - :py:attr:`~br.ok.core.stkobjects.Target.reset_az_el_mask`
              - Reset the az-el mask.
            * - :py:attr:`~br.ok.core.stkobjects.Target.set_az_el_mask`
              - Set an az-el mask. A member of the AzElMaskType enumeration.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Target.access_constraints`
              - Get the constraints imposed on the target.
            * - :py:attr:`~br.ok.core.stkobjects.Target.altitude_reference`
              - Get or set the altitude reference of the object.
            * - :py:attr:`~br.ok.core.stkobjects.Target.chain_analysis_options`
              - Get the target's chain analysis options.
            * - :py:attr:`~br.ok.core.stkobjects.Target.graphics`
              - Get the 2D Graphics properties of the target.
            * - :py:attr:`~br.ok.core.stkobjects.Target.graphics_3d`
              - Get the 3D Graphics properties of the target.
            * - :py:attr:`~br.ok.core.stkobjects.Target.height_above_ground`
              - Height of target above its model of the ground. Height is measured along the normal to surface defined by reference ellipsoid of the central body. Target models the ground as an ellipsoid passing through the ground position. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Target.laser_environment`
              - Get the laser environment.
            * - :py:attr:`~br.ok.core.stkobjects.Target.lighting_maximum_step`
              - Get or set the maximum step size to use when computing lighting. Only applies (and only can be set) when LightingObstructionModel is eLightingObstructionAzElMask or eLightingObstructionTerrain. Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Target.lighting_obstruction_model`
              - Get or set the obstruction model used in lighting computations.
            * - :py:attr:`~br.ok.core.stkobjects.Target.local_time_offset`
              - The amount of the time offset from GMT, if this option is used. Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Target.maximum_range_when_computing_az_el_mask`
              - Get or set the maximum range to use when computing the az el mask using terrain data. Zero indicates to use algorithm default. Only applies when GetAzElMask returns eTerrainData (cannot be set if eMaskFile). Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Target.position`
              - Get the position of the target.
            * - :py:attr:`~br.ok.core.stkobjects.Target.radar_cross_section`
              - Return the radar cross sectoin.
            * - :py:attr:`~br.ok.core.stkobjects.Target.rf_environment`
              - Get the RF environment.
            * - :py:attr:`~br.ok.core.stkobjects.Target.save_terrain_mask_data_in_binary`
              - Save terrain az-el mask data in binary.
            * - :py:attr:`~br.ok.core.stkobjects.Target.terrain_normal`
              - Set the normal to the local terrain.
            * - :py:attr:`~br.ok.core.stkobjects.Target.terrain_normal_data`
              - Data used in specifying terrain slope.
            * - :py:attr:`~br.ok.core.stkobjects.Target.use_local_time_offset`
              - Opt whether to use a local time offset from GMT.
            * - :py:attr:`~br.ok.core.stkobjects.Target.use_terrain`
              - Opt whether to set altitude automatically by using terrain data.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Target


Property detail
---------------

.. py:property:: access_constraints
    :canonical: br.ok.core.stkobjects.Target.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the target.

.. py:property:: altitude_reference
    :canonical: br.ok.core.stkobjects.Target.altitude_reference
    :type: None

    Get or set the altitude reference of the object.

.. py:property:: chain_analysis_options
    :canonical: br.ok.core.stkobjects.Target.chain_analysis_options
    :type: ChainAnalysisOptions

    Get the target's chain analysis options.

.. py:property:: graphics
    :canonical: br.ok.core.stkobjects.Target.graphics
    :type: TargetGraphics

    Get the 2D Graphics properties of the target.

.. py:property:: graphics_3d
    :canonical: br.ok.core.stkobjects.Target.graphics_3d
    :type: TargetGraphics3D

    Get the 3D Graphics properties of the target.

.. py:property:: height_above_ground
    :canonical: br.ok.core.stkobjects.Target.height_above_ground
    :type: None

    Height of target above its model of the ground. Height is measured along the normal to surface defined by reference ellipsoid of the central body. Target models the ground as an ellipsoid passing through the ground position. Uses Distance Dimension.

.. py:property:: laser_environment
    :canonical: br.ok.core.stkobjects.Target.laser_environment
    :type: PlatformLaserEnvironment

    Get the laser environment.

.. py:property:: lighting_maximum_step
    :canonical: br.ok.core.stkobjects.Target.lighting_maximum_step
    :type: float

    Get or set the maximum step size to use when computing lighting. Only applies (and only can be set) when LightingObstructionModel is eLightingObstructionAzElMask or eLightingObstructionTerrain. Uses Time Dimension.

.. py:property:: lighting_obstruction_model
    :canonical: br.ok.core.stkobjects.Target.lighting_obstruction_model
    :type: LightingObstructionModelType

    Get or set the obstruction model used in lighting computations.

.. py:property:: local_time_offset
    :canonical: br.ok.core.stkobjects.Target.local_time_offset
    :type: float

    The amount of the time offset from GMT, if this option is used. Uses Time Dimension.

.. py:property:: maximum_range_when_computing_az_el_mask
    :canonical: br.ok.core.stkobjects.Target.maximum_range_when_computing_az_el_mask
    :type: float

    Get or set the maximum range to use when computing the az el mask using terrain data. Zero indicates to use algorithm default. Only applies when GetAzElMask returns eTerrainData (cannot be set if eMaskFile). Uses Distance Dimension.

.. py:property:: position
    :canonical: br.ok.core.stkobjects.Target.position
    :type: IPosition

    Get the position of the target.

.. py:property:: radar_cross_section
    :canonical: br.ok.core.stkobjects.Target.radar_cross_section
    :type: RadarCrossSectionInheritable

    Return the radar cross sectoin.

.. py:property:: rf_environment
    :canonical: br.ok.core.stkobjects.Target.rf_environment
    :type: PlatformRFEnvironment

    Get the RF environment.

.. py:property:: save_terrain_mask_data_in_binary
    :canonical: br.ok.core.stkobjects.Target.save_terrain_mask_data_in_binary
    :type: bool

    Save terrain az-el mask data in binary.

.. py:property:: terrain_normal
    :canonical: br.ok.core.stkobjects.Target.terrain_normal
    :type: None

    Set the normal to the local terrain.

.. py:property:: terrain_normal_data
    :canonical: br.ok.core.stkobjects.Target.terrain_normal_data
    :type: ITerrainNormData

    Data used in specifying terrain slope.

.. py:property:: use_local_time_offset
    :canonical: br.ok.core.stkobjects.Target.use_local_time_offset
    :type: bool

    Opt whether to use a local time offset from GMT.

.. py:property:: use_terrain
    :canonical: br.ok.core.stkobjects.Target.use_terrain
    :type: bool

    Opt whether to set altitude automatically by using terrain data.


Method detail
-------------





.. py:method:: get_az_el_mask(self) -> AzElMaskType
    :canonical: br.ok.core.stkobjects.Target.get_az_el_mask

    Get the az-el mask. A member of the AzElMaskType enumeration.

    :Returns:

        :obj:`~AzElMaskType`

.. py:method:: get_az_el_mask_data(self) -> typing.Any
    :canonical: br.ok.core.stkobjects.Target.get_az_el_mask_data

    Get az-el mask data.

    :Returns:

        :obj:`~typing.Any`
















.. py:method:: reset_az_el_mask(self) -> None
    :canonical: br.ok.core.stkobjects.Target.reset_az_el_mask

    Reset the az-el mask.

    :Returns:

        :obj:`~None`



.. py:method:: set_az_el_mask(self, type: AzElMaskType, data: typing.Any) -> None
    :canonical: br.ok.core.stkobjects.Target.set_az_el_mask

    Set an az-el mask. A member of the AzElMaskType enumeration.

    :Parameters:

        **type** : :obj:`~AzElMaskType`

        **data** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`









