VehicleInterpolation
====================

.. py:class:: br.steak.core.stkobjects.VehicleInterpolation

   Class defining interpolation for the HPOP integrator.

.. py:currentmodule:: VehicleInterpolation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleInterpolation.method`
              - Get or set the interpolation method.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleInterpolation.order`
              - Interpolation order. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleInterpolation.vop_mu`
              - Get or set the gravitational parameter used by the VOP method, in the range 1.993002209e+14 to 7.972008836e+14 for Earth based vehicles. Dimensionless.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleInterpolation


Property detail
---------------

.. py:property:: method
    :canonical: br.steak.core.stkobjects.VehicleInterpolation.method
    :type: VehicleInterpolationMethod

    Get or set the interpolation method.

.. py:property:: order
    :canonical: br.steak.core.stkobjects.VehicleInterpolation.order
    :type: int

    Interpolation order. Dimensionless.

.. py:property:: vop_mu
    :canonical: br.steak.core.stkobjects.VehicleInterpolation.vop_mu
    :type: float

    Get or set the gravitational parameter used by the VOP method, in the range 1.993002209e+14 to 7.972008836e+14 for Earth based vehicles. Dimensionless.


