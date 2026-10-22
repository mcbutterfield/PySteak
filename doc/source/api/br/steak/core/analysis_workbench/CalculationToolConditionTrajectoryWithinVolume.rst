CalculationToolConditionTrajectoryWithinVolume
==============================================

.. py:class:: br.steak.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume

   Bases: :py:class:`~br.steak.core.analysis_workbench.ICalculationToolCondition`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by determining if input trajectory point is within extents of specified volume grid coordinate.

.. py:currentmodule:: CalculationToolConditionTrajectoryWithinVolume

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume.constraint`
              - Get the volume constraint on trajectory point.
            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume.point`
              - Get the trajectory point from the condition.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import CalculationToolConditionTrajectoryWithinVolume


Property detail
---------------

.. py:property:: constraint
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on trajectory point.

.. py:property:: point
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume.point
    :type: IVectorGeometryToolPoint

    Get the trajectory point from the condition.


