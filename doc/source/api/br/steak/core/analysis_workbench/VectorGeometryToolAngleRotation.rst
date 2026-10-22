VectorGeometryToolAngleRotation
===============================

.. py:class:: br.steak.core.analysis_workbench.VectorGeometryToolAngleRotation

   Bases: :py:class:`~br.steak.core.analysis_workbench.IVectorGeometryToolAngle`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

.. py:currentmodule:: VectorGeometryToolAngleRotation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolAngleRotation.from_axes`
              - Specify an axes to rotate from.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolAngleRotation.reference_direction`
              - Specify a rotation direction.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolAngleRotation.to_axes`
              - Specify an axes to rotate to.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import VectorGeometryToolAngleRotation


Property detail
---------------

.. py:property:: from_axes
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolAngleRotation.from_axes
    :type: VectorGeometryToolAxesReference

    Specify an axes to rotate from.

.. py:property:: reference_direction
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolAngleRotation.reference_direction
    :type: PrincipalAxisOfRotationType

    Specify a rotation direction.

.. py:property:: to_axes
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolAngleRotation.to_axes
    :type: VectorGeometryToolAxesReference

    Specify an axes to rotate to.


