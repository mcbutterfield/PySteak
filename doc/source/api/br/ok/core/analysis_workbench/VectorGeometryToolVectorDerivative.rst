VectorGeometryToolVectorDerivative
==================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A vector derivative of a vector computed with respect to specified axes.

.. py:currentmodule:: VectorGeometryToolVectorDerivative

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative.differencing_time_step`
              - Time step used in numerical evaluation of derivatives using central differencing.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative.force_use_of_numerical_differences`
              - Force the use of numerical differences even if the derivative can be computed analytically.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative.vector`
              - Specify a base vector.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolVectorDerivative


Property detail
---------------

.. py:property:: differencing_time_step
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.

.. py:property:: force_use_of_numerical_differences
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative.force_use_of_numerical_differences
    :type: bool

    Force the use of numerical differences even if the derivative can be computed analytically.

.. py:property:: reference_axes
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: vector
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorDerivative.vector
    :type: VectorGeometryToolVectorReference

    Specify a base vector.


