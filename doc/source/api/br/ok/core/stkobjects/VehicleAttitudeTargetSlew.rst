VehicleAttitudeTargetSlew
=========================

.. py:class:: br.ok.core.stkobjects.VehicleAttitudeTargetSlew

   Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

.. py:currentmodule:: VehicleAttitudeTargetSlew

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleAttitudeTargetSlew.is_slew_mode_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleAttitudeTargetSlew.set_slew_mode_type`
              - Select an attitude slew mode.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode`
              - Return a currently selected attitude slew configuration.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode_type`
              - Select an attitude slew mode.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleAttitudeTargetSlew


Property detail
---------------

.. py:property:: slew_mode
    :canonical: br.ok.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode
    :type: IVehicleAttitudeSlewBase

    Return a currently selected attitude slew configuration.

.. py:property:: slew_mode_supported_types
    :canonical: br.ok.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: slew_mode_type
    :canonical: br.ok.core.stkobjects.VehicleAttitudeTargetSlew.slew_mode_type
    :type: VehicleSlewMode

    Select an attitude slew mode.


Method detail
-------------

.. py:method:: is_slew_mode_type_supported(self, slew_mode: VehicleSlewMode) -> bool
    :canonical: br.ok.core.stkobjects.VehicleAttitudeTargetSlew.is_slew_mode_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **slew_mode** : :obj:`~VehicleSlewMode`


    :Returns:

        :obj:`~bool`

.. py:method:: set_slew_mode_type(self, slew_mode: VehicleSlewMode) -> None
    :canonical: br.ok.core.stkobjects.VehicleAttitudeTargetSlew.set_slew_mode_type

    Select an attitude slew mode.

    :Parameters:

        **slew_mode** : :obj:`~VehicleSlewMode`


    :Returns:

        :obj:`~None`




