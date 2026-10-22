
The ``stkobjects`` module
=========================


.. py:module:: br.ok.core.stkobjects


Summary
-------

.. tab-set::

    .. tab-item:: Subpackages

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:obj:`~br.ok.core.stkobjects.aviator`

    .. tab-item:: Submodules

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:mod:`~br.ok.core.stkobjects.astrogator`


    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.ok.core.stkobjects.IAccessAdvanced`
              - Interface for configuring advanced targeting access computation properties.

            * - :py:class:`~br.ok.core.stkobjects.IAccessConstraint`
              - AccessConstraint used to access the AccessConstraint attributes.

            * - :py:class:`~br.ok.core.stkobjects.IAccessConstraintMinMaxBase`
              - Access Constraint used for min/max constraints.

            * - :py:class:`~br.ok.core.stkobjects.IAccessInterval`
              - Base interface for ITimePeriod and TimeIntervalCollection.

            * - :py:class:`~br.ok.core.stkobjects.IAnimation`
              - Provide methods to control scenario animation.

            * - :py:class:`~br.ok.core.stkobjects.IAntennaBeam`
              - Provide access to an antenna beam.

            * - :py:class:`~br.ok.core.stkobjects.IAntennaBeamSelectionStrategy`
              - Provide access to a beam selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.IAntennaContour`
              - IAntennaContour Interface for a antenna's contour properties.

            * - :py:class:`~br.ok.core.stkobjects.IAntennaHFSSDesign`
              - Provide access to the properties and methods defining an HFSS design.

            * - :py:class:`~br.ok.core.stkobjects.IAntennaModel`
              - Provide access to the properties and methods defining an antenna model.

            * - :py:class:`~br.ok.core.stkobjects.IAntennaModelOpticalSimple`
              - Provide access to the properties and methods defining a simple optical antenna model.

            * - :py:class:`~br.ok.core.stkobjects.IAreaTypeData`
              - Base interface IAreaTypeData. AreaTypePatternCollection and AreaTypeEllipse derive from it.

            * - :py:class:`~br.ok.core.stkobjects.IAtmosphericAbsorptionModel`
              - Provide access to the properties and methods an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.IAtmosphericAbsorptionModelTIREM`
              - Provide access to the properties and methods of the TIREM atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.IAtmosphericTurbulenceModel`
              - Provide access to a refractive index structure parameter model.

            * - :py:class:`~br.ok.core.stkobjects.IAzElMaskData`
              - Base interface IAzElMaskData. SensorAzElMaskFile implements this interface.

            * - :py:class:`~br.ok.core.stkobjects.IBeamformer`
              - Provide access to the properties and methods defining a beamformer.

            * - :py:class:`~br.ok.core.stkobjects.ICelestialBodyInformation`
              - The interface represents information associated with a celestial body.

            * - :py:class:`~br.ok.core.stkobjects.ICelestialBodyInformationCollection`
              - Represents a collection of celestial bodies.

            * - :py:class:`~br.ok.core.stkobjects.IChainTimePeriod`
              - Chain time period options.

            * - :py:class:`~br.ok.core.stkobjects.IClassicalLocation`
              - Base Interface of all IClassicalLocation* interfaces.

            * - :py:class:`~br.ok.core.stkobjects.IClassicalSizeShape`
              - Base Interface for SizeShape property. ClassicalSizeShapeAltitude, ClassicalSizeShapeMeanMotion, ClassicalSizeShapePeriod, ClassicalSizeShapeRadius and ClassicalSizeShapeSemimajorAxis derive from this.

            * - :py:class:`~br.ok.core.stkobjects.ICloneable`
              - Interface for a component.

            * - :py:class:`~br.ok.core.stkobjects.ICloudsAndFogFadingLossModel`
              - Provide access to the properties and methods for Clouds and Fog loss models.

            * - :py:class:`~br.ok.core.stkobjects.ICommSystemAccessEventDetection`
              - Provide access to the properties an access event detection algorithm.

            * - :py:class:`~br.ok.core.stkobjects.ICommSystemAccessSamplingMethod`
              - Provide access to the properties for the sampling method.

            * - :py:class:`~br.ok.core.stkobjects.ICommSystemLinkSelectionCriteria`
              - Provide access to a link selection criteria.

            * - :py:class:`~br.ok.core.stkobjects.IComponentInfo`
              - Interface for a component.

            * - :py:class:`~br.ok.core.stkobjects.IComponentLinkEmbedControl`
              - Interface for a control which manages the linking or embedding of a component from the component browser.

            * - :py:class:`~br.ok.core.stkobjects.IConstellationConstraintRestriction`
              - A base interface for all interfaces returned by the Restriction property of the ConstellationConstraints interface. It can be cast to ConstellationConstraintObjectRestriction.

            * - :py:class:`~br.ok.core.stkobjects.ICoverageBounds`
              - Base interface for ICoverageBoundsCustom, CoverageBoundsGlobal, CoverageBoundsLatitude, CoverageBoundsLatitudeLines, CoverageBoundsLongitudeLines, CoverageBoundsCustomBoundary.

            * - :py:class:`~br.ok.core.stkobjects.ICoverageResolution`
              - Base interface for CoverageResolutionArea, CoverageResolutionDistance and CoverageResolutionLatLon, used to define coverage resolution (spacing between grid points).

            * - :py:class:`~br.ok.core.stkobjects.IDataProvider`
              - Represents the Sub Data Provider (i.e. ``Fixed`` in ``Cartesian Position`` group on satellites, or ``Cartesian Position`` on facilities).

            * - :py:class:`~br.ok.core.stkobjects.IDataProviderInfo`
              - Provide methods for retrieving the information about data providers.

            * - :py:class:`~br.ok.core.stkobjects.IDelaunayActionVariable`
              - Interface for Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~br.ok.core.stkobjects.IDemodulatorModel`
              - Provide access to the properties and methods defining a demodulator model.

            * - :py:class:`~br.ok.core.stkobjects.IDirectionProvider`
              - Provide access to the properties and methods defining an direction provider.

            * - :py:class:`~br.ok.core.stkobjects.IDisplayDistance`
              - Base interface IDisplayDistance. ISensorProjectionDisplayDistance, SensorProjectionConstantAltitude and SensorProjectionObjectAltitude derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IDisplayTime`
              - The display time interface.

            * - :py:class:`~br.ok.core.stkobjects.IDisplayTimesData`
              - Base Interface IDisplayTimesData. TimeIntervalCollection, DisplayTimesDuringAccess and DisplayTimesTimeComponent derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IElementConfiguration`
              - Provide access to the properties and methods defining an element configuration.

            * - :py:class:`~br.ok.core.stkobjects.IElementConfigurationPolygon`
              - Provide access to the properties and methods defining a polygon element configuration.

            * - :py:class:`~br.ok.core.stkobjects.IEOIR`
              - Property used to access IEOIR interface.

            * - :py:class:`~br.ok.core.stkobjects.IEOIRShapeObject`
              - A shape object interface.

            * - :py:class:`~br.ok.core.stkobjects.IEventDetectionStrategy`
              - Define a base interface for the event detection strategies.

            * - :py:class:`~br.ok.core.stkobjects.IFigureOfMeritDefinition`
              - Figure of Merit definition.

            * - :py:class:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :py:class:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionData`
              - IFigureOfMeritDefinitionData.

            * - :py:class:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.IFigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :py:class:`~br.ok.core.stkobjects.IFigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :py:class:`~br.ok.core.stkobjects.IFigureOfMeritNavigationAccuracyMethod`
              - Navigation Accuracy Figure of Merit type.

            * - :py:class:`~br.ok.core.stkobjects.IFlightPathAngle`
              - Base Interface IFlightPathAngle. MixedSphericalFlightPathAngleHorizontal, MixedSphericalFlightPathAngleVertical, SphericalFlightPathAngleHorizontal and SphericalFlightPathAngleVertical derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IGeodeticSize`
              - Base Interface IGeodeticSize. DeticSizeAltitude and DeticSizeRadius derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IGraphics3DMarkerData`
              - Base Interface IGraphics3DMarkerData.

            * - :py:class:`~br.ok.core.stkobjects.IGraphics3DModel`
              - IGraphics3DModel used to access the 3D model attributes.

            * - :py:class:`~br.ok.core.stkobjects.IGraphics3DModelData`
              - IGraphics3DModelData base interface. Graphics3DModelFile and Graphics3DModelCollection derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`
              - IGraphics3DReferenceAnalysisWorkbenchComponent used to access the shared properties of all 3D RefCrdn.

            * - :py:class:`~br.ok.core.stkobjects.IGreatArcGraphics`
              - 2D Graphics common for all Great Arc Vehicles.

            * - :py:class:`~br.ok.core.stkobjects.IGreatArcGraphics3D`
              - 3D Graphics common for all Great Arc Vehicles.

            * - :py:class:`~br.ok.core.stkobjects.IGreatArcVehicle`
              - A base interface for all Great Arc Vehicles.

            * - :py:class:`~br.ok.core.stkobjects.IGroundLocation`
              - Interface containing properties common to ground location objects (i.e. Target, Place, and Facility).

            * - :py:class:`~br.ok.core.stkobjects.IGroundLocationGraphics`
              - IGroundLocationGraphics used to access the 2-d graphics properties for a ground location.

            * - :py:class:`~br.ok.core.stkobjects.IGroundLocationGraphics3D`
              - IGroundLocationGraphics3D Interface. For 3D properties of a ground location.

            * - :py:class:`~br.ok.core.stkobjects.IIonosphericFadingLossModel`
              - Provide access to the properties and methods for an Ionospheric Fading loss model.

            * - :py:class:`~br.ok.core.stkobjects.ILaserAtmosphericLossModel`
              - Provide access to the properties and methods for a laser atmospheric absorption loss model.

            * - :py:class:`~br.ok.core.stkobjects.ILaserTroposphericScintillationLossModel`
              - Provide access to the properties and methods for a laser tropospheric scintillation loss model.

            * - :py:class:`~br.ok.core.stkobjects.ILatitudeLongitudeAltitudePosition`
              - Interface to set and retrieve the LLA position type.

            * - :py:class:`~br.ok.core.stkobjects.ILifetimeInformation`
              - Provide the information about the lifetime of the object.

            * - :py:class:`~br.ok.core.stkobjects.IModulatorModel`
              - Provide access to the properties and methods defining a modulator model.

            * - :py:class:`~br.ok.core.stkobjects.IModulatorModelScriptPlugin`
              - Provide access to the properties and methods defining an script plugin modulator model.

            * - :py:class:`~br.ok.core.stkobjects.IOrbitDisplayData`
              - IOrbitDisplayData Interface. PlanetOrbitDisplayTime derives from this.

            * - :py:class:`~br.ok.core.stkobjects.IOrientationAscNode`
              - Base Interface to OrientationLongitudeOfAscending and OrientationRightAscensionOfAscendingNode.

            * - :py:class:`~br.ok.core.stkobjects.IPointingStrategy`
              - Provide the base interface for a pointing strategy.

            * - :py:class:`~br.ok.core.stkobjects.IPolarization`
              - Provide the base interface for the a polarization object.

            * - :py:class:`~br.ok.core.stkobjects.IPolarizationCrossPolLeakage`
              - Provide the interface for polarization cross pol leakage.

            * - :py:class:`~br.ok.core.stkobjects.IPolarizationElliptical`
              - Provide the interface for elliptical polarization.

            * - :py:class:`~br.ok.core.stkobjects.IPolarizationHorizontal`
              - Provide the interface for linear polarization.

            * - :py:class:`~br.ok.core.stkobjects.IPolarizationLinear`
              - Provide the interface for linear polarization.

            * - :py:class:`~br.ok.core.stkobjects.IPolarizationVertical`
              - Provide the interface for linear polarization.

            * - :py:class:`~br.ok.core.stkobjects.IPositionSourceData`
              - Base interface to PlanetPositionCentralBody and PlanetPositionFile.

            * - :py:class:`~br.ok.core.stkobjects.IPropagator`
              - Base vehicle propagator interface.

            * - :py:class:`~br.ok.core.stkobjects.IPropagatorSGP4LoadData`
              - Load Method Data interface.

            * - :py:class:`~br.ok.core.stkobjects.IProvideSpatialInfo`
              - Provide methods for accessing spatial information for an object.

            * - :py:class:`~br.ok.core.stkobjects.IRadarActivity`
              - Provide access to the properties and methods defining radar activity.

            * - :py:class:`~br.ok.core.stkobjects.IRadarContinuousWaveAnalysisMode`
              - Interface which defines an continuous wave analysis.

            * - :py:class:`~br.ok.core.stkobjects.IRadarCrossSectionComputeStrategy`
              - Provide access to the properties and methods defining a radar cross section compute Strategy.

            * - :py:class:`~br.ok.core.stkobjects.IRadarModeBistaticReceiver`
              - Provide access to the properties and methods defining a bistatic receiver mode.

            * - :py:class:`~br.ok.core.stkobjects.IRadarModeBistaticTransmitter`
              - Provide access to the properties and methods defining a bistatic transmitter mode.

            * - :py:class:`~br.ok.core.stkobjects.IRadarModel`
              - Provide access to the properties and methods defining a radar model.

            * - :py:class:`~br.ok.core.stkobjects.IRadarModeMonostatic`
              - Provide access to the properties and methods defining a monostatic mode.

            * - :py:class:`~br.ok.core.stkobjects.IRadarProbabilityOfDetection`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :py:class:`~br.ok.core.stkobjects.IRadarProbabilityOfDetectionCFAR`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :py:class:`~br.ok.core.stkobjects.IRadarPulseIntegration`
              - Interface which defines an integration method.

            * - :py:class:`~br.ok.core.stkobjects.IRadarSTCAttenuation`
              - Provide access to the properties and methods defining a radar STC attenuation.

            * - :py:class:`~br.ok.core.stkobjects.IRadarSTCAttenuationMap`
              - Provide access to the properties and methods defining a radar STC attenuation map.

            * - :py:class:`~br.ok.core.stkobjects.IRadarWaveformSearchTrack`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~br.ok.core.stkobjects.IRainLossModel`
              - Provide access to the properties and methods a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.IReceiverModel`
              - Provide access to the properties and methods defining a receiver model.

            * - :py:class:`~br.ok.core.stkobjects.IReceiverModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin receiver model.

            * - :py:class:`~br.ok.core.stkobjects.IRefractionModelBase`
              - A base interface for the Refraction Models.

            * - :py:class:`~br.ok.core.stkobjects.IReTransmitterModel`
              - Provide access to the properties and methods defining a re-transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.IRFFilterModel`
              - Provide access to the properties and methods defining an RF filter model.

            * - :py:class:`~br.ok.core.stkobjects.ISamplingMethodStrategy`
              - Define a base interface for the sampling method strategies.

            * - :py:class:`~br.ok.core.stkobjects.IScatteringPointModel`
              - Provide access to the properties and methods defining a scattering point model model.

            * - :py:class:`~br.ok.core.stkobjects.IScatteringPointProvider`
              - Provide access to the properties and methods defining a scattering point provider.

            * - :py:class:`~br.ok.core.stkobjects.ISensorPattern`
              - Base interface ISensorPattern. SensorComplexConicPattern, SensorCustomPattern, SensorHalfPowerPattern, SensorRectangularPattern, SensorSARPattern, SensorEOIRPattern and SensorSimpleConicPattern implement this interface.

            * - :py:class:`~br.ok.core.stkobjects.ISensorPointing`
              - Base interface ISensorPointing. SensorPointing3DModel, SensorPointingExternal, SensorPointingFixed, SensorPointingFixedInAxes, SensorPointingGrazingAltitude, SensorPointingTargeted, SensorPointingAlongVector and SensorPointingSchedule implement this interface.

            * - :py:class:`~br.ok.core.stkobjects.ISensorPointingTargetedBoresight`
              - Base interface ISensorPointingTargetedBoresight. SensorPointingTargetedBoresightFixed and SensorPointingTargetedBoresightTrack derive from this.

            * - :py:class:`~br.ok.core.stkobjects.ISensorProjectionDisplayDistance`
              - ISensorProjectionDisplayDistance Interface for setting projection altitude options for a sensor.

            * - :py:class:`~br.ok.core.stkobjects.ISolarActivityConfiguration`
              - Provide access to the properties and methods defining the solar activity configuration.

            * - :py:class:`~br.ok.core.stkobjects.ISRPModelBase`
              - A base interface for solar radiation pressure models.

            * - :py:class:`~br.ok.core.stkobjects.ISTKObject`
              - Represents the instance of STK object.

            * - :py:class:`~br.ok.core.stkobjects.ISTKObjectCollection`
              - Represents a collection of STK objects.

            * - :py:class:`~br.ok.core.stkobjects.ISTKObjectElementCollection`
              - Represents a collection of STK objects.

            * - :py:class:`~br.ok.core.stkobjects.ITargetSelectionMethod`
              - Provide access to the properties and methods defining a target selection method.

            * - :py:class:`~br.ok.core.stkobjects.ITerrainNormData`
              - Base Interface ITerrainNormData. TerrainNormalSlopeAzimuth derives from this interface.

            * - :py:class:`~br.ok.core.stkobjects.ITimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :py:class:`~br.ok.core.stkobjects.ITransmitterModel`
              - Provide access to the properties and methods defining a transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.ITransmitterModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.ITroposphericScintillationFadingLossModel`
              - Provide access to the properties and methods for a TropoSpheric Scintillation Fading loss model.

            * - :py:class:`~br.ok.core.stkobjects.IUrbanTerrestrialLossModel`
              - Provide access to the properties and methods for an urban/terrestrial loss model.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleAttitude`
              - Base interface for vehicle attitude options.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleAttitudeProfile`
              - The base interface that all vehicle attitude profiles are derived from.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleAttitudeSlewBase`
              - Represents an attitude slew base type.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleAttitudeStandard`
              - Standard attitude profile.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleBreakAngle`
              - Base Interface IVehicleBreakAngle. VehicleBreakAngleBreakByLatitude and VehicleBreakAngleBreakByLongitude derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleCoordinateAxes`
              - IVehicleCoordinateAxes.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGPSAlmanacProperties`
              - A common base interface for GPS almanac properties.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DAttributes`
              - Base Interface for Vehicle 2D Graphics Attributes.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DAttributesBasic`
              - Basic 2D Graphics Attributes for a vehicle.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DAttributesDisplayState`
              - Provide access to non-trivial properties of 2D vehicle attributes.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DElevation`
              - Base Interface IVehicleGraphics2DElevation. VehicleGraphics2DElevationGroundElevation, IVehicleGraphics2DElevationsSwathHalfWidth and IVehicleGraphics2DElevationsSwathHalfAngle derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DPass`
              - interface IVehicleGraphics2DPass. VehicleGraphics2DPassShowPasses and VehicleGraphics2DPassResolution derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DTimeComponentsElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DTimeEventType`
              - Base Interface IVehicleGraphics2DTimeEventType. VehicleGraphics2DTimeEventTypeLine, VehicleGraphics2DTimeEventTypeMarker and VehicleGraphics2DTimeEventTypeText derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics3DAttributes`
              - Base Interface IVehicleGraphics3DAttributes. VehicleGraphics3DAttributesBasic and VehicleGraphics3DAttributesIntervals derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics3DBPlaneTargetPointPosition`
              - A base class for BPlane target point position interfaces.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics3DProximity`
              - Base Proximity graphics interface.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics3DProximityAreaObject`
              - A base class that defines methods and properties common to all proximity area objects.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics3DSigmaScale`
              - Base Interface IVehicleGraphics3DSigmaScale. VehicleGraphics3DSigmaScaleScale and VehicleGraphics3DSigmaScaleProbability derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics3DSystemsElementBase`
              - Define methods and properties used to configure the 3D properties of a reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleGraphics3DTickData`
              - Base interface IVehicleGraphics3DTickData. VehicleGraphics3DTickDataLine and VehicleGraphics3DTickDataPoint derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleHPOPDragModel`
              - A base interface for drag models.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleImpact`
              - Base Interface IVehicleImpact. VehicleImpactLocationDetic and VehicleImpactLocationCentric derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleImpactLocation`
              - Base interface IVehicleImpactLocation. VehicleImpactLocationLaunchAzEl and VehicleImpactLocationPoint derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleLaunch`
              - Base interface IVehicleLaunch. LaunchVehicleLocationDetic and LaunchVehicleLocationCentric derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleLaunchControl`
              - Base Interface IVehicleLaunchControl. LaunchVehicleControlFixedApogeeAltitude, LaunchVehicleControlFixedDeltaV, IVehicleLaunchControlDixedDeltaVMinEcc and IVehicleLaunchControlTimeOfFlight derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleLeadTrailData`
              - Base interface IVehicleLeadTrailData.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleLeadTrailDataFraction`
              - The percentage of the leading or trailing portion of a vehicle's path that will display in the 2D or 3D window.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleLeadTrailDataTime`
              - Configure the amount of time to display the vehicle's path in 2D or 3D window.

            * - :py:class:`~br.ok.core.stkobjects.IVehiclePassNumbering`
              - Base Interaface IVehiclePassNumbering. PassBreakNumberingDateOfFirstPass and PassBreakNumberingFirstPassNumber derive from this.

            * - :py:class:`~br.ok.core.stkobjects.IVehiclePointing`
              - Interface for target pointing attitude profiles, which override the basic attitude profile for a satellite and have a selected axis point in the direction of one or more selected targets, subject to applicable access constraints.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleSolarFluxGeoMagnitude`
              - Base Interface IVehicleSolarFluxGeoMagnitude. SolarFluxGeoMagneticValueSettings and SolarFluxGeoMagneticFileSettings derive from this interface.

            * - :py:class:`~br.ok.core.stkobjects.IVehicleWaypointAltitudeReference`
              - Base interface for the altitude references.

            * - :py:class:`~br.ok.core.stkobjects.IVolumetricGridDefinition`
              - Base interface IVolumetricGridDefinition. VolumetricGridSpatialCalculation and VolumetricExternalFile implement this interface.

            * - :py:class:`~br.ok.core.stkobjects.IWaveform`
              - Provide access to the properties and methods defining an antenna model.

            * - :py:class:`~br.ok.core.stkobjects.IWaveformSelectionStrategy`
              - Provide the base interface for a waveform selection strategy.


    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.ok.core.stkobjects.Access`
              - Class defining Access.

            * - :py:class:`~br.ok.core.stkobjects.AccessAdvancedSettings`
              - Class defining advanced Access settings.

            * - :py:class:`~br.ok.core.stkobjects.AccessAllowedTimeIntervals`
              - Allow configuring the access time period using a list of timeline intervals.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraint`
              - Class defining access constraints.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintAnalysisWorkbench`
              - Class related to Analysis Workbench constraints.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection`
              - Collection of Analysis Workbench constraints.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintAnalysisWorkbenchComponent`
              - Class related to Vector constraints.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintAngle`
              - Class defining Angle constraints, limiting access to intervals during which the selected angle is within the specified minimum and maximum limits.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintBackground`
              - Class related to the Background constraint, which constrains access periods based on whether the Earth is or is not in the background.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintCentralBodyObstruction`
              - Class defining constraints in terms of obstruction by a specified central body.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintCollection`
              - Collection of access constraints.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintCondition`
              - Class defining access constraints in terms of lighting conditions.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintElevationRiseSet`
              - Class defining the Elevation Rise-Set constraint.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection`
              - Collection of Exclusion Zones used in Exclusion Zone constraint.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintGrazingAltitude`
              - Class defining the Grazing Altidude constraint.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintGroundTrack`
              - Class related to the Ground Track constraint, which constrains access to the Ascending or Descending side of the Satellite's ground track.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintIntervals`
              - Class defining the Intervals constraint.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintLatitudeLongitudeZone`
              - Class defining the Exclusion Zone constraint.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintMinMaxBase`
              - Class related to defining constraints in terms of minimum and/or maximum values.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintNoiseTemperature`
              - Class defining the System Noise Temperature constraint.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintObjExAngle`
              - Class defining the Object Exclusion Angle constraint.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintPluginMinMax`
              - Class related to defining access plugin constraints in terms of minimum and/or maximum values.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintTimeSlipRange`
              - Class for controlling the use the Time Slip constraint for a missile or launch vehicle, used with the Close Approach Tool.

            * - :py:class:`~br.ok.core.stkobjects.AccessEventDetection`
              - Define properties and methods to configure the event detection strategy used in access computations.

            * - :py:class:`~br.ok.core.stkobjects.AccessGraphics`
              - Class defining 2D Graphics for Access.

            * - :py:class:`~br.ok.core.stkobjects.AccessSampling`
              - Define properties and methods to configure the sampling strategy used in access computations.

            * - :py:class:`~br.ok.core.stkobjects.AccessTargetTime`
              - Class for defining Sensor target times in terms of access.

            * - :py:class:`~br.ok.core.stkobjects.AccessTargetTimesCollection`
              - Collection of access times.

            * - :py:class:`~br.ok.core.stkobjects.AccessTimePeriod`
              - Allow configuring the object's access interval.

            * - :py:class:`~br.ok.core.stkobjects.AdditionalGainLoss`
              - Class defining additional gains and losses.

            * - :py:class:`~br.ok.core.stkobjects.AdditionalGainLossCollection`
              - Class defining a collection of additional gains and losses.

            * - :py:class:`~br.ok.core.stkobjects.AdvCAT`
              - AdvCAT properties.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATAdvancedEllipsoid`
              - AdvCAT advanced ellipsoid properties.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATAdvancedSettings`
              - AdvCAT advanced properties.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATAvailableObjectCollection`
              - Read-only collection of available objects.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATChosenObject`
              - A chosen object.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATChosenObjectCollection`
              - The chosen object collection.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATGraphics3D`
              - AdvCAT VO properties.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATPreFilters`
              - AdvCAT pre-filters properties.

            * - :py:class:`~br.ok.core.stkobjects.Aircraft`
              - Aircraft object.

            * - :py:class:`~br.ok.core.stkobjects.AircraftExportTools`
              - The Aircraft Export Tools.

            * - :py:class:`~br.ok.core.stkobjects.AircraftGraphics`
              - 2D Graphics for an aircraft.

            * - :py:class:`~br.ok.core.stkobjects.AircraftGraphics3D`
              - 3D Graphics properties for an aircraft.

            * - :py:class:`~br.ok.core.stkobjects.Antenna`
              - Class defining the antenna object.

            * - :py:class:`~br.ok.core.stkobjects.AntennaBeam`
              - Class defining an antenna beam.

            * - :py:class:`~br.ok.core.stkobjects.AntennaBeamCollection`
              - Class defining an antenna beam collection.

            * - :py:class:`~br.ok.core.stkobjects.AntennaBeamSelectionStrategy`
              - Class defining a beam selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.AntennaBeamSelectionStrategyAggregate`
              - Class defining a aggregated beam selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.AntennaBeamSelectionStrategyMaximumGain`
              - Class defining a maximum gain beam selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.AntennaBeamSelectionStrategyMinimumBoresightAngle`
              - Class defining a minimum boresight angle beam selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.AntennaBeamSelectionStrategyScriptPlugin`
              - Class defining a script plugin beam selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.AntennaBeamTransmit`
              - Class defining a transmit antenna beam.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourEIRP`
              - Class defining an antenna eirp contour properties.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourFluxDensity`
              - Class defining an antenna flux density contour properties.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourGain`
              - Class defining an antenna gain contour properties.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourGraphics`
              - Class defining contour Graphics properties of a Antenna.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourLevel`
              - Class defining an antenna contour level.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourLevelCollection`
              - Class defining a collection of antenna contour levels.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourRIP`
              - Class defining an antenna rip contour properties.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourSpectralFluxDensity`
              - Class defining an antenna spectral flux density contour properties.

            * - :py:class:`~br.ok.core.stkobjects.AntennaControl`
              - Class defining the properties for a antenna control.

            * - :py:class:`~br.ok.core.stkobjects.AntennaGraphics`
              - Class defining 2D Graphics properties of a Antenna.

            * - :py:class:`~br.ok.core.stkobjects.AntennaGraphics3D`
              - Class defining 3D Graphics properties of a Antenna.

            * - :py:class:`~br.ok.core.stkobjects.AntennaHFSSDesign`
              - Class defining an HFSS design.

            * - :py:class:`~br.ok.core.stkobjects.AntennaHFSSDesignHelixQuadrifilarShort`
              - Class defining an HFSS helix quadrifilar short design.

            * - :py:class:`~br.ok.core.stkobjects.AntennaHFSSDesignSlotGap`
              - Class defining an HFSS slot gap design.

            * - :py:class:`~br.ok.core.stkobjects.AntennaHFSSDesignWireDipole`
              - Class defining an HFSS wire dipole design.

            * - :py:class:`~br.ok.core.stkobjects.AntennaHFSSDesignWireMonopole`
              - Class defining an HFSS wire monopole design.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModel`
              - Class defining a generic antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelANSYSffdFormat`
              - Class defining an antenna pattern ANSYS ffd model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularBessel`
              - Class defining a circular bessel aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularBesselEnvelope`
              - Class defining a circular bessel envelope aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularCosine`
              - Class defining a circular cosine aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularCosinePedestal`
              - Class defining a circular cosine pedestal aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularCosineSquared`
              - Class defining a circular cosine squared aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularCosineSquaredPedestal`
              - Class defining a circular cosine squared pedestal aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularSincIntegerPower`
              - Class defining a circular sinc integer power aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularSincRealPower`
              - Class defining a circular sinc real power aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureCircularUniform`
              - Class defining a circular uniform aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureRectangularCosine`
              - Class defining a rectangular cosine aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureRectangularCosinePedestal`
              - Class defining a rectangular cosine pedestal aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureRectangularCosineSquared`
              - Class defining a rectangular cosine squared aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal`
              - Class defining a rectangular cosine squared pedestal aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureRectangularSincIntegerPower`
              - Class defining a rectangular sinc integer power aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureRectangularSincRealPower`
              - Class defining a rectangular sinc real power aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelApertureRectangularUniform`
              - Class defining a rectangular uniform aperture antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelCosecantSquared`
              - Class defining a cosecant squared antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelDipole`
              - Class defining a dipole antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelElevationAzimuthCuts`
              - Class defining a pattern elevation/azimuth cuts antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelExternal`
              - Class defining a external antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelGaussian`
              - Class defining a gaussian antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelGIMROC`
              - Class defining a GIMROC antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelGPSFRPA`
              - Class defining a GPS FRPA antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelGPSGlobal`
              - Class defining a GPS global antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelHelix`
              - Class defining a helix antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelHemispherical`
              - Class defining a hemispherical antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelHFSSDesign`
              - Class defining an HFSS design antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelHfssEepArray`
              - Class defining an HFSS EEP array antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelIEEE1979`
              - Class defining a IEEE 1979 antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelIntelSat`
              - Class defining a IntelSat antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelIsotropic`
              - Class defining a isotropic antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUBO1213CoPolar`
              - Class defining a ITU-R BO1213 co-polar antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUBO1213CrossPolar`
              - Class defining a ITU-R BO1213 cross-polar antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUF1245`
              - Class defining a ITU-R F1245-3 antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUS1528R12Circular`
              - Class defining a ITU-R S1528 1.2 circular antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUS1528R12Rectangular`
              - Class defining a ITU-R S1528 1.2 rectangular antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUS1528R13`
              - Class defining a ITU-R S1528 1.3 antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUS465`
              - Class defining a ITU-R S465-6 antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUS580`
              - Class defining a ITU-R S580-6 antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUS672Circular`
              - Class defining a ITU-R S672 circular antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUS672Rectangular`
              - Class defining a ITU-R S672-4 rectangular antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelITUS731`
              - Class defining a ITU-R S731 antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelOpticalGaussian`
              - Class defining a gaussian optical antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelOpticalSimple`
              - Class defining a simple optical antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelParabolic`
              - Class defining a parabolic antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelPencilBeam`
              - Class defining a pencil beam antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelPhasedArray`
              - Class defining a phased array antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelRectangularPattern`
              - Class defining a rectangular pattern antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelRemcomUanFormat`
              - Class defining an antenna pattern Remcom uan model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelScriptPlugin`
              - Class defining a script plguin antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelSquareHorn`
              - Class defining a square horn antenna model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelTicraGRASPFormat`
              - Class defining an antenna pattern Ticra GRASP model.

            * - :py:class:`~br.ok.core.stkobjects.AntennaNoiseTemperature`
              - Class defining antenna noise temperature.

            * - :py:class:`~br.ok.core.stkobjects.AntennaSystem`
              - Class defining an antenna system.

            * - :py:class:`~br.ok.core.stkobjects.AntennaVolumeGraphics`
              - Class defining 3D Volume Graphics properties of a Antenna.

            * - :py:class:`~br.ok.core.stkobjects.AntennaVolumeLevel`
              - Class defining an antenna volume level.

            * - :py:class:`~br.ok.core.stkobjects.AntennaVolumeLevelCollection`
              - Class defining a collection of antenna volume levels.

            * - :py:class:`~br.ok.core.stkobjects.AreaTarget`
              - Class defining the AreaTarget object.

            * - :py:class:`~br.ok.core.stkobjects.AreaTargetCommonTasks`
              - Class defining the Area Target Common class.

            * - :py:class:`~br.ok.core.stkobjects.AreaTargetGraphics`
              - Class to define the 2D attributes of an AreaTarget.

            * - :py:class:`~br.ok.core.stkobjects.AreaTargetGraphics3D`
              - Class to define the 3D attributes of an AreaTarget.

            * - :py:class:`~br.ok.core.stkobjects.AreaTypeEllipse`
              - Class defining the AreaTarget AreaType in terms of MajorAxis, MinorAxis and Bearing.

            * - :py:class:`~br.ok.core.stkobjects.AreaTypePattern`
              - Class defining coordinates of the AreaTarget AreaType.

            * - :py:class:`~br.ok.core.stkobjects.AreaTypePatternCollection`
              - Class defining the list of coordinates of the AreaTarget AreaType.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModel`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelCOMPlugin`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelITURP676Version9`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelScriptPlugin`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelSimpleSatcom`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelTIREM550`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelTIREM630`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericTurbulenceModel`
              - Class defining a atmospheric turbulence model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericTurbulenceModelConstant`
              - Class defining a constant atmospheric turbulence model.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericTurbulenceModelHufnagelValley`
              - Class defining a Hufnagel Valley atmospheric turbulence model.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileAlignedAndConstrained`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileAlignmentOffset`
              - Alignment offset for various attitude profiles.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileAviator`
              - The profile used for Aviator aircraft.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileConstraintOffset`
              - Constraint offset for various attitude profiles.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileCoordinatedTurn`
              - Coordinated turn attitude profile for aircraft.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileFixedInAxes`
              - Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileGPS`
              - GPS Attitude profile.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileInertial`
              - Inertially fixed attitude profile: maintains a constant orientation of the body-fixed axes with respect to the inertial axes, using the selected coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfilePrecessingSpin`
              - Precessing Spin attitude profile, in which the spin axis of the satellite specified in the body frame is offset through the nutation angle away from the angular momentum direction specified in the inertial frame.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileSpinAboutSettings`
              - Shared for Spin About Nadir and Spin About Sun Vector profile parameters.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileSpinning`
              - Spinning attitude profile.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfileYawToNadir`
              - A profile useful for satellites with highly elliptical orbits.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeScheduleTimesCollection`
              - List of scheduled accesses.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeScheduleTimesElement`
              - Parameters for scheduled times for target pointing attitude.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeStandardBasic`
              - Basic attitude profile.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeStandardOrbit`
              - Standard attitude profile for satellite.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeStandardRoute`
              - Standard attitude profile for aircraft.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeStandardTrajectory`
              - Standard attitude profile for launch vehicle or missile.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeTorque`
              - Torque file to use in defining integrated attitude.

            * - :py:class:`~br.ok.core.stkobjects.AvailableFeatures`
              - Class is used to check the availability of the features such as Astrogator, etc.

            * - :py:class:`~br.ok.core.stkobjects.BasicAzElMask`
              - The Azimuth-Elevation Mask class.

            * - :py:class:`~br.ok.core.stkobjects.Beamformer`
              - Class defining a beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerASCIIFile`
              - Class defining a beamformer ascii file.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerBlackmanHarris`
              - Class defining a Blackman-Harris tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerCosine`
              - Class defining a cosine tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerCosineX`
              - Class defining a cosine^X tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerCustomTaperFile`
              - Class defining a custom taper file beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerDolphChebyshev`
              - Class defining a Dolph-Chebyshev tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerHamming`
              - Class defining a Hamming tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerHann`
              - Class defining a Hann tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerMVDR`
              - Class defining a beamformer mvdr.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerRaisedCosine`
              - Class defining a raised cosine tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerRaisedCosineSquared`
              - Class defining a raised cosine squared tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerScript`
              - Class defining a beamformer script plugin.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerTaylor`
              - Class defining a Taylor tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerUniform`
              - Class defining a uniform tapered beamformer.

            * - :py:class:`~br.ok.core.stkobjects.BeerBouguerLambertLawLayer`
              - Class defining a row of an input back off vs output back off table.

            * - :py:class:`~br.ok.core.stkobjects.BeerBouguerLambertLawLayerCollection`
              - Class defining collection of Beer-Bouguer-Lamber Law atmosphere layers.

            * - :py:class:`~br.ok.core.stkobjects.CentralBody`
              - A central body coclass.

            * - :py:class:`~br.ok.core.stkobjects.CentralBodyCollection`
              - Central body collection coclass.

            * - :py:class:`~br.ok.core.stkobjects.CentralBodyEllipsoid`
              - Central body's ellipsoid information.

            * - :py:class:`~br.ok.core.stkobjects.CentralBodyTerrainCollection`
              - Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

            * - :py:class:`~br.ok.core.stkobjects.CentralBodyTerrainCollectionElement`
              - Element of collection of terrain associated with central body.

            * - :py:class:`~br.ok.core.stkobjects.Chain`
              - Chain Class is used to access the methods and properties of the STK Chain Object.

            * - :py:class:`~br.ok.core.stkobjects.ChainAnalysisOptions`
              - Class containing analysis options for an object when computing optimal strands of a chain.

            * - :py:class:`~br.ok.core.stkobjects.ChainConnection`
              - Class defining Chain connections.

            * - :py:class:`~br.ok.core.stkobjects.ChainConnectionCollection`
              - Class defining a collection of Chain connections.

            * - :py:class:`~br.ok.core.stkobjects.ChainConstraints`
              - Chain constraints.

            * - :py:class:`~br.ok.core.stkobjects.ChainGraphics`
              - 2D graphics properties of a chain.

            * - :py:class:`~br.ok.core.stkobjects.ChainGraphics2DAnimation`
              - 2D Animation graphics for a chain.

            * - :py:class:`~br.ok.core.stkobjects.ChainGraphics2DStatic`
              - 2D static graphics for a chain.

            * - :py:class:`~br.ok.core.stkobjects.ChainGraphics3D`
              - 3D graphics properties of a chain.

            * - :py:class:`~br.ok.core.stkobjects.ChainOptimalStrandOpts`
              - Do not use this class, as it is deprecated. Use ChainStrandAnalysisOpts instead. Class defining Chain optimal strand options.

            * - :py:class:`~br.ok.core.stkobjects.ChainStrandAnalysisOpts`
              - Class defining Chain strand analysis options.

            * - :py:class:`~br.ok.core.stkobjects.ChainTimePeriod`
              - Chain time period options.

            * - :py:class:`~br.ok.core.stkobjects.ChainUserSpecifiedTimePeriod`
              - User-specified time period for the chain.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalLocationArgumentOfLatitude`
              - Argument of Latitude, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalLocationEccentricAnomaly`
              - Eccentric Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalLocationMeanAnomaly`
              - Mean Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalLocationTimePastAscendingNode`
              - Time Past Ascending Node, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalLocationTimePastPerigee`
              - Time Past Perigee, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalLocationTrueAnomaly`
              - True Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalOrientation`
              - Orbit orientation in the Classical (Keplerian) system.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalSizeShapeAltitude`
              - Orbit size and shape using altitude.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalSizeShapeMeanMotion`
              - Orbit size and shape using Mean Motion and Eccentricity.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalSizeShapePeriod`
              - Orbit size and shape using Period and Eccentricity.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalSizeShapeRadius`
              - Orbit size and shape using Radius.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalSizeShapeSemimajorAxis`
              - Orbit size and shape using Semimajor Axis and Eccentricity.

            * - :py:class:`~br.ok.core.stkobjects.CloudsAndFogFadingLossModel`
              - Class defining a clouds and fog fading loss model.

            * - :py:class:`~br.ok.core.stkobjects.CloudsAndFogFadingLossModelP840Version6`
              - Class defining a clouds and fog Loss ITU-R P.840-6 model.

            * - :py:class:`~br.ok.core.stkobjects.CloudsAndFogFadingLossModelP840Version7`
              - Class defining a clouds and fog Loss ITU-R P.840-7 model.

            * - :py:class:`~br.ok.core.stkobjects.CommRadCartesianLocation`
              - Class defining a location.

            * - :py:class:`~br.ok.core.stkobjects.CommRadComplexNumber`
              - Class defining a complex number.

            * - :py:class:`~br.ok.core.stkobjects.CommRadComplexNumberCollection`
              - Class defining a collection of complex numbers.

            * - :py:class:`~br.ok.core.stkobjects.CommRadPluginConfiguration`
              - Class defining plugin configuration.

            * - :py:class:`~br.ok.core.stkobjects.CommSystem`
              - Class defining a CommSystem object.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessEventDetection`
              - Class defining a CommSystem access options.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessEventDetectionSamplesOnly`
              - Class defining a CommSystem access options.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessEventDetectionSubsample`
              - Class defining a CommSystem access options.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessOptions`
              - Class defining a CommSystem access options.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessSamplingMethod`
              - Class defining a CommSystem access options.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessSamplingMethodAdaptive`
              - Class defining a CommSystem access options.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessSamplingMethodFixed`
              - Class defining a CommSystem access options.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemGraphics`
              - Class defining 2D Graphics properties of a CommSystem.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemGraphics3D`
              - Class defining 3D Graphics properties of a CommSystem.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemLinkSelectionCriteria`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemLinkSelectionCriteriaMaximumElevation`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemLinkSelectionCriteriaMinimumRange`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemLinkSelectionCriteriaScriptPlugin`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~br.ok.core.stkobjects.ComponentAttrLinkEmbedControl`
              - Attribute based component link/embed control.

            * - :py:class:`~br.ok.core.stkobjects.ComponentDirectory`
              - Manages all components.

            * - :py:class:`~br.ok.core.stkobjects.ComponentInfo`
              - Class defining a component.

            * - :py:class:`~br.ok.core.stkobjects.ComponentInfoCollection`
              - The collection of components and component folders.

            * - :py:class:`~br.ok.core.stkobjects.Constellation`
              - Class represents the STK Constellation.

            * - :py:class:`~br.ok.core.stkobjects.ConstellationConstraintObjectRestriction`
              - Class related to the constellation constraint restrictions.

            * - :py:class:`~br.ok.core.stkobjects.ConstellationConstraintRestriction`
              - Class related to the constellation constraint restrictions.

            * - :py:class:`~br.ok.core.stkobjects.ConstellationConstraints`
              - Class related to the constellation constraints.

            * - :py:class:`~br.ok.core.stkobjects.ConstellationGraphics`
              - 2D Graphics properties of the STK Constellation.

            * - :py:class:`~br.ok.core.stkobjects.ConstellationRouting`
              - Routing properties of the STK Constellation.

            * - :py:class:`~br.ok.core.stkobjects.CoverageAdvancedSettings`
              - Advanced Properties.

            * - :py:class:`~br.ok.core.stkobjects.CoverageAreaTargetsCollection`
              - Collection of Area Targets.

            * - :py:class:`~br.ok.core.stkobjects.CoverageAssetListCollection`
              - Asset List.

            * - :py:class:`~br.ok.core.stkobjects.CoverageAssetListElement`
              - Coverage asset.

            * - :py:class:`~br.ok.core.stkobjects.CoverageBoundsCustomBoundary`
              - Custom Boundary.

            * - :py:class:`~br.ok.core.stkobjects.CoverageBoundsCustomRegions`
              - Custom Regions.

            * - :py:class:`~br.ok.core.stkobjects.CoverageBoundsGlobal`
              - Global: grid covering the entire globe.

            * - :py:class:`~br.ok.core.stkobjects.CoverageBoundsLatitude`
              - Latitude Bounds: create a grid between user-specified Minimum and Maximum Latitude boundaries.

            * - :py:class:`~br.ok.core.stkobjects.CoverageBoundsLatitudeLine`
              - Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

            * - :py:class:`~br.ok.core.stkobjects.CoverageBoundsLatitudeLongitudeRegion`
              - LatLon Region: create a region between user-specified Minimum and Maximum Latitude and Longitude boundaries.

            * - :py:class:`~br.ok.core.stkobjects.CoverageBoundsLongitudeLine`
              - Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

            * - :py:class:`~br.ok.core.stkobjects.CoverageDefinition`
              - The CoverageDefinition class.

            * - :py:class:`~br.ok.core.stkobjects.CoverageEllipse`
              - Elliptical area of interest.

            * - :py:class:`~br.ok.core.stkobjects.CoverageEllipseCollection`
              - Collection of elliptical areas of interest.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGraphics`
              - 2D graphics display options for the coverage grid.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGraphics2DAnimation`
              - 2D animation graphics options for the coverage grid.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGraphics2DProgress`
              - Progress graphics for access calculations.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGraphics2DStatic`
              - Static 2D graphics display options for the coverage grid.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGraphics3D`
              - CoverageGraphics3DStatic Class.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGraphics3DAttributes`
              - 3D animation or static graphics options.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGrid`
              - Grid Definition and resolution.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGridInspector`
              - CoverageGridInspector class provides methods to use the grid inspector tool for coverage definition.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGridPointSelection`
              - Represents a set of points selected with the grid inspector.

            * - :py:class:`~br.ok.core.stkobjects.CoverageInterval`
              - Coverage interval: the time period over which coverage is computed.

            * - :py:class:`~br.ok.core.stkobjects.CoverageLatLonBox`
              - Latitude/longitude box area of interest.

            * - :py:class:`~br.ok.core.stkobjects.CoverageLatLonBoxCollection`
              - Collection of latitude/longitude boxes of interest.

            * - :py:class:`~br.ok.core.stkobjects.CoveragePointDefinition`
              - Point Definition: methods and parameters for specifying the location of points on the coverage grid.

            * - :py:class:`~br.ok.core.stkobjects.CoveragePointFileListCollection`
              - Point file list collection.

            * - :py:class:`~br.ok.core.stkobjects.CoverageRegionFilesCollection`
              - Collection of Region Files.

            * - :py:class:`~br.ok.core.stkobjects.CoverageResolutionArea`
              - Area: Define the location of grid coordinates by using the specified area to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~br.ok.core.stkobjects.CoverageResolutionDistance`
              - Distance: Define the location of the grid coordinates by using the specified distance to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~br.ok.core.stkobjects.CoverageResolutionLatLon`
              - Lat/Lon: Determine the location of grid coordinates by specifying a latitude/longitude resolution value.

            * - :py:class:`~br.ok.core.stkobjects.CoverageSelectedGridPoint`
              - Represents a point selected with the grid inspector.

            * - :py:class:`~br.ok.core.stkobjects.CustomPropagationModel`
              - Class defining a custom propatation model.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderCollection`
              - Collection of data providers attached to the current STK object.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderElement`
              - Class defining a data provider element.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderElements`
              - Elements returned by the data provider (e.g. ``x``, ``y``, ``z``).

            * - :py:class:`~br.ok.core.stkobjects.DataProviderFixed`
              - Support for fixed data providers (i.e. non time-dependent like Facility position).

            * - :py:class:`~br.ok.core.stkobjects.DataProviderGroup`
              - Group of sub data providers (e.g. ``Cartesian Position`` on Satellites).

            * - :py:class:`~br.ok.core.stkobjects.DataProviderInterval`
              - Support for interval data providers (e.g. Facility lighting times).

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResult`
              - Results returned by the data provider.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultDataSet`
              - Represents a dataset in the collection of datasets returned by the data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultDataSetCollection`
              - Represents a collection of datasets in the interval returned by the data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultInterval`
              - Represents a interval in the collection of intervals returned by the data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultIntervalCollection`
              - Represents a collection of intervals returned by the data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultStatisticResult`
              - Results returned by statistics computation.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultStatistics`
              - Class used to compute statistics and time varying extremum on data provider result data sets.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultSubSection`
              - Represents a subsection in the data returned by the data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultSubSectionCollection`
              - Represents a collection of subsections returned by the data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultTextMessage`
              - Notification or failure messages returned by the data provider.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultTimeArrayElements`
              - Provide a array result of element values for each time array value.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultTimeVaryingExtremumResult`
              - Results returned by time varying extremum computation.

            * - :py:class:`~br.ok.core.stkobjects.DataProviders`
              - Class defining data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderTimeVarying`
              - Support for time-dependent data providers (e.g. Satellite position).

            * - :py:class:`~br.ok.core.stkobjects.DelaunayG`
              - Delaunay Variable G, the magnitude of the orbital angular momentum.

            * - :py:class:`~br.ok.core.stkobjects.DelaunayGOverSQRTmu`
              - Delaunay Variable G/SQRT(mu), i.e. G divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~br.ok.core.stkobjects.DelaunayH`
              - Value of Delaunay Variable H, which is the Z component of the orbital angular momentum.

            * - :py:class:`~br.ok.core.stkobjects.DelaunayHOverSQRTmu`
              - Delaunay Variable H/SQRT(mu), i.e. H divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~br.ok.core.stkobjects.DelaunayL`
              - Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~br.ok.core.stkobjects.DelaunayLOverSQRTmu`
              - Delaunay Variable L/SQRT(mu), i.e. L divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModel`
              - Class defining a demodulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModel16PSK`
              - Class defining a 16PSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModel8PSK`
              - Class defining a 8PSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelBOC`
              - Class defining a BOC modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelBPSK`
              - Class defining a BPSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelDPSK`
              - Class defining a DPSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelExternal`
              - Class defining a external modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelFSK`
              - Class defining a FSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelMSK`
              - Class defining a MSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelNFSK`
              - Class defining a NFSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelOQPSK`
              - Class defining a OQPSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelQAM1024`
              - Class defining a QAM 1024 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelQAM128`
              - Class defining a QAM 128 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelQAM16`
              - Class defining a QAM 16 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelQAM256`
              - Class defining a QAM 256 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelQAM32`
              - Class defining a QAM 32 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelQAM64`
              - Class defining a QAM 64 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelQPSK`
              - Class defining a QPSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelScriptPlugin`
              - Class defining a script plugin modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :py:class:`~br.ok.core.stkobjects.DeticSizeAltitude`
              - Altitude and Altitude Rate (for Geodetic coordinate type).

            * - :py:class:`~br.ok.core.stkobjects.DeticSizeRadius`
              - Radius and Radius Rate (for Geodetic coordinate type).

            * - :py:class:`~br.ok.core.stkobjects.DirectionProvider`
              - Class defining a direction provider.

            * - :py:class:`~br.ok.core.stkobjects.DirectionProviderASCIIFile`
              - Class defining an ascii file direction provider.

            * - :py:class:`~br.ok.core.stkobjects.DirectionProviderLink`
              - Class defining an link direction provider.

            * - :py:class:`~br.ok.core.stkobjects.DirectionProviderObject`
              - Class defining an object direction provider.

            * - :py:class:`~br.ok.core.stkobjects.DirectionProviderScript`
              - Class defining an script plugin direction provider.

            * - :py:class:`~br.ok.core.stkobjects.DisplayTimesDuringAccess`
              - Class defining display intervals in terms of access to objects.

            * - :py:class:`~br.ok.core.stkobjects.DisplayTimesTimeComponent`
              - Provide methods to configure the display times using Timeline API components.

            * - :py:class:`~br.ok.core.stkobjects.Element`
              - Class defining a phased array element.

            * - :py:class:`~br.ok.core.stkobjects.ElementCollection`
              - Class defining a phased array element collection.

            * - :py:class:`~br.ok.core.stkobjects.ElementConfiguration`
              - Class defining an element configuration.

            * - :py:class:`~br.ok.core.stkobjects.ElementConfigurationASCIIFile`
              - Class defining a ascii file element configuration.

            * - :py:class:`~br.ok.core.stkobjects.ElementConfigurationCircular`
              - Class defining a circular element configuration.

            * - :py:class:`~br.ok.core.stkobjects.ElementConfigurationHexagon`
              - Class defining a hexagon element configuration.

            * - :py:class:`~br.ok.core.stkobjects.ElementConfigurationHfssEepFile`
              - Class defining an HFSS EEP file element configuration.

            * - :py:class:`~br.ok.core.stkobjects.ElementConfigurationLinear`
              - Class defining a linear element configuration.

            * - :py:class:`~br.ok.core.stkobjects.ElementConfigurationPolygon`
              - Class defining a polygon element configuration.

            * - :py:class:`~br.ok.core.stkobjects.EOIR`
              - EOIR interface class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRMaterialElement`
              - EOIRMaterialElement class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRMaterialElementCollection`
              - Collection of material elements.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShape`
              - EOIRShape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeBox`
              - Box shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeCollection`
              - Collection of shapes.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeCone`
              - Cone shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeCoupler`
              - Coupler shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeCustomMesh`
              - CustomMesh shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeCylinder`
              - Cylinder shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeGEOComm`
              - GEOComm shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeLEOComm`
              - LEOComm shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeLEOImaging`
              - LEOImaging shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeNone`
              - None shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeObject`
              - Represents a generic shape object.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapePlate`
              - Plate shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeSphere`
              - Sphere shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeTargetSignature`
              - TargetSignature shape class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRStage`
              - Stage base class.

            * - :py:class:`~br.ok.core.stkobjects.EOIRStagePlume`
              - Plume shape class.

            * - :py:class:`~br.ok.core.stkobjects.EquinoctialSizeShapeMeanMotion`
              - Mean Motion, an element of the Equinoctial coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.EquinoctialSizeShapeSemimajorAxis`
              - Semimajor Axis, an element of the Equinoctial coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.EventDetectionNoSubSampling`
              - Define event detection strategy that uses samples only (without sub-sampling).

            * - :py:class:`~br.ok.core.stkobjects.EventDetectionSubSampling`
              - Event detection strategy involving subsampling.

            * - :py:class:`~br.ok.core.stkobjects.ExportToolStepSize`
              - ExportToolStepSize Class.

            * - :py:class:`~br.ok.core.stkobjects.ExportToolTimePeriod`
              - Specify Time Period.

            * - :py:class:`~br.ok.core.stkobjects.Facility`
              - Class defining the Facility object.

            * - :py:class:`~br.ok.core.stkobjects.FacilityGraphics`
              - 2D Graphics properties of a Facility.

            * - :py:class:`~br.ok.core.stkobjects.FacilityGraphics3D`
              - 3D Graphics properties of a Facility.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMerit`
              - Figure of Merit properties.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritAssetListCollection`
              - List of assets available for specifying range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritAssetListElement`
              - Asset list item (for Navigation Accuracy FOM).

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionAccessConstraint`
              - Access Constraint Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionAccessSeparation`
              - Access Separation Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionAgeOfData`
              - Age of Data Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionDataBest4`
              - Navigation accuracy based on best 4 satellites.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionDataBestN`
              - Navigation accuracy based on best N satellites.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionDataMinimumMaximum`
              - Minimum and maximum data values for navigation accuracy.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionDataMinimumNumberOfAssets`
              - Minimum number of assets.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionDataPercentLevel`
              - Specified percent level for the 'percent below' Navigation Accuracy compute option.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionNavigationAccuracy`
              - Navigation Accuracy.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionRevisitTime`
              - Revisit Time Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionScalarCalculation`
              - Scalar Calculation Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionSimpleCoverage`
              - Simple Coverage Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData`
              - System Age Of Data Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionSystemResponseTime`
              - System Response Time Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionTimeAverageGap`
              - Time Average Gap Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics`
              - FigureOfMeritGraphics Class.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DAttributesAnimation`
              - Animation graphics for a Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DColorOptions`
              - Color options for contour legend.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DContoursAnimation`
              - Animation contour properties.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DLegend`
              - Contour legend properties.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DLegendWindow`
              - Properties of contour legend on 2D map.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection`
              - Collection of Level Attributes.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesElement`
              - 2D graphics attributes of contour levels.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DPositionOnMap`
              - Coordinates of contour legend in pixels on 2D map.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DRampColor`
              - Color ramp method for contours: select start and end colors to define spectrum segment.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DRangeColorOptions`
              - Range color options for contour legend.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DTextOptions`
              - Text display options for contour legend.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics3D`
              - Figure of Merit 3D graphics.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics3DAttributes`
              - 3D static graphics properties for a Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics3DLegendWindow`
              - 3D graphics contours legend.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGridInspector`
              - FigureOfMeritGridInspector class provides methods to use the grid inspector tool for FOM.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritNavigationAccuracyMethodConstant`
              - Constant Value method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritNavigationAccuracyMethodElevationAngle`
              - Elevation Angle method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritSatisfaction`
              - Satisfaction properties for a Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritUncertainties`
              - Receiver range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~br.ok.core.stkobjects.Graphics2DRangeContours`
              - Class defining 2D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DArticulationFile`
              - Class defining the vo articulation file.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DAzElMask`
              - Class to define display labels and adjust the translucency of the 3D azimuth-elevation mask for a facility, place or target.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DBorderWall`
              - Class defining 3D Graphics border wall properties.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DDataDisplayCollection`
              - Collection of 3D Graphics data display text.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DDataDisplayElement`
              - Class defining 3D Graphics data display element.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DDetailThreshold`
              - Class defining detail thresholds as an aid for improving performance when viewing in 3D.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DLabelSwapDistance`
              - Control the level of detail in labels and other screen objects at specified distances.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DMarker`
              - Class defining the 3D marker to represent an object at a specified threshold.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DMarkerFile`
              - Class defining 3D marker file attributes.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DMarkerShape`
              - Class defining the marker type that represents the object in the 3D Graphics window.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DModelArticulation`
              - Class defining 3D model articulations.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DModelCollection`
              - Collection representing 3D model list.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DModelFile`
              - Class defining 3D model file.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DModelglTFImageBased`
              - Class defining glTF Reflection Settings.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DModelItem`
              - Class defining selection and display of 3D models.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DModelPointing`
              - List of pointable model elements.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DModelTransformation`
              - Class to modify transformation values.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DModelTransformationCollection`
              - Collection of available transformations in a model.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DOffset`
              - Class defining 3D offset attributes.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DOffsetAttachment`
              - Class defining attach points for the attachment of lines to objects.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DOffsetLabel`
              - Class defining the offset of the position of an object label in the 3D Graphics window.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DOffsetRotate`
              - Class defining rotation in the object body frame's X, Y and Z directions.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DOffsetTransformation`
              - Class defining model translation in the object body frame's X, Y and Z directions.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DPointableElementsCollection`
              - List of Pointable Elements.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DPointableElementsElement`
              - Pointable elements for 3D model pointing.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DRangeContours`
              - Class defining 3D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DReferenceAngle`
              - Class defining a reference angle (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DReferenceAxes`
              - Class defining a set of reference axes (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DReferencePlane`
              - Class defining a reference plane (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DReferencePoint`
              - Class defining a reference point (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DReferenceVector`
              - Class defining a reference vector (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection`
              - Collection of reference vectors, axes, points, planes and angles (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DVaporTrail`
              - Vapor trail attributes.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DVector`
              - Class defining 3D vectors.

            * - :py:class:`~br.ok.core.stkobjects.GroundVehicle`
              - Ground vehicle object.

            * - :py:class:`~br.ok.core.stkobjects.GroundVehicleExportTools`
              - The GroundVehicle Export Tools.

            * - :py:class:`~br.ok.core.stkobjects.GroundVehicleGraphics`
              - 2D Graphics properties for ground vehicles.

            * - :py:class:`~br.ok.core.stkobjects.GroundVehicleGraphics3D`
              - GroundVehicleGraphics3DVO Class.

            * - :py:class:`~br.ok.core.stkobjects.IntegratorStepSizeControl`
              - Class defining step size control for the HPOP integrator.

            * - :py:class:`~br.ok.core.stkobjects.IntegratorTimeRegularization`
              - Class defining time regularization for the HPOP integrator, i.e. integration the orbit with respect to regularized time.

            * - :py:class:`~br.ok.core.stkobjects.IonosphericFadingLossModel`
              - Class defining a Ionospheric fading loss model.

            * - :py:class:`~br.ok.core.stkobjects.IonosphericFadingLossModelP531Version13`
              - Class defining a Ionospheric fading loss P.531-13 model.

            * - :py:class:`~br.ok.core.stkobjects.KeyValueCollection`
              - A collection of keys and values associated with the keys.

            * - :py:class:`~br.ok.core.stkobjects.LabelNote`
              - Class defining label notes.

            * - :py:class:`~br.ok.core.stkobjects.LabelNoteCollection`
              - Collection representing label notes list.

            * - :py:class:`~br.ok.core.stkobjects.LaserAtmosphericLossModel`
              - Class defining an laser propagation loss model.

            * - :py:class:`~br.ok.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw`
              - Class defining an laser propagation loss model.

            * - :py:class:`~br.ok.core.stkobjects.LaserEnvironment`
              - Class defining the laser environment for an object.

            * - :py:class:`~br.ok.core.stkobjects.LaserPropagationChannel`
              - Class defining the properties for laser propagatoin models.

            * - :py:class:`~br.ok.core.stkobjects.LaserTroposphericScintillationLossModel`
              - Class defining an laser tropospheric scintillation loss model.

            * - :py:class:`~br.ok.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814`
              - Class defining an ITU-R P.1814 laser tropospheric scintillation loss model.

            * - :py:class:`~br.ok.core.stkobjects.LatitudeLongitudeAltitudeCentric`
              - Geocentric LLA position.

            * - :py:class:`~br.ok.core.stkobjects.LatitudeLongitudeAltitudeDetic`
              - Geodetic LLA position.

            * - :py:class:`~br.ok.core.stkobjects.LatitudeLongitudeAltitudePosition`
              - Class defining position defined in terms of latitude, longitude and altitude (LLA).

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicle`
              - Launch vehicle object.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleControlFixedApogeeAltitude`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed apogee altitude.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleControlFixedDeltaV`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleControlFixedDeltaVMinimumEccentricity`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V with minimum eccentricity.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleControlFixedTimeOfFlight`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed time of flight.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleExportTools`
              - The LaunchVehicle Export Tools.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleGraphics`
              - 2D Graphics for a launch vehicle.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleGraphics3D`
              - 3D Graphics for a launch vehicle.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleInitialState`
              - Class defining launch vehicle initial state.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleLocationCentric`
              - Class defining geocentric launch latitude, longitude and radius for a Missile or LaunchVehicle.

            * - :py:class:`~br.ok.core.stkobjects.LaunchVehicleLocationDetic`
              - Class defining geodetic launch latitude, longitude and altitude for a Missile or LaunchVehicle.

            * - :py:class:`~br.ok.core.stkobjects.LevelAttribute`
              - Properties defining display of contour levels.

            * - :py:class:`~br.ok.core.stkobjects.LevelAttributeCollection`
              - Collection of properties defining display of contour levels.

            * - :py:class:`~br.ok.core.stkobjects.LineTarget`
              - Line Target Path properties.

            * - :py:class:`~br.ok.core.stkobjects.LineTargetGraphics`
              - The LineTargetGraphics class.

            * - :py:class:`~br.ok.core.stkobjects.LineTargetGraphics3D`
              - The LineTargetGraphics3D class.

            * - :py:class:`~br.ok.core.stkobjects.LineTargetPoint`
              - Line Target Point.

            * - :py:class:`~br.ok.core.stkobjects.LineTargetPointCollection`
              - The collection of points for the line target.

            * - :py:class:`~br.ok.core.stkobjects.LinkMargin`
              - Class defining a link margin computation object.

            * - :py:class:`~br.ok.core.stkobjects.LinkToObject`
              - Class defining a link to an STK object.

            * - :py:class:`~br.ok.core.stkobjects.LocationVectorGeometryToolPoint`
              - The location based upon a Vector Geometry Tool Point.

            * - :py:class:`~br.ok.core.stkobjects.MilitaryStandard2525bSymbols`
              - MilitaryStandard2525bSymbols class provides methods to create 2525b symbols.

            * - :py:class:`~br.ok.core.stkobjects.Missile`
              - Missile object.

            * - :py:class:`~br.ok.core.stkobjects.MissileEOIR`
              - MissileEOIR interface class.

            * - :py:class:`~br.ok.core.stkobjects.MissileExportTools`
              - The Missile Export Tools.

            * - :py:class:`~br.ok.core.stkobjects.MissileGraphics`
              - 2D Graphics for missiles.

            * - :py:class:`~br.ok.core.stkobjects.MissileGraphics3D`
              - 3D Graphics for missiles.

            * - :py:class:`~br.ok.core.stkobjects.MixedSphericalFlightPathAngleHorizontal`
              - Horizontal Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.MixedSphericalFlightPathAngleVertical`
              - Vertical Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.MODTRANLookupTablePropagationModel`
              - Class defining an MODTRAN-based lookup table propagation model.

            * - :py:class:`~br.ok.core.stkobjects.MODTRANPropagationModel`
              - Class defining a MODTRAN propagation model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModel`
              - Class defining a modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModel16PSK`
              - Class defining a 16PSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModel8PSK`
              - Class defining a 8PSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelBOC`
              - Class defining a BOC modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelBPSK`
              - Class defining a BPSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelDPSK`
              - Class defining a DPSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelExternal`
              - Class defining a external modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelFSK`
              - Class defining a FSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelMSK`
              - Class defining a MSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelNFSK`
              - Class defining a NFSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelOQPSK`
              - Class defining a OQPSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelQAM1024`
              - Class defining a QAM 1024 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelQAM128`
              - Class defining a QAM 128 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelQAM16`
              - Class defining a QAM 16 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelQAM256`
              - Class defining a QAM 256 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelQAM32`
              - Class defining a QAM 32 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelQAM64`
              - Class defining a QAM 64 modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelQPSK`
              - Class defining a QPSK modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelScriptPluginCustomPSD`
              - Class defining a custom PSD script plugin modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelScriptPluginIdealPSD`
              - Class defining a ideal PSD script plugin modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :py:class:`~br.ok.core.stkobjects.MTO`
              - Multi-Track Object (MTO).

            * - :py:class:`~br.ok.core.stkobjects.MTOAnalysis`
              - MTO Spatial State Info.

            * - :py:class:`~br.ok.core.stkobjects.MTOAnalysisFieldOfView`
              - MTO Field Of View Computation.

            * - :py:class:`~br.ok.core.stkobjects.MTOAnalysisPosition`
              - MTO Position Computation.

            * - :py:class:`~br.ok.core.stkobjects.MTOAnalysisRange`
              - MTO Range Computation.

            * - :py:class:`~br.ok.core.stkobjects.MTOAnalysisVisibility`
              - MTO Visibility Computation.

            * - :py:class:`~br.ok.core.stkobjects.MTODefaultGraphics2DTrack`
              - 2D graphics attributes for default MTO tracks.

            * - :py:class:`~br.ok.core.stkobjects.MTODefaultGraphics3DTrack`
              - 3D graphics properties for default MTO tracks.

            * - :py:class:`~br.ok.core.stkobjects.MTODefaultTrack`
              - Default MTO track.

            * - :py:class:`~br.ok.core.stkobjects.MTOGlobalTrackOptions`
              - Global MTO track options.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics`
              - MTO 2D Graphics.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics2DFadeTimes`
              - MTO track fade times.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics2DGlobalTrackOptions`
              - Global 2D graphics options for an MTO.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics2DLeadTrailTimes`
              - MTO track lead/trail times.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics2DLine`
              - MTO track line display options.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics2DMarker`
              - Define the 2D graphics attributes of the selected MTO track or tracks.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics2DTrack`
              - 2D graphics attributes for each track in the MTO.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics2DTrackCollection`
              - MTO 2D Graphics Track List.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3D`
              - MTO 3D graphics properties.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DDropLines`
              - MTO droplines.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DGlobalTrackOptions`
              - Global 3D graphics MTO track options.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DMarker`
              - MTO 3D graphics marker options.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DModel`
              - MTO track model options.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DModelArticulation`
              - Class defining MTO model articulations.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DPoint`
              - MTO track 3D marker point options.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DSwapDistances`
              - MTO track 3D swap distances.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DTrack`
              - 3D graphics properties for MTO tracks.

            * - :py:class:`~br.ok.core.stkobjects.MTOGraphics3DTrackCollection`
              - MTO 3D Graphics Track List.

            * - :py:class:`~br.ok.core.stkobjects.MTOTrack`
              - List of MTO tracks with basic information about each.

            * - :py:class:`~br.ok.core.stkobjects.MTOTrackCollection`
              - MTO Track List.

            * - :py:class:`~br.ok.core.stkobjects.MTOTrackPoint`
              - The points defined for the selected track.

            * - :py:class:`~br.ok.core.stkobjects.MTOTrackPointCollection`
              - MTO track point list.

            * - :py:class:`~br.ok.core.stkobjects.ObjectCoverage`
              - Class defining object coverage.

            * - :py:class:`~br.ok.core.stkobjects.ObjectCoverageFigureOfMerit`
              - Class defining the fom on the coverage object tool.

            * - :py:class:`~br.ok.core.stkobjects.ObjectLaserEnvironment`
              - Class defining the laser environment for an object.

            * - :py:class:`~br.ok.core.stkobjects.ObjectLink`
              - Class defining name of an STK object.

            * - :py:class:`~br.ok.core.stkobjects.ObjectLinkCollection`
              - Collection of names of STK objects that are available in the current Scenario.

            * - :py:class:`~br.ok.core.stkobjects.ObjectRFEnvironment`
              - Class defining the RF environment for an object.

            * - :py:class:`~br.ok.core.stkobjects.OceanTides`
              - Class defining the contribution of ocean tides.

            * - :py:class:`~br.ok.core.stkobjects.OnePointAccess`
              - One Point Access.

            * - :py:class:`~br.ok.core.stkobjects.OnePointAccessConstraint`
              - One Point Access Result.

            * - :py:class:`~br.ok.core.stkobjects.OnePointAccessConstraintCollection`
              - Represents the access constraints for the one point access computation.

            * - :py:class:`~br.ok.core.stkobjects.OnePointAccessResult`
              - One Point Access Result.

            * - :py:class:`~br.ok.core.stkobjects.OnePointAccessResultCollection`
              - Represents the data sets for one point access.

            * - :py:class:`~br.ok.core.stkobjects.OrbitState`
              - Class defining orbit state.

            * - :py:class:`~br.ok.core.stkobjects.OrbitStateCartesian`
              - Cartesian coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.OrbitStateClassical`
              - Classical (Keplerian) coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.OrbitStateCoordinateSystem`
              - Selection of coordinate epoch for coordinate systems that do not have pre-established epochs.

            * - :py:class:`~br.ok.core.stkobjects.OrbitStateDelaunay`
              - Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

            * - :py:class:`~br.ok.core.stkobjects.OrbitStateDetic`
              - Geodetic coordinate type (available only with a Fixed coordinate system).

            * - :py:class:`~br.ok.core.stkobjects.OrbitStateEquinoctial`
              - Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

            * - :py:class:`~br.ok.core.stkobjects.OrbitStateMixedSpherical`
              - Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

            * - :py:class:`~br.ok.core.stkobjects.OrbitStateSpherical`
              - Spherical coordinate type: defines the path of an orbit using polar coordinates.

            * - :py:class:`~br.ok.core.stkobjects.OrientationLongitudeOfAscending`
              - Earth-fixed longitude where the satellite crosses the inertial equator from south to north.

            * - :py:class:`~br.ok.core.stkobjects.OrientationRightAscensionOfAscendingNode`
              - Angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane.

            * - :py:class:`~br.ok.core.stkobjects.PassBreak`
              - Satellite Pass Break properties.

            * - :py:class:`~br.ok.core.stkobjects.PassBreakNumberingDateOfFirstPass`
              - Date of first pass for pass numbering.

            * - :py:class:`~br.ok.core.stkobjects.PassBreakNumberingFirstPassNumber`
              - First pass number.

            * - :py:class:`~br.ok.core.stkobjects.PathCollection`
              - Allow adding and removing of paths.

            * - :py:class:`~br.ok.core.stkobjects.Place`
              - Class defining the Place object.

            * - :py:class:`~br.ok.core.stkobjects.PlaceGraphics`
              - 2D Graphics properties of a Place.

            * - :py:class:`~br.ok.core.stkobjects.PlaceGraphics3D`
              - 3D Graphics properties of a Place.

            * - :py:class:`~br.ok.core.stkobjects.Planet`
              - Class defining the Planet object.

            * - :py:class:`~br.ok.core.stkobjects.PlanetCommonTasks`
              - Class defining the Planet Common class.

            * - :py:class:`~br.ok.core.stkobjects.PlanetGraphics`
              - Class defining 2D Graphics properties of a Planet.

            * - :py:class:`~br.ok.core.stkobjects.PlanetGraphics3D`
              - Class defining 3D Graphics properties of a Planet.

            * - :py:class:`~br.ok.core.stkobjects.PlanetOrbitDisplayTime`
              - Class defining display time of a planet's orbit.

            * - :py:class:`~br.ok.core.stkobjects.PlanetPositionCentralBody`
              - Class defining central body used to define Planet object.

            * - :py:class:`~br.ok.core.stkobjects.PlanetPositionFile`
              - Class defining the planetary ephemeris file.

            * - :py:class:`~br.ok.core.stkobjects.PlatformLaserEnvironment`
              - Class defining the laser environment for an platform.

            * - :py:class:`~br.ok.core.stkobjects.PlatformRFEnvironment`
              - Class defining local atmosphere.

            * - :py:class:`~br.ok.core.stkobjects.PointingStrategy`
              - Class defining a pointing strategy.

            * - :py:class:`~br.ok.core.stkobjects.PointingStrategyFixed`
              - Class defining a fixed pointing strategy.

            * - :py:class:`~br.ok.core.stkobjects.PointingStrategySpinning`
              - Class defining a spinning pointing strategy.

            * - :py:class:`~br.ok.core.stkobjects.PointingStrategyTargeted`
              - Class defining a targeted pointing strategy.

            * - :py:class:`~br.ok.core.stkobjects.PointTargetGraphics3DModel`
              - Point properties for a 3D model.

            * - :py:class:`~br.ok.core.stkobjects.Polarization`
              - Class defining an polarization.

            * - :py:class:`~br.ok.core.stkobjects.PolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :py:class:`~br.ok.core.stkobjects.PolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :py:class:`~br.ok.core.stkobjects.PolarizationLeftHandCircular`
              - Class defining a LHC polarization.

            * - :py:class:`~br.ok.core.stkobjects.PolarizationLinear`
              - Class defining a linear polarization.

            * - :py:class:`~br.ok.core.stkobjects.PolarizationRightHandCircular`
              - Class defining a RHC polarization.

            * - :py:class:`~br.ok.core.stkobjects.PolarizationVertical`
              - Class defining a vertical polarization.

            * - :py:class:`~br.ok.core.stkobjects.Preferences`
              - Allow configuring STK preferences.

            * - :py:class:`~br.ok.core.stkobjects.PreferencesConnect`
              - Allow configuring connect preferences.

            * - :py:class:`~br.ok.core.stkobjects.PreferencesPythonPlugins`
              - Allow configuring Python plugin preferences.

            * - :py:class:`~br.ok.core.stkobjects.PreferencesVDF`
              - Allow configuring VDF preferences.

            * - :py:class:`~br.ok.core.stkobjects.Priority`
              - Class defining a target priority.

            * - :py:class:`~br.ok.core.stkobjects.PriorityCollection`
              - Class defining a priority data collection.

            * - :py:class:`~br.ok.core.stkobjects.ProgressBarEventArguments`
              - Represents a structure used by the Percent Complete events.

            * - :py:class:`~br.ok.core.stkobjects.PropagationChannel`
              - Class defining the propagation channel.

            * - :py:class:`~br.ok.core.stkobjects.Propagator11Parameters`
              - The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

            * - :py:class:`~br.ok.core.stkobjects.Propagator11ParametersDescriptor`
              - 11-Param file definition.

            * - :py:class:`~br.ok.core.stkobjects.Propagator11ParametersDescriptorCollection`
              - A collection of 11-Parameter files.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorAviator`
              - Class defining the Mission Modler propagator for an Aircraft.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorBallistic`
              - Class defining the ballistic propagator for a Missile.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorDefinitionExportTool`
              - PropagatorDefinitionExportTool Class.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorGPS`
              - GPS propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorGreatArc`
              - Class defining the Great Arc propagator for an Aircraft, Ship or GroundVehicle.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorHPOP`
              - Class defining the High Precision Orbit Propagator (HPOP).

            * - :py:class:`~br.ok.core.stkobjects.PropagatorHPOPStaticForceModelSettings`
              - Class defining static force model options for the HPOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection`
              - Collection of third-body gravity options for the LOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorHPOPThirdBodyGravityElement`
              - Class defining third-body gravity options for the LOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorJ2Perturbation`
              - Class defining the J2 perturbation propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorJ4Perturbation`
              - Class defining the J4 perturbation propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorLOP`
              - Class defining the Long-term Orbit Predictor (LOP).

            * - :py:class:`~br.ok.core.stkobjects.PropagatorLOPThirdBodyGravity`
              - Third body gravity options for Long-range Orbit Predictor (LOP) propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorRealtime`
              - Realtime propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorRealtimeCartesianPoints`
              - PropagatorRealtimeCartesianPoints Class.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorRealtimeDeticPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorRealtimeHeadingPitch`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorRealtimePointBuilder`
              - Allow the user to create vehicle's ephemeris by appending ephemeris points.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorRealtimeUTMPoints`
              - Add one ephemeris point.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4`
              - Class defining the SGP4 propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4AutoUpdate`
              - SGP4 AutoUpdate.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4AutoUpdateFileSource`
              - Configure the SGP4 automatic updates using file(s).

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4AutoUpdateOnlineSource`
              - Configure the SGP4 automatic updates using online source (AGI server).

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4AutoUpdateProperties`
              - SGP4 AutoUpdate properties.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4CommonTasks`
              - Most commonly used functionality when working with SGP4 propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4LoadFile`
              - SGP4 propagator. Allows the user to load segments from file.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4OnlineLoad`
              - SGP4 propagator. Allows the user to load segments from online.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4PropagatorSettings`
              - Encapsulates the SGP4 propagator settings.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4Segment`
              - SGP4 propagator segment.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4SegmentCollection`
              - Set of Trajectories.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSimpleAscent`
              - Class defining the simple ascent propagator for a launch vehicle.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSP3`
              - The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSP3File`
              - SP3 file data.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSP3FileCollection`
              - A collection of SP3 files.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSPICE`
              - Class defining the SPICE propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSPICESegment`
              - SPICE propagator segment.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSPICESegmentsCollection`
              - Collection of segments for a vehicle.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSTKExternal`
              - Class defining the STK External propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorTwoBody`
              - Class defining the two body propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorUserExternal`
              - Class defining the user-external propagator.

            * - :py:class:`~br.ok.core.stkobjects.Radar`
              - Class defining the radar object.

            * - :py:class:`~br.ok.core.stkobjects.RadarAccessGraphics`
              - Class defining access graphics properties of a Radar.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivity`
              - Class defining radar activity.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityAlwaysActive`
              - Class defining radar always active activity.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityAlwaysInactive`
              - Class defining radar always active inactivity.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityTimeComponentList`
              - Class defining a radar time component list activity.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityTimeComponentListCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityTimeComponentListElement`
              - Class defining an element of the time components activity list.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityTimeIntervalList`
              - Class defining a radar time component list activity.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityTimeIntervalListCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityTimeIntervalListElement`
              - Class defining an element of the time components activity list.

            * - :py:class:`~br.ok.core.stkobjects.RadarAntennaBeam`
              - Class defining a radar antenna beam.

            * - :py:class:`~br.ok.core.stkobjects.RadarAntennaBeamCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~br.ok.core.stkobjects.RadarClutter`
              - Class defining a radar clutter.

            * - :py:class:`~br.ok.core.stkobjects.RadarContinuousWaveAnalysisModeFixedTime`
              - Class defining the continuous wave fixed time analysis mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarContinuousWaveAnalysisModeGoalSNR`
              - Class defining the continuous wave goal SNR analysis mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSection`
              - Class defining a radar cross section.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionComputeStrategy`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionComputeStrategyAnsysCSVFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionComputeStrategyConstantValue`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionComputeStrategyExternalFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionComputeStrategyPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionComputeStrategyScriptPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionContourLevel`
              - Class defining an radar cross section contour level.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionContourLevelCollection`
              - Class defining a collection of radar cross section contour levels.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionFrequencyBand`
              - Class defining a inheritable radar cross section frequency band.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionFrequencyBandCollection`
              - Class defining a inheritable radar cross section frequency band collection.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionGraphics`
              - Class defining graphics properties of radar cross section.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionGraphics3D`
              - Class defining 3D Graphics properties of radar cross section.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionInheritable`
              - Class defining a inheritable radar cross section.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionModel`
              - Class defining a radar cross section model.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionVolumeGraphics`
              - Class defining 3D Volume Graphics properties of radar cross section.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionVolumeLevel`
              - Class defining an radar cross section volume level.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionVolumeLevelCollection`
              - Class defining a collection of radar cross section volume levels.

            * - :py:class:`~br.ok.core.stkobjects.RadarDopplerClutterFilters`
              - Class defining the properties for doppler clutter filters.

            * - :py:class:`~br.ok.core.stkobjects.RadarGraphics`
              - Class defining 2D Graphics properties of a Radar.

            * - :py:class:`~br.ok.core.stkobjects.RadarGraphics3D`
              - Class defining 3D Graphics properties of a Radar.

            * - :py:class:`~br.ok.core.stkobjects.RadarJamming`
              - Class defining radar jamming.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeBistaticReceiver`
              - Class defining a bistatic receiver radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeBistaticReceiverSAR`
              - Class defining a bistatic receiver sar radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeBistaticReceiverSearchTrack`
              - Class defining a bistatic receiver search/track radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeBistaticTransmitter`
              - Class defining a bistatic transmitter radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeBistaticTransmitterSAR`
              - Class defining a bistatic transmitter sar radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeBistaticTransmitterSearchTrack`
              - Class defining a bistatic transmitter search/track radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModel`
              - Class defining a generic radar model.

            * - :py:class:`~br.ok.core.stkobjects.RadarModelBistaticReceiver`
              - Class defining a bistatic receiver radar model.

            * - :py:class:`~br.ok.core.stkobjects.RadarModelBistaticTransmitter`
              - Class defining a bistatic transmitter radar model.

            * - :py:class:`~br.ok.core.stkobjects.RadarModelMonostatic`
              - Class defining a monostatic radar model.

            * - :py:class:`~br.ok.core.stkobjects.RadarModelMultifunction`
              - Class defining a multifunction radar model.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeMonostatic`
              - Class defining a monostatic radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeMonostaticSAR`
              - Class defining a monostatic sar radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModeMonostaticSearchTrack`
              - Class defining a monostatic search/track radar mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarModulator`
              - Class defining a radar modulator.

            * - :py:class:`~br.ok.core.stkobjects.RadarMultifunctionDetectionProcessing`
              - Class defining multifunction radar detection processing.

            * - :py:class:`~br.ok.core.stkobjects.RadarMultifunctionWaveformStrategySettings`
              - Class defining the waveform selection strategy settings.

            * - :py:class:`~br.ok.core.stkobjects.RadarMultipathGraphics`
              - Class defining multipath graphics properties of a Radar.

            * - :py:class:`~br.ok.core.stkobjects.RadarProbabilityOfDetection`
              - Class defining the probability of detection.

            * - :py:class:`~br.ok.core.stkobjects.RadarProbabilityOfDetectionCFAR`
              - Class defining the probability of detection cfar.

            * - :py:class:`~br.ok.core.stkobjects.RadarProbabilityOfDetectionCFARCellAveraging`
              - Class defining the probability of detection cell averaging cfar.

            * - :py:class:`~br.ok.core.stkobjects.RadarProbabilityOfDetectionCFAROrderedStatistics`
              - Class defining the probability of detection ordered statistics cfar.

            * - :py:class:`~br.ok.core.stkobjects.RadarProbabilityOfDetectionNonCFAR`
              - Class defining the non CFAR probability of detection cfar.

            * - :py:class:`~br.ok.core.stkobjects.RadarProbabilityOfDetectionPlugin`
              - Class defining the probability of detection plugin.

            * - :py:class:`~br.ok.core.stkobjects.RadarPulseIntegrationFixedNumberOfPulses`
              - Class defining the fixed number of pulses integration method.

            * - :py:class:`~br.ok.core.stkobjects.RadarPulseIntegrationGoalSNR`
              - Class defining the goal SNR integration method.

            * - :py:class:`~br.ok.core.stkobjects.RadarReceiver`
              - Class defining the radar transmitter.

            * - :py:class:`~br.ok.core.stkobjects.RadarSTCAttenuation`
              - Class defining an radar stc.

            * - :py:class:`~br.ok.core.stkobjects.RadarSTCAttenuationDecayFactor`
              - Class defining an radar decay factor stc.

            * - :py:class:`~br.ok.core.stkobjects.RadarSTCAttenuationDecaySlope`
              - Class defining an radar decay slope stc.

            * - :py:class:`~br.ok.core.stkobjects.RadarSTCAttenuationMapAzimuthRange`
              - Class defining an radar stc azimuth-range map.

            * - :py:class:`~br.ok.core.stkobjects.RadarSTCAttenuationMapElevationRange`
              - Class defining an radar stc elevation-range map.

            * - :py:class:`~br.ok.core.stkobjects.RadarSTCAttenuationMapRange`
              - Class defining an radar stc range map.

            * - :py:class:`~br.ok.core.stkobjects.RadarSTCAttenuationPlugin`
              - Class defining an radar stc Com Plugin.

            * - :py:class:`~br.ok.core.stkobjects.RadarTransmitter`
              - Class defining the radar transmitter.

            * - :py:class:`~br.ok.core.stkobjects.RadarTransmitterMultifunction`
              - Class defining the multifunction radar transmitter.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous`
              - Class defining a bistatic receiver continuous waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF`
              - Class defining a bistatic receiver fixed PRF waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformBistaticTransmitterSearchTrackContinuous`
              - Class defining a bistatic transmitter continuous waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformBistaticTransmitterSearchTrackFixedPRF`
              - Class defining a bistatic transmitter fixed PRF waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous`
              - Class defining a monostatic continuous waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF`
              - Class defining a monostatic fixed PRF waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformSarPulseDefinition`
              - Class defining the pulse definition for a SAR waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformSarPulseIntegration`
              - Class defining the pulse integration for a SAR waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformSearchTrackPulseDefinition`
              - Class defining the pulse definition for a search track waveform.

            * - :py:class:`~br.ok.core.stkobjects.RadiationPressure`
              - Class defining solar radiation pressure on a vehicle.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModel`
              - Class defining a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModelCCIR1983`
              - Class defining a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModelCrane1982`
              - Class defining a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModelCrane1985`
              - Class defining a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModelITURP618Version10`
              - Class defining a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModelITURP618Version12`
              - Class defining a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModelITURP618Version13`
              - Class defining a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModelScriptPlugin`
              - Class defining a rain loss model.

            * - :py:class:`~br.ok.core.stkobjects.ReceivePolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :py:class:`~br.ok.core.stkobjects.ReceivePolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :py:class:`~br.ok.core.stkobjects.ReceivePolarizationLeftHandCircular`
              - Class defining a LHC polarization.

            * - :py:class:`~br.ok.core.stkobjects.ReceivePolarizationLinear`
              - Class defining a linear polarization.

            * - :py:class:`~br.ok.core.stkobjects.ReceivePolarizationRightHandCircular`
              - Class defining a RHC polarization.

            * - :py:class:`~br.ok.core.stkobjects.ReceivePolarizationVertical`
              - Class defining a receive vertical polarization.

            * - :py:class:`~br.ok.core.stkobjects.Receiver`
              - Class defining the receiver object.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverGraphics`
              - Class defining 2D Graphics properties of a Receiver.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverGraphics3D`
              - Class defining 3D Graphics properties of a Receiver.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModel`
              - Class defining a generic receiver model.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelCable`
              - Class defining a cable receiver model.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelComplex`
              - Class defining a complex receiver model.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelLaser`
              - Class defining a laser receiver model.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelMedium`
              - Class defining a medium receiver model.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelMultibeam`
              - Class defining a mutibeam receiver model.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelScriptPluginLaser`
              - Class defining a laser script plugin receiver model.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelScriptPluginRF`
              - Class defining a RF script plugin receiver model.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelSimple`
              - Class defining a simple receiver model.

            * - :py:class:`~br.ok.core.stkobjects.RefractionCoefficients`
              - Coefficients for a polynomial in time_since_year_start that models the refraction index.

            * - :py:class:`~br.ok.core.stkobjects.RefractionModelEffectiveRadiusMethod`
              - Effective Radius Method.

            * - :py:class:`~br.ok.core.stkobjects.RefractionModelITURP8344`
              - ITU-R P.834-4.

            * - :py:class:`~br.ok.core.stkobjects.RefractionModelSCFMethod`
              - SCF Method.

            * - :py:class:`~br.ok.core.stkobjects.RepeatGroundTrackNumbering`
              - Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

            * - :py:class:`~br.ok.core.stkobjects.ReTransmitterModelComplex`
              - Class defining a complex re-transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.ReTransmitterModelMedium`
              - Class defining a medium re-transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.ReTransmitterModelSimple`
              - Class defining a simple re-transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.RFEnvironment`
              - Class defining the RF environment.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModel`
              - Class defining a generic RF filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelBessel`
              - Class defining a bessel filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelButterworth`
              - Class defining a butterworth filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelChebyshev`
              - Class defining a Chebyshev filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelCosineWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelElliptic`
              - Class defining a elliptic filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelExternal`
              - Class defining a external filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelFIR`
              - Class defining a FIR filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelFIRBoxCar`
              - Class defining a FIR box car filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelGaussianWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelHammingWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelIIR`
              - Class defining a IIR box car filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelRaisedCosine`
              - Class defining a raised cosine filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelRCLowPass`
              - Class defining a rc low pass filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelRectangular`
              - Class defining a rectangular filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelRootRaisedCosine`
              - Class defining a root raised cosine filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelScriptPlugin`
              - Class defining a script plugin filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelSinc`
              - Class defining a sinc filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelSincEnvelopeSinc`
              - Class defining a Sinc Envelope Sinc filter model.

            * - :py:class:`~br.ok.core.stkobjects.RFInterference`
              - Class defining radar jamming.

            * - :py:class:`~br.ok.core.stkobjects.RotationRateAndOffset`
              - RotationRateAndOffset Class.

            * - :py:class:`~br.ok.core.stkobjects.SamplingMethodAdaptive`
              - Define an adaptive sampling method.

            * - :py:class:`~br.ok.core.stkobjects.SamplingMethodFixedStep`
              - Define a fixed time-step sampling method.

            * - :py:class:`~br.ok.core.stkobjects.Satellite`
              - Satellite properties.

            * - :py:class:`~br.ok.core.stkobjects.SatelliteCollection`
              - The SatelliteCollection class.

            * - :py:class:`~br.ok.core.stkobjects.SatelliteExportTools`
              - The Satellite Export Tools.

            * - :py:class:`~br.ok.core.stkobjects.SatelliteGraphics`
              - Satellite 2D Graphics properties.

            * - :py:class:`~br.ok.core.stkobjects.SatelliteGraphics3D`
              - 3D Graphics properties of a satellite.

            * - :py:class:`~br.ok.core.stkobjects.SatelliteGraphics3DModel`
              - All Satellite's VO Model properties.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointCollection`
              - Class defining a collection of scattering points.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointCollectionElement`
              - Class defining a scattering point collection element.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointModel`
              - Class defining a scattering point model.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointModelConstantCoefficient`
              - Class defining a constant coefficient scattering point model.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointModelPlugin`
              - Class defining a plugin scattering point model.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointModelWindTurbine`
              - Class defining a wind turbine scattering point model.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProvider`
              - Class defining a scattering point provider.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderCollection`
              - Class defining an scattering point provider collection.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderCollectionElement`
              - Class defining a scattering point provider collection element.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderList`
              - Class defining a scattering point provider list.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderPlugin`
              - Class defining a plugin scattering point provider.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderPointsFile`
              - Class defining a scattring point provider where the points are defined in an ascii text file.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderRangeOverCFARCells`
              - Class defining a range over CFAR cells scattering point provider.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderSinglePoint`
              - Class defining a single point scattring point provider.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderSmoothOblateEarth`
              - Class defining a smooth oblate earth scattering point provider.

            * - :py:class:`~br.ok.core.stkobjects.Scenario`
              - Class defining the Scenario object.

            * - :py:class:`~br.ok.core.stkobjects.Scenario3dFont`
              - Font properties for Scenario 3D Graphics.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioAnimation`
              - Class defining the animation properties of a Scenario.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioAnimationTimePeriod`
              - Configure the scenario's animation time.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioBeforeSaveEventArguments`
              - Contains information about the changes in the object's state.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioDatabase`
              - Class defining database settings of the Scenario.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioDatabaseCollection`
              - Collection of Scenario database settings.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioEarthData`
              - Class defining the Earth Orientation Parameters of a Scenario.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioGraphics`
              - Class defining the 2D Graphics properties of a Scenario.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioGraphics3D`
              - Class defining 3D Graphics properties of the Scenario.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioSpaceEnvironment`
              - SpaceEnvironment settings.

            * - :py:class:`~br.ok.core.stkobjects.ScheduleTime`
              - Class for defining Sensor target times in terms of a specified schedule.

            * - :py:class:`~br.ok.core.stkobjects.ScheduleTimeCollection`
              - Collection of user-scheduled access times.

            * - :py:class:`~br.ok.core.stkobjects.Sensor`
              - Class defining the Sensor class.

            * - :py:class:`~br.ok.core.stkobjects.SensorAccessAdvancedSettings`
              - Sensor's advanced targeting access computation properties.

            * - :py:class:`~br.ok.core.stkobjects.SensorAzElMaskFile`
              - Class to define a Sensor's Azimuth-Elevation mask.

            * - :py:class:`~br.ok.core.stkobjects.SensorCommonTasks`
              - Class defining the Sensor Common class.

            * - :py:class:`~br.ok.core.stkobjects.SensorComplexConicPattern`
              - Class defining the complex conic pattern for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorCustomPattern`
              - Class defining the custom pattern for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBand`
              - Class defining an EOIR band.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandCollection`
              - Class defining the band collection for an EOIR Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRPattern`
              - Class defining the EOIR pattern for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRRadiometricPair`
              - Class defining an Sensitivities item.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRSaturationCollection`
              - Class defining the Saturations collection for an EOIR Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRSensitivityCollection`
              - Class defining the Sensitivities collection for an EOIR Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics`
              - Class defining the 2D Graphics properties of a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3D`
              - Class defining 3D Graphics properties of a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DOffset`
              - Class defining 3D Graphics vertex offset properties of a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DProjectionElement`
              - Represents elements of the space and target projection collections.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DPulse`
              - Class defining 3D pulse properties of a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DSpaceProjectionCollection`
              - Time Dependent Space Projection List.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DTargetProjectionCollection`
              - Time Dependent Target Projection List.

            * - :py:class:`~br.ok.core.stkobjects.SensorHalfPowerPattern`
              - Class defining the half-power pattern for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointing3DModel`
              - Class defining the 3D model pointing type for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingAlongVector`
              - Class defining the along vector pointing type for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingExternal`
              - Class defining the external file-defined pointing type for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingFixed`
              - Class defining the fixed pointing type for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingFixedInAxes`
              - Class defining the fixed in axes pointing type for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingGrazingAltitude`
              - Class defining Grazing Altitude pointing type for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingSchedule`
              - Allow to schedule a sensor to point at a specific location at a specific time.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingSpinning`
              - Class defining the spinning pointing type for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingTargeted`
              - Class defining the targeted pointing type for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingTargetedBoresightFixed`
              - Class defining a targeted Sensor with fixed boresight.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingTargetedBoresightTrack`
              - Class defining a targeted sensor with tracking boresight.

            * - :py:class:`~br.ok.core.stkobjects.SensorProjection`
              - Class defining the projection properties of a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorProjectionConstantAltitude`
              - Class defining projection altitude options for constant altitude for a sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorProjectionDisplayDistance`
              - Class defining projection altitude options for a sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorProjectionObjectAltitude`
              - Class defining projection altitude options for object altitude for a sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorRectangularPattern`
              - Class defining the rectangular pattern for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorSARPattern`
              - Class defining the Synthetic Aperture Radar (SAR) pattern for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorSimpleConicPattern`
              - Class defining the simple conic pattern for a Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorTarget`
              - Class defining a Sensor target.

            * - :py:class:`~br.ok.core.stkobjects.SensorTargetCollection`
              - Class defining the target collection for a target-pointing Sensor.

            * - :py:class:`~br.ok.core.stkobjects.SensorUnknownPattern`
              - Unsupported/unknown sensor pattern.

            * - :py:class:`~br.ok.core.stkobjects.Ship`
              - Ship object.

            * - :py:class:`~br.ok.core.stkobjects.ShipExportTools`
              - The Ship Export Tools.

            * - :py:class:`~br.ok.core.stkobjects.ShipGraphics`
              - 2D Graphics options for a ship.

            * - :py:class:`~br.ok.core.stkobjects.ShipGraphics3D`
              - 3D Graphics attributes for a ship.

            * - :py:class:`~br.ok.core.stkobjects.SolarActivityConfiguration`
              - Class defining a solar activity configuration.

            * - :py:class:`~br.ok.core.stkobjects.SolarActivityConfigurationSolarFlux`
              - Class defining the solar flux configuration.

            * - :py:class:`~br.ok.core.stkobjects.SolarActivityConfigurationSunspotNumber`
              - Class defining sunspot number configuration.

            * - :py:class:`~br.ok.core.stkobjects.SolarFluxGeoMagneticFileSettings`
              - Class defining the option to load a vehicle's solar flux and/or GeoMag properties from an external file.

            * - :py:class:`~br.ok.core.stkobjects.SolarFluxGeoMagneticValueSettings`
              - Class defining the option to enter a vehicle's solar flux and/or GeoMag properties manually, depending on the selected atmospheric density model.

            * - :py:class:`~br.ok.core.stkobjects.SolarRadiationPressureModelGPS`
              - GPS Solar Radiation Pressure Model.

            * - :py:class:`~br.ok.core.stkobjects.SolarRadiationPressureModelPlugin`
              - Plugin Light Reflection Model.

            * - :py:class:`~br.ok.core.stkobjects.SolarRadiationPressureModelPluginSettings`
              - Plugin Light Reflection Model Settings.

            * - :py:class:`~br.ok.core.stkobjects.SolarRadiationPressureModelSpherical`
              - Spherical Solar Radiation Pressure Model.

            * - :py:class:`~br.ok.core.stkobjects.SolidTides`
              - Class defining the contribution of solid tides.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironment`
              - SpaceEnvironment settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentGraphics`
              - Graphics settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticField`
              - Magnetic field settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D`
              - Geomagnetic field graphics settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentMagnitudeFieldLine`
              - Graphics settings for displaying magnetic field lines.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentParticleFlux`
              - Particle Flux settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentRadiation`
              - Radiation model settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection`
              - Collection of dose rate elements computed for a shielding thickness.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentRadiationDoseRateElement`
              - Class defining dose rate information computed for a shielding thickness.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentRadiationEnergyMethodEnergies`
              - Set the electron and proton energies to consider.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentRadiationEnergyValues`
              - Energy values used by the Radiation Environment model.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentRadiationEnvironment`
              - Radiation Environment model settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentSAAContour`
              - SAA settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentScenarioGraphics3D`
              - 3D Graphics settings.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentVehicleTemperature`
              - Vehicle Temperature settings.

            * - :py:class:`~br.ok.core.stkobjects.SpatialState`
              - Represents a position and an attitude of an object.

            * - :py:class:`~br.ok.core.stkobjects.SphericalFlightPathAngleHorizontal`
              - Horizontal Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.SphericalFlightPathAngleVertical`
              - Vertical Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.Star`
              - Class defining the Star object.

            * - :py:class:`~br.ok.core.stkobjects.StarCollection`
              - Represents a collection of stars.

            * - :py:class:`~br.ok.core.stkobjects.StarGraphics`
              - Class defining 2D Graphics properties of a Star.

            * - :py:class:`~br.ok.core.stkobjects.StarGraphics3D`
              - Class defining 3D Graphics properties of a Star.

            * - :py:class:`~br.ok.core.stkobjects.StarInformation`
              - Represents a celestial body information.

            * - :py:class:`~br.ok.core.stkobjects.STKObject`
              - Represents a generic STK object.

            * - :py:class:`~br.ok.core.stkobjects.STKObjectChangedEventArguments`
              - Contains information about the changes in the object's state.

            * - :py:class:`~br.ok.core.stkobjects.STKObjectCutCopyPasteEventArguments`
              - Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

            * - :py:class:`~br.ok.core.stkobjects.STKObjectModelContext`
              - STKObjectModelContext class provides methods to create instance of STKObjectRoot class.

            * - :py:class:`~br.ok.core.stkobjects.STKObjectPreDeleteEventArguments`
              - Arguments for the OnStkObjectPreDelete event.

            * - :py:class:`~br.ok.core.stkobjects.STKObjectRoot`
              - Top-level object in the Object Model Hierarchy.

            * - :py:class:`~br.ok.core.stkobjects.Subset`
              - The Subset class.

            * - :py:class:`~br.ok.core.stkobjects.Swath`
              - Class defining Swath properties.

            * - :py:class:`~br.ok.core.stkobjects.SystemNoiseTemperature`
              - Class defining system noise temperature.

            * - :py:class:`~br.ok.core.stkobjects.Target`
              - Class defining the Target object.

            * - :py:class:`~br.ok.core.stkobjects.TargetGraphics`
              - Class defining 2D Graphics for a Target object.

            * - :py:class:`~br.ok.core.stkobjects.TargetGraphics3D`
              - Class defining 3D Graphics for a Target object.

            * - :py:class:`~br.ok.core.stkobjects.TargetSelectionMethod`
              - Class defining a target selection method.

            * - :py:class:`~br.ok.core.stkobjects.TargetSelectionMethodClosingVelocity`
              - Class defining a closing velocity-based target selection method.

            * - :py:class:`~br.ok.core.stkobjects.TargetSelectionMethodPriority`
              - Class defining a priority-based target selection method.

            * - :py:class:`~br.ok.core.stkobjects.TargetSelectionMethodRange`
              - Class defining a range-based target selection method.

            * - :py:class:`~br.ok.core.stkobjects.Terrain`
              - Class defining terrain data for a Scenario.

            * - :py:class:`~br.ok.core.stkobjects.TerrainCollection`
              - Collection of terrain data files available in the Scenario for visualization and analysis.

            * - :py:class:`~br.ok.core.stkobjects.TerrainNormalSlopeAzimuth`
              - Class defining Slope/Azimuth data for the TerrainNormal.

            * - :py:class:`~br.ok.core.stkobjects.Tileset3D`
              - Class defining Analytical 3DTileset for a Scenario.

            * - :py:class:`~br.ok.core.stkobjects.Tileset3DCollection`
              - Collection of 3DTilesets available in the Scenario for analysis.

            * - :py:class:`~br.ok.core.stkobjects.TimeIntervalCollection`
              - Class defining display intervals.

            * - :py:class:`~br.ok.core.stkobjects.TimeIntervalCollectionReadOnly`
              - Read-only collection of intervals.

            * - :py:class:`~br.ok.core.stkobjects.TimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :py:class:`~br.ok.core.stkobjects.TimePeriodValue`
              - Provide methods and properties to configure a time value.

            * - :py:class:`~br.ok.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable`
              - Class defining an input back off vs output back off table.

            * - :py:class:`~br.ok.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTableRow`
              - Class defining a row of an input back off vs output back off table.

            * - :py:class:`~br.ok.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable`
              - Class defining an input back off vs C/Im table.

            * - :py:class:`~br.ok.core.stkobjects.TransferFunctionInputBackOffVsCOverImTableRow`
              - Class defining a row of an input back off vs C/Im table.

            * - :py:class:`~br.ok.core.stkobjects.TransferFunctionPolynomialCollection`
              - Class defining a collection of polynomial coefficients.

            * - :py:class:`~br.ok.core.stkobjects.Transmitter`
              - Class defining the transmitter object.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterGraphics`
              - Class defining 2D Graphics properties of a Transmitter.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterGraphics3D`
              - Class defining 3D Graphics properties of a Transmitter.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModel`
              - Class defining a generic transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelCable`
              - Class defining a cable transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelComplex`
              - Class defining a complex transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelLaser`
              - Class defining a laser transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelMedium`
              - Class defining a medium transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelMultibeam`
              - Class defining a multibeam transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelScriptPluginLaser`
              - Class defining a laser script plugin transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelScriptPluginRF`
              - Class defining a RF script plugin transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelSimple`
              - Class defining a simple transmitter model.

            * - :py:class:`~br.ok.core.stkobjects.TroposphericScintillationFadingLossModel`
              - Class defining a tropospheric scintillation fading loss model.

            * - :py:class:`~br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12`
              - Class defining a tropospheric scintillation fading loss P.618-12 model.

            * - :py:class:`~br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8`
              - Class defining a tropospheric scintillation fading loss P.618-8 model.

            * - :py:class:`~br.ok.core.stkobjects.UrbanTerrestrialLossModel`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~br.ok.core.stkobjects.UrbanTerrestrialLossModelTwoRay`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~br.ok.core.stkobjects.UrbanTerrestrialLossModelWirelessInSite64`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAccessAdvancedSettings`
              - Vehicle advanced targeting access computation properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeExportTool`
              - VehicleAttitudeExportTool Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeExternal`
              - External attitude (.a) file.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeMaximumSlewAcceleration`
              - Define the maximum slew acceleration by entering maximum overall magnitude. You can constrain the slew acceleration in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeMaximumSlewRate`
              - Define the maximum slew rate by entering a maximum overall magnitude. You can constrain the slew rate in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudePointing`
              - Target pointing attitude parameters.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeRealTime`
              - Real time attitude.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeRealTimeDataReference`
              - Reference attitude profile for the incoming attitude data.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeSlewConstrained`
              - Constrained slew mode.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeSlewFixedRate`
              - Fixed rate slew.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeSlewFixedTime`
              - Fixed time slew.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeTargetSlew`
              - Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitudeTrendingControlAviator`
              - Trending controls for Aviator attitude.

            * - :py:class:`~br.ok.core.stkobjects.VehicleBreakAngleBreakByLatitude`
              - Pass break latitude.

            * - :py:class:`~br.ok.core.stkobjects.VehicleBreakAngleBreakByLongitude`
              - Pass break longitude.

            * - :py:class:`~br.ok.core.stkobjects.VehicleCentralBodies`
              - Satellite Central Bodies.

            * - :py:class:`~br.ok.core.stkobjects.VehicleConsiderAnalysisCollection`
              - The Consider Analysis list for HPOP covariance.

            * - :py:class:`~br.ok.core.stkobjects.VehicleConsiderAnalysisCollectionElement`
              - Item in Consider Analysis list for HPOP covariance.

            * - :py:class:`~br.ok.core.stkobjects.VehicleCoordinateAxesCustom`
              - Custom.

            * - :py:class:`~br.ok.core.stkobjects.VehicleCorrelationListCollection`
              - Collection representing HPOP covariance matrix.

            * - :py:class:`~br.ok.core.stkobjects.VehicleCorrelationListElement`
              - Class representing an element of an HPOP covariance matrix.

            * - :py:class:`~br.ok.core.stkobjects.VehicleCovariance`
              - Class defining HPOP covariance.

            * - :py:class:`~br.ok.core.stkobjects.VehicleDefinition`
              - Pass break definition properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleDuration`
              - Look ahead and look behind duration options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEclipseBodies`
              - Satellite Eclipse Bodies, for defining the eclipse central body list used for lighting computations.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEclipsingBodies`
              - Eclipsing bodies.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEllipseDataCollection`
              - Ellipse Data Collection.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEllipseDataElement`
              - Ground ellipse data.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEOIR`
              - VehicleEOIR interface class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEphemerisBinaryExportTool`
              - VehicleEphemerisBinaryExportTool Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEphemerisCCSDSExportTool`
              - VehicleEphemerisCCSDSExportTool Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEphemerisCCSDSv2ExportTool`
              - The Ephemeris/Attitude Export Tool for CCSDSv2 Ephemeris type.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEphemerisCCSDSv3ExportTool`
              - The Ephemeris/Attitude Export Tool for CCSDSv3 Ephemeris type.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEphemerisCode500ExportTool`
              - VehicleEphemerisCode500ExportTool Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEphemerisExportTool`
              - VehicleEphemerisExportTool Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEphemerisSPICEExportTool`
              - VehicleEphemerisSPICEExportTool Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleExponentialDensityModelParameters`
              - Class defining the Exponential atmospheric density model for the LOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAlmanacProperties`
              - A common base for GPS almanac properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAlmanacPropertiesSEM`
              - SEM almanac properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAlmanacPropertiesSP3`
              - SP3 almanac properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAlmanacPropertiesYUMA`
              - YUMA almanac properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAutoUpdate`
              - GPS AutoUpdate.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAutoUpdateFileSource`
              - GPS automatic updates using almanac file(s).

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAutoUpdateOnlineSource`
              - GPS automatic updates using online source (AGI server).

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAutoUpdateProperties`
              - GPS AutoUpdate properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSElement`
              - An element of the GPS element collection.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSElementCollection`
              - A collection of GPS elements.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSSpecifyAlmanac`
              - Specify a GPS almanac.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesAccess`
              - Vehicle 2D Graphics display based on access intervals.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesCustom`
              - Vehicle 2D graphics display based on custom intervals.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesOrbit`
              - 2D Graphics attributes for a satellite.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime`
              - 2D Graphics attributes for a vehicle based on real time data state.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesRoute`
              - 2D Graphics attributes for aircraft, ships and ground vehicles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesTimeComponents`
              - Allow configuring the 2D attributes using the time components.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesTrajectory`
              - 2D Graphics attributes for launch vehicles and missiles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DElevationContours`
              - General settings regarding display of elevation contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DElevationGroundElevation`
              - Ground elevation for vehicle swath.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DElevationsCollection`
              - Collection for elevation contours. Used by vehicles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DElevationsElement`
              - 2D Graphics settings for elevation contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DElevationSwathHalfWidth`
              - Half width for vehicle swath.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DElevationVehicleHalfAngle`
              - Half angle for vehicle swath.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DGroundEllipsesCollection`
              - Collection of ground ellipse 2D graphics properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DGroundEllipsesElement`
              - Ground ellipse 2D graphics properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DInterval`
              - 2D Graphics display based on custom intervals.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DIntervalsCollection`
              - Custom Intervals Graphics List.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DLeadDataFraction`
              - 2D Graphics pass: fraction of leading portion of vehicle track to display.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DLeadDataTime`
              - 2D Graphics pass: time-defined segment of leading portion of vehicle track to display.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DLeadTrailData`
              - 2D Graphics pass properties: lead/trail for ground tracks.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DLighting`
              - Lighting.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DLightingElement`
              - Lighting condition properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DLine`
              - Line Style and Line Width properties used in displaying vehicle tracks.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DOrbitPassData`
              - VehicleGraphics2DOrbitPassData Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DPasses`
              - Settings for satellite pass display graphics.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DPassResolution`
              - Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DPassShowPasses`
              - Beginning and end pass numbers to display.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DRoutePassData`
              - Great arc route pass data.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DRouteResolution`
              - Route resolution for great arc vehicles defined in terms of ephemeris steps.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DSAA`
              - South Atlantic Anomaly contour settings.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DSwath`
              - Vehicle swath.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeComponentsCollection`
              - A collection of time components used to configure the object appearance in 2D and 3D views.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeComponentsEventCollectionElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with event interval collections only.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeComponentsEventElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with all types of event components except for the event interval collections.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventsCollection`
              - A satellite's time events collection.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventsElement`
              - 2D Graphics time event.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeLine`
              - 2D Graphics time event: line type.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker`
              - 2D Graphics time event: marker type.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventTypeText`
              - 2D Graphics time event: text type.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTrailDataFraction`
              - 2D Graphics pass: fraction of trailing portion of vehicle track to display.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTrailDataTime`
              - 2D Graphics pass: time-defined segment of trailing portion of vehicle track to display.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTrajectoryPassData`
              - 2D Graphics ground track and trajectory properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTrajectoryResolution`
              - Ground track and trajectory resolution for launch vehicles and missiles in terms of ephemeris steps.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DWaypointMarker`
              - Display options for waypoint and turn markers in the 2D Graphics window.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection`
              - A list of 2D definitions for the vehicle way points.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DWaypointMarkersElement`
              - 2D Graphics properties of element of waypoint collection.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DAttributesBasic`
              - Basic 3D graphics for covariance pointing contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DAttributesIntervals`
              - 3D graphics based on intervals for covariance pointing contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBearingBox`
              - Define a volume, relative to a bearing from the North, around an object.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBearingEllipse`
              - Define an ellipse, relative to a bearing from the North, around the object.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneEvent`
              - 3D BPlane Event.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneInstance`
              - An element in the VehicleGraphics3DBPlanePointCollection.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneInstancesCollection`
              - A list of available b-plane instances.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlanePoint`
              - 3D BPlane Additional Point.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlanePointCollection`
              - VehicleGraphics3DBPlanePointCollection Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlanes`
              - 3D BPlanes properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint`
              - 3D BPlane TargetPoint.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPointPositionCartesian`
              - Cartesian.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPointPositionPolar`
              - 3D BPlane target point position polar.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTemplate`
              - An element of VehicleGraphics3DBPlaneTemplatesCollection.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTemplateDisplayCollection`
              - 3D DisplayElements collection for BPlane.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTemplateDisplayElement`
              - Element of VehicleGraphics3DBPlaneTemplateDisplayCollection.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTemplatesCollection`
              - A list of available b-plane templates.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DControlBox`
              - Define a volume around the object that moves with the object.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DCovariance`
              - 3D position covariance ellipsoids.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DCovariancePointingContour`
              - Covariance pointing contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DDataFraction`
              - Fraction for 3D track display.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DDataTime`
              - Time.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DDefaultAttributes`
              - Default graphics attributes for covariance pointing contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DDropLinePathItem`
              - Drop lines at intervals along the vehicle's path.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection`
              - Collection of drop lines from the vehicle's orbit or trajectory.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DDropLinePositionItem`
              - Drop lines from the vehicle's current position.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DDropLinePositionItemCollection`
              - Lines dropped from the vehicle's position.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DElevationContours`
              - 3D elevation angle contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DEllipsoid`
              - Define an ellipsoid around the vehicle object.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DGeoBox`
              - Geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DIntervalsCollection`
              - List of Intervals.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DIntervalsElement`
              - Intervals graphics for covariance pointing contour.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DLeadTrailData`
              - LaunchVehicleGraphics3DTrajectory2 Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DLineOfBearing`
              - Define a line of bearing which is drawn from an origin in the direction of a bearing.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DModelRoute`
              - 3D marker for great arc vehicles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DModelTrajectory`
              - Marker for launch vehicle or missile.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DOrbitDropLines`
              - Droplines collections.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DOrbitPassData`
              - Satellite 3D ground and orbit track data.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DOrbitProximity`
              - Proximity graphics.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DOrbitTickMarks`
              - Tick mark for satellites.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DOrbitTrackData`
              - 3D leading/trailing track data for satellites.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DPass`
              - 3D pass for satellites.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DPathTickMarks`
              - Tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DRoute`
              - VehicleGraphics3DRoute2 Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DRouteDropLines`
              - Droplines for great arc vehicles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DRouteProximity`
              - Proximity graphics for GreatArc Vehicles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DSAA`
              - 3D South Atlantic Anomaly contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DSigmaScaleProbability`
              - Sigma probability for indirect sizing of covariance pointing contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DSigmaScaleScale`
              - Sigma scale for direct sizing of covariance pointing contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DSize`
              - 3D graphics vector size.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DSystemsCollection`
              - List of Systems.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DSystemsElement`
              - Element for reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DSystemsSpecialElement`
              - Define methods and properties to configure 3D properties of Inertial or Fixed reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DTickDataLine`
              - Line type tick marks.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DTickDataPoint`
              - Point type tick mark.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DTrajectory`
              - LaunchVehicleGraphics3DTrajectory Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DTrajectoryDropLines`
              - Droplines for launch vehicles and missiles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DTrajectoryPassData`
              - 3D ground track and trajectory data for a launch vehicle or missile.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DTrajectoryProximity`
              - VehicleGraphics3DTrajectoryProximity Class.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DTrajectoryTickMarks`
              - Tick mark data for launch vehicles and missiles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DTrajectoryTrackData`
              - 3D leading/trailing track data for launch vehicles and missiles.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DVelocityCovariance`
              - 3D velocity covariance ellipsoids.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DWaypointMarkersCollection`
              - Collection of Waypoint Markers .

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DWaypointMarkersElement`
              - 3D waypoint.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGravity`
              - Class defining gravity modeling options for a vehicle.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGroundEllipseElement`
              - Ground ellipse.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGroundEllipsesCollection`
              - List of Ground Ellipses.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity`
              - Class defining Central Body Gravity options for the High Precision Orbit Propagator (HPOP).

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPDragModel`
              - HPOP Drag Model Base CoClass.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPDragModelPlugin`
              - Plugin Drag Model.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPDragModelPluginSettings`
              - Plugin Drag Model Settings.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPDragModelSpherical`
              - Spherical Drag Pressure Model.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPForceModel`
              - Class defining HPOP force models.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPForceModelDrag`
              - Class defining the HPOP atmospheric drag model.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPForceModelDragOptions`
              - Class defining HPOP atmospheric drag options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPForceModelMoreOptions`
              - Class defining additional force model options for HPOP.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressure`
              - Class defining HPOP solar radiation pressure properties.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel`
              - SRP Model Base CoClass.

            * - :py:class:`~br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureOptions`
              - Class defining HPOP solar radiation pressure options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleImpactLocationCentric`
              - Class defining geocentric impact latitude, longitude and radius for a Missile.

            * - :py:class:`~br.ok.core.stkobjects.VehicleImpactLocationDetic`
              - Class defining geodetic impact latitude, longitude and altitude for a Missile.

            * - :py:class:`~br.ok.core.stkobjects.VehicleImpactLocationLaunchAzEl`
              - Class defining the option to use azimuth and elevation to specify the Missile's impact location.

            * - :py:class:`~br.ok.core.stkobjects.VehicleImpactLocationPoint`
              - Class defining a Missile's impact location.

            * - :py:class:`~br.ok.core.stkobjects.VehicleInertia`
              - Satellite inertia matrix parameters.

            * - :py:class:`~br.ok.core.stkobjects.VehicleInitialState`
              - Class defining the initial state of the vehicle.

            * - :py:class:`~br.ok.core.stkobjects.VehicleIntegratedAttitude`
              - Integrated Attitude generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

            * - :py:class:`~br.ok.core.stkobjects.VehicleIntegrator`
              - Class defining the HPOP integrator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleInterpolation`
              - Class defining interpolation for the HPOP integrator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleLOPCentralBodyGravity`
              - Class defining gravity options for the LOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleLOPDragSettings`
              - Class defining advanced atmospheric density options for the LOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleLOPForceModel`
              - Class defining the force model for the LOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleLOPForceModelDrag`
              - Class defining the atmospheric drag model for the LOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleLOPSolarRadiationPressure`
              - Class defining the solar radiation pressure model for the LOP propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleMassProperties`
              - Satellite Mass properties.

            * - :py:class:`~br.ok.core.stkobjects.VehiclePhysicalData`
              - Class defining physical data for the LOP force model.

            * - :py:class:`~br.ok.core.stkobjects.VehiclePluginPropagator`
              - Class defining a propagator plugin for HPOP for customization of the accelerations used in the propagation of the satellite trajectory.

            * - :py:class:`~br.ok.core.stkobjects.VehiclePluginSettings`
              - Class defining force model plugin settings for HPOP.

            * - :py:class:`~br.ok.core.stkobjects.VehiclePositionVelocityCollection`
              - Collection of position and velocity elements for HPOP covariance.

            * - :py:class:`~br.ok.core.stkobjects.VehiclePositionVelocityElement`
              - Class defining position and velocity elements for HPOP covariance.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpatialInformation`
              - Represents a spatial information of the vehicle.

            * - :py:class:`~br.ok.core.stkobjects.VehicleTargetPointingCollection`
              - List of Attitude Targets.

            * - :py:class:`~br.ok.core.stkobjects.VehicleTargetPointingElement`
              - Target pointing data for target pointing attitude.

            * - :py:class:`~br.ok.core.stkobjects.VehicleTargetPointingIntervalCollection`
              - Represents a collection of scheduled targeting intervals.

            * - :py:class:`~br.ok.core.stkobjects.VehicleTargetTimes`
              - Target times for target pointing attitude.

            * - :py:class:`~br.ok.core.stkobjects.VehicleVector`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~br.ok.core.stkobjects.VehicleWaypointAltitudeReference`
              - Altitude references.

            * - :py:class:`~br.ok.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain`
              - Terrain altitude reference.

            * - :py:class:`~br.ok.core.stkobjects.VehicleWaypointsCollection`
              - Collection of waypoints for a Great Arc vehicle.

            * - :py:class:`~br.ok.core.stkobjects.VehicleWaypointsElement`
              - Class defining a waypoint for a Great Arc vehicle.

            * - :py:class:`~br.ok.core.stkobjects.VehicleZonalPropagatorInitialState`
              - Class defining initial state for the J2/4 propagators.

            * - :py:class:`~br.ok.core.stkobjects.Volumetric`
              - The Volumetric class.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricAdvancedSettings`
              - Class defining the volumetric Computed Data Save options.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricAnalysisInterval`
              - Class defining the volumetric analysis interval.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricExportTool`
              - The Volumetric Export Tool.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricExternalFile`
              - Class defining the volume external file.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3D`
              - Class defining 3D graphics properties of volumetric object.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DActiveGridPoints`
              - Class defining Active Grid Points for Volumetric Object.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DCrossSection`
              - Class defining planar cross-sections through the volumetric grid.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DCrossSectionPlane`
              - Class defining cross-section plane for volumetric grid.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection`
              - Class defining collection of cross-section planes for volumetric grid.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DGrid`
              - Class defining grid properties of 3D graphics for volumetric object.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DLegend`
              - Class defining Boundary/Fill legend for volumetric object.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevel`
              - Class defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection`
              - Class defining collections of defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevels`
              - Class defining Spatial Calculation Levels for Volumetric Object.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGraphics3DVolume`
              - Class defining planar cross-sections through the volumetric grid.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricGridSpatialCalculation`
              - Class defining the volume grid spatial calculation.

            * - :py:class:`~br.ok.core.stkobjects.Waveform`
              - Class defining a waveform.

            * - :py:class:`~br.ok.core.stkobjects.WaveformPulseDefinition`
              - Class defining the pulse definition for a rectangular waveform.

            * - :py:class:`~br.ok.core.stkobjects.WaveformRectangular`
              - Class defining a rectangular waveform.

            * - :py:class:`~br.ok.core.stkobjects.WaveformSelectionStrategy`
              - Class defining the waveform selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.WaveformSelectionStrategyFixed`
              - Class defining the waveform selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.WaveformSelectionStrategyRangeLimits`
              - Class defining the range limits waveform selection strategy.

            * - :py:class:`~br.ok.core.stkobjects.WirelessInSite64GeometryData`
              - Class defining the REMCOM Wireless InSite 64 geometry data.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.ok.core.stkobjects.AberrationType`
              - The model of aberration to be used in access computations.

            * - :py:class:`~br.ok.core.stkobjects.AccessConstraintType`
              - Available Access Constraint.

            * - :py:class:`~br.ok.core.stkobjects.AccessTimeType`
              - The time period to use for the access computation.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATConjunctionType`
              - Mode for computing events involving conjunction TCA.

            * - :py:class:`~br.ok.core.stkobjects.AdvCATEllipsoidClassType`
              - Method for determining Ellipsoid Sizing method (class).

            * - :py:class:`~br.ok.core.stkobjects.AdvCATSecondaryEllipsoidsVisibilityType`
              - Type of visible Secondary Ellipsoids.

            * - :py:class:`~br.ok.core.stkobjects.AircraftWGS84WarningType`
              - Display mode options for aircraft mission modeler WGS84 warning.

            * - :py:class:`~br.ok.core.stkobjects.AltitudeReferenceType`
              - Altitude reference options.

            * - :py:class:`~br.ok.core.stkobjects.AnalysisWorkbenchAccessConstraintType`
              - Available Analysis Workbench Access Constraints.

            * - :py:class:`~br.ok.core.stkobjects.AnimationActionType`
              - Animation action options.

            * - :py:class:`~br.ok.core.stkobjects.AnimationDirectionType`
              - Animation direction options.

            * - :py:class:`~br.ok.core.stkobjects.AnimationEndTimeMode`
              - Animation modes.

            * - :py:class:`~br.ok.core.stkobjects.AnimationOptionType`
              - Animation Options.

            * - :py:class:`~br.ok.core.stkobjects.AntennaContourType`
              - Antenna contour types.

            * - :py:class:`~br.ok.core.stkobjects.AntennaControlReferenceType`
              - Antenna control reference type.

            * - :py:class:`~br.ok.core.stkobjects.AntennaGraphicsCoordinateSystem`
              - Coordinate system for defining antenna graphics resolution.

            * - :py:class:`~br.ok.core.stkobjects.AntennaHFSSDesignHelixTurnDirection`
              - HFSS Design antenna helix quadrifilar turn directions.

            * - :py:class:`~br.ok.core.stkobjects.AntennaHFSSDesignStatus`
              - HFSS Design antenna model statuses.

            * - :py:class:`~br.ok.core.stkobjects.AntennaHFSSDesignType`
              - HFSS Design antenna model types.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelCosecantSquaredSidelobeType`
              - Cosecant Squared antenna sidelobe selection types.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelInputType`
              - Diameter computation input type.

            * - :py:class:`~br.ok.core.stkobjects.AntennaModelType`
              - Antenna model types.

            * - :py:class:`~br.ok.core.stkobjects.AreaType`
              - Methods of defining the area target's boundaries.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericAbsorptionModelType`
              - Atmospheric absorption model types.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericDensityModel`
              - Atmospheric density models.

            * - :py:class:`~br.ok.core.stkobjects.AtmosphericTurbulenceModelType`
              - Refractive index structure parameter model types.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeCoordinateAxes`
              - Attitude export options.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeInclude`
              - Details to include in an exported Attitude file.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeProfile`
              - Predefined attitude profiles.

            * - :py:class:`~br.ok.core.stkobjects.AttitudeStandardType`
              - AttitudeStandardType tells the user which interface to cast to. eRouteAttitudeStandard -> AttitudeStandardRoute, eTrajectoryAttitudeStandard -> AttitudeStandardTrajectory, eOrbitAttitudeStanard -> AttitudeStandardOrbit.

            * - :py:class:`~br.ok.core.stkobjects.AxisOffset`
              - Specify the axis offset for the sensor 3D Vertex Offset.

            * - :py:class:`~br.ok.core.stkobjects.AzElMaskType`
              - Obscura types of the facility, place or target for AzElMask definition.

            * - :py:class:`~br.ok.core.stkobjects.BeamformerType`
              - Beamformer types.

            * - :py:class:`~br.ok.core.stkobjects.BeamSelectionStrategyType`
              - Beam selection strategy types.

            * - :py:class:`~br.ok.core.stkobjects.BorderWallUpperLowerEdgeAltitudeReference`
              - Border Wall upper and lower edge altitude references.

            * - :py:class:`~br.ok.core.stkobjects.BoresightType`
              - About boresight options for sensors of targeted pointing type.

            * - :py:class:`~br.ok.core.stkobjects.BuildHeightReferenceMethod`
              - REMCOM Wireless InSite RT building height reference method.

            * - :py:class:`~br.ok.core.stkobjects.BuildingHeightUnit`
              - REMCOM Wireless InSite RT building height unit.

            * - :py:class:`~br.ok.core.stkobjects.CCSDSDateFormat`
              - The date format of the file.

            * - :py:class:`~br.ok.core.stkobjects.CCSDSEphemerisFormatType`
              - The ephemeris format of the file.

            * - :py:class:`~br.ok.core.stkobjects.CCSDSReferenceFrame`
              - Reference Frame.

            * - :py:class:`~br.ok.core.stkobjects.CCSDSTimeSystem`
              - Time System.

            * - :py:class:`~br.ok.core.stkobjects.ChainConstellationConstraintsMode`
              - Constellation Constraints Mode.

            * - :py:class:`~br.ok.core.stkobjects.ChainCoverageAssetMode`
              - Chain Cov Asset Mode.

            * - :py:class:`~br.ok.core.stkobjects.ChainGraphics2DNetworkDataMode`
              - Chain graphics network data mode, show percentage or data rate usage.

            * - :py:class:`~br.ok.core.stkobjects.ChainOptimalStrandCalculationScalarMetricType`
              - Chain optimal strand calculation scalar type.

            * - :py:class:`~br.ok.core.stkobjects.ChainOptimalStrandCompareStrandsType`
              - Chain optimal strand link comparison type.

            * - :py:class:`~br.ok.core.stkobjects.ChainOptimalStrandLinkCompareType`
              - Chain optimal strand link comparison type.

            * - :py:class:`~br.ok.core.stkobjects.ChainOptimalStrandMetricType`
              - Chain optimal strand metric type.

            * - :py:class:`~br.ok.core.stkobjects.ChainParentPlatformRestriction`
              - Options for a chain's From and To Parent Platform Restriction.

            * - :py:class:`~br.ok.core.stkobjects.ChainStrandAnalysisComputeType`
              - Chain strand analysis compute type.

            * - :py:class:`~br.ok.core.stkobjects.ChainTimePeriodType`
              - Compute Time Period Type.

            * - :py:class:`~br.ok.core.stkobjects.CircularApertureInputType`
              - Circular aperture antenna input type.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalLocation`
              - Classical (Keplerian) element used to specify the spacecraft's location within its orbit at epoch.

            * - :py:class:`~br.ok.core.stkobjects.ClassicalSizeShape`
              - Pairs of Classical (Keplerian) elements used to specify orbit size and shape.

            * - :py:class:`~br.ok.core.stkobjects.CloudsAndFogFadingLossModelType`
              - Clouds and Fog loss model types.

            * - :py:class:`~br.ok.core.stkobjects.CloudsAndFogLiquidWaterChoiceType`
              - Clouds and Fog loss model liquid water content choices.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessEventDetectionType`
              - CommSystem access options event detection type.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemAccessSamplingMethodType`
              - CommSystem access options sampling method type.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemConstrainingRole`
              - CommSystem constraining role.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemLinkSelectionCriteriaType`
              - Link selection strategy types.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemReferenceBandwidth`
              - CommSystem reference bandwidth.

            * - :py:class:`~br.ok.core.stkobjects.CommSystemSaveMode`
              - CommSystem save mode.

            * - :py:class:`~br.ok.core.stkobjects.Component`
              - The different types of components in the component browser.

            * - :py:class:`~br.ok.core.stkobjects.ComponentLinkEmbedControlReferenceType`
              - Component link/embed control reference type.

            * - :py:class:`~br.ok.core.stkobjects.ConnectAuthenticationMode`
              - Determine the authentication mode for the connect.

            * - :py:class:`~br.ok.core.stkobjects.Constants`
              - Constants contains base IDs for various structures.

            * - :py:class:`~br.ok.core.stkobjects.ConstellationConstraintRestrictionType`
              - The values of the enumeration are used to define constellation constraints that allow you to specify the criteria to be used when constellations are combined with other objects in a chain.

            * - :py:class:`~br.ok.core.stkobjects.ConstellationFromToParentConstraint`
              - Options for a chain's From and To Parent Constraints.

            * - :py:class:`~br.ok.core.stkobjects.ConstraintBackground`
              - Options for the Background constraint, and Advanced vehicle constraint.

            * - :py:class:`~br.ok.core.stkobjects.ConstraintGroundTrack`
              - Options for the Ground Track constraint, an Advanced vehicle constraint.

            * - :py:class:`~br.ok.core.stkobjects.ConstraintLighting`
              - Options for the Lighting access constraint.

            * - :py:class:`~br.ok.core.stkobjects.Coverage3dDrawAtAltitudeMode`
              - Coverage definition drawing modes for filled graphics when showing at altitude in 3D Graphics window.

            * - :py:class:`~br.ok.core.stkobjects.CoverageAltitudeMethod`
              - Method for specifying the altitude of a grid point.

            * - :py:class:`~br.ok.core.stkobjects.CoverageAssetGrouping`
              - Coverage asset grouping options.

            * - :py:class:`~br.ok.core.stkobjects.CoverageAssetStatus`
              - Coverage asset status.

            * - :py:class:`~br.ok.core.stkobjects.CoverageBounds`
              - Coverage bounds options: values of the enumeration represent polymorphic object types.

            * - :py:class:`~br.ok.core.stkobjects.CoverageCustomRegionAlgorithm`
              - The enumerations are used to enable/disable the special gridding algorithms triggered when Custom Region grid includes a single small region (longitude span less than 1 deg).

            * - :py:class:`~br.ok.core.stkobjects.CoverageDataRetention`
              - Data retention options.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGridClass`
              - Classes of objects that can be used as templates to associate access constraints, basic object properties and, in some cases, altitude with points in the grid.

            * - :py:class:`~br.ok.core.stkobjects.CoverageGroundAltitudeMethod`
              - Method for specifying the ground altitude of a grid point.

            * - :py:class:`~br.ok.core.stkobjects.CoveragePointAltitudeMethod`
              - Custom point altitude method.

            * - :py:class:`~br.ok.core.stkobjects.CoveragePointLocationMethod`
              - Point location method.

            * - :py:class:`~br.ok.core.stkobjects.CoverageRegionAccessAccelerationType`
              - Regional acceleration options.

            * - :py:class:`~br.ok.core.stkobjects.CoverageResolution`
              - Coverage grid resolution options: values of the enumeration represent polymorphic object types.

            * - :py:class:`~br.ok.core.stkobjects.CoverageSatisfactionType`
              - The condition on the number of assets covering a grid point that must be satisfied for a valid access.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderElementType`
              - Specify the type of data returned by data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderResultCategory`
              - Specify the category of results returned by the data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataProviderType`
              - Specify the type of the result returned by data providers.

            * - :py:class:`~br.ok.core.stkobjects.DataSaveMode`
              - Access Save Mode.

            * - :py:class:`~br.ok.core.stkobjects.DelaunayGType`
              - Select whether to use the default representation of Delaunay G or G/SQRT(mu).

            * - :py:class:`~br.ok.core.stkobjects.DelaunayHType`
              - Select whether to use the default representation of Delaunay H or H/SQRT(mu).

            * - :py:class:`~br.ok.core.stkobjects.DelaunayLType`
              - Select whether to use the default representation of Delaunay L or L/SQRT(mu).

            * - :py:class:`~br.ok.core.stkobjects.DemodulatorModelType`
              - Demodulator model types.

            * - :py:class:`~br.ok.core.stkobjects.DeticPositionType`
              - LLA Position Types.

            * - :py:class:`~br.ok.core.stkobjects.DirectionProviderType`
              - Direction Provider types.

            * - :py:class:`~br.ok.core.stkobjects.DisplayTimesType`
              - Display times options for the object.

            * - :py:class:`~br.ok.core.stkobjects.DistanceOnSphere`
              - Type of line which connects the two points.

            * - :py:class:`~br.ok.core.stkobjects.DragModel`
              - Drag model types.

            * - :py:class:`~br.ok.core.stkobjects.ElementConfigurationType`
              - Element configuration types.

            * - :py:class:`~br.ok.core.stkobjects.EOIRFlightType`
              - EOIR Flight Types.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeMaterialSpecificationType`
              - Designation of how material properties are specified.

            * - :py:class:`~br.ok.core.stkobjects.EOIRShapeType`
              - The object geometry which will be rendered in the synthetic scene window.

            * - :py:class:`~br.ok.core.stkobjects.EOIRThermalModelType`
              - EOIR thermal models.

            * - :py:class:`~br.ok.core.stkobjects.EphemerisCoordinateSystemType`
              - The Coordinate System of the file.

            * - :py:class:`~br.ok.core.stkobjects.EphemerisCovarianceType`
              - The covariance data export type.

            * - :py:class:`~br.ok.core.stkobjects.EphemExportToolFileFormat`
              - Ephemeris Export Tool file formats.

            * - :py:class:`~br.ok.core.stkobjects.EphemSourceType`
              - Central body ephemeris sources.

            * - :py:class:`~br.ok.core.stkobjects.EquinoctialFormulation`
              - Formulation: retrograde or posigrade.

            * - :py:class:`~br.ok.core.stkobjects.EquinoctialSizeShape`
              - Opt whether to use Mean Motion or Semimajor Axis to specify the orbit size (Equinoctial coordinate type).

            * - :py:class:`~br.ok.core.stkobjects.ErrorCode`
              - Error codes.

            * - :py:class:`~br.ok.core.stkobjects.EventDetection`
              - Available event detection strategies.

            * - :py:class:`~br.ok.core.stkobjects.ExportToolStepSizeType`
              - The Step Size type for an attitude file.

            * - :py:class:`~br.ok.core.stkobjects.ExportToolTimePeriodType`
              - Values of the enumeration represent polymorphic object types.

            * - :py:class:`~br.ok.core.stkobjects.ExportToolVersionFormat`
              - The version format of the file.

            * - :py:class:`~br.ok.core.stkobjects.ExternalEphemerisFormatType`
              - Ephemeris file formats supported by the Stk external propagator.

            * - :py:class:`~br.ok.core.stkobjects.ExternalFileMessageLevelType`
              - Ephemeris file message level used by the Stk external propagator.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritAcrossAssets`
              - Across Assets options: specify which value of the constraint is to be selected based on all currently available assets.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritCompute`
              - Figure of Merit compute options.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritConstraintName`
              - Available constraints to use for the Access Constraint Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritDefinitionType`
              - Figure of Merit types: values of the enumeration represent polymorphic object types.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritEndGapOption`
              - End gap options: control consideration of gaps at ends of analysis intervals.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DAccumulation`
              - Accumulation options: control the sense and persistence of animation graphics for a Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DColorMethod`
              - Methods for assigning colors to contour levels.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DContourType`
              - Contour fill options.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DDirection`
              - Level order display options for the contour legend.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritGraphics2DFloatingPointFormat`
              - Format options for floating point numbers.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritInvalidValueActionType`
              - Invalid Value Action: Controls consideration of time samples usage for computing navigation solution when insufficient number of assets are available at one or more of the time samples used.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritMethod`
              - Dilution of Precision method.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritNavigationAccuracyMethod`
              - Options for uncertainty in one-way range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritNavigationComputeType`
              - Allowed number of assets for the navigation solution.

            * - :py:class:`~br.ok.core.stkobjects.FigureOfMeritSatisfactionType`
              - Satisfaction options: determine whether satisfaction is achieved based on the value of the figure of merit.

            * - :py:class:`~br.ok.core.stkobjects.FrequencySpecificationType`
              - Frequency Specification Type.

            * - :py:class:`~br.ok.core.stkobjects.GeodeticSize`
              - Size options for the Geodetic coordinate type.

            * - :py:class:`~br.ok.core.stkobjects.GeometricElementType`
              - Options for the VORefCrdn Type.

            * - :py:class:`~br.ok.core.stkobjects.GPSAttitudeModelType`
              - GPS attitude profile model types.

            * - :py:class:`~br.ok.core.stkobjects.GPSReferenceWeek`
              - GPS almanac reference week.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DACAPCoefficientDataType`
              - VOACAP coefficient data type.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DACAPSolarActivityConfigurationType`
              - VOACAP solar activity configuration type.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DFontSize`
              - Font size for data display.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DFormat`
              - Font format for data display.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DLabelSwapDistanceType`
              - Label swap distance options.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DLocation`
              - Location options for the display of textual data in the 3D Graphics window.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DMarkerOrientation`
              - 3D graphics marker orientations.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DMarkerOriginType`
              - Options for the Graphics3DMarker X or Y Origin property.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DXOrigin`
              - X origin options for positioning data display.

            * - :py:class:`~br.ok.core.stkobjects.Graphics3DYOrigin`
              - Y origin options for positioning data display.

            * - :py:class:`~br.ok.core.stkobjects.HelpContextIdentifierType`
              - Help context IDs.

            * - :py:class:`~br.ok.core.stkobjects.HFSSFarFieldDataGainType`
              - Gain type.

            * - :py:class:`~br.ok.core.stkobjects.IntersectionType`
              - Intersection display options for sensor projection.

            * - :py:class:`~br.ok.core.stkobjects.IonosphericFadingLossModelType`
              - Ionospheric loss model types.

            * - :py:class:`~br.ok.core.stkobjects.ITURP676AtmosphereDataType`
              - ITU-R P.676-13 atmosphere data type.

            * - :py:class:`~br.ok.core.stkobjects.IvClockHost`
              - Clock host options for access. Time values are reported with a clock colocated with the clock host object.

            * - :py:class:`~br.ok.core.stkobjects.IvColorMode`
              - Color mode options for access graphics.

            * - :py:class:`~br.ok.core.stkobjects.IvTimeSense`
              - Mode of signal transmission of the designated clock host.

            * - :py:class:`~br.ok.core.stkobjects.LaserPropagationLossModelType`
              - Laser propagation loss model types.

            * - :py:class:`~br.ok.core.stkobjects.LaserTroposphericScintillationLossModelType`
              - Laser tropospheric scintillation loss model types.

            * - :py:class:`~br.ok.core.stkobjects.LatticeType`
              - Lattice types.

            * - :py:class:`~br.ok.core.stkobjects.LeadTrailData`
              - Lead and trail types for track display.

            * - :py:class:`~br.ok.core.stkobjects.LightingObstructionModelType`
              - Obstruction model used in lighting computations.

            * - :py:class:`~br.ok.core.stkobjects.LimitsExceededBehaviorType`
              - Limits Exceeded Behavior types.

            * - :py:class:`~br.ok.core.stkobjects.LineWidth`
              - Line widths.

            * - :py:class:`~br.ok.core.stkobjects.LinkMarginType`
              - Link margin types.

            * - :py:class:`~br.ok.core.stkobjects.LoadMethod`
              - TLE load options.

            * - :py:class:`~br.ok.core.stkobjects.LookAheadPropagator`
              - Propagators used for calculating ephemeris for look ahead purposes. The enumeration is used with realtime propagators.

            * - :py:class:`~br.ok.core.stkobjects.LOPAtmosphericDensityModel`
              - LOP Atmospheric density models.

            * - :py:class:`~br.ok.core.stkobjects.LowAltitudeAtmosphericDensityModel`
              - Low Altitude Atmospheric density models.

            * - :py:class:`~br.ok.core.stkobjects.MarkerShape3d`
              - 3D marker shapes.

            * - :py:class:`~br.ok.core.stkobjects.MarkerType`
              - Marker style options for a waypoint.

            * - :py:class:`~br.ok.core.stkobjects.MethodToComputeSunPosition`
              - Methods to compute sun position.

            * - :py:class:`~br.ok.core.stkobjects.MixedSphericalFlightPathAngleType`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :py:class:`~br.ok.core.stkobjects.ModelGltfReflectionMapType`
              - Settings for glTF Reflection.

            * - :py:class:`~br.ok.core.stkobjects.ModelType`
              - Display options 3D model.

            * - :py:class:`~br.ok.core.stkobjects.ModtranAerosolModelType`
              - MODTRAN-derived lookup table aerosol model extinction types.

            * - :py:class:`~br.ok.core.stkobjects.ModtranCloudModelType`
              - MODTRAN Cloud model types.

            * - :py:class:`~br.ok.core.stkobjects.ModulatorModelType`
              - Modulator model types.

            * - :py:class:`~br.ok.core.stkobjects.MTOEntirety`
              - MTO Entirety Mode.

            * - :py:class:`~br.ok.core.stkobjects.MTOInputDataType`
              - MTO Input Data Type.

            * - :py:class:`~br.ok.core.stkobjects.MTOObjectInterval`
              - MTO object interval type.

            * - :py:class:`~br.ok.core.stkobjects.MTORangeMode`
              - MTO Range Mode.

            * - :py:class:`~br.ok.core.stkobjects.MTOTrackEvaluationType`
              - MTO Track Eval Mode.

            * - :py:class:`~br.ok.core.stkobjects.MTOVisibilityMode`
              - MTO Visibility Mode.

            * - :py:class:`~br.ok.core.stkobjects.NoiseTemperatureComputeType`
              - System noise temperature compute type.

            * - :py:class:`~br.ok.core.stkobjects.NoiseTemperatureMethod`
              - Noise temperature computation method.

            * - :py:class:`~br.ok.core.stkobjects.NoteShowType`
              - Options for specifying when a label note displays.

            * - :py:class:`~br.ok.core.stkobjects.NotificationFilterMask`
              - The notification flags are used to enable/disable STK Object Model event notifications.

            * - :py:class:`~br.ok.core.stkobjects.OffsetFrameType`
              - Frame options for label offset.

            * - :py:class:`~br.ok.core.stkobjects.OnePointAccessStatus`
              - One point access status.

            * - :py:class:`~br.ok.core.stkobjects.OnePointAccessSummary`
              - One point access summary type.

            * - :py:class:`~br.ok.core.stkobjects.OrientationAscNode`
              - Ascending node-related options for use in specifying orbit orientation.

            * - :py:class:`~br.ok.core.stkobjects.PlanetOrbitDisplayType`
              - Orbit display options for a planet.

            * - :py:class:`~br.ok.core.stkobjects.PlanetPositionSourceType`
              - Options for defining a planet.

            * - :py:class:`~br.ok.core.stkobjects.PointingStrategyType`
              - Pointing strategy type.

            * - :py:class:`~br.ok.core.stkobjects.PolarizationReferenceAxis`
              - Polarization reference axis.

            * - :py:class:`~br.ok.core.stkobjects.PolarizationType`
              - Polarization Type.

            * - :py:class:`~br.ok.core.stkobjects.PRFMode`
              - Radar search/track prf modes.

            * - :py:class:`~br.ok.core.stkobjects.ProjectionHorizontalDatumType`
              - REMCOM Wireless InSite RT project/horizontal datum type.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorDisplayCoordinateType`
              - Propagator Display Coordinate Types.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorSGP4SwitchMethod`
              - TLE Switch method for the SGP4 propagator.

            * - :py:class:`~br.ok.core.stkobjects.PropagatorType`
              - Vehicle propagators (available for vehicle types listed in parentheses).

            * - :py:class:`~br.ok.core.stkobjects.PulseWidthMode`
              - Radar search/track pulse width modes.

            * - :py:class:`~br.ok.core.stkobjects.RadarActivityType`
              - Radar activity times strategy.

            * - :py:class:`~br.ok.core.stkobjects.RadarContinuousWaveAnalysisMode`
              - Radar continuous wave analysis mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarCrossSectionContourGraphicsPolarization`
              - Radar cross section contour graphics polarization.

            * - :py:class:`~br.ok.core.stkobjects.RadarFrequencySpecificationType`
              - SNR Contour Type.

            * - :py:class:`~br.ok.core.stkobjects.RadarMode`
              - Radar mode types.

            * - :py:class:`~br.ok.core.stkobjects.RadarModelType`
              - Radar system types.

            * - :py:class:`~br.ok.core.stkobjects.RadarProbabilityOfDetectionType`
              - Radar probability of detection type.

            * - :py:class:`~br.ok.core.stkobjects.RadarPulseIntegrationType`
              - Radar pulse integration type.

            * - :py:class:`~br.ok.core.stkobjects.RadarPulseIntegratorType`
              - Radar pulse integrator type.

            * - :py:class:`~br.ok.core.stkobjects.RadarSarPcrMode`
              - Radar SAR pulse compression ratio modes.

            * - :py:class:`~br.ok.core.stkobjects.RadarSarPRFMode`
              - Radar SAR prf modes.

            * - :py:class:`~br.ok.core.stkobjects.RadarSARPulseIntegrationAnalysisMode`
              - Radar sar pulse integration mode.

            * - :py:class:`~br.ok.core.stkobjects.RadarSarRangeResolutionMode`
              - Radar SAR range resolution modes.

            * - :py:class:`~br.ok.core.stkobjects.RadarSearchTrackPRFMode`
              - Radar search/track prf modes.

            * - :py:class:`~br.ok.core.stkobjects.RadarSearchTrackPulseWidthMode`
              - Radar search/track pulse width modes.

            * - :py:class:`~br.ok.core.stkobjects.RadarSNRContourType`
              - SNR Contour Type.

            * - :py:class:`~br.ok.core.stkobjects.RadarSTCAttenuationType`
              - Stc Attenuation Type.

            * - :py:class:`~br.ok.core.stkobjects.RadarSwerlingCase`
              - Radar swerling case.

            * - :py:class:`~br.ok.core.stkobjects.RadarWaveformSearchTrackType`
              - Radar search/track waveform types.

            * - :py:class:`~br.ok.core.stkobjects.RainLossModelType`
              - Rain loss model types.

            * - :py:class:`~br.ok.core.stkobjects.RCSComputeStrategy`
              - Radar cross section compute strategy.

            * - :py:class:`~br.ok.core.stkobjects.ReceiverModelType`
              - Receiver model types.

            * - :py:class:`~br.ok.core.stkobjects.RectangularApertureInputType`
              - Rectangular aperture antenna input type.

            * - :py:class:`~br.ok.core.stkobjects.ReTransmitterOpMode`
              - Re-Transmitter operational mode.

            * - :py:class:`~br.ok.core.stkobjects.RFFilterModelType`
              - RF filter model types.

            * - :py:class:`~br.ok.core.stkobjects.RouteGraphics3DMarkerType`
              - Waypoint marker options.

            * - :py:class:`~br.ok.core.stkobjects.SamplingMethod`
              - Available sampling methods.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointModelType`
              - Scattering point model type.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderListType`
              - Scattering Point Provider List Type.

            * - :py:class:`~br.ok.core.stkobjects.ScatteringPointProviderType`
              - Scattering point provider type.

            * - :py:class:`~br.ok.core.stkobjects.Scenario3dPointSize`
              - Font size in points.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioEndLoopType`
              - Scenario animation cycle options.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioRefreshDeltaType`
              - Scenario animation refresh update options.

            * - :py:class:`~br.ok.core.stkobjects.ScenarioTimeStepType`
              - Scenario animation time step options.

            * - :py:class:`~br.ok.core.stkobjects.SensorAltitudeCrossingDirection`
              - Options for specifying the direction in which the sensor's field of view crosses the specified altitude.

            * - :py:class:`~br.ok.core.stkobjects.SensorAltitudeCrossingSideType`
              - Options for specifying which crossings are computed and displayed in the 2D Graphics window.

            * - :py:class:`~br.ok.core.stkobjects.SensorAzElBoresightAxisType`
              - Primary boresight axis for Sensor Az-El mask.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandImageQuality`
              - EOIR band image quality levels.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandOpticalInputMode`
              - EOIR optical input parameter specification.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandOpticalTransmissionMode`
              - EOIR optical transmission parameter specification mode.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandQuantizationMode`
              - EOIR mode of determining quantization step size.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandQuantumEfficiencyMode`
              - EOIR quantum efficiency specification mode.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandRadiometricParameterLevelType`
              - EOIR radiometric detector parameter level of specification.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandSaturationMode`
              - EOIR band irradiance or radiance reference mode.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandSpatialInputMode`
              - EOIR spatial input parameter specification.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandSpectralRelativeSystemResponseUnitsType`
              - EOIR spectral relative system response units specification.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandSpectralShape`
              - EOIR overall system spectral shape determination.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRBandWavelengthType`
              - EOIR band diffraction wavelength reference type.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRJitterType`
              - EOIR jitter type.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRProcessingLevelType`
              - EOIR processing levels.

            * - :py:class:`~br.ok.core.stkobjects.SensorEOIRScanMode`
              - EOIR sensor scan mode.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DInheritFrom2D`
              - Options for how projection distances that are computed based on 2D Graphics projection settings are displayed in the 3D Graphics window.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DProjectionTimeDependencyType`
              - The different ways to determine the sensor's space projection distance in the 3D window.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DProjectionType`
              - Options for a sensor's 3D Graphics Projection Type.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DPulseFrequencyPreset`
              - Options for a sensor's 3D Graphics Pulse Frequency presets.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DPulseStyle`
              - Options for a sensor's 3D Graphics Pulse Style.

            * - :py:class:`~br.ok.core.stkobjects.SensorGraphics3DVisualAppearance`
              - Options optimizing the visual appearance of projections.

            * - :py:class:`~br.ok.core.stkobjects.SensorLocation`
              - Sensor Location Type options.

            * - :py:class:`~br.ok.core.stkobjects.SensorPattern`
              - Sensor patterns.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointing`
              - Sensor pointing options.

            * - :py:class:`~br.ok.core.stkobjects.SensorPointingTargetedBoresightType`
              - Boresight types for sensors of targeted pointing type.

            * - :py:class:`~br.ok.core.stkobjects.SensorProjectionDistanceType`
              - Sensor 2D Graphics Projection 'Project To' options.

            * - :py:class:`~br.ok.core.stkobjects.SensorRefractionType`
              - Sensor refraction models.

            * - :py:class:`~br.ok.core.stkobjects.SensorScanMode`
              - Options for the Sensor Spinning Scan Mode.

            * - :py:class:`~br.ok.core.stkobjects.SolarRadiationPressureModelType`
              - Solar radiation pressure model types.

            * - :py:class:`~br.ok.core.stkobjects.SolarRadiationPressureShadowModelType`
              - Shadow model options for solar radiation pressure.

            * - :py:class:`~br.ok.core.stkobjects.SolidTide`
              - The Solid Tide Type for force modeling.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentCrresProtonActivity`
              - Activity level for CRRESPRO model.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentCrresRadiationActivity`
              - Activity level for CRRESRAD model.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticExternalField`
              - External magnetic field.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticFieldColorMode`
              - Mode by which color is assigned.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticFieldColorScaleType`
              - Scaling of magnetic field to use when assigning color/translucency.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticMainField`
              - Main magnetic field.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentNasaModelsActivity`
              - Activity level for the NASA models NASAELE and NASAPRO.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentSAAChannel`
              - Energy level for SAA protons.

            * - :py:class:`~br.ok.core.stkobjects.SpaceEnvironmentSAAFluxLevel`
              - Flux level for SAA contour.

            * - :py:class:`~br.ok.core.stkobjects.SpacingUnit`
              - Spacing Units.

            * - :py:class:`~br.ok.core.stkobjects.SphericalFlightPathAzimuthType`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :py:class:`~br.ok.core.stkobjects.SpiceInterpolation`
              - The SPICE interpolation type.

            * - :py:class:`~br.ok.core.stkobjects.StarReferenceFrame`
              - Star reference frame types.

            * - :py:class:`~br.ok.core.stkobjects.StatisticType`
              - The different statistics that might be available for a data set.

            * - :py:class:`~br.ok.core.stkobjects.STKObjectType`
              - STK objects.

            * - :py:class:`~br.ok.core.stkobjects.SurfaceLinesTerrain`
              - Options for surface lines on terrain.

            * - :py:class:`~br.ok.core.stkobjects.SurfaceReference`
              - Options for surface reference of earth globes.

            * - :py:class:`~br.ok.core.stkobjects.SwathComputationalMethod`
              - Computationals methods for generating swaths.

            * - :py:class:`~br.ok.core.stkobjects.TargetSelectionMethod`
              - Target Selection Method types.

            * - :py:class:`~br.ok.core.stkobjects.TerrainFileType`
              - Terrain file type options.

            * - :py:class:`~br.ok.core.stkobjects.TerrainNormalType`
              - Methods of defining the slope of the local terrain for the facility, place or target.

            * - :py:class:`~br.ok.core.stkobjects.TextOutlineStyle`
              - The text outline style for 2D graphics display.

            * - :py:class:`~br.ok.core.stkobjects.ThirdBodyGravitySourceType`
              - Sources for 3rd body gravitation data.

            * - :py:class:`~br.ok.core.stkobjects.TickData`
              - Tick mark options. Tick marks represent milestones at specified intervals along a vehicle's track in the 3D Graphics window.

            * - :py:class:`~br.ok.core.stkobjects.Tileset3DSourceType`
              - 3DTileset source type options.

            * - :py:class:`~br.ok.core.stkobjects.TimePeriodValueType`
              - Time value types.

            * - :py:class:`~br.ok.core.stkobjects.TimeVaryingExtremum`
              - The different time varying extremum that might be available for a data set.

            * - :py:class:`~br.ok.core.stkobjects.TIREMPolarizationType`
              - TIREM polarization type.

            * - :py:class:`~br.ok.core.stkobjects.TrackMode`
              - Track mode options for tracking boresights.

            * - :py:class:`~br.ok.core.stkobjects.TrajectoryType`
              - Trajectory type for a point.

            * - :py:class:`~br.ok.core.stkobjects.TransferFunctionType`
              - Transmitter model types.

            * - :py:class:`~br.ok.core.stkobjects.TransmitterModelType`
              - Transmitter model types.

            * - :py:class:`~br.ok.core.stkobjects.TroposphericScintillationAverageTimeChoiceType`
              - TroposphericScintillation loss model average time choices.

            * - :py:class:`~br.ok.core.stkobjects.TroposphericScintillationFadingLossModelType`
              - TropoScintillation loss model types.

            * - :py:class:`~br.ok.core.stkobjects.UrbanTerrestrialLossModelType`
              - urban/terrestrial loss model types.

            * - :py:class:`~br.ok.core.stkobjects.VectorAxesConnectType`
              - Methods for connecting geometric elements.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAltitudeReference`
              - Reference altitude options for waypoints.

            * - :py:class:`~br.ok.core.stkobjects.VehicleAttitude`
              - Available attitude types.

            * - :py:class:`~br.ok.core.stkobjects.VehicleBreakAngleType`
              - Definition options for setting pass breaks:.

            * - :py:class:`~br.ok.core.stkobjects.VehicleConsiderAnalysisType`
              - Consider parameters for HPOP covariance.

            * - :py:class:`~br.ok.core.stkobjects.VehicleCoordinateSystem`
              - Coordinate system used for measurement of latitude and longitude.

            * - :py:class:`~br.ok.core.stkobjects.VehicleCorrelationListType`
              - Correlation List row and column values.

            * - :py:class:`~br.ok.core.stkobjects.VehicleDirection`
              - Direction of latitude crossing at the beginning of a pass.

            * - :py:class:`~br.ok.core.stkobjects.VehicleEllipseOptionType`
              - Elliptical motion modeling options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleFrame`
              - Frame options for covariance matrix.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGeomagneticFluxSourceType`
              - GeomagFluxSrc.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGeomagneticFluxUpdateRateType`
              - Geomagnetic flux update rate options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAlmanacType`
              - GPS Almanac types.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSAutomaticUpdateSourceType`
              - The sources to retrieve GPS elements from upon propagation.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSElementSelectionType`
              - GPS Selection method for the GPS propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGPSSwitchMethod`
              - GPS Switch method for the GPS propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DAttributeType`
              - Criteria for displaying a vehicle's 2D Graphics attributes.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DElevation`
              - Options for vehicle swath.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DOffset`
              - Options for offset direction for 2D time events graphics.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DOptionType`
              - Display options for vehicle swath.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DPass`
              - Pass display options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DTimeEventType`
              - 2D Graphics time event graphics options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics2DVisibleSideType`
              - Pass display direction options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DAttributeType`
              - Options for 3D graphics for covariance pointing contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPointPosition`
              - Values of the enumeration represent polymorphic object types.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DDropLineType`
              - Options for where to end drop lines.

            * - :py:class:`~br.ok.core.stkobjects.VehicleGraphics3DSigmaScale`
              - Sigma scale options for sizing covariance pointing contours.

            * - :py:class:`~br.ok.core.stkobjects.VehicleImpact`
              - Impact location options.

            * - :py:class:`~br.ok.core.stkobjects.VehicleImpactLocation`
              - Options for specifying missile impact point.

            * - :py:class:`~br.ok.core.stkobjects.VehicleIntegrationModel`
              - Integration methods.

            * - :py:class:`~br.ok.core.stkobjects.VehicleInterpolationMethod`
              - Interpolation methods.

            * - :py:class:`~br.ok.core.stkobjects.VehicleLaunch`
              - Options for launch coordinates.

            * - :py:class:`~br.ok.core.stkobjects.VehicleLaunchControl`
              - Flight parameters for a missile.

            * - :py:class:`~br.ok.core.stkobjects.VehicleLookAheadMethod`
              - Look ahead duration methods.

            * - :py:class:`~br.ok.core.stkobjects.VehicleMethod`
              - Step size control options.

            * - :py:class:`~br.ok.core.stkobjects.VehiclePartialPassMeasurement`
              - Partial Pass Measurement methods (typically used for reporting data).

            * - :py:class:`~br.ok.core.stkobjects.VehiclePassNumbering`
              - Pass numbering options.

            * - :py:class:`~br.ok.core.stkobjects.VehiclePredictorCorrectorScheme`
              - Predictor Corrector schemes.

            * - :py:class:`~br.ok.core.stkobjects.VehiclePropagationFrame`
              - Propagation frames used by J2/J4/TwoBody propagators.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSGP4AutomaticUpdateSourceType`
              - The TLE sources where the SGP4 propagator retrieves TLEs from automatically upon propagation.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSGP4TLESelectionType`
              - TLE Selection method for the SGP4 propagator.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSlewMode`
              - Target slew modes.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSlewTimingBetweenTargetType`
              - Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSolarFluxGeomagneticType`
              - Options for specifying solar and geomagnetic flux.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpaceEnvironmentApSource`
              - Mode for computing 15 day average Ap.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpaceEnvironmentComputationMode`
              - Models that are to be included when modeling radiation.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpaceEnvironmentDetectorGeometry`
              - Detector geometry.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpaceEnvironmentDetectorType`
              - Detector material.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpaceEnvironmentDoseChannel`
              - Dose channel.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpaceEnvironmentF10P7SourceType`
              - Mode for computing 13-month average F10.7.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpaceEnvironmentMaterial`
              - Material.

            * - :py:class:`~br.ok.core.stkobjects.VehicleSpaceEnvironmentShapeModel`
              - Thermal shape model.

            * - :py:class:`~br.ok.core.stkobjects.VehicleWaypointComputationMethod`
              - Methods for computing waypoints.

            * - :py:class:`~br.ok.core.stkobjects.VehicleWaypointInterpolationMethod`
              - Interpolation methods.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricDataExportFormatType`
              - Volumetric data export format types.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricDefinitionType`
              - Volume grid definition types.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricDisplayQualityType`
              - Quality of the graphics display types.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricDisplayVolumeType`
              - Graphics volume display type.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricLegendNumericNotationType`
              - Legend numeric notation types.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricLevelOrder`
              - Legend level display order.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricSaveComputedDataType`
              - Save Computed Data types.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricSpatialCalculationEvaluationType`
              - Evaluation of Spatial Calculation types.

            * - :py:class:`~br.ok.core.stkobjects.VolumetricVolumeGridExportType`
              - Volumetric data export types.

            * - :py:class:`~br.ok.core.stkobjects.WaveformSelectionStrategyType`
              - Waveform selection strategy type.

            * - :py:class:`~br.ok.core.stkobjects.WaveformType`
              - Waveform types.



Description
-----------

The following is an overview of the classes, interfaces and enumerations of the STK Object Model.


.. py:currentmodule:: br.ok.core.stkobjects


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    🖿 aviator<stkobjects/aviator>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    🗎 astrogator<stkobjects/astrogator>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IAccessAdvanced<stkobjects/IAccessAdvanced>
     IAccessConstraint<stkobjects/IAccessConstraint>
     IAccessConstraintMinMaxBase<stkobjects/IAccessConstraintMinMaxBase>
     IAccessInterval<stkobjects/IAccessInterval>
     IAnimation<stkobjects/IAnimation>
     IAntennaBeam<stkobjects/IAntennaBeam>
     IAntennaBeamSelectionStrategy<stkobjects/IAntennaBeamSelectionStrategy>
     IAntennaContour<stkobjects/IAntennaContour>
     IAntennaHFSSDesign<stkobjects/IAntennaHFSSDesign>
     IAntennaModel<stkobjects/IAntennaModel>
     IAntennaModelOpticalSimple<stkobjects/IAntennaModelOpticalSimple>
     IAreaTypeData<stkobjects/IAreaTypeData>
     IAtmosphericAbsorptionModel<stkobjects/IAtmosphericAbsorptionModel>
     IAtmosphericAbsorptionModelTIREM<stkobjects/IAtmosphericAbsorptionModelTIREM>
     IAtmosphericTurbulenceModel<stkobjects/IAtmosphericTurbulenceModel>
     IAzElMaskData<stkobjects/IAzElMaskData>
     IBeamformer<stkobjects/IBeamformer>
     ICelestialBodyInformation<stkobjects/ICelestialBodyInformation>
     ICelestialBodyInformationCollection<stkobjects/ICelestialBodyInformationCollection>
     IChainTimePeriod<stkobjects/IChainTimePeriod>
     IClassicalLocation<stkobjects/IClassicalLocation>
     IClassicalSizeShape<stkobjects/IClassicalSizeShape>
     ICloneable<stkobjects/ICloneable>
     ICloudsAndFogFadingLossModel<stkobjects/ICloudsAndFogFadingLossModel>
     ICommSystemAccessEventDetection<stkobjects/ICommSystemAccessEventDetection>
     ICommSystemAccessSamplingMethod<stkobjects/ICommSystemAccessSamplingMethod>
     ICommSystemLinkSelectionCriteria<stkobjects/ICommSystemLinkSelectionCriteria>
     IComponentInfo<stkobjects/IComponentInfo>
     IComponentLinkEmbedControl<stkobjects/IComponentLinkEmbedControl>
     IConstellationConstraintRestriction<stkobjects/IConstellationConstraintRestriction>
     ICoverageBounds<stkobjects/ICoverageBounds>
     ICoverageResolution<stkobjects/ICoverageResolution>
     IDataProvider<stkobjects/IDataProvider>
     IDataProviderInfo<stkobjects/IDataProviderInfo>
     IDelaunayActionVariable<stkobjects/IDelaunayActionVariable>
     IDemodulatorModel<stkobjects/IDemodulatorModel>
     IDirectionProvider<stkobjects/IDirectionProvider>
     IDisplayDistance<stkobjects/IDisplayDistance>
     IDisplayTime<stkobjects/IDisplayTime>
     IDisplayTimesData<stkobjects/IDisplayTimesData>
     IElementConfiguration<stkobjects/IElementConfiguration>
     IElementConfigurationPolygon<stkobjects/IElementConfigurationPolygon>
     IEOIR<stkobjects/IEOIR>
     IEOIRShapeObject<stkobjects/IEOIRShapeObject>
     IEventDetectionStrategy<stkobjects/IEventDetectionStrategy>
     IFigureOfMeritDefinition<stkobjects/IFigureOfMeritDefinition>
     IFigureOfMeritDefinitionCompute<stkobjects/IFigureOfMeritDefinitionCompute>
     IFigureOfMeritDefinitionData<stkobjects/IFigureOfMeritDefinitionData>
     IFigureOfMeritDefinitionDilutionOfPrecision<stkobjects/IFigureOfMeritDefinitionDilutionOfPrecision>
     IFigureOfMeritDefinitionResponseTime<stkobjects/IFigureOfMeritDefinitionResponseTime>
     IFigureOfMeritGraphics2DAttributes<stkobjects/IFigureOfMeritGraphics2DAttributes>
     IFigureOfMeritGraphics2DContours<stkobjects/IFigureOfMeritGraphics2DContours>
     IFigureOfMeritNavigationAccuracyMethod<stkobjects/IFigureOfMeritNavigationAccuracyMethod>
     IFlightPathAngle<stkobjects/IFlightPathAngle>
     IGeodeticSize<stkobjects/IGeodeticSize>
     IGraphics3DMarkerData<stkobjects/IGraphics3DMarkerData>
     IGraphics3DModel<stkobjects/IGraphics3DModel>
     IGraphics3DModelData<stkobjects/IGraphics3DModelData>
     IGraphics3DReferenceAnalysisWorkbenchComponent<stkobjects/IGraphics3DReferenceAnalysisWorkbenchComponent>
     IGreatArcGraphics<stkobjects/IGreatArcGraphics>
     IGreatArcGraphics3D<stkobjects/IGreatArcGraphics3D>
     IGreatArcVehicle<stkobjects/IGreatArcVehicle>
     IGroundLocation<stkobjects/IGroundLocation>
     IGroundLocationGraphics<stkobjects/IGroundLocationGraphics>
     IGroundLocationGraphics3D<stkobjects/IGroundLocationGraphics3D>
     IIonosphericFadingLossModel<stkobjects/IIonosphericFadingLossModel>
     ILaserAtmosphericLossModel<stkobjects/ILaserAtmosphericLossModel>
     ILaserTroposphericScintillationLossModel<stkobjects/ILaserTroposphericScintillationLossModel>
     ILatitudeLongitudeAltitudePosition<stkobjects/ILatitudeLongitudeAltitudePosition>
     ILifetimeInformation<stkobjects/ILifetimeInformation>
     IModulatorModel<stkobjects/IModulatorModel>
     IModulatorModelScriptPlugin<stkobjects/IModulatorModelScriptPlugin>
     IOrbitDisplayData<stkobjects/IOrbitDisplayData>
     IOrientationAscNode<stkobjects/IOrientationAscNode>
     IPointingStrategy<stkobjects/IPointingStrategy>
     IPolarization<stkobjects/IPolarization>
     IPolarizationCrossPolLeakage<stkobjects/IPolarizationCrossPolLeakage>
     IPolarizationElliptical<stkobjects/IPolarizationElliptical>
     IPolarizationHorizontal<stkobjects/IPolarizationHorizontal>
     IPolarizationLinear<stkobjects/IPolarizationLinear>
     IPolarizationVertical<stkobjects/IPolarizationVertical>
     IPositionSourceData<stkobjects/IPositionSourceData>
     IPropagator<stkobjects/IPropagator>
     IPropagatorSGP4LoadData<stkobjects/IPropagatorSGP4LoadData>
     IProvideSpatialInfo<stkobjects/IProvideSpatialInfo>
     IRadarActivity<stkobjects/IRadarActivity>
     IRadarContinuousWaveAnalysisMode<stkobjects/IRadarContinuousWaveAnalysisMode>
     IRadarCrossSectionComputeStrategy<stkobjects/IRadarCrossSectionComputeStrategy>
     IRadarModeBistaticReceiver<stkobjects/IRadarModeBistaticReceiver>
     IRadarModeBistaticTransmitter<stkobjects/IRadarModeBistaticTransmitter>
     IRadarModel<stkobjects/IRadarModel>
     IRadarModeMonostatic<stkobjects/IRadarModeMonostatic>
     IRadarProbabilityOfDetection<stkobjects/IRadarProbabilityOfDetection>
     IRadarProbabilityOfDetectionCFAR<stkobjects/IRadarProbabilityOfDetectionCFAR>
     IRadarPulseIntegration<stkobjects/IRadarPulseIntegration>
     IRadarSTCAttenuation<stkobjects/IRadarSTCAttenuation>
     IRadarSTCAttenuationMap<stkobjects/IRadarSTCAttenuationMap>
     IRadarWaveformSearchTrack<stkobjects/IRadarWaveformSearchTrack>
     IRainLossModel<stkobjects/IRainLossModel>
     IReceiverModel<stkobjects/IReceiverModel>
     IReceiverModelScriptPlugin<stkobjects/IReceiverModelScriptPlugin>
     IRefractionModelBase<stkobjects/IRefractionModelBase>
     IReTransmitterModel<stkobjects/IReTransmitterModel>
     IRFFilterModel<stkobjects/IRFFilterModel>
     ISamplingMethodStrategy<stkobjects/ISamplingMethodStrategy>
     IScatteringPointModel<stkobjects/IScatteringPointModel>
     IScatteringPointProvider<stkobjects/IScatteringPointProvider>
     ISensorPattern<stkobjects/ISensorPattern>
     ISensorPointing<stkobjects/ISensorPointing>
     ISensorPointingTargetedBoresight<stkobjects/ISensorPointingTargetedBoresight>
     ISensorProjectionDisplayDistance<stkobjects/ISensorProjectionDisplayDistance>
     ISolarActivityConfiguration<stkobjects/ISolarActivityConfiguration>
     ISRPModelBase<stkobjects/ISRPModelBase>
     ISTKObject<stkobjects/ISTKObject>
     ISTKObjectCollection<stkobjects/ISTKObjectCollection>
     ISTKObjectElementCollection<stkobjects/ISTKObjectElementCollection>
     ITargetSelectionMethod<stkobjects/ITargetSelectionMethod>
     ITerrainNormData<stkobjects/ITerrainNormData>
     ITimePeriod<stkobjects/ITimePeriod>
     ITransmitterModel<stkobjects/ITransmitterModel>
     ITransmitterModelScriptPlugin<stkobjects/ITransmitterModelScriptPlugin>
     ITroposphericScintillationFadingLossModel<stkobjects/ITroposphericScintillationFadingLossModel>
     IUrbanTerrestrialLossModel<stkobjects/IUrbanTerrestrialLossModel>
     IVehicleAttitude<stkobjects/IVehicleAttitude>
     IVehicleAttitudeProfile<stkobjects/IVehicleAttitudeProfile>
     IVehicleAttitudeSlewBase<stkobjects/IVehicleAttitudeSlewBase>
     IVehicleAttitudeStandard<stkobjects/IVehicleAttitudeStandard>
     IVehicleBreakAngle<stkobjects/IVehicleBreakAngle>
     IVehicleCoordinateAxes<stkobjects/IVehicleCoordinateAxes>
     IVehicleGPSAlmanacProperties<stkobjects/IVehicleGPSAlmanacProperties>
     IVehicleGraphics2DAttributes<stkobjects/IVehicleGraphics2DAttributes>
     IVehicleGraphics2DAttributesBasic<stkobjects/IVehicleGraphics2DAttributesBasic>
     IVehicleGraphics2DAttributesDisplayState<stkobjects/IVehicleGraphics2DAttributesDisplayState>
     IVehicleGraphics2DElevation<stkobjects/IVehicleGraphics2DElevation>
     IVehicleGraphics2DPass<stkobjects/IVehicleGraphics2DPass>
     IVehicleGraphics2DTimeComponentsElement<stkobjects/IVehicleGraphics2DTimeComponentsElement>
     IVehicleGraphics2DTimeEventType<stkobjects/IVehicleGraphics2DTimeEventType>
     IVehicleGraphics3DAttributes<stkobjects/IVehicleGraphics3DAttributes>
     IVehicleGraphics3DBPlaneTargetPointPosition<stkobjects/IVehicleGraphics3DBPlaneTargetPointPosition>
     IVehicleGraphics3DProximity<stkobjects/IVehicleGraphics3DProximity>
     IVehicleGraphics3DProximityAreaObject<stkobjects/IVehicleGraphics3DProximityAreaObject>
     IVehicleGraphics3DSigmaScale<stkobjects/IVehicleGraphics3DSigmaScale>
     IVehicleGraphics3DSystemsElementBase<stkobjects/IVehicleGraphics3DSystemsElementBase>
     IVehicleGraphics3DTickData<stkobjects/IVehicleGraphics3DTickData>
     IVehicleHPOPDragModel<stkobjects/IVehicleHPOPDragModel>
     IVehicleImpact<stkobjects/IVehicleImpact>
     IVehicleImpactLocation<stkobjects/IVehicleImpactLocation>
     IVehicleLaunch<stkobjects/IVehicleLaunch>
     IVehicleLaunchControl<stkobjects/IVehicleLaunchControl>
     IVehicleLeadTrailData<stkobjects/IVehicleLeadTrailData>
     IVehicleLeadTrailDataFraction<stkobjects/IVehicleLeadTrailDataFraction>
     IVehicleLeadTrailDataTime<stkobjects/IVehicleLeadTrailDataTime>
     IVehiclePassNumbering<stkobjects/IVehiclePassNumbering>
     IVehiclePointing<stkobjects/IVehiclePointing>
     IVehicleSolarFluxGeoMagnitude<stkobjects/IVehicleSolarFluxGeoMagnitude>
     IVehicleWaypointAltitudeReference<stkobjects/IVehicleWaypointAltitudeReference>
     IVolumetricGridDefinition<stkobjects/IVolumetricGridDefinition>
     IWaveform<stkobjects/IWaveform>
     IWaveformSelectionStrategy<stkobjects/IWaveformSelectionStrategy>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     Access<stkobjects/Access>
     AccessAdvancedSettings<stkobjects/AccessAdvancedSettings>
     AccessAllowedTimeIntervals<stkobjects/AccessAllowedTimeIntervals>
     AccessConstraint<stkobjects/AccessConstraint>
     AccessConstraintAnalysisWorkbench<stkobjects/AccessConstraintAnalysisWorkbench>
     AccessConstraintAnalysisWorkbenchCollection<stkobjects/AccessConstraintAnalysisWorkbenchCollection>
     AccessConstraintAnalysisWorkbenchComponent<stkobjects/AccessConstraintAnalysisWorkbenchComponent>
     AccessConstraintAngle<stkobjects/AccessConstraintAngle>
     AccessConstraintBackground<stkobjects/AccessConstraintBackground>
     AccessConstraintCentralBodyObstruction<stkobjects/AccessConstraintCentralBodyObstruction>
     AccessConstraintCollection<stkobjects/AccessConstraintCollection>
     AccessConstraintCondition<stkobjects/AccessConstraintCondition>
     AccessConstraintElevationRiseSet<stkobjects/AccessConstraintElevationRiseSet>
     AccessConstraintExclZonesCollection<stkobjects/AccessConstraintExclZonesCollection>
     AccessConstraintGrazingAltitude<stkobjects/AccessConstraintGrazingAltitude>
     AccessConstraintGroundTrack<stkobjects/AccessConstraintGroundTrack>
     AccessConstraintIntervals<stkobjects/AccessConstraintIntervals>
     AccessConstraintLatitudeLongitudeZone<stkobjects/AccessConstraintLatitudeLongitudeZone>
     AccessConstraintMinMaxBase<stkobjects/AccessConstraintMinMaxBase>
     AccessConstraintNoiseTemperature<stkobjects/AccessConstraintNoiseTemperature>
     AccessConstraintObjExAngle<stkobjects/AccessConstraintObjExAngle>
     AccessConstraintPluginMinMax<stkobjects/AccessConstraintPluginMinMax>
     AccessConstraintTimeSlipRange<stkobjects/AccessConstraintTimeSlipRange>
     AccessEventDetection<stkobjects/AccessEventDetection>
     AccessGraphics<stkobjects/AccessGraphics>
     AccessSampling<stkobjects/AccessSampling>
     AccessTargetTime<stkobjects/AccessTargetTime>
     AccessTargetTimesCollection<stkobjects/AccessTargetTimesCollection>
     AccessTimePeriod<stkobjects/AccessTimePeriod>
     AdditionalGainLoss<stkobjects/AdditionalGainLoss>
     AdditionalGainLossCollection<stkobjects/AdditionalGainLossCollection>
     AdvCAT<stkobjects/AdvCAT>
     AdvCATAdvancedEllipsoid<stkobjects/AdvCATAdvancedEllipsoid>
     AdvCATAdvancedSettings<stkobjects/AdvCATAdvancedSettings>
     AdvCATAvailableObjectCollection<stkobjects/AdvCATAvailableObjectCollection>
     AdvCATChosenObject<stkobjects/AdvCATChosenObject>
     AdvCATChosenObjectCollection<stkobjects/AdvCATChosenObjectCollection>
     AdvCATGraphics3D<stkobjects/AdvCATGraphics3D>
     AdvCATPreFilters<stkobjects/AdvCATPreFilters>
     Aircraft<stkobjects/Aircraft>
     AircraftExportTools<stkobjects/AircraftExportTools>
     AircraftGraphics<stkobjects/AircraftGraphics>
     AircraftGraphics3D<stkobjects/AircraftGraphics3D>
     Antenna<stkobjects/Antenna>
     AntennaBeam<stkobjects/AntennaBeam>
     AntennaBeamCollection<stkobjects/AntennaBeamCollection>
     AntennaBeamSelectionStrategy<stkobjects/AntennaBeamSelectionStrategy>
     AntennaBeamSelectionStrategyAggregate<stkobjects/AntennaBeamSelectionStrategyAggregate>
     AntennaBeamSelectionStrategyMaximumGain<stkobjects/AntennaBeamSelectionStrategyMaximumGain>
     AntennaBeamSelectionStrategyMinimumBoresightAngle<stkobjects/AntennaBeamSelectionStrategyMinimumBoresightAngle>
     AntennaBeamSelectionStrategyScriptPlugin<stkobjects/AntennaBeamSelectionStrategyScriptPlugin>
     AntennaBeamTransmit<stkobjects/AntennaBeamTransmit>
     AntennaContourEIRP<stkobjects/AntennaContourEIRP>
     AntennaContourFluxDensity<stkobjects/AntennaContourFluxDensity>
     AntennaContourGain<stkobjects/AntennaContourGain>
     AntennaContourGraphics<stkobjects/AntennaContourGraphics>
     AntennaContourLevel<stkobjects/AntennaContourLevel>
     AntennaContourLevelCollection<stkobjects/AntennaContourLevelCollection>
     AntennaContourRIP<stkobjects/AntennaContourRIP>
     AntennaContourSpectralFluxDensity<stkobjects/AntennaContourSpectralFluxDensity>
     AntennaControl<stkobjects/AntennaControl>
     AntennaGraphics<stkobjects/AntennaGraphics>
     AntennaGraphics3D<stkobjects/AntennaGraphics3D>
     AntennaHFSSDesign<stkobjects/AntennaHFSSDesign>
     AntennaHFSSDesignHelixQuadrifilarShort<stkobjects/AntennaHFSSDesignHelixQuadrifilarShort>
     AntennaHFSSDesignSlotGap<stkobjects/AntennaHFSSDesignSlotGap>
     AntennaHFSSDesignWireDipole<stkobjects/AntennaHFSSDesignWireDipole>
     AntennaHFSSDesignWireMonopole<stkobjects/AntennaHFSSDesignWireMonopole>
     AntennaModel<stkobjects/AntennaModel>
     AntennaModelANSYSffdFormat<stkobjects/AntennaModelANSYSffdFormat>
     AntennaModelApertureCircularBessel<stkobjects/AntennaModelApertureCircularBessel>
     AntennaModelApertureCircularBesselEnvelope<stkobjects/AntennaModelApertureCircularBesselEnvelope>
     AntennaModelApertureCircularCosine<stkobjects/AntennaModelApertureCircularCosine>
     AntennaModelApertureCircularCosinePedestal<stkobjects/AntennaModelApertureCircularCosinePedestal>
     AntennaModelApertureCircularCosineSquared<stkobjects/AntennaModelApertureCircularCosineSquared>
     AntennaModelApertureCircularCosineSquaredPedestal<stkobjects/AntennaModelApertureCircularCosineSquaredPedestal>
     AntennaModelApertureCircularSincIntegerPower<stkobjects/AntennaModelApertureCircularSincIntegerPower>
     AntennaModelApertureCircularSincRealPower<stkobjects/AntennaModelApertureCircularSincRealPower>
     AntennaModelApertureCircularUniform<stkobjects/AntennaModelApertureCircularUniform>
     AntennaModelApertureRectangularCosine<stkobjects/AntennaModelApertureRectangularCosine>
     AntennaModelApertureRectangularCosinePedestal<stkobjects/AntennaModelApertureRectangularCosinePedestal>
     AntennaModelApertureRectangularCosineSquared<stkobjects/AntennaModelApertureRectangularCosineSquared>
     AntennaModelApertureRectangularCosineSquaredPedestal<stkobjects/AntennaModelApertureRectangularCosineSquaredPedestal>
     AntennaModelApertureRectangularSincIntegerPower<stkobjects/AntennaModelApertureRectangularSincIntegerPower>
     AntennaModelApertureRectangularSincRealPower<stkobjects/AntennaModelApertureRectangularSincRealPower>
     AntennaModelApertureRectangularUniform<stkobjects/AntennaModelApertureRectangularUniform>
     AntennaModelCosecantSquared<stkobjects/AntennaModelCosecantSquared>
     AntennaModelDipole<stkobjects/AntennaModelDipole>
     AntennaModelElevationAzimuthCuts<stkobjects/AntennaModelElevationAzimuthCuts>
     AntennaModelExternal<stkobjects/AntennaModelExternal>
     AntennaModelGaussian<stkobjects/AntennaModelGaussian>
     AntennaModelGIMROC<stkobjects/AntennaModelGIMROC>
     AntennaModelGPSFRPA<stkobjects/AntennaModelGPSFRPA>
     AntennaModelGPSGlobal<stkobjects/AntennaModelGPSGlobal>
     AntennaModelHelix<stkobjects/AntennaModelHelix>
     AntennaModelHemispherical<stkobjects/AntennaModelHemispherical>
     AntennaModelHFSSDesign<stkobjects/AntennaModelHFSSDesign>
     AntennaModelHfssEepArray<stkobjects/AntennaModelHfssEepArray>
     AntennaModelIEEE1979<stkobjects/AntennaModelIEEE1979>
     AntennaModelIntelSat<stkobjects/AntennaModelIntelSat>
     AntennaModelIsotropic<stkobjects/AntennaModelIsotropic>
     AntennaModelITUBO1213CoPolar<stkobjects/AntennaModelITUBO1213CoPolar>
     AntennaModelITUBO1213CrossPolar<stkobjects/AntennaModelITUBO1213CrossPolar>
     AntennaModelITUF1245<stkobjects/AntennaModelITUF1245>
     AntennaModelITUS1528R12Circular<stkobjects/AntennaModelITUS1528R12Circular>
     AntennaModelITUS1528R12Rectangular<stkobjects/AntennaModelITUS1528R12Rectangular>
     AntennaModelITUS1528R13<stkobjects/AntennaModelITUS1528R13>
     AntennaModelITUS465<stkobjects/AntennaModelITUS465>
     AntennaModelITUS580<stkobjects/AntennaModelITUS580>
     AntennaModelITUS672Circular<stkobjects/AntennaModelITUS672Circular>
     AntennaModelITUS672Rectangular<stkobjects/AntennaModelITUS672Rectangular>
     AntennaModelITUS731<stkobjects/AntennaModelITUS731>
     AntennaModelOpticalGaussian<stkobjects/AntennaModelOpticalGaussian>
     AntennaModelOpticalSimple<stkobjects/AntennaModelOpticalSimple>
     AntennaModelParabolic<stkobjects/AntennaModelParabolic>
     AntennaModelPencilBeam<stkobjects/AntennaModelPencilBeam>
     AntennaModelPhasedArray<stkobjects/AntennaModelPhasedArray>
     AntennaModelRectangularPattern<stkobjects/AntennaModelRectangularPattern>
     AntennaModelRemcomUanFormat<stkobjects/AntennaModelRemcomUanFormat>
     AntennaModelScriptPlugin<stkobjects/AntennaModelScriptPlugin>
     AntennaModelSquareHorn<stkobjects/AntennaModelSquareHorn>
     AntennaModelTicraGRASPFormat<stkobjects/AntennaModelTicraGRASPFormat>
     AntennaNoiseTemperature<stkobjects/AntennaNoiseTemperature>
     AntennaSystem<stkobjects/AntennaSystem>
     AntennaVolumeGraphics<stkobjects/AntennaVolumeGraphics>
     AntennaVolumeLevel<stkobjects/AntennaVolumeLevel>
     AntennaVolumeLevelCollection<stkobjects/AntennaVolumeLevelCollection>
     AreaTarget<stkobjects/AreaTarget>
     AreaTargetCommonTasks<stkobjects/AreaTargetCommonTasks>
     AreaTargetGraphics<stkobjects/AreaTargetGraphics>
     AreaTargetGraphics3D<stkobjects/AreaTargetGraphics3D>
     AreaTypeEllipse<stkobjects/AreaTypeEllipse>
     AreaTypePattern<stkobjects/AreaTypePattern>
     AreaTypePatternCollection<stkobjects/AreaTypePatternCollection>
     AtmosphericAbsorptionModel<stkobjects/AtmosphericAbsorptionModel>
     AtmosphericAbsorptionModelCOMPlugin<stkobjects/AtmosphericAbsorptionModelCOMPlugin>
     AtmosphericAbsorptionModelGraphics3DACAP<stkobjects/AtmosphericAbsorptionModelGraphics3DACAP>
     AtmosphericAbsorptionModelITURP676Version13<stkobjects/AtmosphericAbsorptionModelITURP676Version13>
     AtmosphericAbsorptionModelITURP676Version9<stkobjects/AtmosphericAbsorptionModelITURP676Version9>
     AtmosphericAbsorptionModelScriptPlugin<stkobjects/AtmosphericAbsorptionModelScriptPlugin>
     AtmosphericAbsorptionModelSimpleSatcom<stkobjects/AtmosphericAbsorptionModelSimpleSatcom>
     AtmosphericAbsorptionModelTIREM550<stkobjects/AtmosphericAbsorptionModelTIREM550>
     AtmosphericAbsorptionModelTIREM630<stkobjects/AtmosphericAbsorptionModelTIREM630>
     AtmosphericTurbulenceModel<stkobjects/AtmosphericTurbulenceModel>
     AtmosphericTurbulenceModelConstant<stkobjects/AtmosphericTurbulenceModelConstant>
     AtmosphericTurbulenceModelHufnagelValley<stkobjects/AtmosphericTurbulenceModelHufnagelValley>
     AttitudeProfileAlignedAndConstrained<stkobjects/AttitudeProfileAlignedAndConstrained>
     AttitudeProfileAlignmentOffset<stkobjects/AttitudeProfileAlignmentOffset>
     AttitudeProfileAviator<stkobjects/AttitudeProfileAviator>
     AttitudeProfileConstraintOffset<stkobjects/AttitudeProfileConstraintOffset>
     AttitudeProfileCoordinatedTurn<stkobjects/AttitudeProfileCoordinatedTurn>
     AttitudeProfileFixedInAxes<stkobjects/AttitudeProfileFixedInAxes>
     AttitudeProfileGPS<stkobjects/AttitudeProfileGPS>
     AttitudeProfileInertial<stkobjects/AttitudeProfileInertial>
     AttitudeProfilePrecessingSpin<stkobjects/AttitudeProfilePrecessingSpin>
     AttitudeProfileSpinAboutSettings<stkobjects/AttitudeProfileSpinAboutSettings>
     AttitudeProfileSpinning<stkobjects/AttitudeProfileSpinning>
     AttitudeProfileYawToNadir<stkobjects/AttitudeProfileYawToNadir>
     AttitudeScheduleTimesCollection<stkobjects/AttitudeScheduleTimesCollection>
     AttitudeScheduleTimesElement<stkobjects/AttitudeScheduleTimesElement>
     AttitudeStandardBasic<stkobjects/AttitudeStandardBasic>
     AttitudeStandardOrbit<stkobjects/AttitudeStandardOrbit>
     AttitudeStandardRoute<stkobjects/AttitudeStandardRoute>
     AttitudeStandardTrajectory<stkobjects/AttitudeStandardTrajectory>
     AttitudeTorque<stkobjects/AttitudeTorque>
     AvailableFeatures<stkobjects/AvailableFeatures>
     BasicAzElMask<stkobjects/BasicAzElMask>
     Beamformer<stkobjects/Beamformer>
     BeamformerASCIIFile<stkobjects/BeamformerASCIIFile>
     BeamformerBlackmanHarris<stkobjects/BeamformerBlackmanHarris>
     BeamformerCosine<stkobjects/BeamformerCosine>
     BeamformerCosineX<stkobjects/BeamformerCosineX>
     BeamformerCustomTaperFile<stkobjects/BeamformerCustomTaperFile>
     BeamformerDolphChebyshev<stkobjects/BeamformerDolphChebyshev>
     BeamformerHamming<stkobjects/BeamformerHamming>
     BeamformerHann<stkobjects/BeamformerHann>
     BeamformerMVDR<stkobjects/BeamformerMVDR>
     BeamformerRaisedCosine<stkobjects/BeamformerRaisedCosine>
     BeamformerRaisedCosineSquared<stkobjects/BeamformerRaisedCosineSquared>
     BeamformerScript<stkobjects/BeamformerScript>
     BeamformerTaylor<stkobjects/BeamformerTaylor>
     BeamformerUniform<stkobjects/BeamformerUniform>
     BeerBouguerLambertLawLayer<stkobjects/BeerBouguerLambertLawLayer>
     BeerBouguerLambertLawLayerCollection<stkobjects/BeerBouguerLambertLawLayerCollection>
     CentralBody<stkobjects/CentralBody>
     CentralBodyCollection<stkobjects/CentralBodyCollection>
     CentralBodyEllipsoid<stkobjects/CentralBodyEllipsoid>
     CentralBodyTerrainCollection<stkobjects/CentralBodyTerrainCollection>
     CentralBodyTerrainCollectionElement<stkobjects/CentralBodyTerrainCollectionElement>
     Chain<stkobjects/Chain>
     ChainAnalysisOptions<stkobjects/ChainAnalysisOptions>
     ChainConnection<stkobjects/ChainConnection>
     ChainConnectionCollection<stkobjects/ChainConnectionCollection>
     ChainConstraints<stkobjects/ChainConstraints>
     ChainGraphics<stkobjects/ChainGraphics>
     ChainGraphics2DAnimation<stkobjects/ChainGraphics2DAnimation>
     ChainGraphics2DStatic<stkobjects/ChainGraphics2DStatic>
     ChainGraphics3D<stkobjects/ChainGraphics3D>
     ChainOptimalStrandOpts<stkobjects/ChainOptimalStrandOpts>
     ChainStrandAnalysisOpts<stkobjects/ChainStrandAnalysisOpts>
     ChainTimePeriod<stkobjects/ChainTimePeriod>
     ChainUserSpecifiedTimePeriod<stkobjects/ChainUserSpecifiedTimePeriod>
     ClassicalLocationArgumentOfLatitude<stkobjects/ClassicalLocationArgumentOfLatitude>
     ClassicalLocationEccentricAnomaly<stkobjects/ClassicalLocationEccentricAnomaly>
     ClassicalLocationMeanAnomaly<stkobjects/ClassicalLocationMeanAnomaly>
     ClassicalLocationTimePastAscendingNode<stkobjects/ClassicalLocationTimePastAscendingNode>
     ClassicalLocationTimePastPerigee<stkobjects/ClassicalLocationTimePastPerigee>
     ClassicalLocationTrueAnomaly<stkobjects/ClassicalLocationTrueAnomaly>
     ClassicalOrientation<stkobjects/ClassicalOrientation>
     ClassicalSizeShapeAltitude<stkobjects/ClassicalSizeShapeAltitude>
     ClassicalSizeShapeMeanMotion<stkobjects/ClassicalSizeShapeMeanMotion>
     ClassicalSizeShapePeriod<stkobjects/ClassicalSizeShapePeriod>
     ClassicalSizeShapeRadius<stkobjects/ClassicalSizeShapeRadius>
     ClassicalSizeShapeSemimajorAxis<stkobjects/ClassicalSizeShapeSemimajorAxis>
     CloudsAndFogFadingLossModel<stkobjects/CloudsAndFogFadingLossModel>
     CloudsAndFogFadingLossModelP840Version6<stkobjects/CloudsAndFogFadingLossModelP840Version6>
     CloudsAndFogFadingLossModelP840Version7<stkobjects/CloudsAndFogFadingLossModelP840Version7>
     CommRadCartesianLocation<stkobjects/CommRadCartesianLocation>
     CommRadComplexNumber<stkobjects/CommRadComplexNumber>
     CommRadComplexNumberCollection<stkobjects/CommRadComplexNumberCollection>
     CommRadPluginConfiguration<stkobjects/CommRadPluginConfiguration>
     CommSystem<stkobjects/CommSystem>
     CommSystemAccessEventDetection<stkobjects/CommSystemAccessEventDetection>
     CommSystemAccessEventDetectionSamplesOnly<stkobjects/CommSystemAccessEventDetectionSamplesOnly>
     CommSystemAccessEventDetectionSubsample<stkobjects/CommSystemAccessEventDetectionSubsample>
     CommSystemAccessOptions<stkobjects/CommSystemAccessOptions>
     CommSystemAccessSamplingMethod<stkobjects/CommSystemAccessSamplingMethod>
     CommSystemAccessSamplingMethodAdaptive<stkobjects/CommSystemAccessSamplingMethodAdaptive>
     CommSystemAccessSamplingMethodFixed<stkobjects/CommSystemAccessSamplingMethodFixed>
     CommSystemGraphics<stkobjects/CommSystemGraphics>
     CommSystemGraphics3D<stkobjects/CommSystemGraphics3D>
     CommSystemLinkSelectionCriteria<stkobjects/CommSystemLinkSelectionCriteria>
     CommSystemLinkSelectionCriteriaMaximumElevation<stkobjects/CommSystemLinkSelectionCriteriaMaximumElevation>
     CommSystemLinkSelectionCriteriaMinimumRange<stkobjects/CommSystemLinkSelectionCriteriaMinimumRange>
     CommSystemLinkSelectionCriteriaScriptPlugin<stkobjects/CommSystemLinkSelectionCriteriaScriptPlugin>
     ComponentAttrLinkEmbedControl<stkobjects/ComponentAttrLinkEmbedControl>
     ComponentDirectory<stkobjects/ComponentDirectory>
     ComponentInfo<stkobjects/ComponentInfo>
     ComponentInfoCollection<stkobjects/ComponentInfoCollection>
     Constellation<stkobjects/Constellation>
     ConstellationConstraintObjectRestriction<stkobjects/ConstellationConstraintObjectRestriction>
     ConstellationConstraintRestriction<stkobjects/ConstellationConstraintRestriction>
     ConstellationConstraints<stkobjects/ConstellationConstraints>
     ConstellationGraphics<stkobjects/ConstellationGraphics>
     ConstellationRouting<stkobjects/ConstellationRouting>
     CoverageAdvancedSettings<stkobjects/CoverageAdvancedSettings>
     CoverageAreaTargetsCollection<stkobjects/CoverageAreaTargetsCollection>
     CoverageAssetListCollection<stkobjects/CoverageAssetListCollection>
     CoverageAssetListElement<stkobjects/CoverageAssetListElement>
     CoverageBoundsCustomBoundary<stkobjects/CoverageBoundsCustomBoundary>
     CoverageBoundsCustomRegions<stkobjects/CoverageBoundsCustomRegions>
     CoverageBoundsGlobal<stkobjects/CoverageBoundsGlobal>
     CoverageBoundsLatitude<stkobjects/CoverageBoundsLatitude>
     CoverageBoundsLatitudeLine<stkobjects/CoverageBoundsLatitudeLine>
     CoverageBoundsLatitudeLongitudeRegion<stkobjects/CoverageBoundsLatitudeLongitudeRegion>
     CoverageBoundsLongitudeLine<stkobjects/CoverageBoundsLongitudeLine>
     CoverageDefinition<stkobjects/CoverageDefinition>
     CoverageEllipse<stkobjects/CoverageEllipse>
     CoverageEllipseCollection<stkobjects/CoverageEllipseCollection>
     CoverageGraphics<stkobjects/CoverageGraphics>
     CoverageGraphics2DAnimation<stkobjects/CoverageGraphics2DAnimation>
     CoverageGraphics2DProgress<stkobjects/CoverageGraphics2DProgress>
     CoverageGraphics2DStatic<stkobjects/CoverageGraphics2DStatic>
     CoverageGraphics3D<stkobjects/CoverageGraphics3D>
     CoverageGraphics3DAttributes<stkobjects/CoverageGraphics3DAttributes>
     CoverageGrid<stkobjects/CoverageGrid>
     CoverageGridInspector<stkobjects/CoverageGridInspector>
     CoverageGridPointSelection<stkobjects/CoverageGridPointSelection>
     CoverageInterval<stkobjects/CoverageInterval>
     CoverageLatLonBox<stkobjects/CoverageLatLonBox>
     CoverageLatLonBoxCollection<stkobjects/CoverageLatLonBoxCollection>
     CoveragePointDefinition<stkobjects/CoveragePointDefinition>
     CoveragePointFileListCollection<stkobjects/CoveragePointFileListCollection>
     CoverageRegionFilesCollection<stkobjects/CoverageRegionFilesCollection>
     CoverageResolutionArea<stkobjects/CoverageResolutionArea>
     CoverageResolutionDistance<stkobjects/CoverageResolutionDistance>
     CoverageResolutionLatLon<stkobjects/CoverageResolutionLatLon>
     CoverageSelectedGridPoint<stkobjects/CoverageSelectedGridPoint>
     CustomPropagationModel<stkobjects/CustomPropagationModel>
     DataProviderCollection<stkobjects/DataProviderCollection>
     DataProviderElement<stkobjects/DataProviderElement>
     DataProviderElements<stkobjects/DataProviderElements>
     DataProviderFixed<stkobjects/DataProviderFixed>
     DataProviderGroup<stkobjects/DataProviderGroup>
     DataProviderInterval<stkobjects/DataProviderInterval>
     DataProviderResult<stkobjects/DataProviderResult>
     DataProviderResultDataSet<stkobjects/DataProviderResultDataSet>
     DataProviderResultDataSetCollection<stkobjects/DataProviderResultDataSetCollection>
     DataProviderResultInterval<stkobjects/DataProviderResultInterval>
     DataProviderResultIntervalCollection<stkobjects/DataProviderResultIntervalCollection>
     DataProviderResultStatisticResult<stkobjects/DataProviderResultStatisticResult>
     DataProviderResultStatistics<stkobjects/DataProviderResultStatistics>
     DataProviderResultSubSection<stkobjects/DataProviderResultSubSection>
     DataProviderResultSubSectionCollection<stkobjects/DataProviderResultSubSectionCollection>
     DataProviderResultTextMessage<stkobjects/DataProviderResultTextMessage>
     DataProviderResultTimeArrayElements<stkobjects/DataProviderResultTimeArrayElements>
     DataProviderResultTimeVaryingExtremumResult<stkobjects/DataProviderResultTimeVaryingExtremumResult>
     DataProviders<stkobjects/DataProviders>
     DataProviderTimeVarying<stkobjects/DataProviderTimeVarying>
     DelaunayG<stkobjects/DelaunayG>
     DelaunayGOverSQRTmu<stkobjects/DelaunayGOverSQRTmu>
     DelaunayH<stkobjects/DelaunayH>
     DelaunayHOverSQRTmu<stkobjects/DelaunayHOverSQRTmu>
     DelaunayL<stkobjects/DelaunayL>
     DelaunayLOverSQRTmu<stkobjects/DelaunayLOverSQRTmu>
     DemodulatorModel<stkobjects/DemodulatorModel>
     DemodulatorModel16PSK<stkobjects/DemodulatorModel16PSK>
     DemodulatorModel8PSK<stkobjects/DemodulatorModel8PSK>
     DemodulatorModelBOC<stkobjects/DemodulatorModelBOC>
     DemodulatorModelBPSK<stkobjects/DemodulatorModelBPSK>
     DemodulatorModelDPSK<stkobjects/DemodulatorModelDPSK>
     DemodulatorModelExternal<stkobjects/DemodulatorModelExternal>
     DemodulatorModelExternalSource<stkobjects/DemodulatorModelExternalSource>
     DemodulatorModelFSK<stkobjects/DemodulatorModelFSK>
     DemodulatorModelMSK<stkobjects/DemodulatorModelMSK>
     DemodulatorModelNarrowbandUniform<stkobjects/DemodulatorModelNarrowbandUniform>
     DemodulatorModelNFSK<stkobjects/DemodulatorModelNFSK>
     DemodulatorModelOQPSK<stkobjects/DemodulatorModelOQPSK>
     DemodulatorModelPulsedSignal<stkobjects/DemodulatorModelPulsedSignal>
     DemodulatorModelQAM1024<stkobjects/DemodulatorModelQAM1024>
     DemodulatorModelQAM128<stkobjects/DemodulatorModelQAM128>
     DemodulatorModelQAM16<stkobjects/DemodulatorModelQAM16>
     DemodulatorModelQAM256<stkobjects/DemodulatorModelQAM256>
     DemodulatorModelQAM32<stkobjects/DemodulatorModelQAM32>
     DemodulatorModelQAM64<stkobjects/DemodulatorModelQAM64>
     DemodulatorModelQPSK<stkobjects/DemodulatorModelQPSK>
     DemodulatorModelScriptPlugin<stkobjects/DemodulatorModelScriptPlugin>
     DemodulatorModelWidebandGaussian<stkobjects/DemodulatorModelWidebandGaussian>
     DemodulatorModelWidebandUniform<stkobjects/DemodulatorModelWidebandUniform>
     DeticSizeAltitude<stkobjects/DeticSizeAltitude>
     DeticSizeRadius<stkobjects/DeticSizeRadius>
     DirectionProvider<stkobjects/DirectionProvider>
     DirectionProviderASCIIFile<stkobjects/DirectionProviderASCIIFile>
     DirectionProviderLink<stkobjects/DirectionProviderLink>
     DirectionProviderObject<stkobjects/DirectionProviderObject>
     DirectionProviderScript<stkobjects/DirectionProviderScript>
     DisplayTimesDuringAccess<stkobjects/DisplayTimesDuringAccess>
     DisplayTimesTimeComponent<stkobjects/DisplayTimesTimeComponent>
     Element<stkobjects/Element>
     ElementCollection<stkobjects/ElementCollection>
     ElementConfiguration<stkobjects/ElementConfiguration>
     ElementConfigurationASCIIFile<stkobjects/ElementConfigurationASCIIFile>
     ElementConfigurationCircular<stkobjects/ElementConfigurationCircular>
     ElementConfigurationHexagon<stkobjects/ElementConfigurationHexagon>
     ElementConfigurationHfssEepFile<stkobjects/ElementConfigurationHfssEepFile>
     ElementConfigurationLinear<stkobjects/ElementConfigurationLinear>
     ElementConfigurationPolygon<stkobjects/ElementConfigurationPolygon>
     EOIR<stkobjects/EOIR>
     EOIRMaterialElement<stkobjects/EOIRMaterialElement>
     EOIRMaterialElementCollection<stkobjects/EOIRMaterialElementCollection>
     EOIRShape<stkobjects/EOIRShape>
     EOIRShapeBox<stkobjects/EOIRShapeBox>
     EOIRShapeCollection<stkobjects/EOIRShapeCollection>
     EOIRShapeCone<stkobjects/EOIRShapeCone>
     EOIRShapeCoupler<stkobjects/EOIRShapeCoupler>
     EOIRShapeCustomMesh<stkobjects/EOIRShapeCustomMesh>
     EOIRShapeCylinder<stkobjects/EOIRShapeCylinder>
     EOIRShapeGEOComm<stkobjects/EOIRShapeGEOComm>
     EOIRShapeLEOComm<stkobjects/EOIRShapeLEOComm>
     EOIRShapeLEOImaging<stkobjects/EOIRShapeLEOImaging>
     EOIRShapeNone<stkobjects/EOIRShapeNone>
     EOIRShapeObject<stkobjects/EOIRShapeObject>
     EOIRShapePlate<stkobjects/EOIRShapePlate>
     EOIRShapeSphere<stkobjects/EOIRShapeSphere>
     EOIRShapeTargetSignature<stkobjects/EOIRShapeTargetSignature>
     EOIRStage<stkobjects/EOIRStage>
     EOIRStagePlume<stkobjects/EOIRStagePlume>
     EquinoctialSizeShapeMeanMotion<stkobjects/EquinoctialSizeShapeMeanMotion>
     EquinoctialSizeShapeSemimajorAxis<stkobjects/EquinoctialSizeShapeSemimajorAxis>
     EventDetectionNoSubSampling<stkobjects/EventDetectionNoSubSampling>
     EventDetectionSubSampling<stkobjects/EventDetectionSubSampling>
     ExportToolStepSize<stkobjects/ExportToolStepSize>
     ExportToolTimePeriod<stkobjects/ExportToolTimePeriod>
     Facility<stkobjects/Facility>
     FacilityGraphics<stkobjects/FacilityGraphics>
     FacilityGraphics3D<stkobjects/FacilityGraphics3D>
     FigureOfMerit<stkobjects/FigureOfMerit>
     FigureOfMeritAssetListCollection<stkobjects/FigureOfMeritAssetListCollection>
     FigureOfMeritAssetListElement<stkobjects/FigureOfMeritAssetListElement>
     FigureOfMeritDefinitionAccessConstraint<stkobjects/FigureOfMeritDefinitionAccessConstraint>
     FigureOfMeritDefinitionAccessSeparation<stkobjects/FigureOfMeritDefinitionAccessSeparation>
     FigureOfMeritDefinitionAgeOfData<stkobjects/FigureOfMeritDefinitionAgeOfData>
     FigureOfMeritDefinitionCompute<stkobjects/FigureOfMeritDefinitionCompute>
     FigureOfMeritDefinitionDataBest4<stkobjects/FigureOfMeritDefinitionDataBest4>
     FigureOfMeritDefinitionDataBestN<stkobjects/FigureOfMeritDefinitionDataBestN>
     FigureOfMeritDefinitionDataMinimumMaximum<stkobjects/FigureOfMeritDefinitionDataMinimumMaximum>
     FigureOfMeritDefinitionDataMinimumNumberOfAssets<stkobjects/FigureOfMeritDefinitionDataMinimumNumberOfAssets>
     FigureOfMeritDefinitionDataPercentLevel<stkobjects/FigureOfMeritDefinitionDataPercentLevel>
     FigureOfMeritDefinitionDilutionOfPrecision<stkobjects/FigureOfMeritDefinitionDilutionOfPrecision>
     FigureOfMeritDefinitionNavigationAccuracy<stkobjects/FigureOfMeritDefinitionNavigationAccuracy>
     FigureOfMeritDefinitionResponseTime<stkobjects/FigureOfMeritDefinitionResponseTime>
     FigureOfMeritDefinitionRevisitTime<stkobjects/FigureOfMeritDefinitionRevisitTime>
     FigureOfMeritDefinitionScalarCalculation<stkobjects/FigureOfMeritDefinitionScalarCalculation>
     FigureOfMeritDefinitionSimpleCoverage<stkobjects/FigureOfMeritDefinitionSimpleCoverage>
     FigureOfMeritDefinitionSystemAgeOfData<stkobjects/FigureOfMeritDefinitionSystemAgeOfData>
     FigureOfMeritDefinitionSystemResponseTime<stkobjects/FigureOfMeritDefinitionSystemResponseTime>
     FigureOfMeritDefinitionTimeAverageGap<stkobjects/FigureOfMeritDefinitionTimeAverageGap>
     FigureOfMeritGraphics<stkobjects/FigureOfMeritGraphics>
     FigureOfMeritGraphics2DAttributes<stkobjects/FigureOfMeritGraphics2DAttributes>
     FigureOfMeritGraphics2DAttributesAnimation<stkobjects/FigureOfMeritGraphics2DAttributesAnimation>
     FigureOfMeritGraphics2DColorOptions<stkobjects/FigureOfMeritGraphics2DColorOptions>
     FigureOfMeritGraphics2DContours<stkobjects/FigureOfMeritGraphics2DContours>
     FigureOfMeritGraphics2DContoursAnimation<stkobjects/FigureOfMeritGraphics2DContoursAnimation>
     FigureOfMeritGraphics2DLegend<stkobjects/FigureOfMeritGraphics2DLegend>
     FigureOfMeritGraphics2DLegendWindow<stkobjects/FigureOfMeritGraphics2DLegendWindow>
     FigureOfMeritGraphics2DLevelAttributesCollection<stkobjects/FigureOfMeritGraphics2DLevelAttributesCollection>
     FigureOfMeritGraphics2DLevelAttributesElement<stkobjects/FigureOfMeritGraphics2DLevelAttributesElement>
     FigureOfMeritGraphics2DPositionOnMap<stkobjects/FigureOfMeritGraphics2DPositionOnMap>
     FigureOfMeritGraphics2DRampColor<stkobjects/FigureOfMeritGraphics2DRampColor>
     FigureOfMeritGraphics2DRangeColorOptions<stkobjects/FigureOfMeritGraphics2DRangeColorOptions>
     FigureOfMeritGraphics2DTextOptions<stkobjects/FigureOfMeritGraphics2DTextOptions>
     FigureOfMeritGraphics3D<stkobjects/FigureOfMeritGraphics3D>
     FigureOfMeritGraphics3DAttributes<stkobjects/FigureOfMeritGraphics3DAttributes>
     FigureOfMeritGraphics3DLegendWindow<stkobjects/FigureOfMeritGraphics3DLegendWindow>
     FigureOfMeritGridInspector<stkobjects/FigureOfMeritGridInspector>
     FigureOfMeritNavigationAccuracyMethodConstant<stkobjects/FigureOfMeritNavigationAccuracyMethodConstant>
     FigureOfMeritNavigationAccuracyMethodElevationAngle<stkobjects/FigureOfMeritNavigationAccuracyMethodElevationAngle>
     FigureOfMeritSatisfaction<stkobjects/FigureOfMeritSatisfaction>
     FigureOfMeritUncertainties<stkobjects/FigureOfMeritUncertainties>
     Graphics2DRangeContours<stkobjects/Graphics2DRangeContours>
     Graphics3DArticulationFile<stkobjects/Graphics3DArticulationFile>
     Graphics3DAzElMask<stkobjects/Graphics3DAzElMask>
     Graphics3DBorderWall<stkobjects/Graphics3DBorderWall>
     Graphics3DDataDisplayCollection<stkobjects/Graphics3DDataDisplayCollection>
     Graphics3DDataDisplayElement<stkobjects/Graphics3DDataDisplayElement>
     Graphics3DDetailThreshold<stkobjects/Graphics3DDetailThreshold>
     Graphics3DLabelSwapDistance<stkobjects/Graphics3DLabelSwapDistance>
     Graphics3DMarker<stkobjects/Graphics3DMarker>
     Graphics3DMarkerFile<stkobjects/Graphics3DMarkerFile>
     Graphics3DMarkerShape<stkobjects/Graphics3DMarkerShape>
     Graphics3DModelArticulation<stkobjects/Graphics3DModelArticulation>
     Graphics3DModelCollection<stkobjects/Graphics3DModelCollection>
     Graphics3DModelFile<stkobjects/Graphics3DModelFile>
     Graphics3DModelglTFImageBased<stkobjects/Graphics3DModelglTFImageBased>
     Graphics3DModelItem<stkobjects/Graphics3DModelItem>
     Graphics3DModelPointing<stkobjects/Graphics3DModelPointing>
     Graphics3DModelTransformation<stkobjects/Graphics3DModelTransformation>
     Graphics3DModelTransformationCollection<stkobjects/Graphics3DModelTransformationCollection>
     Graphics3DOffset<stkobjects/Graphics3DOffset>
     Graphics3DOffsetAttachment<stkobjects/Graphics3DOffsetAttachment>
     Graphics3DOffsetLabel<stkobjects/Graphics3DOffsetLabel>
     Graphics3DOffsetRotate<stkobjects/Graphics3DOffsetRotate>
     Graphics3DOffsetTransformation<stkobjects/Graphics3DOffsetTransformation>
     Graphics3DPointableElementsCollection<stkobjects/Graphics3DPointableElementsCollection>
     Graphics3DPointableElementsElement<stkobjects/Graphics3DPointableElementsElement>
     Graphics3DRangeContours<stkobjects/Graphics3DRangeContours>
     Graphics3DReferenceAngle<stkobjects/Graphics3DReferenceAngle>
     Graphics3DReferenceAxes<stkobjects/Graphics3DReferenceAxes>
     Graphics3DReferencePlane<stkobjects/Graphics3DReferencePlane>
     Graphics3DReferencePoint<stkobjects/Graphics3DReferencePoint>
     Graphics3DReferenceVector<stkobjects/Graphics3DReferenceVector>
     Graphics3DReferenceVectorGeometryToolComponentCollection<stkobjects/Graphics3DReferenceVectorGeometryToolComponentCollection>
     Graphics3DVaporTrail<stkobjects/Graphics3DVaporTrail>
     Graphics3DVector<stkobjects/Graphics3DVector>
     GroundVehicle<stkobjects/GroundVehicle>
     GroundVehicleExportTools<stkobjects/GroundVehicleExportTools>
     GroundVehicleGraphics<stkobjects/GroundVehicleGraphics>
     GroundVehicleGraphics3D<stkobjects/GroundVehicleGraphics3D>
     IntegratorStepSizeControl<stkobjects/IntegratorStepSizeControl>
     IntegratorTimeRegularization<stkobjects/IntegratorTimeRegularization>
     IonosphericFadingLossModel<stkobjects/IonosphericFadingLossModel>
     IonosphericFadingLossModelP531Version13<stkobjects/IonosphericFadingLossModelP531Version13>
     KeyValueCollection<stkobjects/KeyValueCollection>
     LabelNote<stkobjects/LabelNote>
     LabelNoteCollection<stkobjects/LabelNoteCollection>
     LaserAtmosphericLossModel<stkobjects/LaserAtmosphericLossModel>
     LaserAtmosphericLossModelBeerBouguerLambertLaw<stkobjects/LaserAtmosphericLossModelBeerBouguerLambertLaw>
     LaserEnvironment<stkobjects/LaserEnvironment>
     LaserPropagationChannel<stkobjects/LaserPropagationChannel>
     LaserTroposphericScintillationLossModel<stkobjects/LaserTroposphericScintillationLossModel>
     LaserTroposphericScintillationLossModelITURP1814<stkobjects/LaserTroposphericScintillationLossModelITURP1814>
     LatitudeLongitudeAltitudeCentric<stkobjects/LatitudeLongitudeAltitudeCentric>
     LatitudeLongitudeAltitudeDetic<stkobjects/LatitudeLongitudeAltitudeDetic>
     LatitudeLongitudeAltitudePosition<stkobjects/LatitudeLongitudeAltitudePosition>
     LaunchVehicle<stkobjects/LaunchVehicle>
     LaunchVehicleControlFixedApogeeAltitude<stkobjects/LaunchVehicleControlFixedApogeeAltitude>
     LaunchVehicleControlFixedDeltaV<stkobjects/LaunchVehicleControlFixedDeltaV>
     LaunchVehicleControlFixedDeltaVMinimumEccentricity<stkobjects/LaunchVehicleControlFixedDeltaVMinimumEccentricity>
     LaunchVehicleControlFixedTimeOfFlight<stkobjects/LaunchVehicleControlFixedTimeOfFlight>
     LaunchVehicleExportTools<stkobjects/LaunchVehicleExportTools>
     LaunchVehicleGraphics<stkobjects/LaunchVehicleGraphics>
     LaunchVehicleGraphics3D<stkobjects/LaunchVehicleGraphics3D>
     LaunchVehicleInitialState<stkobjects/LaunchVehicleInitialState>
     LaunchVehicleLocationCentric<stkobjects/LaunchVehicleLocationCentric>
     LaunchVehicleLocationDetic<stkobjects/LaunchVehicleLocationDetic>
     LevelAttribute<stkobjects/LevelAttribute>
     LevelAttributeCollection<stkobjects/LevelAttributeCollection>
     LineTarget<stkobjects/LineTarget>
     LineTargetGraphics<stkobjects/LineTargetGraphics>
     LineTargetGraphics3D<stkobjects/LineTargetGraphics3D>
     LineTargetPoint<stkobjects/LineTargetPoint>
     LineTargetPointCollection<stkobjects/LineTargetPointCollection>
     LinkMargin<stkobjects/LinkMargin>
     LinkToObject<stkobjects/LinkToObject>
     LocationVectorGeometryToolPoint<stkobjects/LocationVectorGeometryToolPoint>
     MilitaryStandard2525bSymbols<stkobjects/MilitaryStandard2525bSymbols>
     Missile<stkobjects/Missile>
     MissileEOIR<stkobjects/MissileEOIR>
     MissileExportTools<stkobjects/MissileExportTools>
     MissileGraphics<stkobjects/MissileGraphics>
     MissileGraphics3D<stkobjects/MissileGraphics3D>
     MixedSphericalFlightPathAngleHorizontal<stkobjects/MixedSphericalFlightPathAngleHorizontal>
     MixedSphericalFlightPathAngleVertical<stkobjects/MixedSphericalFlightPathAngleVertical>
     MODTRANLookupTablePropagationModel<stkobjects/MODTRANLookupTablePropagationModel>
     MODTRANPropagationModel<stkobjects/MODTRANPropagationModel>
     ModulatorModel<stkobjects/ModulatorModel>
     ModulatorModel16PSK<stkobjects/ModulatorModel16PSK>
     ModulatorModel8PSK<stkobjects/ModulatorModel8PSK>
     ModulatorModelBOC<stkobjects/ModulatorModelBOC>
     ModulatorModelBPSK<stkobjects/ModulatorModelBPSK>
     ModulatorModelDPSK<stkobjects/ModulatorModelDPSK>
     ModulatorModelExternal<stkobjects/ModulatorModelExternal>
     ModulatorModelExternalSource<stkobjects/ModulatorModelExternalSource>
     ModulatorModelFSK<stkobjects/ModulatorModelFSK>
     ModulatorModelMSK<stkobjects/ModulatorModelMSK>
     ModulatorModelNarrowbandUniform<stkobjects/ModulatorModelNarrowbandUniform>
     ModulatorModelNFSK<stkobjects/ModulatorModelNFSK>
     ModulatorModelOQPSK<stkobjects/ModulatorModelOQPSK>
     ModulatorModelPulsedSignal<stkobjects/ModulatorModelPulsedSignal>
     ModulatorModelQAM1024<stkobjects/ModulatorModelQAM1024>
     ModulatorModelQAM128<stkobjects/ModulatorModelQAM128>
     ModulatorModelQAM16<stkobjects/ModulatorModelQAM16>
     ModulatorModelQAM256<stkobjects/ModulatorModelQAM256>
     ModulatorModelQAM32<stkobjects/ModulatorModelQAM32>
     ModulatorModelQAM64<stkobjects/ModulatorModelQAM64>
     ModulatorModelQPSK<stkobjects/ModulatorModelQPSK>
     ModulatorModelScriptPluginCustomPSD<stkobjects/ModulatorModelScriptPluginCustomPSD>
     ModulatorModelScriptPluginIdealPSD<stkobjects/ModulatorModelScriptPluginIdealPSD>
     ModulatorModelWidebandGaussian<stkobjects/ModulatorModelWidebandGaussian>
     ModulatorModelWidebandUniform<stkobjects/ModulatorModelWidebandUniform>
     MTO<stkobjects/MTO>
     MTOAnalysis<stkobjects/MTOAnalysis>
     MTOAnalysisFieldOfView<stkobjects/MTOAnalysisFieldOfView>
     MTOAnalysisPosition<stkobjects/MTOAnalysisPosition>
     MTOAnalysisRange<stkobjects/MTOAnalysisRange>
     MTOAnalysisVisibility<stkobjects/MTOAnalysisVisibility>
     MTODefaultGraphics2DTrack<stkobjects/MTODefaultGraphics2DTrack>
     MTODefaultGraphics3DTrack<stkobjects/MTODefaultGraphics3DTrack>
     MTODefaultTrack<stkobjects/MTODefaultTrack>
     MTOGlobalTrackOptions<stkobjects/MTOGlobalTrackOptions>
     MTOGraphics<stkobjects/MTOGraphics>
     MTOGraphics2DFadeTimes<stkobjects/MTOGraphics2DFadeTimes>
     MTOGraphics2DGlobalTrackOptions<stkobjects/MTOGraphics2DGlobalTrackOptions>
     MTOGraphics2DLeadTrailTimes<stkobjects/MTOGraphics2DLeadTrailTimes>
     MTOGraphics2DLine<stkobjects/MTOGraphics2DLine>
     MTOGraphics2DMarker<stkobjects/MTOGraphics2DMarker>
     MTOGraphics2DTrack<stkobjects/MTOGraphics2DTrack>
     MTOGraphics2DTrackCollection<stkobjects/MTOGraphics2DTrackCollection>
     MTOGraphics3D<stkobjects/MTOGraphics3D>
     MTOGraphics3DDropLines<stkobjects/MTOGraphics3DDropLines>
     MTOGraphics3DGlobalTrackOptions<stkobjects/MTOGraphics3DGlobalTrackOptions>
     MTOGraphics3DMarker<stkobjects/MTOGraphics3DMarker>
     MTOGraphics3DModel<stkobjects/MTOGraphics3DModel>
     MTOGraphics3DModelArticulation<stkobjects/MTOGraphics3DModelArticulation>
     MTOGraphics3DPoint<stkobjects/MTOGraphics3DPoint>
     MTOGraphics3DSwapDistances<stkobjects/MTOGraphics3DSwapDistances>
     MTOGraphics3DTrack<stkobjects/MTOGraphics3DTrack>
     MTOGraphics3DTrackCollection<stkobjects/MTOGraphics3DTrackCollection>
     MTOTrack<stkobjects/MTOTrack>
     MTOTrackCollection<stkobjects/MTOTrackCollection>
     MTOTrackPoint<stkobjects/MTOTrackPoint>
     MTOTrackPointCollection<stkobjects/MTOTrackPointCollection>
     ObjectCoverage<stkobjects/ObjectCoverage>
     ObjectCoverageFigureOfMerit<stkobjects/ObjectCoverageFigureOfMerit>
     ObjectLaserEnvironment<stkobjects/ObjectLaserEnvironment>
     ObjectLink<stkobjects/ObjectLink>
     ObjectLinkCollection<stkobjects/ObjectLinkCollection>
     ObjectRFEnvironment<stkobjects/ObjectRFEnvironment>
     OceanTides<stkobjects/OceanTides>
     OnePointAccess<stkobjects/OnePointAccess>
     OnePointAccessConstraint<stkobjects/OnePointAccessConstraint>
     OnePointAccessConstraintCollection<stkobjects/OnePointAccessConstraintCollection>
     OnePointAccessResult<stkobjects/OnePointAccessResult>
     OnePointAccessResultCollection<stkobjects/OnePointAccessResultCollection>
     OrbitState<stkobjects/OrbitState>
     OrbitStateCartesian<stkobjects/OrbitStateCartesian>
     OrbitStateClassical<stkobjects/OrbitStateClassical>
     OrbitStateCoordinateSystem<stkobjects/OrbitStateCoordinateSystem>
     OrbitStateDelaunay<stkobjects/OrbitStateDelaunay>
     OrbitStateDetic<stkobjects/OrbitStateDetic>
     OrbitStateEquinoctial<stkobjects/OrbitStateEquinoctial>
     OrbitStateMixedSpherical<stkobjects/OrbitStateMixedSpherical>
     OrbitStateSpherical<stkobjects/OrbitStateSpherical>
     OrientationLongitudeOfAscending<stkobjects/OrientationLongitudeOfAscending>
     OrientationRightAscensionOfAscendingNode<stkobjects/OrientationRightAscensionOfAscendingNode>
     PassBreak<stkobjects/PassBreak>
     PassBreakNumberingDateOfFirstPass<stkobjects/PassBreakNumberingDateOfFirstPass>
     PassBreakNumberingFirstPassNumber<stkobjects/PassBreakNumberingFirstPassNumber>
     PathCollection<stkobjects/PathCollection>
     Place<stkobjects/Place>
     PlaceGraphics<stkobjects/PlaceGraphics>
     PlaceGraphics3D<stkobjects/PlaceGraphics3D>
     Planet<stkobjects/Planet>
     PlanetCommonTasks<stkobjects/PlanetCommonTasks>
     PlanetGraphics<stkobjects/PlanetGraphics>
     PlanetGraphics3D<stkobjects/PlanetGraphics3D>
     PlanetOrbitDisplayTime<stkobjects/PlanetOrbitDisplayTime>
     PlanetPositionCentralBody<stkobjects/PlanetPositionCentralBody>
     PlanetPositionFile<stkobjects/PlanetPositionFile>
     PlatformLaserEnvironment<stkobjects/PlatformLaserEnvironment>
     PlatformRFEnvironment<stkobjects/PlatformRFEnvironment>
     PointingStrategy<stkobjects/PointingStrategy>
     PointingStrategyFixed<stkobjects/PointingStrategyFixed>
     PointingStrategySpinning<stkobjects/PointingStrategySpinning>
     PointingStrategyTargeted<stkobjects/PointingStrategyTargeted>
     PointTargetGraphics3DModel<stkobjects/PointTargetGraphics3DModel>
     Polarization<stkobjects/Polarization>
     PolarizationElliptical<stkobjects/PolarizationElliptical>
     PolarizationHorizontal<stkobjects/PolarizationHorizontal>
     PolarizationLeftHandCircular<stkobjects/PolarizationLeftHandCircular>
     PolarizationLinear<stkobjects/PolarizationLinear>
     PolarizationRightHandCircular<stkobjects/PolarizationRightHandCircular>
     PolarizationVertical<stkobjects/PolarizationVertical>
     Preferences<stkobjects/Preferences>
     PreferencesConnect<stkobjects/PreferencesConnect>
     PreferencesPythonPlugins<stkobjects/PreferencesPythonPlugins>
     PreferencesVDF<stkobjects/PreferencesVDF>
     Priority<stkobjects/Priority>
     PriorityCollection<stkobjects/PriorityCollection>
     ProgressBarEventArguments<stkobjects/ProgressBarEventArguments>
     PropagationChannel<stkobjects/PropagationChannel>
     Propagator11Parameters<stkobjects/Propagator11Parameters>
     Propagator11ParametersDescriptor<stkobjects/Propagator11ParametersDescriptor>
     Propagator11ParametersDescriptorCollection<stkobjects/Propagator11ParametersDescriptorCollection>
     PropagatorAviator<stkobjects/PropagatorAviator>
     PropagatorBallistic<stkobjects/PropagatorBallistic>
     PropagatorDefinitionExportTool<stkobjects/PropagatorDefinitionExportTool>
     PropagatorGPS<stkobjects/PropagatorGPS>
     PropagatorGreatArc<stkobjects/PropagatorGreatArc>
     PropagatorHPOP<stkobjects/PropagatorHPOP>
     PropagatorHPOPStaticForceModelSettings<stkobjects/PropagatorHPOPStaticForceModelSettings>
     PropagatorHPOPThirdBodyGravityCollection<stkobjects/PropagatorHPOPThirdBodyGravityCollection>
     PropagatorHPOPThirdBodyGravityElement<stkobjects/PropagatorHPOPThirdBodyGravityElement>
     PropagatorJ2Perturbation<stkobjects/PropagatorJ2Perturbation>
     PropagatorJ4Perturbation<stkobjects/PropagatorJ4Perturbation>
     PropagatorLOP<stkobjects/PropagatorLOP>
     PropagatorLOPThirdBodyGravity<stkobjects/PropagatorLOPThirdBodyGravity>
     PropagatorRealtime<stkobjects/PropagatorRealtime>
     PropagatorRealtimeCartesianPoints<stkobjects/PropagatorRealtimeCartesianPoints>
     PropagatorRealtimeDeticPoints<stkobjects/PropagatorRealtimeDeticPoints>
     PropagatorRealtimeHeadingPitch<stkobjects/PropagatorRealtimeHeadingPitch>
     PropagatorRealtimePointBuilder<stkobjects/PropagatorRealtimePointBuilder>
     PropagatorRealtimeUTMPoints<stkobjects/PropagatorRealtimeUTMPoints>
     PropagatorSGP4<stkobjects/PropagatorSGP4>
     PropagatorSGP4AutoUpdate<stkobjects/PropagatorSGP4AutoUpdate>
     PropagatorSGP4AutoUpdateFileSource<stkobjects/PropagatorSGP4AutoUpdateFileSource>
     PropagatorSGP4AutoUpdateOnlineSource<stkobjects/PropagatorSGP4AutoUpdateOnlineSource>
     PropagatorSGP4AutoUpdateProperties<stkobjects/PropagatorSGP4AutoUpdateProperties>
     PropagatorSGP4CommonTasks<stkobjects/PropagatorSGP4CommonTasks>
     PropagatorSGP4LoadFile<stkobjects/PropagatorSGP4LoadFile>
     PropagatorSGP4OnlineLoad<stkobjects/PropagatorSGP4OnlineLoad>
     PropagatorSGP4PropagatorSettings<stkobjects/PropagatorSGP4PropagatorSettings>
     PropagatorSGP4Segment<stkobjects/PropagatorSGP4Segment>
     PropagatorSGP4SegmentCollection<stkobjects/PropagatorSGP4SegmentCollection>
     PropagatorSimpleAscent<stkobjects/PropagatorSimpleAscent>
     PropagatorSP3<stkobjects/PropagatorSP3>
     PropagatorSP3File<stkobjects/PropagatorSP3File>
     PropagatorSP3FileCollection<stkobjects/PropagatorSP3FileCollection>
     PropagatorSPICE<stkobjects/PropagatorSPICE>
     PropagatorSPICESegment<stkobjects/PropagatorSPICESegment>
     PropagatorSPICESegmentsCollection<stkobjects/PropagatorSPICESegmentsCollection>
     PropagatorSTKExternal<stkobjects/PropagatorSTKExternal>
     PropagatorTwoBody<stkobjects/PropagatorTwoBody>
     PropagatorUserExternal<stkobjects/PropagatorUserExternal>
     Radar<stkobjects/Radar>
     RadarAccessGraphics<stkobjects/RadarAccessGraphics>
     RadarActivity<stkobjects/RadarActivity>
     RadarActivityAlwaysActive<stkobjects/RadarActivityAlwaysActive>
     RadarActivityAlwaysInactive<stkobjects/RadarActivityAlwaysInactive>
     RadarActivityTimeComponentList<stkobjects/RadarActivityTimeComponentList>
     RadarActivityTimeComponentListCollection<stkobjects/RadarActivityTimeComponentListCollection>
     RadarActivityTimeComponentListElement<stkobjects/RadarActivityTimeComponentListElement>
     RadarActivityTimeIntervalList<stkobjects/RadarActivityTimeIntervalList>
     RadarActivityTimeIntervalListCollection<stkobjects/RadarActivityTimeIntervalListCollection>
     RadarActivityTimeIntervalListElement<stkobjects/RadarActivityTimeIntervalListElement>
     RadarAntennaBeam<stkobjects/RadarAntennaBeam>
     RadarAntennaBeamCollection<stkobjects/RadarAntennaBeamCollection>
     RadarClutter<stkobjects/RadarClutter>
     RadarContinuousWaveAnalysisModeFixedTime<stkobjects/RadarContinuousWaveAnalysisModeFixedTime>
     RadarContinuousWaveAnalysisModeGoalSNR<stkobjects/RadarContinuousWaveAnalysisModeGoalSNR>
     RadarCrossSection<stkobjects/RadarCrossSection>
     RadarCrossSectionComputeStrategy<stkobjects/RadarCrossSectionComputeStrategy>
     RadarCrossSectionComputeStrategyAnsysCSVFile<stkobjects/RadarCrossSectionComputeStrategyAnsysCSVFile>
     RadarCrossSectionComputeStrategyConstantValue<stkobjects/RadarCrossSectionComputeStrategyConstantValue>
     RadarCrossSectionComputeStrategyExternalFile<stkobjects/RadarCrossSectionComputeStrategyExternalFile>
     RadarCrossSectionComputeStrategyPlugin<stkobjects/RadarCrossSectionComputeStrategyPlugin>
     RadarCrossSectionComputeStrategyScriptPlugin<stkobjects/RadarCrossSectionComputeStrategyScriptPlugin>
     RadarCrossSectionContourLevel<stkobjects/RadarCrossSectionContourLevel>
     RadarCrossSectionContourLevelCollection<stkobjects/RadarCrossSectionContourLevelCollection>
     RadarCrossSectionFrequencyBand<stkobjects/RadarCrossSectionFrequencyBand>
     RadarCrossSectionFrequencyBandCollection<stkobjects/RadarCrossSectionFrequencyBandCollection>
     RadarCrossSectionGraphics<stkobjects/RadarCrossSectionGraphics>
     RadarCrossSectionGraphics3D<stkobjects/RadarCrossSectionGraphics3D>
     RadarCrossSectionInheritable<stkobjects/RadarCrossSectionInheritable>
     RadarCrossSectionModel<stkobjects/RadarCrossSectionModel>
     RadarCrossSectionVolumeGraphics<stkobjects/RadarCrossSectionVolumeGraphics>
     RadarCrossSectionVolumeLevel<stkobjects/RadarCrossSectionVolumeLevel>
     RadarCrossSectionVolumeLevelCollection<stkobjects/RadarCrossSectionVolumeLevelCollection>
     RadarDopplerClutterFilters<stkobjects/RadarDopplerClutterFilters>
     RadarGraphics<stkobjects/RadarGraphics>
     RadarGraphics3D<stkobjects/RadarGraphics3D>
     RadarJamming<stkobjects/RadarJamming>
     RadarModeBistaticReceiver<stkobjects/RadarModeBistaticReceiver>
     RadarModeBistaticReceiverSAR<stkobjects/RadarModeBistaticReceiverSAR>
     RadarModeBistaticReceiverSearchTrack<stkobjects/RadarModeBistaticReceiverSearchTrack>
     RadarModeBistaticTransmitter<stkobjects/RadarModeBistaticTransmitter>
     RadarModeBistaticTransmitterSAR<stkobjects/RadarModeBistaticTransmitterSAR>
     RadarModeBistaticTransmitterSearchTrack<stkobjects/RadarModeBistaticTransmitterSearchTrack>
     RadarModel<stkobjects/RadarModel>
     RadarModelBistaticReceiver<stkobjects/RadarModelBistaticReceiver>
     RadarModelBistaticTransmitter<stkobjects/RadarModelBistaticTransmitter>
     RadarModelMonostatic<stkobjects/RadarModelMonostatic>
     RadarModelMultifunction<stkobjects/RadarModelMultifunction>
     RadarModeMonostatic<stkobjects/RadarModeMonostatic>
     RadarModeMonostaticSAR<stkobjects/RadarModeMonostaticSAR>
     RadarModeMonostaticSearchTrack<stkobjects/RadarModeMonostaticSearchTrack>
     RadarModulator<stkobjects/RadarModulator>
     RadarMultifunctionDetectionProcessing<stkobjects/RadarMultifunctionDetectionProcessing>
     RadarMultifunctionWaveformStrategySettings<stkobjects/RadarMultifunctionWaveformStrategySettings>
     RadarMultipathGraphics<stkobjects/RadarMultipathGraphics>
     RadarProbabilityOfDetection<stkobjects/RadarProbabilityOfDetection>
     RadarProbabilityOfDetectionCFAR<stkobjects/RadarProbabilityOfDetectionCFAR>
     RadarProbabilityOfDetectionCFARCellAveraging<stkobjects/RadarProbabilityOfDetectionCFARCellAveraging>
     RadarProbabilityOfDetectionCFAROrderedStatistics<stkobjects/RadarProbabilityOfDetectionCFAROrderedStatistics>
     RadarProbabilityOfDetectionNonCFAR<stkobjects/RadarProbabilityOfDetectionNonCFAR>
     RadarProbabilityOfDetectionPlugin<stkobjects/RadarProbabilityOfDetectionPlugin>
     RadarPulseIntegrationFixedNumberOfPulses<stkobjects/RadarPulseIntegrationFixedNumberOfPulses>
     RadarPulseIntegrationGoalSNR<stkobjects/RadarPulseIntegrationGoalSNR>
     RadarReceiver<stkobjects/RadarReceiver>
     RadarSTCAttenuation<stkobjects/RadarSTCAttenuation>
     RadarSTCAttenuationDecayFactor<stkobjects/RadarSTCAttenuationDecayFactor>
     RadarSTCAttenuationDecaySlope<stkobjects/RadarSTCAttenuationDecaySlope>
     RadarSTCAttenuationMapAzimuthRange<stkobjects/RadarSTCAttenuationMapAzimuthRange>
     RadarSTCAttenuationMapElevationRange<stkobjects/RadarSTCAttenuationMapElevationRange>
     RadarSTCAttenuationMapRange<stkobjects/RadarSTCAttenuationMapRange>
     RadarSTCAttenuationPlugin<stkobjects/RadarSTCAttenuationPlugin>
     RadarTransmitter<stkobjects/RadarTransmitter>
     RadarTransmitterMultifunction<stkobjects/RadarTransmitterMultifunction>
     RadarWaveformBistaticReceiverSearchTrackContinuous<stkobjects/RadarWaveformBistaticReceiverSearchTrackContinuous>
     RadarWaveformBistaticReceiverSearchTrackFixedPRF<stkobjects/RadarWaveformBistaticReceiverSearchTrackFixedPRF>
     RadarWaveformBistaticTransmitterSearchTrackContinuous<stkobjects/RadarWaveformBistaticTransmitterSearchTrackContinuous>
     RadarWaveformBistaticTransmitterSearchTrackFixedPRF<stkobjects/RadarWaveformBistaticTransmitterSearchTrackFixedPRF>
     RadarWaveformMonostaticSearchTrackContinuous<stkobjects/RadarWaveformMonostaticSearchTrackContinuous>
     RadarWaveformMonostaticSearchTrackFixedPRF<stkobjects/RadarWaveformMonostaticSearchTrackFixedPRF>
     RadarWaveformSarPulseDefinition<stkobjects/RadarWaveformSarPulseDefinition>
     RadarWaveformSarPulseIntegration<stkobjects/RadarWaveformSarPulseIntegration>
     RadarWaveformSearchTrackPulseDefinition<stkobjects/RadarWaveformSearchTrackPulseDefinition>
     RadiationPressure<stkobjects/RadiationPressure>
     RainLossModel<stkobjects/RainLossModel>
     RainLossModelCCIR1983<stkobjects/RainLossModelCCIR1983>
     RainLossModelCrane1982<stkobjects/RainLossModelCrane1982>
     RainLossModelCrane1985<stkobjects/RainLossModelCrane1985>
     RainLossModelITURP618Version10<stkobjects/RainLossModelITURP618Version10>
     RainLossModelITURP618Version12<stkobjects/RainLossModelITURP618Version12>
     RainLossModelITURP618Version13<stkobjects/RainLossModelITURP618Version13>
     RainLossModelScriptPlugin<stkobjects/RainLossModelScriptPlugin>
     ReceivePolarizationElliptical<stkobjects/ReceivePolarizationElliptical>
     ReceivePolarizationHorizontal<stkobjects/ReceivePolarizationHorizontal>
     ReceivePolarizationLeftHandCircular<stkobjects/ReceivePolarizationLeftHandCircular>
     ReceivePolarizationLinear<stkobjects/ReceivePolarizationLinear>
     ReceivePolarizationRightHandCircular<stkobjects/ReceivePolarizationRightHandCircular>
     ReceivePolarizationVertical<stkobjects/ReceivePolarizationVertical>
     Receiver<stkobjects/Receiver>
     ReceiverGraphics<stkobjects/ReceiverGraphics>
     ReceiverGraphics3D<stkobjects/ReceiverGraphics3D>
     ReceiverModel<stkobjects/ReceiverModel>
     ReceiverModelCable<stkobjects/ReceiverModelCable>
     ReceiverModelComplex<stkobjects/ReceiverModelComplex>
     ReceiverModelLaser<stkobjects/ReceiverModelLaser>
     ReceiverModelMedium<stkobjects/ReceiverModelMedium>
     ReceiverModelMultibeam<stkobjects/ReceiverModelMultibeam>
     ReceiverModelScriptPluginLaser<stkobjects/ReceiverModelScriptPluginLaser>
     ReceiverModelScriptPluginRF<stkobjects/ReceiverModelScriptPluginRF>
     ReceiverModelSimple<stkobjects/ReceiverModelSimple>
     RefractionCoefficients<stkobjects/RefractionCoefficients>
     RefractionModelEffectiveRadiusMethod<stkobjects/RefractionModelEffectiveRadiusMethod>
     RefractionModelITURP8344<stkobjects/RefractionModelITURP8344>
     RefractionModelSCFMethod<stkobjects/RefractionModelSCFMethod>
     RepeatGroundTrackNumbering<stkobjects/RepeatGroundTrackNumbering>
     ReTransmitterModelComplex<stkobjects/ReTransmitterModelComplex>
     ReTransmitterModelMedium<stkobjects/ReTransmitterModelMedium>
     ReTransmitterModelSimple<stkobjects/ReTransmitterModelSimple>
     RFEnvironment<stkobjects/RFEnvironment>
     RFFilterModel<stkobjects/RFFilterModel>
     RFFilterModelBessel<stkobjects/RFFilterModelBessel>
     RFFilterModelButterworth<stkobjects/RFFilterModelButterworth>
     RFFilterModelChebyshev<stkobjects/RFFilterModelChebyshev>
     RFFilterModelCosineWindow<stkobjects/RFFilterModelCosineWindow>
     RFFilterModelElliptic<stkobjects/RFFilterModelElliptic>
     RFFilterModelExternal<stkobjects/RFFilterModelExternal>
     RFFilterModelFIR<stkobjects/RFFilterModelFIR>
     RFFilterModelFIRBoxCar<stkobjects/RFFilterModelFIRBoxCar>
     RFFilterModelGaussianWindow<stkobjects/RFFilterModelGaussianWindow>
     RFFilterModelHammingWindow<stkobjects/RFFilterModelHammingWindow>
     RFFilterModelIIR<stkobjects/RFFilterModelIIR>
     RFFilterModelRaisedCosine<stkobjects/RFFilterModelRaisedCosine>
     RFFilterModelRCLowPass<stkobjects/RFFilterModelRCLowPass>
     RFFilterModelRectangular<stkobjects/RFFilterModelRectangular>
     RFFilterModelRootRaisedCosine<stkobjects/RFFilterModelRootRaisedCosine>
     RFFilterModelScriptPlugin<stkobjects/RFFilterModelScriptPlugin>
     RFFilterModelSinc<stkobjects/RFFilterModelSinc>
     RFFilterModelSincEnvelopeSinc<stkobjects/RFFilterModelSincEnvelopeSinc>
     RFInterference<stkobjects/RFInterference>
     RotationRateAndOffset<stkobjects/RotationRateAndOffset>
     SamplingMethodAdaptive<stkobjects/SamplingMethodAdaptive>
     SamplingMethodFixedStep<stkobjects/SamplingMethodFixedStep>
     Satellite<stkobjects/Satellite>
     SatelliteCollection<stkobjects/SatelliteCollection>
     SatelliteExportTools<stkobjects/SatelliteExportTools>
     SatelliteGraphics<stkobjects/SatelliteGraphics>
     SatelliteGraphics3D<stkobjects/SatelliteGraphics3D>
     SatelliteGraphics3DModel<stkobjects/SatelliteGraphics3DModel>
     ScatteringPointCollection<stkobjects/ScatteringPointCollection>
     ScatteringPointCollectionElement<stkobjects/ScatteringPointCollectionElement>
     ScatteringPointModel<stkobjects/ScatteringPointModel>
     ScatteringPointModelConstantCoefficient<stkobjects/ScatteringPointModelConstantCoefficient>
     ScatteringPointModelPlugin<stkobjects/ScatteringPointModelPlugin>
     ScatteringPointModelWindTurbine<stkobjects/ScatteringPointModelWindTurbine>
     ScatteringPointProvider<stkobjects/ScatteringPointProvider>
     ScatteringPointProviderCollection<stkobjects/ScatteringPointProviderCollection>
     ScatteringPointProviderCollectionElement<stkobjects/ScatteringPointProviderCollectionElement>
     ScatteringPointProviderList<stkobjects/ScatteringPointProviderList>
     ScatteringPointProviderPlugin<stkobjects/ScatteringPointProviderPlugin>
     ScatteringPointProviderPointsFile<stkobjects/ScatteringPointProviderPointsFile>
     ScatteringPointProviderRangeOverCFARCells<stkobjects/ScatteringPointProviderRangeOverCFARCells>
     ScatteringPointProviderSinglePoint<stkobjects/ScatteringPointProviderSinglePoint>
     ScatteringPointProviderSmoothOblateEarth<stkobjects/ScatteringPointProviderSmoothOblateEarth>
     Scenario<stkobjects/Scenario>
     Scenario3dFont<stkobjects/Scenario3dFont>
     ScenarioAnimation<stkobjects/ScenarioAnimation>
     ScenarioAnimationTimePeriod<stkobjects/ScenarioAnimationTimePeriod>
     ScenarioBeforeSaveEventArguments<stkobjects/ScenarioBeforeSaveEventArguments>
     ScenarioDatabase<stkobjects/ScenarioDatabase>
     ScenarioDatabaseCollection<stkobjects/ScenarioDatabaseCollection>
     ScenarioEarthData<stkobjects/ScenarioEarthData>
     ScenarioGraphics<stkobjects/ScenarioGraphics>
     ScenarioGraphics3D<stkobjects/ScenarioGraphics3D>
     ScenarioSpaceEnvironment<stkobjects/ScenarioSpaceEnvironment>
     ScheduleTime<stkobjects/ScheduleTime>
     ScheduleTimeCollection<stkobjects/ScheduleTimeCollection>
     Sensor<stkobjects/Sensor>
     SensorAccessAdvancedSettings<stkobjects/SensorAccessAdvancedSettings>
     SensorAzElMaskFile<stkobjects/SensorAzElMaskFile>
     SensorCommonTasks<stkobjects/SensorCommonTasks>
     SensorComplexConicPattern<stkobjects/SensorComplexConicPattern>
     SensorCustomPattern<stkobjects/SensorCustomPattern>
     SensorEOIRBand<stkobjects/SensorEOIRBand>
     SensorEOIRBandCollection<stkobjects/SensorEOIRBandCollection>
     SensorEOIRPattern<stkobjects/SensorEOIRPattern>
     SensorEOIRRadiometricPair<stkobjects/SensorEOIRRadiometricPair>
     SensorEOIRSaturationCollection<stkobjects/SensorEOIRSaturationCollection>
     SensorEOIRSensitivityCollection<stkobjects/SensorEOIRSensitivityCollection>
     SensorGraphics<stkobjects/SensorGraphics>
     SensorGraphics3D<stkobjects/SensorGraphics3D>
     SensorGraphics3DOffset<stkobjects/SensorGraphics3DOffset>
     SensorGraphics3DProjectionElement<stkobjects/SensorGraphics3DProjectionElement>
     SensorGraphics3DPulse<stkobjects/SensorGraphics3DPulse>
     SensorGraphics3DSpaceProjectionCollection<stkobjects/SensorGraphics3DSpaceProjectionCollection>
     SensorGraphics3DTargetProjectionCollection<stkobjects/SensorGraphics3DTargetProjectionCollection>
     SensorHalfPowerPattern<stkobjects/SensorHalfPowerPattern>
     SensorPointing3DModel<stkobjects/SensorPointing3DModel>
     SensorPointingAlongVector<stkobjects/SensorPointingAlongVector>
     SensorPointingExternal<stkobjects/SensorPointingExternal>
     SensorPointingFixed<stkobjects/SensorPointingFixed>
     SensorPointingFixedInAxes<stkobjects/SensorPointingFixedInAxes>
     SensorPointingGrazingAltitude<stkobjects/SensorPointingGrazingAltitude>
     SensorPointingSchedule<stkobjects/SensorPointingSchedule>
     SensorPointingSpinning<stkobjects/SensorPointingSpinning>
     SensorPointingTargeted<stkobjects/SensorPointingTargeted>
     SensorPointingTargetedBoresightFixed<stkobjects/SensorPointingTargetedBoresightFixed>
     SensorPointingTargetedBoresightTrack<stkobjects/SensorPointingTargetedBoresightTrack>
     SensorProjection<stkobjects/SensorProjection>
     SensorProjectionConstantAltitude<stkobjects/SensorProjectionConstantAltitude>
     SensorProjectionDisplayDistance<stkobjects/SensorProjectionDisplayDistance>
     SensorProjectionObjectAltitude<stkobjects/SensorProjectionObjectAltitude>
     SensorRectangularPattern<stkobjects/SensorRectangularPattern>
     SensorSARPattern<stkobjects/SensorSARPattern>
     SensorSimpleConicPattern<stkobjects/SensorSimpleConicPattern>
     SensorTarget<stkobjects/SensorTarget>
     SensorTargetCollection<stkobjects/SensorTargetCollection>
     SensorUnknownPattern<stkobjects/SensorUnknownPattern>
     Ship<stkobjects/Ship>
     ShipExportTools<stkobjects/ShipExportTools>
     ShipGraphics<stkobjects/ShipGraphics>
     ShipGraphics3D<stkobjects/ShipGraphics3D>
     SolarActivityConfiguration<stkobjects/SolarActivityConfiguration>
     SolarActivityConfigurationSolarFlux<stkobjects/SolarActivityConfigurationSolarFlux>
     SolarActivityConfigurationSunspotNumber<stkobjects/SolarActivityConfigurationSunspotNumber>
     SolarFluxGeoMagneticFileSettings<stkobjects/SolarFluxGeoMagneticFileSettings>
     SolarFluxGeoMagneticValueSettings<stkobjects/SolarFluxGeoMagneticValueSettings>
     SolarRadiationPressureModelGPS<stkobjects/SolarRadiationPressureModelGPS>
     SolarRadiationPressureModelPlugin<stkobjects/SolarRadiationPressureModelPlugin>
     SolarRadiationPressureModelPluginSettings<stkobjects/SolarRadiationPressureModelPluginSettings>
     SolarRadiationPressureModelSpherical<stkobjects/SolarRadiationPressureModelSpherical>
     SolidTides<stkobjects/SolidTides>
     SpaceEnvironment<stkobjects/SpaceEnvironment>
     SpaceEnvironmentGraphics<stkobjects/SpaceEnvironmentGraphics>
     SpaceEnvironmentMagneticField<stkobjects/SpaceEnvironmentMagneticField>
     SpaceEnvironmentMagnitudeFieldGraphics2D<stkobjects/SpaceEnvironmentMagnitudeFieldGraphics2D>
     SpaceEnvironmentMagnitudeFieldLine<stkobjects/SpaceEnvironmentMagnitudeFieldLine>
     SpaceEnvironmentParticleFlux<stkobjects/SpaceEnvironmentParticleFlux>
     SpaceEnvironmentRadiation<stkobjects/SpaceEnvironmentRadiation>
     SpaceEnvironmentRadiationDoseRateCollection<stkobjects/SpaceEnvironmentRadiationDoseRateCollection>
     SpaceEnvironmentRadiationDoseRateElement<stkobjects/SpaceEnvironmentRadiationDoseRateElement>
     SpaceEnvironmentRadiationEnergyMethodEnergies<stkobjects/SpaceEnvironmentRadiationEnergyMethodEnergies>
     SpaceEnvironmentRadiationEnergyValues<stkobjects/SpaceEnvironmentRadiationEnergyValues>
     SpaceEnvironmentRadiationEnvironment<stkobjects/SpaceEnvironmentRadiationEnvironment>
     SpaceEnvironmentSAAContour<stkobjects/SpaceEnvironmentSAAContour>
     SpaceEnvironmentScenarioGraphics3D<stkobjects/SpaceEnvironmentScenarioGraphics3D>
     SpaceEnvironmentVehicleTemperature<stkobjects/SpaceEnvironmentVehicleTemperature>
     SpatialState<stkobjects/SpatialState>
     SphericalFlightPathAngleHorizontal<stkobjects/SphericalFlightPathAngleHorizontal>
     SphericalFlightPathAngleVertical<stkobjects/SphericalFlightPathAngleVertical>
     Star<stkobjects/Star>
     StarCollection<stkobjects/StarCollection>
     StarGraphics<stkobjects/StarGraphics>
     StarGraphics3D<stkobjects/StarGraphics3D>
     StarInformation<stkobjects/StarInformation>
     STKObject<stkobjects/STKObject>
     STKObjectChangedEventArguments<stkobjects/STKObjectChangedEventArguments>
     STKObjectCutCopyPasteEventArguments<stkobjects/STKObjectCutCopyPasteEventArguments>
     STKObjectModelContext<stkobjects/STKObjectModelContext>
     STKObjectPreDeleteEventArguments<stkobjects/STKObjectPreDeleteEventArguments>
     STKObjectRoot<stkobjects/STKObjectRoot>
     Subset<stkobjects/Subset>
     Swath<stkobjects/Swath>
     SystemNoiseTemperature<stkobjects/SystemNoiseTemperature>
     Target<stkobjects/Target>
     TargetGraphics<stkobjects/TargetGraphics>
     TargetGraphics3D<stkobjects/TargetGraphics3D>
     TargetSelectionMethod<stkobjects/TargetSelectionMethod>
     TargetSelectionMethodClosingVelocity<stkobjects/TargetSelectionMethodClosingVelocity>
     TargetSelectionMethodPriority<stkobjects/TargetSelectionMethodPriority>
     TargetSelectionMethodRange<stkobjects/TargetSelectionMethodRange>
     Terrain<stkobjects/Terrain>
     TerrainCollection<stkobjects/TerrainCollection>
     TerrainNormalSlopeAzimuth<stkobjects/TerrainNormalSlopeAzimuth>
     Tileset3D<stkobjects/Tileset3D>
     Tileset3DCollection<stkobjects/Tileset3DCollection>
     TimeIntervalCollection<stkobjects/TimeIntervalCollection>
     TimeIntervalCollectionReadOnly<stkobjects/TimeIntervalCollectionReadOnly>
     TimePeriod<stkobjects/TimePeriod>
     TimePeriodValue<stkobjects/TimePeriodValue>
     TransferFunctionInputBackOffOutputBackOffTable<stkobjects/TransferFunctionInputBackOffOutputBackOffTable>
     TransferFunctionInputBackOffOutputBackOffTableRow<stkobjects/TransferFunctionInputBackOffOutputBackOffTableRow>
     TransferFunctionInputBackOffVsCOverImTable<stkobjects/TransferFunctionInputBackOffVsCOverImTable>
     TransferFunctionInputBackOffVsCOverImTableRow<stkobjects/TransferFunctionInputBackOffVsCOverImTableRow>
     TransferFunctionPolynomialCollection<stkobjects/TransferFunctionPolynomialCollection>
     Transmitter<stkobjects/Transmitter>
     TransmitterGraphics<stkobjects/TransmitterGraphics>
     TransmitterGraphics3D<stkobjects/TransmitterGraphics3D>
     TransmitterModel<stkobjects/TransmitterModel>
     TransmitterModelCable<stkobjects/TransmitterModelCable>
     TransmitterModelComplex<stkobjects/TransmitterModelComplex>
     TransmitterModelLaser<stkobjects/TransmitterModelLaser>
     TransmitterModelMedium<stkobjects/TransmitterModelMedium>
     TransmitterModelMultibeam<stkobjects/TransmitterModelMultibeam>
     TransmitterModelScriptPluginLaser<stkobjects/TransmitterModelScriptPluginLaser>
     TransmitterModelScriptPluginRF<stkobjects/TransmitterModelScriptPluginRF>
     TransmitterModelSimple<stkobjects/TransmitterModelSimple>
     TroposphericScintillationFadingLossModel<stkobjects/TroposphericScintillationFadingLossModel>
     TroposphericScintillationFadingLossModelP618Version12<stkobjects/TroposphericScintillationFadingLossModelP618Version12>
     TroposphericScintillationFadingLossModelP618Version8<stkobjects/TroposphericScintillationFadingLossModelP618Version8>
     UrbanTerrestrialLossModel<stkobjects/UrbanTerrestrialLossModel>
     UrbanTerrestrialLossModelTwoRay<stkobjects/UrbanTerrestrialLossModelTwoRay>
     UrbanTerrestrialLossModelWirelessInSite64<stkobjects/UrbanTerrestrialLossModelWirelessInSite64>
     VehicleAccessAdvancedSettings<stkobjects/VehicleAccessAdvancedSettings>
     VehicleAttitudeExportTool<stkobjects/VehicleAttitudeExportTool>
     VehicleAttitudeExternal<stkobjects/VehicleAttitudeExternal>
     VehicleAttitudeMaximumSlewAcceleration<stkobjects/VehicleAttitudeMaximumSlewAcceleration>
     VehicleAttitudeMaximumSlewRate<stkobjects/VehicleAttitudeMaximumSlewRate>
     VehicleAttitudePointing<stkobjects/VehicleAttitudePointing>
     VehicleAttitudeRealTime<stkobjects/VehicleAttitudeRealTime>
     VehicleAttitudeRealTimeDataReference<stkobjects/VehicleAttitudeRealTimeDataReference>
     VehicleAttitudeSlewConstrained<stkobjects/VehicleAttitudeSlewConstrained>
     VehicleAttitudeSlewFixedRate<stkobjects/VehicleAttitudeSlewFixedRate>
     VehicleAttitudeSlewFixedTime<stkobjects/VehicleAttitudeSlewFixedTime>
     VehicleAttitudeTargetSlew<stkobjects/VehicleAttitudeTargetSlew>
     VehicleAttitudeTrendingControlAviator<stkobjects/VehicleAttitudeTrendingControlAviator>
     VehicleBreakAngleBreakByLatitude<stkobjects/VehicleBreakAngleBreakByLatitude>
     VehicleBreakAngleBreakByLongitude<stkobjects/VehicleBreakAngleBreakByLongitude>
     VehicleCentralBodies<stkobjects/VehicleCentralBodies>
     VehicleConsiderAnalysisCollection<stkobjects/VehicleConsiderAnalysisCollection>
     VehicleConsiderAnalysisCollectionElement<stkobjects/VehicleConsiderAnalysisCollectionElement>
     VehicleCoordinateAxesCustom<stkobjects/VehicleCoordinateAxesCustom>
     VehicleCorrelationListCollection<stkobjects/VehicleCorrelationListCollection>
     VehicleCorrelationListElement<stkobjects/VehicleCorrelationListElement>
     VehicleCovariance<stkobjects/VehicleCovariance>
     VehicleDefinition<stkobjects/VehicleDefinition>
     VehicleDuration<stkobjects/VehicleDuration>
     VehicleEclipseBodies<stkobjects/VehicleEclipseBodies>
     VehicleEclipsingBodies<stkobjects/VehicleEclipsingBodies>
     VehicleEllipseDataCollection<stkobjects/VehicleEllipseDataCollection>
     VehicleEllipseDataElement<stkobjects/VehicleEllipseDataElement>
     VehicleEOIR<stkobjects/VehicleEOIR>
     VehicleEphemerisBinaryExportTool<stkobjects/VehicleEphemerisBinaryExportTool>
     VehicleEphemerisCCSDSExportTool<stkobjects/VehicleEphemerisCCSDSExportTool>
     VehicleEphemerisCCSDSv2ExportTool<stkobjects/VehicleEphemerisCCSDSv2ExportTool>
     VehicleEphemerisCCSDSv3ExportTool<stkobjects/VehicleEphemerisCCSDSv3ExportTool>
     VehicleEphemerisCode500ExportTool<stkobjects/VehicleEphemerisCode500ExportTool>
     VehicleEphemerisExportTool<stkobjects/VehicleEphemerisExportTool>
     VehicleEphemerisSPICEExportTool<stkobjects/VehicleEphemerisSPICEExportTool>
     VehicleExponentialDensityModelParameters<stkobjects/VehicleExponentialDensityModelParameters>
     VehicleGPSAlmanacProperties<stkobjects/VehicleGPSAlmanacProperties>
     VehicleGPSAlmanacPropertiesSEM<stkobjects/VehicleGPSAlmanacPropertiesSEM>
     VehicleGPSAlmanacPropertiesSP3<stkobjects/VehicleGPSAlmanacPropertiesSP3>
     VehicleGPSAlmanacPropertiesYUMA<stkobjects/VehicleGPSAlmanacPropertiesYUMA>
     VehicleGPSAutoUpdate<stkobjects/VehicleGPSAutoUpdate>
     VehicleGPSAutoUpdateFileSource<stkobjects/VehicleGPSAutoUpdateFileSource>
     VehicleGPSAutoUpdateOnlineSource<stkobjects/VehicleGPSAutoUpdateOnlineSource>
     VehicleGPSAutoUpdateProperties<stkobjects/VehicleGPSAutoUpdateProperties>
     VehicleGPSElement<stkobjects/VehicleGPSElement>
     VehicleGPSElementCollection<stkobjects/VehicleGPSElementCollection>
     VehicleGPSSpecifyAlmanac<stkobjects/VehicleGPSSpecifyAlmanac>
     VehicleGraphics2DAttributesAccess<stkobjects/VehicleGraphics2DAttributesAccess>
     VehicleGraphics2DAttributesCustom<stkobjects/VehicleGraphics2DAttributesCustom>
     VehicleGraphics2DAttributesOrbit<stkobjects/VehicleGraphics2DAttributesOrbit>
     VehicleGraphics2DAttributesRealtime<stkobjects/VehicleGraphics2DAttributesRealtime>
     VehicleGraphics2DAttributesRoute<stkobjects/VehicleGraphics2DAttributesRoute>
     VehicleGraphics2DAttributesTimeComponents<stkobjects/VehicleGraphics2DAttributesTimeComponents>
     VehicleGraphics2DAttributesTrajectory<stkobjects/VehicleGraphics2DAttributesTrajectory>
     VehicleGraphics2DElevationContours<stkobjects/VehicleGraphics2DElevationContours>
     VehicleGraphics2DElevationGroundElevation<stkobjects/VehicleGraphics2DElevationGroundElevation>
     VehicleGraphics2DElevationsCollection<stkobjects/VehicleGraphics2DElevationsCollection>
     VehicleGraphics2DElevationsElement<stkobjects/VehicleGraphics2DElevationsElement>
     VehicleGraphics2DElevationSwathHalfWidth<stkobjects/VehicleGraphics2DElevationSwathHalfWidth>
     VehicleGraphics2DElevationVehicleHalfAngle<stkobjects/VehicleGraphics2DElevationVehicleHalfAngle>
     VehicleGraphics2DGroundEllipsesCollection<stkobjects/VehicleGraphics2DGroundEllipsesCollection>
     VehicleGraphics2DGroundEllipsesElement<stkobjects/VehicleGraphics2DGroundEllipsesElement>
     VehicleGraphics2DInterval<stkobjects/VehicleGraphics2DInterval>
     VehicleGraphics2DIntervalsCollection<stkobjects/VehicleGraphics2DIntervalsCollection>
     VehicleGraphics2DLeadDataFraction<stkobjects/VehicleGraphics2DLeadDataFraction>
     VehicleGraphics2DLeadDataTime<stkobjects/VehicleGraphics2DLeadDataTime>
     VehicleGraphics2DLeadTrailData<stkobjects/VehicleGraphics2DLeadTrailData>
     VehicleGraphics2DLighting<stkobjects/VehicleGraphics2DLighting>
     VehicleGraphics2DLightingElement<stkobjects/VehicleGraphics2DLightingElement>
     VehicleGraphics2DLine<stkobjects/VehicleGraphics2DLine>
     VehicleGraphics2DOrbitPassData<stkobjects/VehicleGraphics2DOrbitPassData>
     VehicleGraphics2DPasses<stkobjects/VehicleGraphics2DPasses>
     VehicleGraphics2DPassResolution<stkobjects/VehicleGraphics2DPassResolution>
     VehicleGraphics2DPassShowPasses<stkobjects/VehicleGraphics2DPassShowPasses>
     VehicleGraphics2DRoutePassData<stkobjects/VehicleGraphics2DRoutePassData>
     VehicleGraphics2DRouteResolution<stkobjects/VehicleGraphics2DRouteResolution>
     VehicleGraphics2DSAA<stkobjects/VehicleGraphics2DSAA>
     VehicleGraphics2DSwath<stkobjects/VehicleGraphics2DSwath>
     VehicleGraphics2DTimeComponentsCollection<stkobjects/VehicleGraphics2DTimeComponentsCollection>
     VehicleGraphics2DTimeComponentsEventCollectionElement<stkobjects/VehicleGraphics2DTimeComponentsEventCollectionElement>
     VehicleGraphics2DTimeComponentsEventElement<stkobjects/VehicleGraphics2DTimeComponentsEventElement>
     VehicleGraphics2DTimeEventsCollection<stkobjects/VehicleGraphics2DTimeEventsCollection>
     VehicleGraphics2DTimeEventsElement<stkobjects/VehicleGraphics2DTimeEventsElement>
     VehicleGraphics2DTimeEventTypeLine<stkobjects/VehicleGraphics2DTimeEventTypeLine>
     VehicleGraphics2DTimeEventTypeMarker<stkobjects/VehicleGraphics2DTimeEventTypeMarker>
     VehicleGraphics2DTimeEventTypeText<stkobjects/VehicleGraphics2DTimeEventTypeText>
     VehicleGraphics2DTrailDataFraction<stkobjects/VehicleGraphics2DTrailDataFraction>
     VehicleGraphics2DTrailDataTime<stkobjects/VehicleGraphics2DTrailDataTime>
     VehicleGraphics2DTrajectoryPassData<stkobjects/VehicleGraphics2DTrajectoryPassData>
     VehicleGraphics2DTrajectoryResolution<stkobjects/VehicleGraphics2DTrajectoryResolution>
     VehicleGraphics2DWaypointMarker<stkobjects/VehicleGraphics2DWaypointMarker>
     VehicleGraphics2DWaypointMarkersCollection<stkobjects/VehicleGraphics2DWaypointMarkersCollection>
     VehicleGraphics2DWaypointMarkersElement<stkobjects/VehicleGraphics2DWaypointMarkersElement>
     VehicleGraphics3DAttributesBasic<stkobjects/VehicleGraphics3DAttributesBasic>
     VehicleGraphics3DAttributesIntervals<stkobjects/VehicleGraphics3DAttributesIntervals>
     VehicleGraphics3DBearingBox<stkobjects/VehicleGraphics3DBearingBox>
     VehicleGraphics3DBearingEllipse<stkobjects/VehicleGraphics3DBearingEllipse>
     VehicleGraphics3DBPlaneEvent<stkobjects/VehicleGraphics3DBPlaneEvent>
     VehicleGraphics3DBPlaneInstance<stkobjects/VehicleGraphics3DBPlaneInstance>
     VehicleGraphics3DBPlaneInstancesCollection<stkobjects/VehicleGraphics3DBPlaneInstancesCollection>
     VehicleGraphics3DBPlanePoint<stkobjects/VehicleGraphics3DBPlanePoint>
     VehicleGraphics3DBPlanePointCollection<stkobjects/VehicleGraphics3DBPlanePointCollection>
     VehicleGraphics3DBPlanes<stkobjects/VehicleGraphics3DBPlanes>
     VehicleGraphics3DBPlaneTargetPoint<stkobjects/VehicleGraphics3DBPlaneTargetPoint>
     VehicleGraphics3DBPlaneTargetPointPositionCartesian<stkobjects/VehicleGraphics3DBPlaneTargetPointPositionCartesian>
     VehicleGraphics3DBPlaneTargetPointPositionPolar<stkobjects/VehicleGraphics3DBPlaneTargetPointPositionPolar>
     VehicleGraphics3DBPlaneTemplate<stkobjects/VehicleGraphics3DBPlaneTemplate>
     VehicleGraphics3DBPlaneTemplateDisplayCollection<stkobjects/VehicleGraphics3DBPlaneTemplateDisplayCollection>
     VehicleGraphics3DBPlaneTemplateDisplayElement<stkobjects/VehicleGraphics3DBPlaneTemplateDisplayElement>
     VehicleGraphics3DBPlaneTemplatesCollection<stkobjects/VehicleGraphics3DBPlaneTemplatesCollection>
     VehicleGraphics3DControlBox<stkobjects/VehicleGraphics3DControlBox>
     VehicleGraphics3DCovariance<stkobjects/VehicleGraphics3DCovariance>
     VehicleGraphics3DCovariancePointingContour<stkobjects/VehicleGraphics3DCovariancePointingContour>
     VehicleGraphics3DDataFraction<stkobjects/VehicleGraphics3DDataFraction>
     VehicleGraphics3DDataTime<stkobjects/VehicleGraphics3DDataTime>
     VehicleGraphics3DDefaultAttributes<stkobjects/VehicleGraphics3DDefaultAttributes>
     VehicleGraphics3DDropLinePathItem<stkobjects/VehicleGraphics3DDropLinePathItem>
     VehicleGraphics3DDropLinePathItemCollection<stkobjects/VehicleGraphics3DDropLinePathItemCollection>
     VehicleGraphics3DDropLinePositionItem<stkobjects/VehicleGraphics3DDropLinePositionItem>
     VehicleGraphics3DDropLinePositionItemCollection<stkobjects/VehicleGraphics3DDropLinePositionItemCollection>
     VehicleGraphics3DElevationContours<stkobjects/VehicleGraphics3DElevationContours>
     VehicleGraphics3DEllipsoid<stkobjects/VehicleGraphics3DEllipsoid>
     VehicleGraphics3DGeoBox<stkobjects/VehicleGraphics3DGeoBox>
     VehicleGraphics3DIntervalsCollection<stkobjects/VehicleGraphics3DIntervalsCollection>
     VehicleGraphics3DIntervalsElement<stkobjects/VehicleGraphics3DIntervalsElement>
     VehicleGraphics3DLeadTrailData<stkobjects/VehicleGraphics3DLeadTrailData>
     VehicleGraphics3DLineOfBearing<stkobjects/VehicleGraphics3DLineOfBearing>
     VehicleGraphics3DModelRoute<stkobjects/VehicleGraphics3DModelRoute>
     VehicleGraphics3DModelTrajectory<stkobjects/VehicleGraphics3DModelTrajectory>
     VehicleGraphics3DOrbitDropLines<stkobjects/VehicleGraphics3DOrbitDropLines>
     VehicleGraphics3DOrbitPassData<stkobjects/VehicleGraphics3DOrbitPassData>
     VehicleGraphics3DOrbitProximity<stkobjects/VehicleGraphics3DOrbitProximity>
     VehicleGraphics3DOrbitTickMarks<stkobjects/VehicleGraphics3DOrbitTickMarks>
     VehicleGraphics3DOrbitTrackData<stkobjects/VehicleGraphics3DOrbitTrackData>
     VehicleGraphics3DPass<stkobjects/VehicleGraphics3DPass>
     VehicleGraphics3DPathTickMarks<stkobjects/VehicleGraphics3DPathTickMarks>
     VehicleGraphics3DRoute<stkobjects/VehicleGraphics3DRoute>
     VehicleGraphics3DRouteDropLines<stkobjects/VehicleGraphics3DRouteDropLines>
     VehicleGraphics3DRouteProximity<stkobjects/VehicleGraphics3DRouteProximity>
     VehicleGraphics3DSAA<stkobjects/VehicleGraphics3DSAA>
     VehicleGraphics3DSigmaScaleProbability<stkobjects/VehicleGraphics3DSigmaScaleProbability>
     VehicleGraphics3DSigmaScaleScale<stkobjects/VehicleGraphics3DSigmaScaleScale>
     VehicleGraphics3DSize<stkobjects/VehicleGraphics3DSize>
     VehicleGraphics3DSystemsCollection<stkobjects/VehicleGraphics3DSystemsCollection>
     VehicleGraphics3DSystemsElement<stkobjects/VehicleGraphics3DSystemsElement>
     VehicleGraphics3DSystemsSpecialElement<stkobjects/VehicleGraphics3DSystemsSpecialElement>
     VehicleGraphics3DTickDataLine<stkobjects/VehicleGraphics3DTickDataLine>
     VehicleGraphics3DTickDataPoint<stkobjects/VehicleGraphics3DTickDataPoint>
     VehicleGraphics3DTrajectory<stkobjects/VehicleGraphics3DTrajectory>
     VehicleGraphics3DTrajectoryDropLines<stkobjects/VehicleGraphics3DTrajectoryDropLines>
     VehicleGraphics3DTrajectoryPassData<stkobjects/VehicleGraphics3DTrajectoryPassData>
     VehicleGraphics3DTrajectoryProximity<stkobjects/VehicleGraphics3DTrajectoryProximity>
     VehicleGraphics3DTrajectoryTickMarks<stkobjects/VehicleGraphics3DTrajectoryTickMarks>
     VehicleGraphics3DTrajectoryTrackData<stkobjects/VehicleGraphics3DTrajectoryTrackData>
     VehicleGraphics3DVelocityCovariance<stkobjects/VehicleGraphics3DVelocityCovariance>
     VehicleGraphics3DWaypointMarkersCollection<stkobjects/VehicleGraphics3DWaypointMarkersCollection>
     VehicleGraphics3DWaypointMarkersElement<stkobjects/VehicleGraphics3DWaypointMarkersElement>
     VehicleGravity<stkobjects/VehicleGravity>
     VehicleGroundEllipseElement<stkobjects/VehicleGroundEllipseElement>
     VehicleGroundEllipsesCollection<stkobjects/VehicleGroundEllipsesCollection>
     VehicleHPOPCentralBodyGravity<stkobjects/VehicleHPOPCentralBodyGravity>
     VehicleHPOPDragModel<stkobjects/VehicleHPOPDragModel>
     VehicleHPOPDragModelPlugin<stkobjects/VehicleHPOPDragModelPlugin>
     VehicleHPOPDragModelPluginSettings<stkobjects/VehicleHPOPDragModelPluginSettings>
     VehicleHPOPDragModelSpherical<stkobjects/VehicleHPOPDragModelSpherical>
     VehicleHPOPForceModel<stkobjects/VehicleHPOPForceModel>
     VehicleHPOPForceModelDrag<stkobjects/VehicleHPOPForceModelDrag>
     VehicleHPOPForceModelDragOptions<stkobjects/VehicleHPOPForceModelDragOptions>
     VehicleHPOPForceModelMoreOptions<stkobjects/VehicleHPOPForceModelMoreOptions>
     VehicleHPOPSolarRadiationPressure<stkobjects/VehicleHPOPSolarRadiationPressure>
     VehicleHPOPSolarRadiationPressureModel<stkobjects/VehicleHPOPSolarRadiationPressureModel>
     VehicleHPOPSolarRadiationPressureOptions<stkobjects/VehicleHPOPSolarRadiationPressureOptions>
     VehicleImpactLocationCentric<stkobjects/VehicleImpactLocationCentric>
     VehicleImpactLocationDetic<stkobjects/VehicleImpactLocationDetic>
     VehicleImpactLocationLaunchAzEl<stkobjects/VehicleImpactLocationLaunchAzEl>
     VehicleImpactLocationPoint<stkobjects/VehicleImpactLocationPoint>
     VehicleInertia<stkobjects/VehicleInertia>
     VehicleInitialState<stkobjects/VehicleInitialState>
     VehicleIntegratedAttitude<stkobjects/VehicleIntegratedAttitude>
     VehicleIntegrator<stkobjects/VehicleIntegrator>
     VehicleInterpolation<stkobjects/VehicleInterpolation>
     VehicleLOPCentralBodyGravity<stkobjects/VehicleLOPCentralBodyGravity>
     VehicleLOPDragSettings<stkobjects/VehicleLOPDragSettings>
     VehicleLOPForceModel<stkobjects/VehicleLOPForceModel>
     VehicleLOPForceModelDrag<stkobjects/VehicleLOPForceModelDrag>
     VehicleLOPSolarRadiationPressure<stkobjects/VehicleLOPSolarRadiationPressure>
     VehicleMassProperties<stkobjects/VehicleMassProperties>
     VehiclePhysicalData<stkobjects/VehiclePhysicalData>
     VehiclePluginPropagator<stkobjects/VehiclePluginPropagator>
     VehiclePluginSettings<stkobjects/VehiclePluginSettings>
     VehiclePositionVelocityCollection<stkobjects/VehiclePositionVelocityCollection>
     VehiclePositionVelocityElement<stkobjects/VehiclePositionVelocityElement>
     VehicleSpatialInformation<stkobjects/VehicleSpatialInformation>
     VehicleTargetPointingCollection<stkobjects/VehicleTargetPointingCollection>
     VehicleTargetPointingElement<stkobjects/VehicleTargetPointingElement>
     VehicleTargetPointingIntervalCollection<stkobjects/VehicleTargetPointingIntervalCollection>
     VehicleTargetTimes<stkobjects/VehicleTargetTimes>
     VehicleVector<stkobjects/VehicleVector>
     VehicleWaypointAltitudeReference<stkobjects/VehicleWaypointAltitudeReference>
     VehicleWaypointAltitudeReferenceTerrain<stkobjects/VehicleWaypointAltitudeReferenceTerrain>
     VehicleWaypointsCollection<stkobjects/VehicleWaypointsCollection>
     VehicleWaypointsElement<stkobjects/VehicleWaypointsElement>
     VehicleZonalPropagatorInitialState<stkobjects/VehicleZonalPropagatorInitialState>
     Volumetric<stkobjects/Volumetric>
     VolumetricAdvancedSettings<stkobjects/VolumetricAdvancedSettings>
     VolumetricAnalysisInterval<stkobjects/VolumetricAnalysisInterval>
     VolumetricExportTool<stkobjects/VolumetricExportTool>
     VolumetricExternalFile<stkobjects/VolumetricExternalFile>
     VolumetricGraphics3D<stkobjects/VolumetricGraphics3D>
     VolumetricGraphics3DActiveGridPoints<stkobjects/VolumetricGraphics3DActiveGridPoints>
     VolumetricGraphics3DCrossSection<stkobjects/VolumetricGraphics3DCrossSection>
     VolumetricGraphics3DCrossSectionPlane<stkobjects/VolumetricGraphics3DCrossSectionPlane>
     VolumetricGraphics3DCrossSectionPlaneCollection<stkobjects/VolumetricGraphics3DCrossSectionPlaneCollection>
     VolumetricGraphics3DGrid<stkobjects/VolumetricGraphics3DGrid>
     VolumetricGraphics3DLegend<stkobjects/VolumetricGraphics3DLegend>
     VolumetricGraphics3DSpatialCalculationLevel<stkobjects/VolumetricGraphics3DSpatialCalculationLevel>
     VolumetricGraphics3DSpatialCalculationLevelCollection<stkobjects/VolumetricGraphics3DSpatialCalculationLevelCollection>
     VolumetricGraphics3DSpatialCalculationLevels<stkobjects/VolumetricGraphics3DSpatialCalculationLevels>
     VolumetricGraphics3DVolume<stkobjects/VolumetricGraphics3DVolume>
     VolumetricGridSpatialCalculation<stkobjects/VolumetricGridSpatialCalculation>
     Waveform<stkobjects/Waveform>
     WaveformPulseDefinition<stkobjects/WaveformPulseDefinition>
     WaveformRectangular<stkobjects/WaveformRectangular>
     WaveformSelectionStrategy<stkobjects/WaveformSelectionStrategy>
     WaveformSelectionStrategyFixed<stkobjects/WaveformSelectionStrategyFixed>
     WaveformSelectionStrategyRangeLimits<stkobjects/WaveformSelectionStrategyRangeLimits>
     WirelessInSite64GeometryData<stkobjects/WirelessInSite64GeometryData>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ AberrationType<stkobjects/AberrationType>
    ≔ AccessConstraintType<stkobjects/AccessConstraintType>
    ≔ AccessTimeType<stkobjects/AccessTimeType>
    ≔ AdvCATConjunctionType<stkobjects/AdvCATConjunctionType>
    ≔ AdvCATEllipsoidClassType<stkobjects/AdvCATEllipsoidClassType>
    ≔ AdvCATSecondaryEllipsoidsVisibilityType<stkobjects/AdvCATSecondaryEllipsoidsVisibilityType>
    ≔ AircraftWGS84WarningType<stkobjects/AircraftWGS84WarningType>
    ≔ AltitudeReferenceType<stkobjects/AltitudeReferenceType>
    ≔ AnalysisWorkbenchAccessConstraintType<stkobjects/AnalysisWorkbenchAccessConstraintType>
    ≔ AnimationActionType<stkobjects/AnimationActionType>
    ≔ AnimationDirectionType<stkobjects/AnimationDirectionType>
    ≔ AnimationEndTimeMode<stkobjects/AnimationEndTimeMode>
    ≔ AnimationOptionType<stkobjects/AnimationOptionType>
    ≔ AntennaContourType<stkobjects/AntennaContourType>
    ≔ AntennaControlReferenceType<stkobjects/AntennaControlReferenceType>
    ≔ AntennaGraphicsCoordinateSystem<stkobjects/AntennaGraphicsCoordinateSystem>
    ≔ AntennaHFSSDesignHelixTurnDirection<stkobjects/AntennaHFSSDesignHelixTurnDirection>
    ≔ AntennaHFSSDesignStatus<stkobjects/AntennaHFSSDesignStatus>
    ≔ AntennaHFSSDesignType<stkobjects/AntennaHFSSDesignType>
    ≔ AntennaModelCosecantSquaredSidelobeType<stkobjects/AntennaModelCosecantSquaredSidelobeType>
    ≔ AntennaModelInputType<stkobjects/AntennaModelInputType>
    ≔ AntennaModelType<stkobjects/AntennaModelType>
    ≔ AreaType<stkobjects/AreaType>
    ≔ AtmosphericAbsorptionModelType<stkobjects/AtmosphericAbsorptionModelType>
    ≔ AtmosphericDensityModel<stkobjects/AtmosphericDensityModel>
    ≔ AtmosphericTurbulenceModelType<stkobjects/AtmosphericTurbulenceModelType>
    ≔ AttitudeCoordinateAxes<stkobjects/AttitudeCoordinateAxes>
    ≔ AttitudeInclude<stkobjects/AttitudeInclude>
    ≔ AttitudeProfile<stkobjects/AttitudeProfile>
    ≔ AttitudeStandardType<stkobjects/AttitudeStandardType>
    ≔ AxisOffset<stkobjects/AxisOffset>
    ≔ AzElMaskType<stkobjects/AzElMaskType>
    ≔ BeamformerType<stkobjects/BeamformerType>
    ≔ BeamSelectionStrategyType<stkobjects/BeamSelectionStrategyType>
    ≔ BorderWallUpperLowerEdgeAltitudeReference<stkobjects/BorderWallUpperLowerEdgeAltitudeReference>
    ≔ BoresightType<stkobjects/BoresightType>
    ≔ BuildHeightReferenceMethod<stkobjects/BuildHeightReferenceMethod>
    ≔ BuildingHeightUnit<stkobjects/BuildingHeightUnit>
    ≔ CCSDSDateFormat<stkobjects/CCSDSDateFormat>
    ≔ CCSDSEphemerisFormatType<stkobjects/CCSDSEphemerisFormatType>
    ≔ CCSDSReferenceFrame<stkobjects/CCSDSReferenceFrame>
    ≔ CCSDSTimeSystem<stkobjects/CCSDSTimeSystem>
    ≔ ChainConstellationConstraintsMode<stkobjects/ChainConstellationConstraintsMode>
    ≔ ChainCoverageAssetMode<stkobjects/ChainCoverageAssetMode>
    ≔ ChainGraphics2DNetworkDataMode<stkobjects/ChainGraphics2DNetworkDataMode>
    ≔ ChainOptimalStrandCalculationScalarMetricType<stkobjects/ChainOptimalStrandCalculationScalarMetricType>
    ≔ ChainOptimalStrandCompareStrandsType<stkobjects/ChainOptimalStrandCompareStrandsType>
    ≔ ChainOptimalStrandLinkCompareType<stkobjects/ChainOptimalStrandLinkCompareType>
    ≔ ChainOptimalStrandMetricType<stkobjects/ChainOptimalStrandMetricType>
    ≔ ChainParentPlatformRestriction<stkobjects/ChainParentPlatformRestriction>
    ≔ ChainStrandAnalysisComputeType<stkobjects/ChainStrandAnalysisComputeType>
    ≔ ChainTimePeriodType<stkobjects/ChainTimePeriodType>
    ≔ CircularApertureInputType<stkobjects/CircularApertureInputType>
    ≔ ClassicalLocation<stkobjects/ClassicalLocation>
    ≔ ClassicalSizeShape<stkobjects/ClassicalSizeShape>
    ≔ CloudsAndFogFadingLossModelType<stkobjects/CloudsAndFogFadingLossModelType>
    ≔ CloudsAndFogLiquidWaterChoiceType<stkobjects/CloudsAndFogLiquidWaterChoiceType>
    ≔ CommSystemAccessEventDetectionType<stkobjects/CommSystemAccessEventDetectionType>
    ≔ CommSystemAccessSamplingMethodType<stkobjects/CommSystemAccessSamplingMethodType>
    ≔ CommSystemConstrainingRole<stkobjects/CommSystemConstrainingRole>
    ≔ CommSystemLinkSelectionCriteriaType<stkobjects/CommSystemLinkSelectionCriteriaType>
    ≔ CommSystemReferenceBandwidth<stkobjects/CommSystemReferenceBandwidth>
    ≔ CommSystemSaveMode<stkobjects/CommSystemSaveMode>
    ≔ Component<stkobjects/Component>
    ≔ ComponentLinkEmbedControlReferenceType<stkobjects/ComponentLinkEmbedControlReferenceType>
    ≔ ConnectAuthenticationMode<stkobjects/ConnectAuthenticationMode>
    ≔ Constants<stkobjects/Constants>
    ≔ ConstellationConstraintRestrictionType<stkobjects/ConstellationConstraintRestrictionType>
    ≔ ConstellationFromToParentConstraint<stkobjects/ConstellationFromToParentConstraint>
    ≔ ConstraintBackground<stkobjects/ConstraintBackground>
    ≔ ConstraintGroundTrack<stkobjects/ConstraintGroundTrack>
    ≔ ConstraintLighting<stkobjects/ConstraintLighting>
    ≔ Coverage3dDrawAtAltitudeMode<stkobjects/Coverage3dDrawAtAltitudeMode>
    ≔ CoverageAltitudeMethod<stkobjects/CoverageAltitudeMethod>
    ≔ CoverageAssetGrouping<stkobjects/CoverageAssetGrouping>
    ≔ CoverageAssetStatus<stkobjects/CoverageAssetStatus>
    ≔ CoverageBounds<stkobjects/CoverageBounds>
    ≔ CoverageCustomRegionAlgorithm<stkobjects/CoverageCustomRegionAlgorithm>
    ≔ CoverageDataRetention<stkobjects/CoverageDataRetention>
    ≔ CoverageGridClass<stkobjects/CoverageGridClass>
    ≔ CoverageGroundAltitudeMethod<stkobjects/CoverageGroundAltitudeMethod>
    ≔ CoveragePointAltitudeMethod<stkobjects/CoveragePointAltitudeMethod>
    ≔ CoveragePointLocationMethod<stkobjects/CoveragePointLocationMethod>
    ≔ CoverageRegionAccessAccelerationType<stkobjects/CoverageRegionAccessAccelerationType>
    ≔ CoverageResolution<stkobjects/CoverageResolution>
    ≔ CoverageSatisfactionType<stkobjects/CoverageSatisfactionType>
    ≔ DataProviderElementType<stkobjects/DataProviderElementType>
    ≔ DataProviderResultCategory<stkobjects/DataProviderResultCategory>
    ≔ DataProviderType<stkobjects/DataProviderType>
    ≔ DataSaveMode<stkobjects/DataSaveMode>
    ≔ DelaunayGType<stkobjects/DelaunayGType>
    ≔ DelaunayHType<stkobjects/DelaunayHType>
    ≔ DelaunayLType<stkobjects/DelaunayLType>
    ≔ DemodulatorModelType<stkobjects/DemodulatorModelType>
    ≔ DeticPositionType<stkobjects/DeticPositionType>
    ≔ DirectionProviderType<stkobjects/DirectionProviderType>
    ≔ DisplayTimesType<stkobjects/DisplayTimesType>
    ≔ DistanceOnSphere<stkobjects/DistanceOnSphere>
    ≔ DragModel<stkobjects/DragModel>
    ≔ ElementConfigurationType<stkobjects/ElementConfigurationType>
    ≔ EOIRFlightType<stkobjects/EOIRFlightType>
    ≔ EOIRShapeMaterialSpecificationType<stkobjects/EOIRShapeMaterialSpecificationType>
    ≔ EOIRShapeType<stkobjects/EOIRShapeType>
    ≔ EOIRThermalModelType<stkobjects/EOIRThermalModelType>
    ≔ EphemerisCoordinateSystemType<stkobjects/EphemerisCoordinateSystemType>
    ≔ EphemerisCovarianceType<stkobjects/EphemerisCovarianceType>
    ≔ EphemExportToolFileFormat<stkobjects/EphemExportToolFileFormat>
    ≔ EphemSourceType<stkobjects/EphemSourceType>
    ≔ EquinoctialFormulation<stkobjects/EquinoctialFormulation>
    ≔ EquinoctialSizeShape<stkobjects/EquinoctialSizeShape>
    ≔ ErrorCode<stkobjects/ErrorCode>
    ≔ EventDetection<stkobjects/EventDetection>
    ≔ ExportToolStepSizeType<stkobjects/ExportToolStepSizeType>
    ≔ ExportToolTimePeriodType<stkobjects/ExportToolTimePeriodType>
    ≔ ExportToolVersionFormat<stkobjects/ExportToolVersionFormat>
    ≔ ExternalEphemerisFormatType<stkobjects/ExternalEphemerisFormatType>
    ≔ ExternalFileMessageLevelType<stkobjects/ExternalFileMessageLevelType>
    ≔ FigureOfMeritAcrossAssets<stkobjects/FigureOfMeritAcrossAssets>
    ≔ FigureOfMeritCompute<stkobjects/FigureOfMeritCompute>
    ≔ FigureOfMeritConstraintName<stkobjects/FigureOfMeritConstraintName>
    ≔ FigureOfMeritDefinitionType<stkobjects/FigureOfMeritDefinitionType>
    ≔ FigureOfMeritEndGapOption<stkobjects/FigureOfMeritEndGapOption>
    ≔ FigureOfMeritGraphics2DAccumulation<stkobjects/FigureOfMeritGraphics2DAccumulation>
    ≔ FigureOfMeritGraphics2DColorMethod<stkobjects/FigureOfMeritGraphics2DColorMethod>
    ≔ FigureOfMeritGraphics2DContourType<stkobjects/FigureOfMeritGraphics2DContourType>
    ≔ FigureOfMeritGraphics2DDirection<stkobjects/FigureOfMeritGraphics2DDirection>
    ≔ FigureOfMeritGraphics2DFloatingPointFormat<stkobjects/FigureOfMeritGraphics2DFloatingPointFormat>
    ≔ FigureOfMeritInvalidValueActionType<stkobjects/FigureOfMeritInvalidValueActionType>
    ≔ FigureOfMeritMethod<stkobjects/FigureOfMeritMethod>
    ≔ FigureOfMeritNavigationAccuracyMethod<stkobjects/FigureOfMeritNavigationAccuracyMethod>
    ≔ FigureOfMeritNavigationComputeType<stkobjects/FigureOfMeritNavigationComputeType>
    ≔ FigureOfMeritSatisfactionType<stkobjects/FigureOfMeritSatisfactionType>
    ≔ FrequencySpecificationType<stkobjects/FrequencySpecificationType>
    ≔ GeodeticSize<stkobjects/GeodeticSize>
    ≔ GeometricElementType<stkobjects/GeometricElementType>
    ≔ GPSAttitudeModelType<stkobjects/GPSAttitudeModelType>
    ≔ GPSReferenceWeek<stkobjects/GPSReferenceWeek>
    ≔ Graphics3DACAPCoefficientDataType<stkobjects/Graphics3DACAPCoefficientDataType>
    ≔ Graphics3DACAPSolarActivityConfigurationType<stkobjects/Graphics3DACAPSolarActivityConfigurationType>
    ≔ Graphics3DFontSize<stkobjects/Graphics3DFontSize>
    ≔ Graphics3DFormat<stkobjects/Graphics3DFormat>
    ≔ Graphics3DLabelSwapDistanceType<stkobjects/Graphics3DLabelSwapDistanceType>
    ≔ Graphics3DLocation<stkobjects/Graphics3DLocation>
    ≔ Graphics3DMarkerOrientation<stkobjects/Graphics3DMarkerOrientation>
    ≔ Graphics3DMarkerOriginType<stkobjects/Graphics3DMarkerOriginType>
    ≔ Graphics3DXOrigin<stkobjects/Graphics3DXOrigin>
    ≔ Graphics3DYOrigin<stkobjects/Graphics3DYOrigin>
    ≔ HelpContextIdentifierType<stkobjects/HelpContextIdentifierType>
    ≔ HFSSFarFieldDataGainType<stkobjects/HFSSFarFieldDataGainType>
    ≔ IntersectionType<stkobjects/IntersectionType>
    ≔ IonosphericFadingLossModelType<stkobjects/IonosphericFadingLossModelType>
    ≔ ITURP676AtmosphereDataType<stkobjects/ITURP676AtmosphereDataType>
    ≔ IvClockHost<stkobjects/IvClockHost>
    ≔ IvColorMode<stkobjects/IvColorMode>
    ≔ IvTimeSense<stkobjects/IvTimeSense>
    ≔ LaserPropagationLossModelType<stkobjects/LaserPropagationLossModelType>
    ≔ LaserTroposphericScintillationLossModelType<stkobjects/LaserTroposphericScintillationLossModelType>
    ≔ LatticeType<stkobjects/LatticeType>
    ≔ LeadTrailData<stkobjects/LeadTrailData>
    ≔ LightingObstructionModelType<stkobjects/LightingObstructionModelType>
    ≔ LimitsExceededBehaviorType<stkobjects/LimitsExceededBehaviorType>
    ≔ LineWidth<stkobjects/LineWidth>
    ≔ LinkMarginType<stkobjects/LinkMarginType>
    ≔ LoadMethod<stkobjects/LoadMethod>
    ≔ LookAheadPropagator<stkobjects/LookAheadPropagator>
    ≔ LOPAtmosphericDensityModel<stkobjects/LOPAtmosphericDensityModel>
    ≔ LowAltitudeAtmosphericDensityModel<stkobjects/LowAltitudeAtmosphericDensityModel>
    ≔ MarkerShape3d<stkobjects/MarkerShape3d>
    ≔ MarkerType<stkobjects/MarkerType>
    ≔ MethodToComputeSunPosition<stkobjects/MethodToComputeSunPosition>
    ≔ MixedSphericalFlightPathAngleType<stkobjects/MixedSphericalFlightPathAngleType>
    ≔ ModelGltfReflectionMapType<stkobjects/ModelGltfReflectionMapType>
    ≔ ModelType<stkobjects/ModelType>
    ≔ ModtranAerosolModelType<stkobjects/ModtranAerosolModelType>
    ≔ ModtranCloudModelType<stkobjects/ModtranCloudModelType>
    ≔ ModulatorModelType<stkobjects/ModulatorModelType>
    ≔ MTOEntirety<stkobjects/MTOEntirety>
    ≔ MTOInputDataType<stkobjects/MTOInputDataType>
    ≔ MTOObjectInterval<stkobjects/MTOObjectInterval>
    ≔ MTORangeMode<stkobjects/MTORangeMode>
    ≔ MTOTrackEvaluationType<stkobjects/MTOTrackEvaluationType>
    ≔ MTOVisibilityMode<stkobjects/MTOVisibilityMode>
    ≔ NoiseTemperatureComputeType<stkobjects/NoiseTemperatureComputeType>
    ≔ NoiseTemperatureMethod<stkobjects/NoiseTemperatureMethod>
    ≔ NoteShowType<stkobjects/NoteShowType>
    ≔ NotificationFilterMask<stkobjects/NotificationFilterMask>
    ≔ OffsetFrameType<stkobjects/OffsetFrameType>
    ≔ OnePointAccessStatus<stkobjects/OnePointAccessStatus>
    ≔ OnePointAccessSummary<stkobjects/OnePointAccessSummary>
    ≔ OrientationAscNode<stkobjects/OrientationAscNode>
    ≔ PlanetOrbitDisplayType<stkobjects/PlanetOrbitDisplayType>
    ≔ PlanetPositionSourceType<stkobjects/PlanetPositionSourceType>
    ≔ PointingStrategyType<stkobjects/PointingStrategyType>
    ≔ PolarizationReferenceAxis<stkobjects/PolarizationReferenceAxis>
    ≔ PolarizationType<stkobjects/PolarizationType>
    ≔ PRFMode<stkobjects/PRFMode>
    ≔ ProjectionHorizontalDatumType<stkobjects/ProjectionHorizontalDatumType>
    ≔ PropagatorDisplayCoordinateType<stkobjects/PropagatorDisplayCoordinateType>
    ≔ PropagatorSGP4SwitchMethod<stkobjects/PropagatorSGP4SwitchMethod>
    ≔ PropagatorType<stkobjects/PropagatorType>
    ≔ PulseWidthMode<stkobjects/PulseWidthMode>
    ≔ RadarActivityType<stkobjects/RadarActivityType>
    ≔ RadarContinuousWaveAnalysisMode<stkobjects/RadarContinuousWaveAnalysisMode>
    ≔ RadarCrossSectionContourGraphicsPolarization<stkobjects/RadarCrossSectionContourGraphicsPolarization>
    ≔ RadarFrequencySpecificationType<stkobjects/RadarFrequencySpecificationType>
    ≔ RadarMode<stkobjects/RadarMode>
    ≔ RadarModelType<stkobjects/RadarModelType>
    ≔ RadarProbabilityOfDetectionType<stkobjects/RadarProbabilityOfDetectionType>
    ≔ RadarPulseIntegrationType<stkobjects/RadarPulseIntegrationType>
    ≔ RadarPulseIntegratorType<stkobjects/RadarPulseIntegratorType>
    ≔ RadarSarPcrMode<stkobjects/RadarSarPcrMode>
    ≔ RadarSarPRFMode<stkobjects/RadarSarPRFMode>
    ≔ RadarSARPulseIntegrationAnalysisMode<stkobjects/RadarSARPulseIntegrationAnalysisMode>
    ≔ RadarSarRangeResolutionMode<stkobjects/RadarSarRangeResolutionMode>
    ≔ RadarSearchTrackPRFMode<stkobjects/RadarSearchTrackPRFMode>
    ≔ RadarSearchTrackPulseWidthMode<stkobjects/RadarSearchTrackPulseWidthMode>
    ≔ RadarSNRContourType<stkobjects/RadarSNRContourType>
    ≔ RadarSTCAttenuationType<stkobjects/RadarSTCAttenuationType>
    ≔ RadarSwerlingCase<stkobjects/RadarSwerlingCase>
    ≔ RadarWaveformSearchTrackType<stkobjects/RadarWaveformSearchTrackType>
    ≔ RainLossModelType<stkobjects/RainLossModelType>
    ≔ RCSComputeStrategy<stkobjects/RCSComputeStrategy>
    ≔ ReceiverModelType<stkobjects/ReceiverModelType>
    ≔ RectangularApertureInputType<stkobjects/RectangularApertureInputType>
    ≔ ReTransmitterOpMode<stkobjects/ReTransmitterOpMode>
    ≔ RFFilterModelType<stkobjects/RFFilterModelType>
    ≔ RouteGraphics3DMarkerType<stkobjects/RouteGraphics3DMarkerType>
    ≔ SamplingMethod<stkobjects/SamplingMethod>
    ≔ ScatteringPointModelType<stkobjects/ScatteringPointModelType>
    ≔ ScatteringPointProviderListType<stkobjects/ScatteringPointProviderListType>
    ≔ ScatteringPointProviderType<stkobjects/ScatteringPointProviderType>
    ≔ Scenario3dPointSize<stkobjects/Scenario3dPointSize>
    ≔ ScenarioEndLoopType<stkobjects/ScenarioEndLoopType>
    ≔ ScenarioRefreshDeltaType<stkobjects/ScenarioRefreshDeltaType>
    ≔ ScenarioTimeStepType<stkobjects/ScenarioTimeStepType>
    ≔ SensorAltitudeCrossingDirection<stkobjects/SensorAltitudeCrossingDirection>
    ≔ SensorAltitudeCrossingSideType<stkobjects/SensorAltitudeCrossingSideType>
    ≔ SensorAzElBoresightAxisType<stkobjects/SensorAzElBoresightAxisType>
    ≔ SensorEOIRBandImageQuality<stkobjects/SensorEOIRBandImageQuality>
    ≔ SensorEOIRBandOpticalInputMode<stkobjects/SensorEOIRBandOpticalInputMode>
    ≔ SensorEOIRBandOpticalTransmissionMode<stkobjects/SensorEOIRBandOpticalTransmissionMode>
    ≔ SensorEOIRBandQuantizationMode<stkobjects/SensorEOIRBandQuantizationMode>
    ≔ SensorEOIRBandQuantumEfficiencyMode<stkobjects/SensorEOIRBandQuantumEfficiencyMode>
    ≔ SensorEOIRBandRadiometricParameterLevelType<stkobjects/SensorEOIRBandRadiometricParameterLevelType>
    ≔ SensorEOIRBandSaturationMode<stkobjects/SensorEOIRBandSaturationMode>
    ≔ SensorEOIRBandSpatialInputMode<stkobjects/SensorEOIRBandSpatialInputMode>
    ≔ SensorEOIRBandSpectralRelativeSystemResponseUnitsType<stkobjects/SensorEOIRBandSpectralRelativeSystemResponseUnitsType>
    ≔ SensorEOIRBandSpectralShape<stkobjects/SensorEOIRBandSpectralShape>
    ≔ SensorEOIRBandWavelengthType<stkobjects/SensorEOIRBandWavelengthType>
    ≔ SensorEOIRJitterType<stkobjects/SensorEOIRJitterType>
    ≔ SensorEOIRProcessingLevelType<stkobjects/SensorEOIRProcessingLevelType>
    ≔ SensorEOIRScanMode<stkobjects/SensorEOIRScanMode>
    ≔ SensorGraphics3DInheritFrom2D<stkobjects/SensorGraphics3DInheritFrom2D>
    ≔ SensorGraphics3DProjectionTimeDependencyType<stkobjects/SensorGraphics3DProjectionTimeDependencyType>
    ≔ SensorGraphics3DProjectionType<stkobjects/SensorGraphics3DProjectionType>
    ≔ SensorGraphics3DPulseFrequencyPreset<stkobjects/SensorGraphics3DPulseFrequencyPreset>
    ≔ SensorGraphics3DPulseStyle<stkobjects/SensorGraphics3DPulseStyle>
    ≔ SensorGraphics3DVisualAppearance<stkobjects/SensorGraphics3DVisualAppearance>
    ≔ SensorLocation<stkobjects/SensorLocation>
    ≔ SensorPattern<stkobjects/SensorPattern>
    ≔ SensorPointing<stkobjects/SensorPointing>
    ≔ SensorPointingTargetedBoresightType<stkobjects/SensorPointingTargetedBoresightType>
    ≔ SensorProjectionDistanceType<stkobjects/SensorProjectionDistanceType>
    ≔ SensorRefractionType<stkobjects/SensorRefractionType>
    ≔ SensorScanMode<stkobjects/SensorScanMode>
    ≔ SolarRadiationPressureModelType<stkobjects/SolarRadiationPressureModelType>
    ≔ SolarRadiationPressureShadowModelType<stkobjects/SolarRadiationPressureShadowModelType>
    ≔ SolidTide<stkobjects/SolidTide>
    ≔ SpaceEnvironmentCrresProtonActivity<stkobjects/SpaceEnvironmentCrresProtonActivity>
    ≔ SpaceEnvironmentCrresRadiationActivity<stkobjects/SpaceEnvironmentCrresRadiationActivity>
    ≔ SpaceEnvironmentMagneticExternalField<stkobjects/SpaceEnvironmentMagneticExternalField>
    ≔ SpaceEnvironmentMagneticFieldColorMode<stkobjects/SpaceEnvironmentMagneticFieldColorMode>
    ≔ SpaceEnvironmentMagneticFieldColorScaleType<stkobjects/SpaceEnvironmentMagneticFieldColorScaleType>
    ≔ SpaceEnvironmentMagneticMainField<stkobjects/SpaceEnvironmentMagneticMainField>
    ≔ SpaceEnvironmentNasaModelsActivity<stkobjects/SpaceEnvironmentNasaModelsActivity>
    ≔ SpaceEnvironmentSAAChannel<stkobjects/SpaceEnvironmentSAAChannel>
    ≔ SpaceEnvironmentSAAFluxLevel<stkobjects/SpaceEnvironmentSAAFluxLevel>
    ≔ SpacingUnit<stkobjects/SpacingUnit>
    ≔ SphericalFlightPathAzimuthType<stkobjects/SphericalFlightPathAzimuthType>
    ≔ SpiceInterpolation<stkobjects/SpiceInterpolation>
    ≔ StarReferenceFrame<stkobjects/StarReferenceFrame>
    ≔ StatisticType<stkobjects/StatisticType>
    ≔ STKObjectType<stkobjects/STKObjectType>
    ≔ SurfaceLinesTerrain<stkobjects/SurfaceLinesTerrain>
    ≔ SurfaceReference<stkobjects/SurfaceReference>
    ≔ SwathComputationalMethod<stkobjects/SwathComputationalMethod>
    ≔ TargetSelectionMethod<stkobjects/TargetSelectionMethod>
    ≔ TerrainFileType<stkobjects/TerrainFileType>
    ≔ TerrainNormalType<stkobjects/TerrainNormalType>
    ≔ TextOutlineStyle<stkobjects/TextOutlineStyle>
    ≔ ThirdBodyGravitySourceType<stkobjects/ThirdBodyGravitySourceType>
    ≔ TickData<stkobjects/TickData>
    ≔ Tileset3DSourceType<stkobjects/Tileset3DSourceType>
    ≔ TimePeriodValueType<stkobjects/TimePeriodValueType>
    ≔ TimeVaryingExtremum<stkobjects/TimeVaryingExtremum>
    ≔ TIREMPolarizationType<stkobjects/TIREMPolarizationType>
    ≔ TrackMode<stkobjects/TrackMode>
    ≔ TrajectoryType<stkobjects/TrajectoryType>
    ≔ TransferFunctionType<stkobjects/TransferFunctionType>
    ≔ TransmitterModelType<stkobjects/TransmitterModelType>
    ≔ TroposphericScintillationAverageTimeChoiceType<stkobjects/TroposphericScintillationAverageTimeChoiceType>
    ≔ TroposphericScintillationFadingLossModelType<stkobjects/TroposphericScintillationFadingLossModelType>
    ≔ UrbanTerrestrialLossModelType<stkobjects/UrbanTerrestrialLossModelType>
    ≔ VectorAxesConnectType<stkobjects/VectorAxesConnectType>
    ≔ VehicleAltitudeReference<stkobjects/VehicleAltitudeReference>
    ≔ VehicleAttitude<stkobjects/VehicleAttitude>
    ≔ VehicleBreakAngleType<stkobjects/VehicleBreakAngleType>
    ≔ VehicleConsiderAnalysisType<stkobjects/VehicleConsiderAnalysisType>
    ≔ VehicleCoordinateSystem<stkobjects/VehicleCoordinateSystem>
    ≔ VehicleCorrelationListType<stkobjects/VehicleCorrelationListType>
    ≔ VehicleDirection<stkobjects/VehicleDirection>
    ≔ VehicleEllipseOptionType<stkobjects/VehicleEllipseOptionType>
    ≔ VehicleFrame<stkobjects/VehicleFrame>
    ≔ VehicleGeomagneticFluxSourceType<stkobjects/VehicleGeomagneticFluxSourceType>
    ≔ VehicleGeomagneticFluxUpdateRateType<stkobjects/VehicleGeomagneticFluxUpdateRateType>
    ≔ VehicleGPSAlmanacType<stkobjects/VehicleGPSAlmanacType>
    ≔ VehicleGPSAutomaticUpdateSourceType<stkobjects/VehicleGPSAutomaticUpdateSourceType>
    ≔ VehicleGPSElementSelectionType<stkobjects/VehicleGPSElementSelectionType>
    ≔ VehicleGPSSwitchMethod<stkobjects/VehicleGPSSwitchMethod>
    ≔ VehicleGraphics2DAttributeType<stkobjects/VehicleGraphics2DAttributeType>
    ≔ VehicleGraphics2DElevation<stkobjects/VehicleGraphics2DElevation>
    ≔ VehicleGraphics2DOffset<stkobjects/VehicleGraphics2DOffset>
    ≔ VehicleGraphics2DOptionType<stkobjects/VehicleGraphics2DOptionType>
    ≔ VehicleGraphics2DPass<stkobjects/VehicleGraphics2DPass>
    ≔ VehicleGraphics2DTimeEventType<stkobjects/VehicleGraphics2DTimeEventType>
    ≔ VehicleGraphics2DVisibleSideType<stkobjects/VehicleGraphics2DVisibleSideType>
    ≔ VehicleGraphics3DAttributeType<stkobjects/VehicleGraphics3DAttributeType>
    ≔ VehicleGraphics3DBPlaneTargetPointPosition<stkobjects/VehicleGraphics3DBPlaneTargetPointPosition>
    ≔ VehicleGraphics3DDropLineType<stkobjects/VehicleGraphics3DDropLineType>
    ≔ VehicleGraphics3DSigmaScale<stkobjects/VehicleGraphics3DSigmaScale>
    ≔ VehicleImpact<stkobjects/VehicleImpact>
    ≔ VehicleImpactLocation<stkobjects/VehicleImpactLocation>
    ≔ VehicleIntegrationModel<stkobjects/VehicleIntegrationModel>
    ≔ VehicleInterpolationMethod<stkobjects/VehicleInterpolationMethod>
    ≔ VehicleLaunch<stkobjects/VehicleLaunch>
    ≔ VehicleLaunchControl<stkobjects/VehicleLaunchControl>
    ≔ VehicleLookAheadMethod<stkobjects/VehicleLookAheadMethod>
    ≔ VehicleMethod<stkobjects/VehicleMethod>
    ≔ VehiclePartialPassMeasurement<stkobjects/VehiclePartialPassMeasurement>
    ≔ VehiclePassNumbering<stkobjects/VehiclePassNumbering>
    ≔ VehiclePredictorCorrectorScheme<stkobjects/VehiclePredictorCorrectorScheme>
    ≔ VehiclePropagationFrame<stkobjects/VehiclePropagationFrame>
    ≔ VehicleSGP4AutomaticUpdateSourceType<stkobjects/VehicleSGP4AutomaticUpdateSourceType>
    ≔ VehicleSGP4TLESelectionType<stkobjects/VehicleSGP4TLESelectionType>
    ≔ VehicleSlewMode<stkobjects/VehicleSlewMode>
    ≔ VehicleSlewTimingBetweenTargetType<stkobjects/VehicleSlewTimingBetweenTargetType>
    ≔ VehicleSolarFluxGeomagneticType<stkobjects/VehicleSolarFluxGeomagneticType>
    ≔ VehicleSpaceEnvironmentApSource<stkobjects/VehicleSpaceEnvironmentApSource>
    ≔ VehicleSpaceEnvironmentComputationMode<stkobjects/VehicleSpaceEnvironmentComputationMode>
    ≔ VehicleSpaceEnvironmentDetectorGeometry<stkobjects/VehicleSpaceEnvironmentDetectorGeometry>
    ≔ VehicleSpaceEnvironmentDetectorType<stkobjects/VehicleSpaceEnvironmentDetectorType>
    ≔ VehicleSpaceEnvironmentDoseChannel<stkobjects/VehicleSpaceEnvironmentDoseChannel>
    ≔ VehicleSpaceEnvironmentF10P7SourceType<stkobjects/VehicleSpaceEnvironmentF10P7SourceType>
    ≔ VehicleSpaceEnvironmentMaterial<stkobjects/VehicleSpaceEnvironmentMaterial>
    ≔ VehicleSpaceEnvironmentShapeModel<stkobjects/VehicleSpaceEnvironmentShapeModel>
    ≔ VehicleWaypointComputationMethod<stkobjects/VehicleWaypointComputationMethod>
    ≔ VehicleWaypointInterpolationMethod<stkobjects/VehicleWaypointInterpolationMethod>
    ≔ VolumetricDataExportFormatType<stkobjects/VolumetricDataExportFormatType>
    ≔ VolumetricDefinitionType<stkobjects/VolumetricDefinitionType>
    ≔ VolumetricDisplayQualityType<stkobjects/VolumetricDisplayQualityType>
    ≔ VolumetricDisplayVolumeType<stkobjects/VolumetricDisplayVolumeType>
    ≔ VolumetricLegendNumericNotationType<stkobjects/VolumetricLegendNumericNotationType>
    ≔ VolumetricLevelOrder<stkobjects/VolumetricLevelOrder>
    ≔ VolumetricSaveComputedDataType<stkobjects/VolumetricSaveComputedDataType>
    ≔ VolumetricSpatialCalculationEvaluationType<stkobjects/VolumetricSpatialCalculationEvaluationType>
    ≔ VolumetricVolumeGridExportType<stkobjects/VolumetricVolumeGridExportType>
    ≔ WaveformSelectionStrategyType<stkobjects/WaveformSelectionStrategyType>
    ≔ WaveformType<stkobjects/WaveformType>

