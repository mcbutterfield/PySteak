ScheduleTime
============

.. py:class:: br.ok.core.stkobjects.ScheduleTime

   Class for defining Sensor target times in terms of a specified schedule.

.. py:currentmodule:: ScheduleTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTime.start_time`
              - Start time of the scheduled access period. Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTime.stop_time`
              - Stop time of the scheduled access period. Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTime.target`
              - Object to which there is access during the scheduled period.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ScheduleTime


Property detail
---------------

.. py:property:: start_time
    :canonical: br.ok.core.stkobjects.ScheduleTime.start_time
    :type: typing.Any

    Start time of the scheduled access period. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: br.ok.core.stkobjects.ScheduleTime.stop_time
    :type: typing.Any

    Stop time of the scheduled access period. Uses DateFormat Dimension.

.. py:property:: target
    :canonical: br.ok.core.stkobjects.ScheduleTime.target
    :type: str

    Object to which there is access during the scheduled period.


