VehicleTargetTimes
==================

.. py:class:: br.steak.core.stkobjects.VehicleTargetTimes

   Target times for target pointing attitude.

.. py:currentmodule:: VehicleTargetTimes

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleTargetTimes.deconflict`
              - Deconflict intervals.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleTargetTimes.access_times`
              - Get the access times.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleTargetTimes.schedule_times`
              - Get the scheduled times.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleTargetTimes.use_access_times`
              - Opt whether to use access times as target times; otherwise, scheduled times are used.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleTargetTimes


Property detail
---------------

.. py:property:: access_times
    :canonical: br.steak.core.stkobjects.VehicleTargetTimes.access_times
    :type: AccessTargetTimesCollection

    Get the access times.

.. py:property:: schedule_times
    :canonical: br.steak.core.stkobjects.VehicleTargetTimes.schedule_times
    :type: AttitudeScheduleTimesCollection

    Get the scheduled times.

.. py:property:: use_access_times
    :canonical: br.steak.core.stkobjects.VehicleTargetTimes.use_access_times
    :type: bool

    Opt whether to use access times as target times; otherwise, scheduled times are used.


Method detail
-------------


.. py:method:: deconflict(self) -> None
    :canonical: br.steak.core.stkobjects.VehicleTargetTimes.deconflict

    Deconflict intervals.

    :Returns:

        :obj:`~None`




