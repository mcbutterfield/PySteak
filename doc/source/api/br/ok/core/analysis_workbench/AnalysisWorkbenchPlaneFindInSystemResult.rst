AnalysisWorkbenchPlaneFindInSystemResult
========================================

.. py:class:: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolPlane.FindInSystem method.

.. py:currentmodule:: AnalysisWorkbenchPlaneFindInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.origin_position`
              - The position of the plane's center point in the specified coordinate system.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.x_axis`
              - X-axis vector in the specified reference system.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.y_axis`
              - Y-axis vector in the specified reference system.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import AnalysisWorkbenchPlaneFindInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: origin_position
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.origin_position
    :type: ICartesian3Vector

    The position of the plane's center point in the specified coordinate system.

.. py:property:: x_axis
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference system.

.. py:property:: y_axis
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference system.


