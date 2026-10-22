AnalysisWorkbenchSystemTransformWithRateResult
==============================================

.. py:class:: br.ok.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolSystem.TransformFromWithRate and IVectorGeometryToolSystem.TransformToWithRate methods.

.. py:currentmodule:: AnalysisWorkbenchSystemTransformWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.vector`
              - The transformed vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.velocity`
              - The vector's velocity.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import AnalysisWorkbenchSystemTransformWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.vector
    :type: ICartesian3Vector

    The transformed vector.

.. py:property:: velocity
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.velocity
    :type: ICartesian3Vector

    The vector's velocity.


