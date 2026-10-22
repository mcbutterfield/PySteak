VehicleLOPForceModel
====================

.. py:class:: br.steak.core.stkobjects.VehicleLOPForceModel

   Class defining the force model for the LOP propagator.

.. py:currentmodule:: VehicleLOPForceModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPForceModel.central_body_gravity`
              - Get the central body gravity parameters.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPForceModel.drag`
              - Get the atmospheric drag parameters.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPForceModel.physical_data`
              - Get the physical data parameters.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPForceModel.solar_radiation_pressure`
              - Get the solar radiation pressure parameters.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPForceModel.third_body_gravity`
              - Get the 3rd body gravity parameters.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleLOPForceModel


Property detail
---------------

.. py:property:: central_body_gravity
    :canonical: br.steak.core.stkobjects.VehicleLOPForceModel.central_body_gravity
    :type: VehicleLOPCentralBodyGravity

    Get the central body gravity parameters.

.. py:property:: drag
    :canonical: br.steak.core.stkobjects.VehicleLOPForceModel.drag
    :type: VehicleLOPForceModelDrag

    Get the atmospheric drag parameters.

.. py:property:: physical_data
    :canonical: br.steak.core.stkobjects.VehicleLOPForceModel.physical_data
    :type: VehiclePhysicalData

    Get the physical data parameters.

.. py:property:: solar_radiation_pressure
    :canonical: br.steak.core.stkobjects.VehicleLOPForceModel.solar_radiation_pressure
    :type: VehicleLOPSolarRadiationPressure

    Get the solar radiation pressure parameters.

.. py:property:: third_body_gravity
    :canonical: br.steak.core.stkobjects.VehicleLOPForceModel.third_body_gravity
    :type: PropagatorLOPThirdBodyGravity

    Get the 3rd body gravity parameters.


