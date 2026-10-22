PointTargetGraphics3DModel
==========================

.. py:class:: br.steak.core.stkobjects.PointTargetGraphics3DModel

   Bases: :py:class:`~br.steak.core.stkobjects.IGraphics3DModel`

   Point properties for a 3D model.

.. py:currentmodule:: PointTargetGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.PointTargetGraphics3DModel.gltf_image_based`
              - Get the glTF Image Based properties.
            * - :py:attr:`~br.steak.core.stkobjects.PointTargetGraphics3DModel.gltf_reflection_map_type`
              - Get or set the glTF reflection map type property. A member of the ModelGltfReflectionMapType enumeration.
            * - :py:attr:`~br.steak.core.stkobjects.PointTargetGraphics3DModel.marker`
              - VO Marker attributes.
            * - :py:attr:`~br.steak.core.stkobjects.PointTargetGraphics3DModel.point_size`
              - A size of the point (in pixels).
            * - :py:attr:`~br.steak.core.stkobjects.PointTargetGraphics3DModel.show_point`
              - Whether the point that is shown at certain viewing distances to represent an object, is visible.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import PointTargetGraphics3DModel


Property detail
---------------

.. py:property:: gltf_image_based
    :canonical: br.steak.core.stkobjects.PointTargetGraphics3DModel.gltf_image_based
    :type: Graphics3DModelglTFImageBased

    Get the glTF Image Based properties.

.. py:property:: gltf_reflection_map_type
    :canonical: br.steak.core.stkobjects.PointTargetGraphics3DModel.gltf_reflection_map_type
    :type: ModelGltfReflectionMapType

    Get or set the glTF reflection map type property. A member of the ModelGltfReflectionMapType enumeration.

.. py:property:: marker
    :canonical: br.steak.core.stkobjects.PointTargetGraphics3DModel.marker
    :type: Graphics3DMarker

    VO Marker attributes.

.. py:property:: point_size
    :canonical: br.steak.core.stkobjects.PointTargetGraphics3DModel.point_size
    :type: typing.Any

    A size of the point (in pixels).

.. py:property:: show_point
    :canonical: br.steak.core.stkobjects.PointTargetGraphics3DModel.show_point
    :type: bool

    Whether the point that is shown at certain viewing distances to represent an object, is visible.


