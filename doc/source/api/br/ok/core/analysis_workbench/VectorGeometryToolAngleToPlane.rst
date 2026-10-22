VectorGeometryToolAngleToPlane
==============================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolAngleToPlane

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolAngle`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   An angle between a vector and a plane.

.. py:currentmodule:: VectorGeometryToolAngleToPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAngleToPlane.reference_plane`
              - Specify a reference plane.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAngleToPlane.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAngleToPlane.signed`
              - Control whether the angle is measured as either Positive or Negative when the reference Vector is directed toward the plane's normal, or always positive.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolAngleToPlane


Property detail
---------------

.. py:property:: reference_plane
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAngleToPlane.reference_plane
    :type: VectorGeometryToolPlaneReference

    Specify a reference plane.

.. py:property:: reference_vector
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAngleToPlane.reference_vector
    :type: VectorGeometryToolVectorReference

    Specify a reference vector.

.. py:property:: signed
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAngleToPlane.signed
    :type: SignedAngleType

    Control whether the angle is measured as either Positive or Negative when the reference Vector is directed toward the plane's normal, or always positive.


