SpatialAnalysisToolCalculationDistanceToLocation
================================================

.. py:class:: br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation

   Bases: :py:class:`~br.ok.core.analysis_workbench.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume calc distance to location interface.

.. py:currentmodule:: SpatialAnalysisToolCalculationDistanceToLocation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.along_vector`
              - The Volume Calc Range Along Vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.distance`
              - The Volume Calc range distance types.
            * - :py:attr:`~br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.reference_plane`
              - The Volume Calc Range reference plane.
            * - :py:attr:`~br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.reference_point`
              - The Volume Calc Range reference point.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import SpatialAnalysisToolCalculationDistanceToLocation


Property detail
---------------

.. py:property:: along_vector
    :canonical: br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.along_vector
    :type: IVectorGeometryToolVector

    The Volume Calc Range Along Vector.

.. py:property:: distance
    :canonical: br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.distance
    :type: DistanceToLocationType

    The Volume Calc range distance types.

.. py:property:: reference_plane
    :canonical: br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.reference_plane
    :type: IVectorGeometryToolPlane

    The Volume Calc Range reference plane.

.. py:property:: reference_point
    :canonical: br.ok.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.reference_point
    :type: IVectorGeometryToolPoint

    The Volume Calc Range reference point.


