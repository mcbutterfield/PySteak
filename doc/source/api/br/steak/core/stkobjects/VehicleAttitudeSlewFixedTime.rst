VehicleAttitudeSlewFixedTime
============================

.. py:class:: br.steak.core.stkobjects.VehicleAttitudeSlewFixedTime

   Bases: :py:class:`~br.steak.core.stkobjects.IVehicleAttitudeSlewBase`

   Fixed time slew.

.. py:currentmodule:: VehicleAttitudeSlewFixedTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeSlewFixedTime.match_angular_velocity`
              - Indicate whether to take account of the angular velocity (slope) at the beginning and the end of the slew.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeSlewFixedTime.slew_time`
              - Get or set the time required to change attitude.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleAttitudeSlewFixedTime


Property detail
---------------

.. py:property:: match_angular_velocity
    :canonical: br.steak.core.stkobjects.VehicleAttitudeSlewFixedTime.match_angular_velocity
    :type: bool

    Indicate whether to take account of the angular velocity (slope) at the beginning and the end of the slew.

.. py:property:: slew_time
    :canonical: br.steak.core.stkobjects.VehicleAttitudeSlewFixedTime.slew_time
    :type: float

    Get or set the time required to change attitude.


