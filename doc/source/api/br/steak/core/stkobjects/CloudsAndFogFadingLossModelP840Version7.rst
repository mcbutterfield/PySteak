CloudsAndFogFadingLossModelP840Version7
=======================================

.. py:class:: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7

   Bases: :py:class:`~br.steak.core.stkobjects.ICloudsAndFogFadingLossModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a clouds and fog Loss ITU-R P.840-7 model.

.. py:currentmodule:: CloudsAndFogFadingLossModelP840Version7

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.average_data_month`
              - Get or set the month, (1 - 12) of the year, used to get average liquid water data.
            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.cloud_ceiling`
              - Get or set the cloud ceiling.
            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.cloud_layer_thickness`
              - Get or set the cloud layer thickness.
            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.cloud_liquid_water_density`
              - Get or set the cloud liquid water density.
            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.cloud_temperature`
              - Get or set the cloud temperature.
            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.liquid_water_density_choice`
              - Get or set the cloud liquid water density Choice.
            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.liquid_water_percent_annual_exceeded`
              - Get or set the Liquid water % Annual Exceeded.
            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.liquid_water_percent_monthly_exceeded`
              - Get or set the Liquid water % Monthly Exceeded.
            * - :py:attr:`~br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.use_rain_height_as_cloud_layer_thickness`
              - Get or set the use rain height as cloud layer thickness.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import CloudsAndFogFadingLossModelP840Version7


Property detail
---------------

.. py:property:: average_data_month
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.average_data_month
    :type: int

    Get or set the month, (1 - 12) of the year, used to get average liquid water data.

.. py:property:: cloud_ceiling
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.cloud_ceiling
    :type: float

    Get or set the cloud ceiling.

.. py:property:: cloud_layer_thickness
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.cloud_layer_thickness
    :type: float

    Get or set the cloud layer thickness.

.. py:property:: cloud_liquid_water_density
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.cloud_liquid_water_density
    :type: float

    Get or set the cloud liquid water density.

.. py:property:: cloud_temperature
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.cloud_temperature
    :type: float

    Get or set the cloud temperature.

.. py:property:: liquid_water_density_choice
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.liquid_water_density_choice
    :type: CloudsAndFogLiquidWaterChoiceType

    Get or set the cloud liquid water density Choice.

.. py:property:: liquid_water_percent_annual_exceeded
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.liquid_water_percent_annual_exceeded
    :type: float

    Get or set the Liquid water % Annual Exceeded.

.. py:property:: liquid_water_percent_monthly_exceeded
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.liquid_water_percent_monthly_exceeded
    :type: float

    Get or set the Liquid water % Monthly Exceeded.

.. py:property:: use_rain_height_as_cloud_layer_thickness
    :canonical: br.steak.core.stkobjects.CloudsAndFogFadingLossModelP840Version7.use_rain_height_as_cloud_layer_thickness
    :type: bool

    Get or set the use rain height as cloud layer thickness.


