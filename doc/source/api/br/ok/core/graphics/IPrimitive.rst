IPrimitive
==========

.. py:class:: br.ok.core.graphics.IPrimitive

   Primitives represent objects rendered in the 3D scene.

.. py:currentmodule:: IPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.IPrimitive.automatically_compute_bounding_sphere`
              - Get or set if the primitive's bounding sphere is automatically computed.
            * - :py:attr:`~br.ok.core.graphics.IPrimitive.bounding_sphere`
              - Get or set the bounding sphere that encompasses the primitive. The center is defined in the primitive's reference frame.
            * - :py:attr:`~br.ok.core.graphics.IPrimitive.color`
              - Get or set the primitive's color.
            * - :py:attr:`~br.ok.core.graphics.IPrimitive.display`
              - Get or set if the primitive should be rendered. Both this and display condition must evaluate to true for the primitive to be rendered.
            * - :py:attr:`~br.ok.core.graphics.IPrimitive.display_condition`
              - Get or set the display condition that determines if the primitive should be rendered. Both this and display must evaluate to true for the primitive to be rendered.
            * - :py:attr:`~br.ok.core.graphics.IPrimitive.reference_frame`
              - Get or set the reference frame this primitive is defined and rendered in.
            * - :py:attr:`~br.ok.core.graphics.IPrimitive.tag`
              - Get or set custom value associated with this primitive.
            * - :py:attr:`~br.ok.core.graphics.IPrimitive.translucency`
              - Get or set the primitive's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import IPrimitive


Property detail
---------------

.. py:property:: automatically_compute_bounding_sphere
    :canonical: br.ok.core.graphics.IPrimitive.automatically_compute_bounding_sphere
    :type: bool

    Get or set if the primitive's bounding sphere is automatically computed.

.. py:property:: bounding_sphere
    :canonical: br.ok.core.graphics.IPrimitive.bounding_sphere
    :type: BoundingSphere

    Get or set the bounding sphere that encompasses the primitive. The center is defined in the primitive's reference frame.

.. py:property:: color
    :canonical: br.ok.core.graphics.IPrimitive.color
    :type: Color

    Get or set the primitive's color.

.. py:property:: display
    :canonical: br.ok.core.graphics.IPrimitive.display
    :type: bool

    Get or set if the primitive should be rendered. Both this and display condition must evaluate to true for the primitive to be rendered.

.. py:property:: display_condition
    :canonical: br.ok.core.graphics.IPrimitive.display_condition
    :type: IDisplayCondition

    Get or set the display condition that determines if the primitive should be rendered. Both this and display must evaluate to true for the primitive to be rendered.

.. py:property:: reference_frame
    :canonical: br.ok.core.graphics.IPrimitive.reference_frame
    :type: IVectorGeometryToolSystem

    Get or set the reference frame this primitive is defined and rendered in.

.. py:property:: tag
    :canonical: br.ok.core.graphics.IPrimitive.tag
    :type: typing.Any

    Get or set custom value associated with this primitive.

.. py:property:: translucency
    :canonical: br.ok.core.graphics.IPrimitive.translucency
    :type: float

    Get or set the primitive's translucency. Translucency is between 0 and 1, where 0 is opaque and 1 is transparent.


