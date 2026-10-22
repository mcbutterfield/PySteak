VectorGeometryToolVectorApoapsis
================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolVectorApoapsis

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

.. py:currentmodule:: VectorGeometryToolVectorApoapsis

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorApoapsis.central_body`
              - Specify a central body.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorApoapsis.mean_element_type`
              - Specify the mean element theory type for approximating motion.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorApoapsis.reference_point`
              - Specify a reference point.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolVectorApoapsis


Property detail
---------------

.. py:property:: central_body
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorApoapsis.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: mean_element_type
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorApoapsis.mean_element_type
    :type: MeanElementTheory

    Specify the mean element theory type for approximating motion.

.. py:property:: reference_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorApoapsis.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.


