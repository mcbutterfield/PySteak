TimeToolTimeArrayStartStopTimes
===============================

.. py:class:: br.ok.core.analysis_workbench.TimeToolTimeArrayStartStopTimes

   Bases: :py:class:`~br.ok.core.analysis_workbench.ITimeToolTimeArray`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

.. py:currentmodule:: TimeToolTimeArrayStartStopTimes

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeArrayStartStopTimes.reference_intervals`
              - The reference interval list.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeArrayStartStopTimes.start_stop_option`
              - The edge type. At least one of the two edge types must be selected.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import TimeToolTimeArrayStartStopTimes


Property detail
---------------

.. py:property:: reference_intervals
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeArrayStartStopTimes.reference_intervals
    :type: ITimeToolTimeIntervalList

    The reference interval list.

.. py:property:: start_stop_option
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeArrayStartStopTimes.start_stop_option
    :type: StartStopType

    The edge type. At least one of the two edge types must be selected.


