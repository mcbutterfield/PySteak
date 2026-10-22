TimeToolTimeIntervalSatisfactionConditionFilter
===============================================

.. py:class:: br.steak.core.analysis_workbench.TimeToolTimeIntervalSatisfactionConditionFilter

   Bases: :py:class:`~br.steak.core.analysis_workbench.ITimeToolPruneFilter`

   The filter selects intervals if certain side condition is satisfied at least/most certain duration.

.. py:currentmodule:: TimeToolTimeIntervalSatisfactionConditionFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeIntervalSatisfactionConditionFilter.condition`
              - Get or set the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.
            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeIntervalSatisfactionConditionFilter.duration_type`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeIntervalSatisfactionConditionFilter.interval_duration`
              - A duration of time the condition must be satisfied.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import TimeToolTimeIntervalSatisfactionConditionFilter


Property detail
---------------

.. py:property:: condition
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeIntervalSatisfactionConditionFilter.condition
    :type: ICalculationToolCondition

    Get or set the additional condition to be satisfied At Most or At Least specified duration within any interval for it to be considered in filtered list.

.. py:property:: duration_type
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeIntervalSatisfactionConditionFilter.duration_type
    :type: IntervalDurationType

    Choose a duration type (at least/at most).

.. py:property:: interval_duration
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeIntervalSatisfactionConditionFilter.interval_duration
    :type: float

    A duration of time the condition must be satisfied.


