VectorGeometryToolPointPlaneProjection
======================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneProjection

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

.. py:currentmodule:: VectorGeometryToolPointPlaneProjection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneProjection.reference_plane`
              - Specify a reference plane.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneProjection.source_point`
              - Specify a source point.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolPointPlaneProjection


Property detail
---------------

.. py:property:: reference_plane
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneProjection.reference_plane
    :type: VectorGeometryToolPlaneReference

    Specify a reference plane.

.. py:property:: source_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneProjection.source_point
    :type: VectorGeometryToolPointReference

    Specify a source point.


