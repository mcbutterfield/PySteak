IGraphics3DModel
================

.. py:class:: br.ok.core.stkobjects.IGraphics3DModel

   IGraphics3DModel used to access the 3D model attributes.

.. py:currentmodule:: IGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DModel.articulation`
              - Articulation property.
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DModel.detail_threshold`
              - Get the detail threshold attributes.
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DModel.model_data`
              - Get the model data property.
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DModel.model_type`
              - Get or set the model type property. A member of the ModelType enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DModel.scale_value`
              - Specify the absolute scaling value for the object. The model scale is an exponential scale. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.IGraphics3DModel.visible`
              - Display one or several models in the 3D Graphics window.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IGraphics3DModel


Property detail
---------------

.. py:property:: articulation
    :canonical: br.ok.core.stkobjects.IGraphics3DModel.articulation
    :type: Graphics3DModelArticulation

    Articulation property.

.. py:property:: detail_threshold
    :canonical: br.ok.core.stkobjects.IGraphics3DModel.detail_threshold
    :type: Graphics3DDetailThreshold

    Get the detail threshold attributes.

.. py:property:: model_data
    :canonical: br.ok.core.stkobjects.IGraphics3DModel.model_data
    :type: IGraphics3DModelData

    Get the model data property.

.. py:property:: model_type
    :canonical: br.ok.core.stkobjects.IGraphics3DModel.model_type
    :type: ModelType

    Get or set the model type property. A member of the ModelType enumeration.

.. py:property:: scale_value
    :canonical: br.ok.core.stkobjects.IGraphics3DModel.scale_value
    :type: float

    Specify the absolute scaling value for the object. The model scale is an exponential scale. Dimensionless.

.. py:property:: visible
    :canonical: br.ok.core.stkobjects.IGraphics3DModel.visible
    :type: bool

    Display one or several models in the 3D Graphics window.


