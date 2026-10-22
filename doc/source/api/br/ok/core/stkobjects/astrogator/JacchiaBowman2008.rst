JacchiaBowman2008
=================

.. py:class:: br.ok.core.stkobjects.astrogator.JacchiaBowman2008

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   Jacchia Bowman 2008 atmospheric propagator function.

.. py:currentmodule:: JacchiaBowman2008

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.atmosphere_aug_data_file`
              - Get or set the atmospheric model space weather data file path.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.atmosphere_aug_dtc_file`
              - Get or set the atmospheric model DTC file path.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.atmosphere_data_source`
              - Get or set the atmospheric model data source - data file or constant values.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.drag_correction_type`
              - Drag correction type.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.drag_model_plugin_name`
              - Get or set the name of the drag model plugin.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.drag_model_type`
              - Drag model type.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.dst_d_tc`
              - Temperature change calculated from disturbance storm time (DstDTc). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.f10`
              - Solar Flux (F10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.f10_avg`
              - Average solar Flux (F10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.m10`
              - Solar Flux (M10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.m10_avg`
              - Average solar Flux (M10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.n_plate_definition_file`
              - Drag N-Plate definition file.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.n_plate_stochastic_parameters`
              - NPlate Stochastic Parameters.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.s10`
              - Solar Flux (S10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.s10_avg`
              - Average solar Flux (S10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.stochastic_ballistic_coefficient`
              - Stochastic Ballistic Coefficient.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.stochastic_density_correction`
              - Stochastic StochasticDensity Correction.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.sun_position`
              - Get or set the sun position computation.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.use_stochastic_ballistic_coefficient`
              - True if using stochastic model for ballistic coefficient.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.use_stochastic_density_correction`
              - True if using stochastic model for a density model correction.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.variable_area_history_file`
              - Drag variable area history file.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.y10`
              - Solar Flux (Y10). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.JacchiaBowman2008.y10_avg`
              - Average solar Flux (Y10). Dimensionless.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import JacchiaBowman2008


Property detail
---------------

.. py:property:: atmosphere_aug_data_file
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.atmosphere_aug_data_file
    :type: str

    Get or set the atmospheric model space weather data file path.

.. py:property:: atmosphere_aug_dtc_file
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.atmosphere_aug_dtc_file
    :type: str

    Get or set the atmospheric model DTC file path.

.. py:property:: atmosphere_data_source
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.atmosphere_data_source
    :type: AtmosphereDataSource

    Get or set the atmospheric model data source - data file or constant values.

.. py:property:: drag_correction_type
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.drag_correction_type
    :type: DragCorrectionType

    Drag correction type.

.. py:property:: drag_model_plugin
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.drag_model_plugin
    :type: DragModelPlugin

    Drag model plugin properties.

.. py:property:: drag_model_plugin_name
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.drag_model_plugin_name
    :type: str

    Get or set the name of the drag model plugin.

.. py:property:: drag_model_type
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.drag_model_type
    :type: DragModelType

    Drag model type.

.. py:property:: dst_d_tc
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.dst_d_tc
    :type: float

    Temperature change calculated from disturbance storm time (DstDTc). Dimensionless.

.. py:property:: f10
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.f10
    :type: float

    Solar Flux (F10). Dimensionless.

.. py:property:: f10_avg
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.f10_avg
    :type: float

    Average solar Flux (F10). Dimensionless.

.. py:property:: m10
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.m10
    :type: float

    Solar Flux (M10). Dimensionless.

.. py:property:: m10_avg
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.m10_avg
    :type: float

    Average solar Flux (M10). Dimensionless.

.. py:property:: n_plate_definition_file
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.

.. py:property:: n_plate_stochastic_parameters
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.n_plate_stochastic_parameters
    :type: NPlateStochasticParametersCollection

    NPlate Stochastic Parameters.

.. py:property:: s10
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.s10
    :type: float

    Solar Flux (S10). Dimensionless.

.. py:property:: s10_avg
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.s10_avg
    :type: float

    Average solar Flux (S10). Dimensionless.

.. py:property:: stochastic_ballistic_coefficient
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.stochastic_ballistic_coefficient
    :type: StochasticModelParameters

    Stochastic Ballistic Coefficient.

.. py:property:: stochastic_density_correction
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.stochastic_density_correction
    :type: StochasticDensityCorrection

    Stochastic StochasticDensity Correction.

.. py:property:: sun_position
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.sun_position
    :type: SunPosition

    Get or set the sun position computation.

.. py:property:: use_approximate_altitude
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: use_stochastic_ballistic_coefficient
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.use_stochastic_ballistic_coefficient
    :type: bool

    True if using stochastic model for ballistic coefficient.

.. py:property:: use_stochastic_density_correction
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.use_stochastic_density_correction
    :type: bool

    True if using stochastic model for a density model correction.

.. py:property:: variable_area_history_file
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.variable_area_history_file
    :type: str

    Drag variable area history file.

.. py:property:: y10
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.y10
    :type: float

    Solar Flux (Y10). Dimensionless.

.. py:property:: y10_avg
    :canonical: br.ok.core.stkobjects.astrogator.JacchiaBowman2008.y10_avg
    :type: float

    Average solar Flux (Y10). Dimensionless.


