AnalysisWorkbenchAxesFindInAxesWithRateResult
=============================================

.. py:class:: br.ok.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesWithRateResult

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAxes.FindInAxesWithRate method.

.. py:currentmodule:: AnalysisWorkbenchAxesFindInAxesWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesWithRateResult.angular_velocity`
              - Axes' angular velocity.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesWithRateResult.orientation`
              - The axes' orientation.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import AnalysisWorkbenchAxesFindInAxesWithRateResult


Property detail
---------------

.. py:property:: angular_velocity
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesWithRateResult.angular_velocity
    :type: ICartesian3Vector

    Axes' angular velocity.

.. py:property:: is_valid
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: orientation
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesWithRateResult.orientation
    :type: IOrientation

    The axes' orientation.


