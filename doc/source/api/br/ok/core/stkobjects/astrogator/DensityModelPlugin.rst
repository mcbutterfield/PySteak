DensityModelPlugin
==================

.. py:class:: br.ok.core.stkobjects.astrogator.DensityModelPlugin

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   Plugin atmospheric density propagator function.

.. py:currentmodule:: DensityModelPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_aug_data_file`
              - Get or set the atmospheric model augmented data file path.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_aug_dtc_file`
              - Get or set the atmospheric model augmented geomagnetic data file path.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_data_filename`
              - Get or set the atmospheric model data file path.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_data_geo_magnetic_flux_source`
              - Whether to use Kp or Ap data from the flux file.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_data_geo_magnetic_flux_update_rate`
              - Get or set the update rate for geomagnetic flux values from the flux file.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_data_source`
              - Get or set the atmospheric model data source - data file or constant values.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.computes_pressure`
              - Flag indicates whether this model computes pressure.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.computes_temperature`
              - Flag indicates whether this model computes temperature.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.drag_model_plugin_name`
              - Get or set the name of the drag model plugin.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.drag_model_type`
              - Drag model type.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.dst_d_tc`
              - Temperature change calculated from disturbance storm time (DstDTc). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.f10`
              - Solar Flux (F10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.f10_avg`
              - Average solar Flux (F10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.kp`
              - Geomagnetic Index (Kp). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.m10`
              - Solar Flux (M10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.m10_avg`
              - Average solar Flux (M10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.n_plate_definition_file`
              - Drag N-Plate definition file.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.plugin_config`
              - Get the properties of the selected plugin.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.plugin_identifier`
              - Get or set the plugin name.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.s10`
              - Solar Flux (S10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.s10_avg`
              - Average solar Flux (S10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.sun_position`
              - Get or set the sun position computation.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.uses_augmented_space_weather`
              - Flag indicates whether this model uses augmented flux data.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.variable_area_history_file`
              - Drag variable area history file.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.y10`
              - Solar Flux (Y10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DensityModelPlugin.y10_avg`
              - Average solar Flux (Y10). Dimensionless.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import DensityModelPlugin


Property detail
---------------

.. py:property:: atmosphere_aug_data_file
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_aug_data_file
    :type: str

    Get or set the atmospheric model augmented data file path.

.. py:property:: atmosphere_aug_dtc_file
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_aug_dtc_file
    :type: str

    Get or set the atmospheric model augmented geomagnetic data file path.

.. py:property:: atmosphere_data_filename
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_data_filename
    :type: str

    Get or set the atmospheric model data file path.

.. py:property:: atmosphere_data_geo_magnetic_flux_source
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_data_geo_magnetic_flux_source
    :type: GeoMagneticFluxSource

    Whether to use Kp or Ap data from the flux file.

.. py:property:: atmosphere_data_geo_magnetic_flux_update_rate
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_data_geo_magnetic_flux_update_rate
    :type: GeoMagneticFluxUpdateRate

    Get or set the update rate for geomagnetic flux values from the flux file.

.. py:property:: atmosphere_data_source
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.atmosphere_data_source
    :type: AtmosphereDataSource

    Get or set the atmospheric model data source - data file or constant values.

.. py:property:: computes_pressure
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: computes_temperature
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: drag_model_plugin
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.drag_model_plugin
    :type: DragModelPlugin

    Drag model plugin properties.

.. py:property:: drag_model_plugin_name
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.drag_model_plugin_name
    :type: str

    Get or set the name of the drag model plugin.

.. py:property:: drag_model_type
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.drag_model_type
    :type: DragModelType

    Drag model type.

.. py:property:: dst_d_tc
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.dst_d_tc
    :type: float

    Temperature change calculated from disturbance storm time (DstDTc). Dimensionless.

.. py:property:: f10
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.f10
    :type: float

    Solar Flux (F10). Dimensionless.

.. py:property:: f10_avg
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.f10_avg
    :type: float

    Average solar Flux (F10). Dimensionless.

.. py:property:: kp
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.kp
    :type: float

    Geomagnetic Index (Kp). Dimensionless.

.. py:property:: m10
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.m10
    :type: float

    Solar Flux (M10). Dimensionless.

.. py:property:: m10_avg
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.m10_avg
    :type: float

    Average solar Flux (M10). Dimensionless.

.. py:property:: n_plate_definition_file
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.

.. py:property:: plugin_config
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.plugin_config
    :type: PluginProperties

    Get the properties of the selected plugin.

.. py:property:: plugin_identifier
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.plugin_identifier
    :type: str

    Get or set the plugin name.

.. py:property:: s10
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.s10
    :type: float

    Solar Flux (S10). Dimensionless.

.. py:property:: s10_avg
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.s10_avg
    :type: float

    Average solar Flux (S10). Dimensionless.

.. py:property:: sun_position
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.sun_position
    :type: SunPosition

    Get or set the sun position computation.

.. py:property:: use_approximate_altitude
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: uses_augmented_space_weather
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.uses_augmented_space_weather
    :type: bool

    Flag indicates whether this model uses augmented flux data.

.. py:property:: variable_area_history_file
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: y10
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.y10
    :type: float

    Solar Flux (Y10). Dimensionless.

.. py:property:: y10_avg
    :canonical: br.ok.core.stkobjects.astrogator.DensityModelPlugin.y10_avg
    :type: float

    Average solar Flux (Y10). Dimensionless.


