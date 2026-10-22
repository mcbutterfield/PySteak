VehicleAttitudePointing
=======================

.. py:class:: br.steak.core.stkobjects.VehicleAttitudePointing

   Bases: :py:class:`~br.steak.core.stkobjects.IVehiclePointing`

   Target pointing attitude parameters.

.. py:currentmodule:: VehicleAttitudePointing

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudePointing.advanced`
              - Return advanced targeting access computation properties.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudePointing.target_slew`
              - Define the time required for the vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleAttitudePointing


Property detail
---------------

.. py:property:: advanced
    :canonical: br.steak.core.stkobjects.VehicleAttitudePointing.advanced
    :type: VehicleAccessAdvancedSettings

    Return advanced targeting access computation properties.

.. py:property:: target_slew
    :canonical: br.steak.core.stkobjects.VehicleAttitudePointing.target_slew
    :type: VehicleAttitudeTargetSlew

    Define the time required for the vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.


