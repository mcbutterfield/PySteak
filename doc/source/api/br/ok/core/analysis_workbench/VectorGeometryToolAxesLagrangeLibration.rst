VectorGeometryToolAxesLagrangeLibration
=======================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolAxesLagrangeLibration

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

.. py:currentmodule:: VectorGeometryToolAxesLagrangeLibration

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesLagrangeLibration.point_type`
              - Specify a lagrange point (L1, L2, etc.).
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesLagrangeLibration.primary_central_body`
              - Specify a primary central body.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesLagrangeLibration.secondary_central_bodies`
              - Specify secondary central bodies.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolAxesLagrangeLibration


Property detail
---------------

.. py:property:: point_type
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesLagrangeLibration.point_type
    :type: LagrangeLibrationPointType

    Specify a lagrange point (L1, L2, etc.).

.. py:property:: primary_central_body
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesLagrangeLibration.primary_central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a primary central body.

.. py:property:: secondary_central_bodies
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesLagrangeLibration.secondary_central_bodies
    :type: AnalysisWorkbenchCentralBodyCollection

    Specify secondary central bodies.


