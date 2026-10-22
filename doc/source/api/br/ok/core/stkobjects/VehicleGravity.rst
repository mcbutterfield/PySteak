VehicleGravity
==============

.. py:class:: br.ok.core.stkobjects.VehicleGravity

   Class defining gravity modeling options for a vehicle.

.. py:currentmodule:: VehicleGravity

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGravity.maximum_degree`
              - Maximum degree to use in the gravity field when propagating the state error covariance matrix. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGravity.maximum_order`
              - Maximum order to use in the gravity field when propagating the state error covariance matrix. Dimensionless.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGravity


Property detail
---------------

.. py:property:: maximum_degree
    :canonical: br.ok.core.stkobjects.VehicleGravity.maximum_degree
    :type: int

    Maximum degree to use in the gravity field when propagating the state error covariance matrix. Dimensionless.

.. py:property:: maximum_order
    :canonical: br.ok.core.stkobjects.VehicleGravity.maximum_order
    :type: int

    Maximum order to use in the gravity field when propagating the state error covariance matrix. Dimensionless.


