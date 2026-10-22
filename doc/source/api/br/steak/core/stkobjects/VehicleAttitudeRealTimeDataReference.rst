VehicleAttitudeRealTimeDataReference
====================================

.. py:class:: br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference

   Reference attitude profile for the incoming attitude data.

.. py:currentmodule:: VehicleAttitudeRealTimeDataReference

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.is_profile_type_supported`
              - Get a value indicating whether the specified profile type can be used.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.set_profile_type`
              - Set realtime data reference profile type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile`
              - Return a data reference profile or null if no data reference profile has yet been selected.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile_supported_types`
              - Return an array of valid profiles.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile_type`
              - Get realtime data reference profile type.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleAttitudeRealTimeDataReference


Property detail
---------------

.. py:property:: profile
    :canonical: br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile
    :type: IVehicleAttitudeProfile

    Return a data reference profile or null if no data reference profile has yet been selected.

.. py:property:: profile_supported_types
    :canonical: br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile_supported_types
    :type: list

    Return an array of valid profiles.

.. py:property:: profile_type
    :canonical: br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile_type
    :type: AttitudeProfile

    Get realtime data reference profile type.


Method detail
-------------

.. py:method:: is_profile_type_supported(self, profile: AttitudeProfile) -> bool
    :canonical: br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.is_profile_type_supported

    Get a value indicating whether the specified profile type can be used.

    :Parameters:

        **profile** : :obj:`~AttitudeProfile`


    :Returns:

        :obj:`~bool`




.. py:method:: set_profile_type(self, profile: AttitudeProfile) -> None
    :canonical: br.steak.core.stkobjects.VehicleAttitudeRealTimeDataReference.set_profile_type

    Set realtime data reference profile type.

    :Parameters:

        **profile** : :obj:`~AttitudeProfile`


    :Returns:

        :obj:`~None`

