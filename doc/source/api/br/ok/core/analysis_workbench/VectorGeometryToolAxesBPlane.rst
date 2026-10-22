VectorGeometryToolAxesBPlane
============================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   B-Plane axes using the selected target body and reference vector.

.. py:currentmodule:: VectorGeometryToolAxesBPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane.direction`
              - Specify a direction (incoming or outgoing).
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane.target_body`
              - Specify a target central body.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane.trajectory`
              - Specify a trajectory point.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolAxesBPlane


Property detail
---------------

.. py:property:: direction
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane.direction
    :type: AsymptoteDirectionType

    Specify a direction (incoming or outgoing).

.. py:property:: reference_vector
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane.reference_vector
    :type: VectorGeometryToolVectorReference

    Specify a reference vector.

.. py:property:: target_body
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane.target_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a target central body.

.. py:property:: trajectory
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesBPlane.trajectory
    :type: VectorGeometryToolPointReference

    Specify a trajectory point.


