VectorGeometryToolAxesTrajectory
================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolAxesTrajectory

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Axes based on trajectory of the point relative to the reference coordinate system.

.. py:currentmodule:: VectorGeometryToolAxesTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesTrajectory.reference_system`
              - Specify a reference system.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesTrajectory.trajectory_axes_type`
              - Specify a type of the trajectory's coordinate frame.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesTrajectory.trajectory_point`
              - Specify a trajectory point.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolAxesTrajectory


Property detail
---------------

.. py:property:: reference_system
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesTrajectory.reference_system
    :type: VectorGeometryToolSystemReference

    Specify a reference system.

.. py:property:: trajectory_axes_type
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesTrajectory.trajectory_axes_type
    :type: TrajectoryAxesCoordinatesType

    Specify a type of the trajectory's coordinate frame.

.. py:property:: trajectory_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesTrajectory.trajectory_point
    :type: VectorGeometryToolPointReference

    Specify a trajectory point.


