TextOverlay
===========

.. py:class:: br.steak.core.graphics.TextOverlay

   Bases: :py:class:`~br.steak.core.graphics.IScreenOverlay`, :py:class:`~br.steak.core.graphics.IOverlay`, :py:class:`~br.steak.core.graphics.IScreenOverlayContainer`

   A rectangular overlay that contains text.

.. py:currentmodule:: TextOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.TextOverlay.font`
              - Get or set the graphics font used to style the text.
            * - :py:attr:`~br.steak.core.graphics.TextOverlay.outline_color`
              - Get or set the text's outline color.
            * - :py:attr:`~br.steak.core.graphics.TextOverlay.text`
              - Get or set the text to be rendered to an overlay. Newline characters ('\n') will mark the start of the next line in the text.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import TextOverlay


Property detail
---------------

.. py:property:: font
    :canonical: br.steak.core.graphics.TextOverlay.font
    :type: GraphicsFont

    Get or set the graphics font used to style the text.

.. py:property:: outline_color
    :canonical: br.steak.core.graphics.TextOverlay.outline_color
    :type: Color

    Get or set the text's outline color.

.. py:property:: text
    :canonical: br.steak.core.graphics.TextOverlay.text
    :type: str

    Get or set the text to be rendered to an overlay. Newline characters ('\n') will mark the start of the next line in the text.


