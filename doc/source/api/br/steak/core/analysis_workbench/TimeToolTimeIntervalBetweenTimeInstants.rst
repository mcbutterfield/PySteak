TimeToolTimeIntervalBetweenTimeInstants
=======================================

.. py:class:: br.steak.core.analysis_workbench.TimeToolTimeIntervalBetweenTimeInstants

   Bases: :py:class:`~br.steak.core.analysis_workbench.ITimeToolTimeInterval`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

.. py:currentmodule:: TimeToolTimeIntervalBetweenTimeInstants

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeIntervalBetweenTimeInstants.start_time_instant`
              - The start time instant of the interval.
            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeIntervalBetweenTimeInstants.stop_time_instant`
              - The stop time instant of the interval.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import TimeToolTimeIntervalBetweenTimeInstants


Property detail
---------------

.. py:property:: start_time_instant
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeIntervalBetweenTimeInstants.start_time_instant
    :type: ITimeToolInstant

    The start time instant of the interval.

.. py:property:: stop_time_instant
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeIntervalBetweenTimeInstants.stop_time_instant
    :type: ITimeToolInstant

    The stop time instant of the interval.


