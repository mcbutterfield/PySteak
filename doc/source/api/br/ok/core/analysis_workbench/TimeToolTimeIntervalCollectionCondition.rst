TimeToolTimeIntervalCollectionCondition
=======================================

.. py:class:: br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition

   Bases: :py:class:`~br.ok.core.analysis_workbench.ITimeToolTimeIntervalCollection`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

.. py:currentmodule:: TimeToolTimeIntervalCollectionCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.condition_set`
              - Get/set the condition set object.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.convergence`
              - A Convergence definition, which uses time tolerance to determine when time of extremum is found.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.custom_time_limits`
              - A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.sampling`
              - A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.save_data_option`
              - Determine if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.use_custom_time_limits`
              - Specify whether to use specified custom interval list (see CustomTimeLimits).



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import TimeToolTimeIntervalCollectionCondition


Property detail
---------------

.. py:property:: condition_set
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.condition_set
    :type: ICalculationToolConditionSet

    Get/set the condition set object.

.. py:property:: convergence
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.convergence
    :type: IAnalysisWorkbenchConvergence

    A Convergence definition, which uses time tolerance to determine when time of extremum is found.

.. py:property:: custom_time_limits
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.custom_time_limits
    :type: ITimeToolTimeIntervalList

    A custom interval list or a single interval. By default it is set to overall availability of host object. This determines time limits within which global minimum or maximum is sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: sampling
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.sampling
    :type: IAnalysisWorkbenchSampling

    A Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: save_data_option
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.save_data_option
    :type: SaveDataType

    Determine if computed time of extremum is saved/loaded, otherwise it is recomputed on load if necessary.

.. py:property:: use_custom_time_limits
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition.use_custom_time_limits
    :type: bool

    Specify whether to use specified custom interval list (see CustomTimeLimits).


