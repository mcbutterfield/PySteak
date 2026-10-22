ScreenOverlayPickResult
=======================

.. py:class:: br.steak.core.graphics.ScreenOverlayPickResult

   Describes a picked screen overlay as a result of a call to pick screen overlays.

.. py:currentmodule:: ScreenOverlayPickResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.ScreenOverlayPickResult.control_position`
              - Get the position that was picked within the overall globe control. This is essentially the same position that was passed to pick screen overlays. The array represents the picked position and has a size of 4...
            * - :py:attr:`~br.steak.core.graphics.ScreenOverlayPickResult.overlay`
              - Get the screen overlay that was picked.
            * - :py:attr:`~br.steak.core.graphics.ScreenOverlayPickResult.position`
              - Get the position that was picked within the picked overlay. The array represents the picked position and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import ScreenOverlayPickResult


Property detail
---------------

.. py:property:: control_position
    :canonical: br.steak.core.graphics.ScreenOverlayPickResult.control_position
    :type: list

    Get the position that was picked within the overall globe control. This is essentially the same position that was passed to pick screen overlays. The array represents the picked position and has a size of 4...

.. py:property:: overlay
    :canonical: br.steak.core.graphics.ScreenOverlayPickResult.overlay
    :type: IScreenOverlay

    Get the screen overlay that was picked.

.. py:property:: position
    :canonical: br.steak.core.graphics.ScreenOverlayPickResult.position
    :type: list

    Get the position that was picked within the picked overlay. The array represents the picked position and has a size of 4. The elements are in the order x position, y position, x screen overlay unit, y screen overlay unit.


