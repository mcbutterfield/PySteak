Sensor
======

.. py:class:: br.ok.core.stkobjects.Sensor

   Bases: :py:class:`~br.ok.core.stkobjects.ISTKObject`, :py:class:`~br.ok.core.stkobjects.ILifetimeInformation`, :py:class:`~br.ok.core.stkobjects.IDisplayTime`, :py:class:`~br.ok.core.stkobjects.IProvideSpatialInfo`

   Class defining the Sensor class.

.. py:currentmodule:: Sensor

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Sensor.get_stars_in_field_of_view`
              - Return celestial bodies within the sensor's field of view.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.is_refraction_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.reset_az_el_mask`
              - Reset the az-el mask.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.set_az_el_mask`
              - Set the az-el mask type, using the AzElMaskType enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.set_az_el_mask_file`
              - Path and file name of az-el mask file.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.set_location_type`
              - Set the sensor's location type, a member of the SensorLocation enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.set_pattern_type`
              - Set the pattern type.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.set_pointing_external_file`
              - Set the external pointing type.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.set_pointing_type`
              - Set the sensor's pointing type, using the SensorPointing enumeration.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Sensor.access_constraints`
              - Get constraints imposed on the sensor.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.az_el_mask`
              - Get the az-el mask.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.az_el_mask_data`
              - Get az-el mask data for the sensor.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.chain_analysis_options`
              - Get the sensor's chain analysis options.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.common_tasks`
              - Return an interface that exposes common tasks.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.detector_pitch`
              - Detector pitch used in defining senor resolution. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.focal_length`
              - Focal length used in defining sensor resolution. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.graphics`
              - Get the 2D Graphics properties for the sensor.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.graphics_3d`
              - Get the 3D Graphics properties for the sensor.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.location_data`
              - Get location data for the sensor. The sensor's center point is invalid; all other points are valid choices for the location data.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.location_type`
              - The location type being used by the sensor.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.pattern`
              - Get data defining the sensor pattern.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.pattern_type`
              - Criterion for defining the sensor pattern. A member of the SensorPattern enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.pointing`
              - Get pointing data for the sensor.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.pointing_type`
              - The sensor's pointing type. A member of the SensorPointing enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.refraction`
              - Refraction method, a member of the SensorRefractionType enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.refraction_model`
              - Get a refraction model.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.refraction_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.swath`
              - Get the sensor's swath.
            * - :py:attr:`~br.ok.core.stkobjects.Sensor.use_refraction_in_access`
              - Flag controls whether refraction is applied when computing relative position in Access.



Examples
--------

Sensor Body Mask

.. code-block:: python

    # Sensor sensor: Sensor object
    if os.name == "nt":
        installPath = r"C:\Program Files\AGI\STK_ODTK 13"
    else:
        installPath = os.environ["STK_INSTALL_DIR"]
    bmskPath = ["Data", "Resources", "stktraining", "text", "BodyMask_hga.bmsk"]
    sensor.set_az_el_mask_file(os.path.join(installPath, *bmskPath))


Set Sensor Properties

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pattern and set
    sensor.common_tasks.set_pattern_rectangular(20, 25)
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_az_el(90, 60, AzElAboutBoresight.ROTATE)
    # Change location and set
    sensor.set_location_type(SensorLocation.FIXED)
    sensor.location_data.assign_cartesian(-0.0004, -0.0004, 0.004)


Attach a Sensor Object to a Vehicle

.. code-block:: python

    # Satellite satellite: Satellite object
    sensor = satellite.children.new(STKObjectType.SENSOR, "MySensor")


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Sensor


Property detail
---------------

.. py:property:: access_constraints
    :canonical: br.ok.core.stkobjects.Sensor.access_constraints
    :type: AccessConstraintCollection

    Get constraints imposed on the sensor.

.. py:property:: az_el_mask
    :canonical: br.ok.core.stkobjects.Sensor.az_el_mask
    :type: AzElMaskType

    Get the az-el mask.

.. py:property:: az_el_mask_data
    :canonical: br.ok.core.stkobjects.Sensor.az_el_mask_data
    :type: IAzElMaskData

    Get az-el mask data for the sensor.

.. py:property:: chain_analysis_options
    :canonical: br.ok.core.stkobjects.Sensor.chain_analysis_options
    :type: ChainAnalysisOptions

    Get the sensor's chain analysis options.

.. py:property:: common_tasks
    :canonical: br.ok.core.stkobjects.Sensor.common_tasks
    :type: SensorCommonTasks

    Return an interface that exposes common tasks.

.. py:property:: detector_pitch
    :canonical: br.ok.core.stkobjects.Sensor.detector_pitch
    :type: float

    Detector pitch used in defining senor resolution. Uses SmallDistanceUnit Dimension.

.. py:property:: focal_length
    :canonical: br.ok.core.stkobjects.Sensor.focal_length
    :type: float

    Focal length used in defining sensor resolution. Uses SmallDistanceUnit Dimension.

.. py:property:: graphics
    :canonical: br.ok.core.stkobjects.Sensor.graphics
    :type: SensorGraphics

    Get the 2D Graphics properties for the sensor.

.. py:property:: graphics_3d
    :canonical: br.ok.core.stkobjects.Sensor.graphics_3d
    :type: SensorGraphics3D

    Get the 3D Graphics properties for the sensor.

.. py:property:: location_data
    :canonical: br.ok.core.stkobjects.Sensor.location_data
    :type: ILocationData

    Get location data for the sensor. The sensor's center point is invalid; all other points are valid choices for the location data.

.. py:property:: location_type
    :canonical: br.ok.core.stkobjects.Sensor.location_type
    :type: SensorLocation

    The location type being used by the sensor.

.. py:property:: pattern
    :canonical: br.ok.core.stkobjects.Sensor.pattern
    :type: ISensorPattern

    Get data defining the sensor pattern.

.. py:property:: pattern_type
    :canonical: br.ok.core.stkobjects.Sensor.pattern_type
    :type: SensorPattern

    Criterion for defining the sensor pattern. A member of the SensorPattern enumeration.

.. py:property:: pointing
    :canonical: br.ok.core.stkobjects.Sensor.pointing
    :type: ISensorPointing

    Get pointing data for the sensor.

.. py:property:: pointing_type
    :canonical: br.ok.core.stkobjects.Sensor.pointing_type
    :type: SensorPointing

    The sensor's pointing type. A member of the SensorPointing enumeration.

.. py:property:: refraction
    :canonical: br.ok.core.stkobjects.Sensor.refraction
    :type: SensorRefractionType

    Refraction method, a member of the SensorRefractionType enumeration.

.. py:property:: refraction_model
    :canonical: br.ok.core.stkobjects.Sensor.refraction_model
    :type: IRefractionModelBase

    Get a refraction model.

.. py:property:: refraction_supported_types
    :canonical: br.ok.core.stkobjects.Sensor.refraction_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: swath
    :canonical: br.ok.core.stkobjects.Sensor.swath
    :type: Swath

    Get the sensor's swath.

.. py:property:: use_refraction_in_access
    :canonical: br.ok.core.stkobjects.Sensor.use_refraction_in_access
    :type: bool

    Flag controls whether refraction is applied when computing relative position in Access.


Method detail
-------------










.. py:method:: get_stars_in_field_of_view(self, epoch: typing.Any) -> ICelestialBodyInformationCollection
    :canonical: br.ok.core.stkobjects.Sensor.get_stars_in_field_of_view

    Return celestial bodies within the sensor's field of view.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ICelestialBodyInformationCollection`


.. py:method:: is_refraction_type_supported(self, model: SensorRefractionType) -> bool
    :canonical: br.ok.core.stkobjects.Sensor.is_refraction_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **model** : :obj:`~SensorRefractionType`


    :Returns:

        :obj:`~bool`











.. py:method:: reset_az_el_mask(self) -> None
    :canonical: br.ok.core.stkobjects.Sensor.reset_az_el_mask

    Reset the az-el mask.

    :Returns:

        :obj:`~None`

.. py:method:: set_az_el_mask(self, az_el_mask_type: AzElMaskType) -> None
    :canonical: br.ok.core.stkobjects.Sensor.set_az_el_mask

    Set the az-el mask type, using the AzElMaskType enumeration.

    :Parameters:

        **az_el_mask_type** : :obj:`~AzElMaskType`


    :Returns:

        :obj:`~None`

.. py:method:: set_az_el_mask_file(self, filename: str) -> None
    :canonical: br.ok.core.stkobjects.Sensor.set_az_el_mask_file

    Path and file name of az-el mask file.

    :Parameters:

        **filename** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_location_type(self, location_type: SensorLocation) -> None
    :canonical: br.ok.core.stkobjects.Sensor.set_location_type

    Set the sensor's location type, a member of the SensorLocation enumeration.

    :Parameters:

        **location_type** : :obj:`~SensorLocation`


    :Returns:

        :obj:`~None`

.. py:method:: set_pattern_type(self, pattern_type: SensorPattern) -> None
    :canonical: br.ok.core.stkobjects.Sensor.set_pattern_type

    Set the pattern type.

    :Parameters:

        **pattern_type** : :obj:`~SensorPattern`


    :Returns:

        :obj:`~None`

.. py:method:: set_pointing_external_file(self, sensor_pointing_file: str) -> None
    :canonical: br.ok.core.stkobjects.Sensor.set_pointing_external_file

    Set the external pointing type.

    :Parameters:

        **sensor_pointing_file** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_pointing_type(self, pointing_type: SensorPointing) -> None
    :canonical: br.ok.core.stkobjects.Sensor.set_pointing_type

    Set the sensor's pointing type, using the SensorPointing enumeration.

    :Parameters:

        **pointing_type** : :obj:`~SensorPointing`


    :Returns:

        :obj:`~None`





