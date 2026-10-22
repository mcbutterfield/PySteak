GraphicsFont
============

.. py:class:: br.ok.core.graphics.GraphicsFont

   A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

.. py:currentmodule:: GraphicsFont

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.antialias`
              - Get a value that indicates whether this font is antialiased.
            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.bold`
              - Get a value that indicates whether this font is bold.
            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.italic`
              - Get a value that indicates whether this font is italic.
            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.name`
              - Get the typeface name of the font.
            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.outline`
              - Get a value that indicates whether this font has an outline around its characters.
            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.size`
              - Get the size of the font.
            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.strikeout`
              - Get a value that indicates whether this font has a horizontal line through its characters.
            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.style`
              - Get the font style enumeration that contains the style for this font. This does not include the outline property.
            * - :py:attr:`~br.ok.core.graphics.GraphicsFont.underline`
              - Get a value that indicates whether this font is underlined.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import GraphicsFont


Property detail
---------------

.. py:property:: antialias
    :canonical: br.ok.core.graphics.GraphicsFont.antialias
    :type: bool

    Get a value that indicates whether this font is antialiased.

.. py:property:: bold
    :canonical: br.ok.core.graphics.GraphicsFont.bold
    :type: bool

    Get a value that indicates whether this font is bold.

.. py:property:: italic
    :canonical: br.ok.core.graphics.GraphicsFont.italic
    :type: bool

    Get a value that indicates whether this font is italic.

.. py:property:: name
    :canonical: br.ok.core.graphics.GraphicsFont.name
    :type: str

    Get the typeface name of the font.

.. py:property:: outline
    :canonical: br.ok.core.graphics.GraphicsFont.outline
    :type: bool

    Get a value that indicates whether this font has an outline around its characters.

.. py:property:: size
    :canonical: br.ok.core.graphics.GraphicsFont.size
    :type: int

    Get the size of the font.

.. py:property:: strikeout
    :canonical: br.ok.core.graphics.GraphicsFont.strikeout
    :type: bool

    Get a value that indicates whether this font has a horizontal line through its characters.

.. py:property:: style
    :canonical: br.ok.core.graphics.GraphicsFont.style
    :type: FontStyle

    Get the font style enumeration that contains the style for this font. This does not include the outline property.

.. py:property:: underline
    :canonical: br.ok.core.graphics.GraphicsFont.underline
    :type: bool

    Get a value that indicates whether this font is underlined.


