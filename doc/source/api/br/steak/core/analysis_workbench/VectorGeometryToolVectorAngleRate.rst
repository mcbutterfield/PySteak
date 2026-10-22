VectorGeometryToolVectorAngleRate
=================================

.. py:class:: br.steak.core.analysis_workbench.VectorGeometryToolVectorAngleRate

   Bases: :py:class:`~br.steak.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Angle rate vector perpendicular to the plane in which the angle is defined.

.. py:currentmodule:: VectorGeometryToolVectorAngleRate

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorAngleRate.angle`
              - Specify an angle. The angle vector will be perpendicular to the plane in which the angle is defined.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorAngleRate.differencing_time_step`
              - Time step used in numerical evaluation of derivatives using central differencing.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import VectorGeometryToolVectorAngleRate


Property detail
---------------

.. py:property:: angle
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorAngleRate.angle
    :type: VectorGeometryToolAngleReference

    Specify an angle. The angle vector will be perpendicular to the plane in which the angle is defined.

.. py:property:: differencing_time_step
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorAngleRate.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


