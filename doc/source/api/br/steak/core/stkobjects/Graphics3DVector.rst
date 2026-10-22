Graphics3DVector
================

.. py:class:: br.steak.core.stkobjects.Graphics3DVector

   Class defining 3D vectors.

.. py:currentmodule:: Graphics3DVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DVector.angle_size_scale`
              - The angle size scale. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DVector.scale_relative_to_model`
              - Control whether to scale the geometric elements relative to an object scale with the object's model.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DVector.vector_geometry_tool_components`
              - Get a collection that manages the 3D VGT visualizations.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DVector.vector_size_scale`
              - The size scale of the geometric elements. Dimensionless.



Examples
--------

Add a Vector to display in 3D

.. code-block:: python

    # Satellite satellite: Satellite object
    vector = satellite.graphics_3d.vector
    angVel = vector.vector_geometry_tool_components.add(0, "Satellite/MySatellite AngVelocity")
    angVel.show_label = True


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import Graphics3DVector


Property detail
---------------

.. py:property:: angle_size_scale
    :canonical: br.steak.core.stkobjects.Graphics3DVector.angle_size_scale
    :type: float

    The angle size scale. Dimensionless.

.. py:property:: scale_relative_to_model
    :canonical: br.steak.core.stkobjects.Graphics3DVector.scale_relative_to_model
    :type: bool

    Control whether to scale the geometric elements relative to an object scale with the object's model.

.. py:property:: vector_geometry_tool_components
    :canonical: br.steak.core.stkobjects.Graphics3DVector.vector_geometry_tool_components
    :type: Graphics3DReferenceVectorGeometryToolComponentCollection

    Get a collection that manages the 3D VGT visualizations.

.. py:property:: vector_size_scale
    :canonical: br.steak.core.stkobjects.Graphics3DVector.vector_size_scale
    :type: float

    The size scale of the geometric elements. Dimensionless.


