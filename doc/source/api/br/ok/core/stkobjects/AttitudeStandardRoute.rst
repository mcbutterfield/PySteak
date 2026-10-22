AttitudeStandardRoute
=====================

.. py:class:: br.ok.core.stkobjects.AttitudeStandardRoute

   Bases: :py:class:`~br.ok.core.stkobjects.IVehicleAttitudeStandard`, :py:class:`~br.ok.core.stkobjects.IVehicleAttitude`

   Standard attitude profile for aircraft.

.. py:currentmodule:: AttitudeStandardRoute

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardRoute.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardRoute.external`
              - Get the precomputed (external) attitude properties.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AttitudeStandardRoute


Property detail
---------------

.. py:property:: basic
    :canonical: br.ok.core.stkobjects.AttitudeStandardRoute.basic
    :type: AttitudeStandardBasic

    Get the basic attitude properties.

.. py:property:: external
    :canonical: br.ok.core.stkobjects.AttitudeStandardRoute.external
    :type: VehicleAttitudeExternal

    Get the precomputed (external) attitude properties.


