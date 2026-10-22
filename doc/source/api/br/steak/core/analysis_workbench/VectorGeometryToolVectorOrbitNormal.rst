VectorGeometryToolVectorOrbitNormal
===================================

.. py:class:: br.steak.core.analysis_workbench.VectorGeometryToolVectorOrbitNormal

   Bases: :py:class:`~br.steak.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

.. py:currentmodule:: VectorGeometryToolVectorOrbitNormal

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorOrbitNormal.central_body`
              - Specify a central body.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorOrbitNormal.mean_element_type`
              - Specify the mean element theory type for approximating motion.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorOrbitNormal.reference_point`
              - Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import VectorGeometryToolVectorOrbitNormal


Property detail
---------------

.. py:property:: central_body
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorOrbitNormal.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: mean_element_type
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorOrbitNormal.mean_element_type
    :type: MeanElementTheory

    Specify the mean element theory type for approximating motion.

.. py:property:: reference_point
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorOrbitNormal.reference_point
    :type: VectorGeometryToolPointReference

    Elliptical orbit is fit to the current motion of the reference point according to the selected mean theory.


