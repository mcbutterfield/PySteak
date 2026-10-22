MTOGraphics3DModel
==================

.. py:class:: br.ok.core.stkobjects.MTOGraphics3DModel

   MTO track model options.

.. py:currentmodule:: MTOGraphics3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.MTOGraphics3DModel.articulation`
              - Configures the model articulations.
            * - :py:attr:`~br.ok.core.stkobjects.MTOGraphics3DModel.file_path`
              - Get the full path and file name of the track model file.
            * - :py:attr:`~br.ok.core.stkobjects.MTOGraphics3DModel.filename`
              - Get or set the name of the track model file.
            * - :py:attr:`~br.ok.core.stkobjects.MTOGraphics3DModel.initial_bearing`
              - Get or set the initial bearing of the model, relative to north. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.MTOGraphics3DModel.scale_value`
              - Get or set the exponential scaling value for the track model.
            * - :py:attr:`~br.ok.core.stkobjects.MTOGraphics3DModel.show_graphics`
              - Opt whether to use a model to represent the track in the 3D Graphics window.
            * - :py:attr:`~br.ok.core.stkobjects.MTOGraphics3DModel.z_points_nadir`
              - Opt whether to have the Z axis point to nadir (to orient it as an aircraft) or not (to orient it as a surface vehicle).



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import MTOGraphics3DModel


Property detail
---------------

.. py:property:: articulation
    :canonical: br.ok.core.stkobjects.MTOGraphics3DModel.articulation
    :type: MTOGraphics3DModelArticulation

    Configures the model articulations.

.. py:property:: file_path
    :canonical: br.ok.core.stkobjects.MTOGraphics3DModel.file_path
    :type: str

    Get the full path and file name of the track model file.

.. py:property:: filename
    :canonical: br.ok.core.stkobjects.MTOGraphics3DModel.filename
    :type: str

    Get or set the name of the track model file.

.. py:property:: initial_bearing
    :canonical: br.ok.core.stkobjects.MTOGraphics3DModel.initial_bearing
    :type: float

    Get or set the initial bearing of the model, relative to north. Uses Angle Dimension.

.. py:property:: scale_value
    :canonical: br.ok.core.stkobjects.MTOGraphics3DModel.scale_value
    :type: float

    Get or set the exponential scaling value for the track model.

.. py:property:: show_graphics
    :canonical: br.ok.core.stkobjects.MTOGraphics3DModel.show_graphics
    :type: bool

    Opt whether to use a model to represent the track in the 3D Graphics window.

.. py:property:: z_points_nadir
    :canonical: br.ok.core.stkobjects.MTOGraphics3DModel.z_points_nadir
    :type: bool

    Opt whether to have the Z axis point to nadir (to orient it as an aircraft) or not (to orient it as a surface vehicle).


