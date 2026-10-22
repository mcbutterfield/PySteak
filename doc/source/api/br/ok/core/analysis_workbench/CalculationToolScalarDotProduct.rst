CalculationToolScalarDotProduct
===============================

.. py:class:: br.ok.core.analysis_workbench.CalculationToolScalarDotProduct

   Bases: :py:class:`~br.ok.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Dot product between two vectors.

.. py:currentmodule:: CalculationToolScalarDotProduct

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.dimension`
              - Return a unit of measure, i.e. 'Angle', 'Distance', etc.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.normalize_vector_a`
              - Whether to normalize vector A.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.normalize_vector_b`
              - Whether to normalize vector B.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.vector_a`
              - First vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.vector_b`
              - Second vector.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import CalculationToolScalarDotProduct


Property detail
---------------

.. py:property:: dimension
    :canonical: br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.dimension
    :type: str

    Return a unit of measure, i.e. 'Angle', 'Distance', etc.

.. py:property:: normalize_vector_a
    :canonical: br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.normalize_vector_a
    :type: bool

    Whether to normalize vector A.

.. py:property:: normalize_vector_b
    :canonical: br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.normalize_vector_b
    :type: bool

    Whether to normalize vector B.

.. py:property:: vector_a
    :canonical: br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.vector_a
    :type: IVectorGeometryToolVector

    First vector.

.. py:property:: vector_b
    :canonical: br.ok.core.analysis_workbench.CalculationToolScalarDotProduct.vector_b
    :type: IVectorGeometryToolVector

    Second vector.


