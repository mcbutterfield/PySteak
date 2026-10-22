Graphics3DOffsetLabel
=====================

.. py:class:: br.ok.core.stkobjects.Graphics3DOffsetLabel

   Class defining the offset of the position of an object label in the 3D Graphics window.

.. py:currentmodule:: Graphics3DOffsetLabel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DOffsetLabel.enable`
              - Offset the position of an object label in the 3D Graphics window.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DOffsetLabel.offset_frame`
              - The frame used in computing the offset. A member of the OffsetFrameType enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DOffsetLabel.x`
              - X value of the offset, where positive and negative values move the label to the right and left, respectively. Dimension depends on context.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DOffsetLabel.y`
              - The Y value of the offset, where positive and negative values move the label up and down, respectively. Dimension depends on context.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DOffsetLabel.z`
              - The Z value of the offset, used only when the offset frame is Cartesian, where positive and negative values move the label out of and into the screen, respectively. Uses SmallDistanceUnit Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Graphics3DOffsetLabel


Property detail
---------------

.. py:property:: enable
    :canonical: br.ok.core.stkobjects.Graphics3DOffsetLabel.enable
    :type: bool

    Offset the position of an object label in the 3D Graphics window.

.. py:property:: offset_frame
    :canonical: br.ok.core.stkobjects.Graphics3DOffsetLabel.offset_frame
    :type: OffsetFrameType

    The frame used in computing the offset. A member of the OffsetFrameType enumeration.

.. py:property:: x
    :canonical: br.ok.core.stkobjects.Graphics3DOffsetLabel.x
    :type: float

    X value of the offset, where positive and negative values move the label to the right and left, respectively. Dimension depends on context.

.. py:property:: y
    :canonical: br.ok.core.stkobjects.Graphics3DOffsetLabel.y
    :type: float

    The Y value of the offset, where positive and negative values move the label up and down, respectively. Dimension depends on context.

.. py:property:: z
    :canonical: br.ok.core.stkobjects.Graphics3DOffsetLabel.z
    :type: float

    The Z value of the offset, used only when the offset frame is Cartesian, where positive and negative values move the label out of and into the screen, respectively. Uses SmallDistanceUnit Dimension.


