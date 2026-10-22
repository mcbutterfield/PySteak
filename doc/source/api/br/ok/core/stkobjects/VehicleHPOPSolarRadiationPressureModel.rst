VehicleHPOPSolarRadiationPressureModel
======================================

.. py:class:: br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel

   SRP Model Base CoClass.

.. py:currentmodule:: VehicleHPOPSolarRadiationPressureModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.is_model_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.set_model_type`
              - Change the active solar radiation pressure model type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model`
              - Return the active solar radiation pressure model.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model_type`
              - Return a type of the active solar radiation pressure model.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleHPOPSolarRadiationPressureModel


Property detail
---------------

.. py:property:: model
    :canonical: br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model
    :type: ISRPModelBase

    Return the active solar radiation pressure model.

.. py:property:: model_supported_types
    :canonical: br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: model_type
    :canonical: br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model_type
    :type: SolarRadiationPressureModelType

    Return a type of the active solar radiation pressure model.


Method detail
-------------

.. py:method:: is_model_type_supported(self, srp_model: SolarRadiationPressureModelType) -> bool
    :canonical: br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.is_model_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **srp_model** : :obj:`~SolarRadiationPressureModelType`


    :Returns:

        :obj:`~bool`




.. py:method:: set_model_type(self, srp_model: SolarRadiationPressureModelType) -> None
    :canonical: br.ok.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.set_model_type

    Change the active solar radiation pressure model type.

    :Parameters:

        **srp_model** : :obj:`~SolarRadiationPressureModelType`


    :Returns:

        :obj:`~None`

