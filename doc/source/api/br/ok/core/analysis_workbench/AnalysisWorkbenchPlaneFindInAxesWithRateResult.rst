AnalysisWorkbenchPlaneFindInAxesWithRateResult
==============================================

.. py:class:: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolPlane.FindInAxesWithRate method.

.. py:currentmodule:: AnalysisWorkbenchPlaneFindInAxesWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.x_axis`
              - X-axis vector in the specified reference axes.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.x_axis_rate`
              - The rate of change of X-axis vector in the specified reference axes.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.y_axis`
              - Y-axis vector in the specified reference axes.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.y_axis_rate`
              - The rate of change of Y-axis vector in the specified reference axes.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import AnalysisWorkbenchPlaneFindInAxesWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: x_axis
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference axes.

.. py:property:: x_axis_rate
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.x_axis_rate
    :type: ICartesian3Vector

    The rate of change of X-axis vector in the specified reference axes.

.. py:property:: y_axis
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference axes.

.. py:property:: y_axis_rate
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult.y_axis_rate
    :type: ICartesian3Vector

    The rate of change of Y-axis vector in the specified reference axes.


