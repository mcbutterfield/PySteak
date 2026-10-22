VectorGeometryToolVectorReflection
==================================

.. py:class:: br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection

   Bases: :py:class:`~br.steak.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Incident vector reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

.. py:currentmodule:: VectorGeometryToolVectorReflection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.allow_reflections_on_backside`
              - Control whether to reflect the indicent vector on both sides of the plane.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.incoming_vector`
              - The reflecting vector.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.normal_vector`
              - The vector defines the reflection surface.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.scale_factor`
              - The vector's scale factor.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.use_opposite_of_selected_vector`
              - When set to false, resets the direction of the Incident Vector to default.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import VectorGeometryToolVectorReflection


Property detail
---------------

.. py:property:: allow_reflections_on_backside
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.allow_reflections_on_backside
    :type: bool

    Control whether to reflect the indicent vector on both sides of the plane.

.. py:property:: incoming_vector
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.incoming_vector
    :type: VectorGeometryToolVectorReference

    The reflecting vector.

.. py:property:: normal_vector
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.normal_vector
    :type: VectorGeometryToolVectorReference

    The vector defines the reflection surface.

.. py:property:: scale_factor
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.scale_factor
    :type: float

    The vector's scale factor.

.. py:property:: use_opposite_of_selected_vector
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorReflection.use_opposite_of_selected_vector
    :type: bool

    When set to false, resets the direction of the Incident Vector to default.


