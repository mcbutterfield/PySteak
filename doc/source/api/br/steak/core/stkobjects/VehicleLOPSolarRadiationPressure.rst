VehicleLOPSolarRadiationPressure
================================

.. py:class:: br.steak.core.stkobjects.VehicleLOPSolarRadiationPressure

   Class defining the solar radiation pressure model for the LOP propagator.

.. py:currentmodule:: VehicleLOPSolarRadiationPressure

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPSolarRadiationPressure.atmosphere_height`
              - Height of atmosphere blockage used when calculating shadow entry and exit in solar radiation computations. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPSolarRadiationPressure.cp`
              - Get or set the solar radiation pressure coefficient. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPSolarRadiationPressure.use`
              - Opt whether to use SRP.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleLOPSolarRadiationPressure


Property detail
---------------

.. py:property:: atmosphere_height
    :canonical: br.steak.core.stkobjects.VehicleLOPSolarRadiationPressure.atmosphere_height
    :type: float

    Height of atmosphere blockage used when calculating shadow entry and exit in solar radiation computations. Uses Distance Dimension.

.. py:property:: cp
    :canonical: br.steak.core.stkobjects.VehicleLOPSolarRadiationPressure.cp
    :type: float

    Get or set the solar radiation pressure coefficient. Dimensionless.

.. py:property:: use
    :canonical: br.steak.core.stkobjects.VehicleLOPSolarRadiationPressure.use
    :type: bool

    Opt whether to use SRP.


