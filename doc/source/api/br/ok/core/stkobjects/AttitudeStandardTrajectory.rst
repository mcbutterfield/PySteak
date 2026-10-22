AttitudeStandardTrajectory
==========================

.. py:class:: br.ok.core.stkobjects.AttitudeStandardTrajectory

   Bases: :py:class:`~br.ok.core.stkobjects.IVehicleAttitudeStandard`, :py:class:`~br.ok.core.stkobjects.IVehicleAttitude`

   Standard attitude profile for launch vehicle or missile.

.. py:currentmodule:: AttitudeStandardTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardTrajectory.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardTrajectory.external`
              - Get the precomputed (external) attitude properties.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardTrajectory.pointing`
              - Get the target pointing attitude properties.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AttitudeStandardTrajectory


Property detail
---------------

.. py:property:: basic
    :canonical: br.ok.core.stkobjects.AttitudeStandardTrajectory.basic
    :type: AttitudeStandardBasic

    Get the basic attitude properties.

.. py:property:: external
    :canonical: br.ok.core.stkobjects.AttitudeStandardTrajectory.external
    :type: VehicleAttitudeExternal

    Get the precomputed (external) attitude properties.

.. py:property:: pointing
    :canonical: br.ok.core.stkobjects.AttitudeStandardTrajectory.pointing
    :type: VehicleAttitudePointing

    Get the target pointing attitude properties.


