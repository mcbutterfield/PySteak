AircraftBasicDescentModel
=========================

.. py:class:: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~br.ok.core.stkobjects.aviator.ICatalogItem`

   Class defining the basic descent performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftBasicDescentModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.set_airspeed`
              - Set the airspeed type and value.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.airspeed`
              - Get the airsepeed.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.altitude_rate`
              - Get or set the altitude rate.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.ceiling_altitude`
              - Get or set the ceiling altitude.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.enable_relative_airspeed_tolerance`
              - Get or set whether to enable relative airspeed tolerance.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.fuel_flow`
              - Get or set the Sea Level Fuel Flow.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.relative_airspeed_tolerance`
              - Get or set the relative airspeed tolerance.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.scale_fuel_flow_by_non_std_density`
              - Get or set whether to scale fuel flow by non std density.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.use_aerodynamic_propulsion_fuel`
              - Get or set whether to use Aero/Propulsion fuel flow.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import AircraftBasicDescentModel


Property detail
---------------

.. py:property:: airspeed
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.airspeed
    :type: float

    Get the airsepeed.

.. py:property:: airspeed_type
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: altitude_rate
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.altitude_rate
    :type: float

    Get or set the altitude rate.

.. py:property:: ceiling_altitude
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.ceiling_altitude
    :type: float

    Get or set the ceiling altitude.

.. py:property:: enable_relative_airspeed_tolerance
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.enable_relative_airspeed_tolerance
    :type: bool

    Get or set whether to enable relative airspeed tolerance.

.. py:property:: fuel_flow
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.fuel_flow
    :type: float

    Get or set the Sea Level Fuel Flow.

.. py:property:: relative_airspeed_tolerance
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.relative_airspeed_tolerance
    :type: float

    Get or set the relative airspeed tolerance.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Get or set whether to scale fuel flow by non std density.

.. py:property:: use_aerodynamic_propulsion_fuel
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.use_aerodynamic_propulsion_fuel
    :type: bool

    Get or set whether to use Aero/Propulsion fuel flow.


Method detail
-------------











.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`





.. py:method:: set_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: br.ok.core.stkobjects.aviator.AircraftBasicDescentModel.set_airspeed

    Set the airspeed type and value.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`



