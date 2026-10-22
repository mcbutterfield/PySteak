VectorGeometryToolVectorSurfaceDisplacement
===========================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector`

   Displacement between origin and destination points using surface distance and altitude difference.

.. py:currentmodule:: VectorGeometryToolVectorSurfaceDisplacement

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement.destination_point`
              - Destination point.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement.differencing_time_step`
              - Time step used in displacement on surface vector. (derivatives using central differencing).
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement.origin_point`
              - An origin point.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement.surface_central_body`
              - Get or set the surface central body property.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolVectorSurfaceDisplacement


Property detail
---------------

.. py:property:: destination_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement.destination_point
    :type: IVectorGeometryToolPoint

    Destination point.

.. py:property:: differencing_time_step
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement.differencing_time_step
    :type: float

    Time step used in displacement on surface vector. (derivatives using central differencing).

.. py:property:: origin_point
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement.origin_point
    :type: IVectorGeometryToolPoint

    An origin point.

.. py:property:: surface_central_body
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement.surface_central_body
    :type: str

    Get or set the surface central body property.


