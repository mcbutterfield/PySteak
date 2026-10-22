AnalysisWorkbenchPlaneFindInSystemWithRateResult
================================================

.. py:class:: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolPlane.FindInSystemWithRate method.

.. py:currentmodule:: AnalysisWorkbenchPlaneFindInSystemWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.origin_position`
              - The position of the plane's center point in the specified coordinate system.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.origin_velocity`
              - The rate of change of the position of the plane's center point in the specified coordinate system.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.x_axis`
              - X-axis vector in the specified reference system.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.x_axis_rate`
              - A rate of change of the X-axis vector in the specified reference system.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.y_axis`
              - Y-axis vector in the specified reference system.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.y_axis_rate`
              - A rate of change of the Y-axis vector in the specified reference system.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import AnalysisWorkbenchPlaneFindInSystemWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: origin_position
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.origin_position
    :type: ICartesian3Vector

    The position of the plane's center point in the specified coordinate system.

.. py:property:: origin_velocity
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.origin_velocity
    :type: ICartesian3Vector

    The rate of change of the position of the plane's center point in the specified coordinate system.

.. py:property:: x_axis
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference system.

.. py:property:: x_axis_rate
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.x_axis_rate
    :type: ICartesian3Vector

    A rate of change of the X-axis vector in the specified reference system.

.. py:property:: y_axis
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference system.

.. py:property:: y_axis_rate
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult.y_axis_rate
    :type: ICartesian3Vector

    A rate of change of the Y-axis vector in the specified reference system.


