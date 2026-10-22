VectorGeometryToolAxesAlignedAndConstrained
===========================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

.. py:currentmodule:: VectorGeometryToolAxesAlignedAndConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.alignment_direction`
              - Specify a desired alignment direction and the applicable parameters.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.alignment_reference_vector`
              - Specify an alignment reference vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.constraint_direction`
              - Specify a desired constraint direction and the applicable parameters.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.constraint_reference_vector`
              - Specify a constraint reference vector.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolAxesAlignedAndConstrained


Property detail
---------------

.. py:property:: alignment_direction
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.alignment_direction
    :type: IDirection

    Specify a desired alignment direction and the applicable parameters.

.. py:property:: alignment_reference_vector
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.alignment_reference_vector
    :type: VectorGeometryToolVectorReference

    Specify an alignment reference vector.

.. py:property:: constraint_direction
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.constraint_direction
    :type: IDirection

    Specify a desired constraint direction and the applicable parameters.

.. py:property:: constraint_reference_vector
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained.constraint_reference_vector
    :type: VectorGeometryToolVectorReference

    Specify a constraint reference vector.


