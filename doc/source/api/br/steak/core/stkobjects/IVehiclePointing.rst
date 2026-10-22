IVehiclePointing
================

.. py:class:: br.steak.core.stkobjects.IVehiclePointing

   Interface for target pointing attitude profiles, which override the basic attitude profile for a satellite and have a selected axis point in the direction of one or more selected targets, subject to applicable access constraints.

.. py:currentmodule:: IVehiclePointing

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.IVehiclePointing.target_times`
              - Get the target times.
            * - :py:attr:`~br.steak.core.stkobjects.IVehiclePointing.targets`
              - Get the targets used for the attitude profile.
            * - :py:attr:`~br.steak.core.stkobjects.IVehiclePointing.use_target_pointing`
              - Opt whether to use a target pointing attitude.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import IVehiclePointing


Property detail
---------------

.. py:property:: target_times
    :canonical: br.steak.core.stkobjects.IVehiclePointing.target_times
    :type: VehicleTargetTimes

    Get the target times.

.. py:property:: targets
    :canonical: br.steak.core.stkobjects.IVehiclePointing.targets
    :type: VehicleTargetPointingCollection

    Get the targets used for the attitude profile.

.. py:property:: use_target_pointing
    :canonical: br.steak.core.stkobjects.IVehiclePointing.use_target_pointing
    :type: bool

    Opt whether to use a target pointing attitude.


