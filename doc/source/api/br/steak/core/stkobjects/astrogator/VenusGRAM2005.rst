VenusGRAM2005
=============

.. py:class:: br.steak.core.stkobjects.astrogator.VenusGRAM2005

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   Venus-GRAM 2005 atmospheric propagator function.

.. py:currentmodule:: VenusGRAM2005

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.computes_pressure`
              - Flag indicates whether this model computes pressure.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.computes_temperature`
              - Flag indicates whether this model computes temperature.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.data_directory`
              - Path to the data directory.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.density_type`
              - Low, mean, high or randomly perturbed density type.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.drag_correction_type`
              - Drag correction type.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.drag_model_plugin`
              - Drag model plugin properties.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.drag_model_plugin_name`
              - Get or set the name of the drag model plugin.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.drag_model_type`
              - Drag model type.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.n_plate_definition_file`
              - Drag N-Plate definition file.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.n_plate_stochastic_parameters`
              - NPlate Stochastic Parameters.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.namelist_file`
              - Full path of namelist file.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.stochastic_ballistic_coefficient`
              - Stochastic Ballistic Coefficient.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.stochastic_density_correction`
              - Stochastic StochasticDensity Correction.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.use_approximate_altitude`
              - True if using approximate altitude formula.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.use_stochastic_ballistic_coefficient`
              - True if using stochastic model for ballistic coefficient.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.use_stochastic_density_correction`
              - True if using stochastic model for a density model correction.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.VenusGRAM2005.variable_area_history_file`
              - Drag variable area history file.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import VenusGRAM2005


Property detail
---------------

.. py:property:: computes_pressure
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.computes_pressure
    :type: bool

    Flag indicates whether this model computes pressure.

.. py:property:: computes_temperature
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.computes_temperature
    :type: bool

    Flag indicates whether this model computes temperature.

.. py:property:: data_directory
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.data_directory
    :type: str

    Path to the data directory.

.. py:property:: density_type
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.density_type
    :type: VenusGRAMDensityType

    Low, mean, high or randomly perturbed density type.

.. py:property:: drag_correction_type
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.drag_correction_type
    :type: DragCorrectionType

    Drag correction type.

.. py:property:: drag_model_plugin
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.drag_model_plugin
    :type: DragModelPlugin

    Drag model plugin properties.

.. py:property:: drag_model_plugin_name
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.drag_model_plugin_name
    :type: str

    Get or set the name of the drag model plugin.

.. py:property:: drag_model_type
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.drag_model_type
    :type: DragModelType

    Drag model type.

.. py:property:: n_plate_definition_file
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.n_plate_definition_file
    :type: str

    Drag N-Plate definition file.

.. py:property:: n_plate_stochastic_parameters
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.n_plate_stochastic_parameters
    :type: NPlateStochasticParametersCollection

    NPlate Stochastic Parameters.

.. py:property:: namelist_file
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.namelist_file
    :type: str

    Full path of namelist file.

.. py:property:: stochastic_ballistic_coefficient
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.stochastic_ballistic_coefficient
    :type: StochasticModelParameters

    Stochastic Ballistic Coefficient.

.. py:property:: stochastic_density_correction
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.stochastic_density_correction
    :type: StochasticDensityCorrection

    Stochastic StochasticDensity Correction.

.. py:property:: use_approximate_altitude
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.use_approximate_altitude
    :type: bool

    True if using approximate altitude formula.

.. py:property:: use_stochastic_ballistic_coefficient
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.use_stochastic_ballistic_coefficient
    :type: bool

    True if using stochastic model for ballistic coefficient.

.. py:property:: use_stochastic_density_correction
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.use_stochastic_density_correction
    :type: bool

    True if using stochastic model for a density model correction.

.. py:property:: variable_area_history_file
    :canonical: br.steak.core.stkobjects.astrogator.VenusGRAM2005.variable_area_history_file
    :type: str

    Drag variable area history file.


