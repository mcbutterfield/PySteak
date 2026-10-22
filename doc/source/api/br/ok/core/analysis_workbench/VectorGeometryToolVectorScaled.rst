VectorGeometryToolVectorScaled
==============================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolVectorScaled

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

.. py:currentmodule:: VectorGeometryToolVectorScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScaled.is_normalized`
              - Control whether to convert the reference vector to a unit vector before scalling.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScaled.reference_vector`
              - A vector being scaled.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorScaled.scale`
              - A scaling multiple.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolVectorScaled


Property detail
---------------

.. py:property:: is_normalized
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScaled.is_normalized
    :type: bool

    Control whether to convert the reference vector to a unit vector before scalling.

.. py:property:: reference_vector
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScaled.reference_vector
    :type: VectorGeometryToolVectorReference

    A vector being scaled.

.. py:property:: scale
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorScaled.scale
    :type: float

    A scaling multiple.


