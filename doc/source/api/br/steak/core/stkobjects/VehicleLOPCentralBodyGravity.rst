VehicleLOPCentralBodyGravity
============================

.. py:class:: br.steak.core.stkobjects.VehicleLOPCentralBodyGravity

   Class defining gravity options for the LOP propagator.

.. py:currentmodule:: VehicleLOPCentralBodyGravity

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPCentralBodyGravity.maximum_degree`
              - Get or set the maximum degree of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleLOPCentralBodyGravity.maximum_order`
              - Get or set the maximum order of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleLOPCentralBodyGravity


Property detail
---------------

.. py:property:: maximum_degree
    :canonical: br.steak.core.stkobjects.VehicleLOPCentralBodyGravity.maximum_degree
    :type: int

    Get or set the maximum degree of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.

.. py:property:: maximum_order
    :canonical: br.steak.core.stkobjects.VehicleLOPCentralBodyGravity.maximum_order
    :type: int

    Get or set the maximum order of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.


