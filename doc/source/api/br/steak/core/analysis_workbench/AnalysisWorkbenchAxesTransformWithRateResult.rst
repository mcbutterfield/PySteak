AnalysisWorkbenchAxesTransformWithRateResult
============================================

.. py:class:: br.steak.core.analysis_workbench.AnalysisWorkbenchAxesTransformWithRateResult

   Bases: :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAxes.TransformFromWithRate method.

.. py:currentmodule:: AnalysisWorkbenchAxesTransformWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.AnalysisWorkbenchAxesTransformWithRateResult.is_valid`
              - Indicate whether the result object is valid.
            * - :py:attr:`~br.steak.core.analysis_workbench.AnalysisWorkbenchAxesTransformWithRateResult.vector`
              - The output vector in the current axes.
            * - :py:attr:`~br.steak.core.analysis_workbench.AnalysisWorkbenchAxesTransformWithRateResult.velocity`
              - The vector velocity.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import AnalysisWorkbenchAxesTransformWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: br.steak.core.analysis_workbench.AnalysisWorkbenchAxesTransformWithRateResult.is_valid
    :type: bool

    Indicate whether the result object is valid.

.. py:property:: vector
    :canonical: br.steak.core.analysis_workbench.AnalysisWorkbenchAxesTransformWithRateResult.vector
    :type: ICartesian3Vector

    The output vector in the current axes.

.. py:property:: velocity
    :canonical: br.steak.core.analysis_workbench.AnalysisWorkbenchAxesTransformWithRateResult.velocity
    :type: ICartesian3Vector

    The vector velocity.


