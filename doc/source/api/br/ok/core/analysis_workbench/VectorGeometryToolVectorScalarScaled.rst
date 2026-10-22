VectorGeometryToolVectorScalarScaled
====================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector`

   Scaled version of the input vector using scalar.

.. py:currentmodule:: VectorGeometryToolVectorScalarScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.dimension`
              - A dimension assigned to the output vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.dimension_inheritance`
              - Whether or not to inherit dimension from the input vector or the scalar.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.input_scalar`
              - A variable scale applied to the input vector. Can be based on any Scalar calculation.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.input_vector`
              - An input vector scaled by the scalar. Can be any VGT vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.normalize`
              - Whether to normalize the input vector before applying constant and variable scales.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.scale_factor`
              - A constant scale applied to the input vector.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolVectorScalarScaled


Property detail
---------------

.. py:property:: dimension
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.dimension
    :type: str

    A dimension assigned to the output vector.

.. py:property:: dimension_inheritance
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.dimension_inheritance
    :type: VectorGeometryToolScaledVectorDimensionInheritanceOptionType

    Whether or not to inherit dimension from the input vector or the scalar.

.. py:property:: input_scalar
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.input_scalar
    :type: ICalculationToolScalar

    A variable scale applied to the input vector. Can be based on any Scalar calculation.

.. py:property:: input_vector
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.input_vector
    :type: IVectorGeometryToolVector

    An input vector scaled by the scalar. Can be any VGT vector.

.. py:property:: normalize
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.normalize
    :type: bool

    Whether to normalize the input vector before applying constant and variable scales.

.. py:property:: scale_factor
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScalarScaled.scale_factor
    :type: float

    A constant scale applied to the input vector.


