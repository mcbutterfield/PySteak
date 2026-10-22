VectorGeometryToolPointPlaneIntersection
========================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Point on a plane located along a given direction looking from a given origin.

.. py:currentmodule:: VectorGeometryToolPointPlaneIntersection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.direction_vector`
              - Specify a direction vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.origin_point`
              - Specify the origin point.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.reference_plane`
              - Specify a reference plane.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolPointPlaneIntersection


Property detail
---------------

.. py:property:: direction_vector
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.direction_vector
    :type: VectorGeometryToolVectorReference

    Specify a direction vector.

.. py:property:: origin_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.origin_point
    :type: VectorGeometryToolPointReference

    Specify the origin point.

.. py:property:: reference_plane
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection.reference_plane
    :type: VectorGeometryToolPlaneReference

    Specify a reference plane.


