LaunchVehicleInitialState
=========================

.. py:class:: br.steak.core.stkobjects.LaunchVehicleInitialState

   Class defining launch vehicle initial state.

.. py:currentmodule:: LaunchVehicleInitialState

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicleInitialState.burnout`
              - Get the geocentric or geodetic burnout position coordinates.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicleInitialState.burnout_velocity`
              - Burnout velocity, i.e. the velocity of the vehicle at the stop time.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicleInitialState.launch`
              - Get the geocentric or geodetic launch position coordinates.
            * - :py:attr:`~br.steak.core.stkobjects.LaunchVehicleInitialState.trajectory_epoch`
              - Get the smart epoch component to access the trajectory epoch.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import LaunchVehicleInitialState


Property detail
---------------

.. py:property:: burnout
    :canonical: br.steak.core.stkobjects.LaunchVehicleInitialState.burnout
    :type: ILatitudeLongitudeAltitudePosition

    Get the geocentric or geodetic burnout position coordinates.

.. py:property:: burnout_velocity
    :canonical: br.steak.core.stkobjects.LaunchVehicleInitialState.burnout_velocity
    :type: float

    Burnout velocity, i.e. the velocity of the vehicle at the stop time.

.. py:property:: launch
    :canonical: br.steak.core.stkobjects.LaunchVehicleInitialState.launch
    :type: ILatitudeLongitudeAltitudePosition

    Get the geocentric or geodetic launch position coordinates.

.. py:property:: trajectory_epoch
    :canonical: br.steak.core.stkobjects.LaunchVehicleInitialState.trajectory_epoch
    :type: ITimeToolInstantSmartEpoch

    Get the smart epoch component to access the trajectory epoch.


