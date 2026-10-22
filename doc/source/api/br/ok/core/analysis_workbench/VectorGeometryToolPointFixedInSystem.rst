VectorGeometryToolPointFixedInSystem
====================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolPointFixedInSystem

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Point fixed in a reference coordinate system using the selected coordinate type.

.. py:currentmodule:: VectorGeometryToolPointFixedInSystem

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointFixedInSystem.fixed_point`
              - Specify the point's position. The position is relative with respect to the specified reference system.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolPointFixedInSystem.reference`
              - Specify a reference system.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolPointFixedInSystem


Property detail
---------------

.. py:property:: fixed_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointFixedInSystem.fixed_point
    :type: IPosition

    Specify the point's position. The position is relative with respect to the specified reference system.

.. py:property:: reference
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolPointFixedInSystem.reference
    :type: VectorGeometryToolSystemReference

    Specify a reference system.


