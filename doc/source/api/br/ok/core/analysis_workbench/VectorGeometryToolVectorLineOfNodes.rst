VectorGeometryToolVectorLineOfNodes
===================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolVectorLineOfNodes

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

.. py:currentmodule:: VectorGeometryToolVectorLineOfNodes

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorLineOfNodes.central_body`
              - Specify a central body.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorLineOfNodes.reference_point`
              - Specify a reference point.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolVectorLineOfNodes


Property detail
---------------

.. py:property:: central_body
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorLineOfNodes.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: reference_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorLineOfNodes.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.


