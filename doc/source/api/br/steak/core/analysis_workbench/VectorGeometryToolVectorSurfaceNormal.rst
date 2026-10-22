VectorGeometryToolVectorSurfaceNormal
=====================================

.. py:class:: br.steak.core.analysis_workbench.VectorGeometryToolVectorSurfaceNormal

   Bases: :py:class:`~br.steak.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`

   The normal vector for the surface of a central body at a sub-point obtained using the geodetic projection of the selected point onto the central body.

.. py:currentmodule:: VectorGeometryToolVectorSurfaceNormal

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorSurfaceNormal.central_body`
              - Specify the central body.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorSurfaceNormal.reference_point`
              - Specify a reference point.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorSurfaceNormal.use_terrain`
              - Whether or not to compute the normal using local terrain sources.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import VectorGeometryToolVectorSurfaceNormal


Property detail
---------------

.. py:property:: central_body
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorSurfaceNormal.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify the central body.

.. py:property:: reference_point
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorSurfaceNormal.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.

.. py:property:: use_terrain
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorSurfaceNormal.use_terrain
    :type: bool

    Whether or not to compute the normal using local terrain sources.


