ITimePeriod
===========

.. py:class:: br.ok.core.stkobjects.ITimePeriod

   Provide methods and properties to configure start and stop times.

.. py:currentmodule:: ITimePeriod

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ITimePeriod.duration`
              - A time duration. The value is a relative duration (i.e. ``+1 day``, ``+1 hour``).
            * - :py:attr:`~br.ok.core.stkobjects.ITimePeriod.start_time`
              - Get a start time. Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.ITimePeriod.stop_time`
              - Get a stop time. Uses DateFormat Dimension.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ITimePeriod


Property detail
---------------

.. py:property:: duration
    :canonical: br.ok.core.stkobjects.ITimePeriod.duration
    :type: typing.Any

    A time duration. The value is a relative duration (i.e. ``+1 day``, ``+1 hour``).

.. py:property:: start_time
    :canonical: br.ok.core.stkobjects.ITimePeriod.start_time
    :type: TimePeriodValue

    Get a start time. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: br.ok.core.stkobjects.ITimePeriod.stop_time
    :type: TimePeriodValue

    Get a stop time. Uses DateFormat Dimension.


