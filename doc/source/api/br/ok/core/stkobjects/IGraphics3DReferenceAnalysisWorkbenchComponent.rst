IGraphics3DReferenceAnalysisWorkbenchComponent
==============================================

.. py:class:: br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent

   IGraphics3DReferenceAnalysisWorkbenchComponent used to access the shared properties of all 3D RefCrdn.

.. py:currentmodule:: IGraphics3DReferenceAnalysisWorkbenchComponent

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.color`
              - Color of the component.
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.name`
              - Get the name of the component.
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.show_label`
              - Is the label for the component visible?
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.type_identifier`
              - Type of component (vector, axes, angle, plane, point). A member of the GeometricElementType enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.visible`
              - Whether component is visible.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IGraphics3DReferenceAnalysisWorkbenchComponent


Property detail
---------------

.. py:property:: color
    :canonical: br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.color
    :type: Color

    Color of the component.

.. py:property:: name
    :canonical: br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.name
    :type: str

    Get the name of the component.

.. py:property:: show_label
    :canonical: br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.show_label
    :type: bool

    Is the label for the component visible?

.. py:property:: type_identifier
    :canonical: br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.type_identifier
    :type: GeometricElementType

    Type of component (vector, axes, angle, plane, point). A member of the GeometricElementType enumeration.

.. py:property:: visible
    :canonical: br.ok.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent.visible
    :type: bool

    Whether component is visible.


