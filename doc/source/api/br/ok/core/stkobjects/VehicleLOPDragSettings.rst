VehicleLOPDragSettings
======================

.. py:class:: br.ok.core.stkobjects.VehicleLOPDragSettings

   Class defining advanced atmospheric density options for the LOP propagator.

.. py:currentmodule:: VehicleLOPDragSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleLOPDragSettings.atmosphere_density_model`
              - Atmospheric density model.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleLOPDragSettings.density_weighing_factor`
              - Get or set the scale factor to be used during density calculations. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleLOPDragSettings.exponential_density_model_parameters`
              - Get the exponential density modeling parameters.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleLOPDragSettings.maximum_drag_altitude`
              - Maximum drag altitude, above which drag calculations are not considered. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleLOPDragSettings.use_osculating_altitude`
              - Opt whether to use osculating altitude, which uses a short period variation due to J2 perturbations when calculating altitude.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleLOPDragSettings


Property detail
---------------

.. py:property:: atmosphere_density_model
    :canonical: br.ok.core.stkobjects.VehicleLOPDragSettings.atmosphere_density_model
    :type: LOPAtmosphericDensityModel

    Atmospheric density model.

.. py:property:: density_weighing_factor
    :canonical: br.ok.core.stkobjects.VehicleLOPDragSettings.density_weighing_factor
    :type: float

    Get or set the scale factor to be used during density calculations. Dimensionless.

.. py:property:: exponential_density_model_parameters
    :canonical: br.ok.core.stkobjects.VehicleLOPDragSettings.exponential_density_model_parameters
    :type: VehicleExponentialDensityModelParameters

    Get the exponential density modeling parameters.

.. py:property:: maximum_drag_altitude
    :canonical: br.ok.core.stkobjects.VehicleLOPDragSettings.maximum_drag_altitude
    :type: float

    Maximum drag altitude, above which drag calculations are not considered. Uses Distance Dimension.

.. py:property:: use_osculating_altitude
    :canonical: br.ok.core.stkobjects.VehicleLOPDragSettings.use_osculating_altitude
    :type: bool

    Opt whether to use osculating altitude, which uses a short period variation due to J2 perturbations when calculating altitude.


