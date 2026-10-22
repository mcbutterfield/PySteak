CalculationToolScalarVectorComponent
====================================

.. py:class:: br.ok.core.analysis_workbench.CalculationToolScalarVectorComponent

   Bases: :py:class:`~br.ok.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   The specified component of a vector when resolved in the specified axes.

.. py:currentmodule:: CalculationToolScalarVectorComponent

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolScalarVectorComponent.component`
              - The component of the vector to return as the value of the scalar.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolScalarVectorComponent.input_vector`
              - Vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolScalarVectorComponent.reference_axes`
              - Axes used to resolve the vector's components.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import CalculationToolScalarVectorComponent


Property detail
---------------

.. py:property:: component
    :canonical: br.ok.core.analysis_workbench.CalculationToolScalarVectorComponent.component
    :type: VectorComponentType

    The component of the vector to return as the value of the scalar.

.. py:property:: input_vector
    :canonical: br.ok.core.analysis_workbench.CalculationToolScalarVectorComponent.input_vector
    :type: IVectorGeometryToolVector

    Vector.

.. py:property:: reference_axes
    :canonical: br.ok.core.analysis_workbench.CalculationToolScalarVectorComponent.reference_axes
    :type: IVectorGeometryToolAxes

    Axes used to resolve the vector's components.


