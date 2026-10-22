VectorGeometryToolVectorFixedAtTimeInstant
==========================================

.. py:class:: br.steak.core.analysis_workbench.VectorGeometryToolVectorFixedAtTimeInstant

   Bases: :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.steak.core.analysis_workbench.IVectorGeometryToolVector`

   Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

.. py:currentmodule:: VectorGeometryToolVectorFixedAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorFixedAtTimeInstant.reference_axes`
              - A reference axes. Can be any VGT axes.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorFixedAtTimeInstant.reference_time_instant`
              - A reference time instant. Can be any Time event.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorFixedAtTimeInstant.source_vector`
              - A source vector. Can be any VGT vector.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import VectorGeometryToolVectorFixedAtTimeInstant


Property detail
---------------

.. py:property:: reference_axes
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorFixedAtTimeInstant.reference_axes
    :type: IVectorGeometryToolAxes

    A reference axes. Can be any VGT axes.

.. py:property:: reference_time_instant
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorFixedAtTimeInstant.reference_time_instant
    :type: ITimeToolInstant

    A reference time instant. Can be any Time event.

.. py:property:: source_vector
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorFixedAtTimeInstant.source_vector
    :type: IVectorGeometryToolVector

    A source vector. Can be any VGT vector.


