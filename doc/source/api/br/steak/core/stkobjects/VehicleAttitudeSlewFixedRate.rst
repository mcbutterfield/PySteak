VehicleAttitudeSlewFixedRate
============================

.. py:class:: br.steak.core.stkobjects.VehicleAttitudeSlewFixedRate

   Bases: :py:class:`~br.steak.core.stkobjects.IVehicleAttitudeSlewBase`

   Fixed rate slew.

.. py:currentmodule:: VehicleAttitudeSlewFixedRate

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeSlewFixedRate.maximum_slew_rate`
              - Configure how to constrain the slew rate.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeSlewFixedRate.maximum_slew_time`
              - Limits the maximum slew rate.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleAttitudeSlewFixedRate.slew_timing_between_targets`
              - Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleAttitudeSlewFixedRate


Property detail
---------------

.. py:property:: maximum_slew_rate
    :canonical: br.steak.core.stkobjects.VehicleAttitudeSlewFixedRate.maximum_slew_rate
    :type: VehicleAttitudeMaximumSlewRate

    Configure how to constrain the slew rate.

.. py:property:: maximum_slew_time
    :canonical: br.steak.core.stkobjects.VehicleAttitudeSlewFixedRate.maximum_slew_time
    :type: float

    Limits the maximum slew rate.

.. py:property:: slew_timing_between_targets
    :canonical: br.steak.core.stkobjects.VehicleAttitudeSlewFixedRate.slew_timing_between_targets
    :type: VehicleSlewTimingBetweenTargetType

    Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.


