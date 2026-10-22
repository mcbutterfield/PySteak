LaunchVehicle
=============

.. py:class:: br.steak.core.stkobjects.LaunchVehicle

   Bases: :py:class:`~br.steak.core.stkobjects.ISTKObject`, :py:class:`~br.steak.core.stkobjects.ILifetimeInformation`, :py:class:`~br.steak.core.stkobjects.IProvideSpatialInfo`

   Launch vehicle object.

.. py:currentmodule:: LaunchVehicle

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.is_trajectory_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.set_attitude_type`
              - Set the type of attitude profile used by the launch vehicle.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.set_trajectory_type`
              - Set the propagator type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.access_constraints`
              - Get the constraints imposed on the launch vehicle.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.attitude`
              - Get the launch vehicle's attitude profile.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.attitude_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.attitude_type`
              - Get the type of attitude profile used by the launch vehicle.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.chain_analysis_options`
              - Get the launch vehicle's chain analysis options.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.eclipse_bodies`
              - Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.export_tools`
              - Return the LaunchVehicleExportTools interface.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.graphics`
              - Get the launch vehicle's 2D Graphics properties.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.graphics_3d`
              - Get the launch vehicle's 3D Graphics properties.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.ground_ellipses`
              - Get the launch vehicle's ground ellipses properties.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.laser_environment`
              - Get the laser environment.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.lighting_maximum_step_central_body_shape`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.lighting_maximum_step_terrain`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.radar_cross_section`
              - Return the radar cross sectoin.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.rf_environment`
              - Get the RF environment.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.space_environment`
              - Return the launch vehicle's SpaceEnvironment properties.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.trajectory`
              - Get the launch vehicle's trajectory properties.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.trajectory_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.trajectory_type`
              - Get the propagator type used by the launch vehicle.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicle.use_terrain_in_lighting_computations`
              - Opt whether to compute lighting using terrain data.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import LaunchVehicle


Property detail
---------------

.. py:property:: access_constraints
    :canonical: br.steak.core.stkobjects.LaunchVehicle.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the launch vehicle.

.. py:property:: attitude
    :canonical: br.steak.core.stkobjects.LaunchVehicle.attitude
    :type: IVehicleAttitude

    Get the launch vehicle's attitude profile.

.. py:property:: attitude_supported_types
    :canonical: br.steak.core.stkobjects.LaunchVehicle.attitude_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attitude_type
    :canonical: br.steak.core.stkobjects.LaunchVehicle.attitude_type
    :type: VehicleAttitude

    Get the type of attitude profile used by the launch vehicle.

.. py:property:: chain_analysis_options
    :canonical: br.steak.core.stkobjects.LaunchVehicle.chain_analysis_options
    :type: ChainAnalysisOptions

    Get the launch vehicle's chain analysis options.

.. py:property:: eclipse_bodies
    :canonical: br.steak.core.stkobjects.LaunchVehicle.eclipse_bodies
    :type: VehicleEclipseBodies

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: export_tools
    :canonical: br.steak.core.stkobjects.LaunchVehicle.export_tools
    :type: LaunchVehicleExportTools

    Return the LaunchVehicleExportTools interface.

.. py:property:: graphics
    :canonical: br.steak.core.stkobjects.LaunchVehicle.graphics
    :type: LaunchVehicleGraphics

    Get the launch vehicle's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: br.steak.core.stkobjects.LaunchVehicle.graphics_3d
    :type: LaunchVehicleGraphics3D

    Get the launch vehicle's 3D Graphics properties.

.. py:property:: ground_ellipses
    :canonical: br.steak.core.stkobjects.LaunchVehicle.ground_ellipses
    :type: VehicleGroundEllipsesCollection

    Get the launch vehicle's ground ellipses properties.

.. py:property:: laser_environment
    :canonical: br.steak.core.stkobjects.LaunchVehicle.laser_environment
    :type: PlatformLaserEnvironment

    Get the laser environment.

.. py:property:: lighting_maximum_step_central_body_shape
    :canonical: br.steak.core.stkobjects.LaunchVehicle.lighting_maximum_step_central_body_shape
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: lighting_maximum_step_terrain
    :canonical: br.steak.core.stkobjects.LaunchVehicle.lighting_maximum_step_terrain
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: radar_cross_section
    :canonical: br.steak.core.stkobjects.LaunchVehicle.radar_cross_section
    :type: RadarCrossSectionInheritable

    Return the radar cross sectoin.

.. py:property:: rf_environment
    :canonical: br.steak.core.stkobjects.LaunchVehicle.rf_environment
    :type: PlatformRFEnvironment

    Get the RF environment.

.. py:property:: space_environment
    :canonical: br.steak.core.stkobjects.LaunchVehicle.space_environment
    :type: SpaceEnvironment

    Return the launch vehicle's SpaceEnvironment properties.

.. py:property:: trajectory
    :canonical: br.steak.core.stkobjects.LaunchVehicle.trajectory
    :type: IPropagator

    Get the launch vehicle's trajectory properties.

.. py:property:: trajectory_supported_types
    :canonical: br.steak.core.stkobjects.LaunchVehicle.trajectory_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: trajectory_type
    :canonical: br.steak.core.stkobjects.LaunchVehicle.trajectory_type
    :type: PropagatorType

    Get the propagator type used by the launch vehicle.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: br.steak.core.stkobjects.LaunchVehicle.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.


Method detail
-------------










.. py:method:: is_attitude_type_supported(self, attitude: VehicleAttitude) -> bool
    :canonical: br.steak.core.stkobjects.LaunchVehicle.is_attitude_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attitude** : :obj:`~VehicleAttitude`


    :Returns:

        :obj:`~bool`

.. py:method:: is_trajectory_type_supported(self, trajectory: PropagatorType) -> bool
    :canonical: br.steak.core.stkobjects.LaunchVehicle.is_trajectory_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **trajectory** : :obj:`~PropagatorType`


    :Returns:

        :obj:`~bool`








.. py:method:: set_attitude_type(self, attitude: VehicleAttitude) -> None
    :canonical: br.steak.core.stkobjects.LaunchVehicle.set_attitude_type

    Set the type of attitude profile used by the launch vehicle.

    :Parameters:

        **attitude** : :obj:`~VehicleAttitude`


    :Returns:

        :obj:`~None`

.. py:method:: set_trajectory_type(self, trajectory: PropagatorType) -> None
    :canonical: br.steak.core.stkobjects.LaunchVehicle.set_trajectory_type

    Set the propagator type.

    :Parameters:

        **trajectory** : :obj:`~PropagatorType`


    :Returns:

        :obj:`~None`








