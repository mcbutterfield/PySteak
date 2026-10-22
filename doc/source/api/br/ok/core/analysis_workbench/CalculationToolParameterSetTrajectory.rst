CalculationToolParameterSetTrajectory
=====================================

.. py:class:: br.ok.core.analysis_workbench.CalculationToolParameterSetTrajectory

   Bases: :py:class:`~br.ok.core.analysis_workbench.ICalculationToolParameterSet`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

.. py:currentmodule:: CalculationToolParameterSetTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolParameterSetTrajectory.point`
              - Get the point for which trajectory representations are computed.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolParameterSetTrajectory.reference_system`
              - Get the reference system relative to which trajectory representations are computed.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import CalculationToolParameterSetTrajectory


Property detail
---------------

.. py:property:: point
    :canonical: br.ok.core.analysis_workbench.CalculationToolParameterSetTrajectory.point
    :type: IVectorGeometryToolPoint

    Get the point for which trajectory representations are computed.

.. py:property:: reference_system
    :canonical: br.ok.core.analysis_workbench.CalculationToolParameterSetTrajectory.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system relative to which trajectory representations are computed.


