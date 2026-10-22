VectorGeometryToolPointAtTimeInstant
====================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolPointAtTimeInstant

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolPoint`

   Point fixed relative to reference system based on another point evaluated at specified time instant.

.. py:currentmodule:: VectorGeometryToolPointAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointAtTimeInstant.reference_system`
              - A reference system. Can be any VGT system.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointAtTimeInstant.reference_time_instant`
              - A reference time instant. Can be any Time event.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointAtTimeInstant.source_point`
              - A source point. Can be any VGT point.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolPointAtTimeInstant


Property detail
---------------

.. py:property:: reference_system
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointAtTimeInstant.reference_system
    :type: IVectorGeometryToolSystem

    A reference system. Can be any VGT system.

.. py:property:: reference_time_instant
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointAtTimeInstant.reference_time_instant
    :type: ITimeToolInstant

    A reference time instant. Can be any Time event.

.. py:property:: source_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointAtTimeInstant.source_point
    :type: IVectorGeometryToolPoint

    A source point. Can be any VGT point.


