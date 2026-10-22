AccessTimePeriod
================

.. py:class:: br.steak.core.stkobjects.AccessTimePeriod

   Bases: :py:class:`~br.steak.core.stkobjects.ITimePeriod`, :py:class:`~br.steak.core.stkobjects.IAccessInterval`

   Allow configuring the object's access interval.

.. py:currentmodule:: AccessTimePeriod

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AccessTimePeriod.access_interval`
              - Return an access interval.
            * - :py:attr:`~br.steak.core.stkobjects.AccessTimePeriod.duration`
              - A time duration. The value is a relative duration (i.e. ``+1 day``, ``+1 hour``).
            * - :py:attr:`~br.steak.core.stkobjects.AccessTimePeriod.start_time`
              - Get a start time. Uses DateFormat Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.AccessTimePeriod.stop_time`
              - Get a stop time. Uses DateFormat Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AccessTimePeriod


Property detail
---------------

.. py:property:: access_interval
    :canonical: br.steak.core.stkobjects.AccessTimePeriod.access_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Return an access interval.

.. py:property:: duration
    :canonical: br.steak.core.stkobjects.AccessTimePeriod.duration
    :type: typing.Any

    A time duration. The value is a relative duration (i.e. ``+1 day``, ``+1 hour``).

.. py:property:: start_time
    :canonical: br.steak.core.stkobjects.AccessTimePeriod.start_time
    :type: TimePeriodValue

    Get a start time. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: br.steak.core.stkobjects.AccessTimePeriod.stop_time
    :type: TimePeriodValue

    Get a stop time. Uses DateFormat Dimension.


