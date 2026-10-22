Scenario3dFont
==============

.. py:class:: br.ok.core.stkobjects.Scenario3dFont

   Font properties for Scenario 3D Graphics.

.. py:currentmodule:: Scenario3dFont

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Scenario3dFont.is_font_available`
              - Return whether the specified font is installed in the system.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Scenario3dFont.available_fonts`
              - Names of fonts installed in the system.
            * - :py:attr:`~br.ok.core.stkobjects.Scenario3dFont.bold`
              - Specify whether the font is bold.
            * - :py:attr:`~br.ok.core.stkobjects.Scenario3dFont.italic`
              - Specify whether the font is italic.
            * - :py:attr:`~br.ok.core.stkobjects.Scenario3dFont.name`
              - Get or set the font name.
            * - :py:attr:`~br.ok.core.stkobjects.Scenario3dFont.point_size`
              - Font size in points.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Scenario3dFont


Property detail
---------------

.. py:property:: available_fonts
    :canonical: br.ok.core.stkobjects.Scenario3dFont.available_fonts
    :type: list

    Names of fonts installed in the system.

.. py:property:: bold
    :canonical: br.ok.core.stkobjects.Scenario3dFont.bold
    :type: bool

    Specify whether the font is bold.

.. py:property:: italic
    :canonical: br.ok.core.stkobjects.Scenario3dFont.italic
    :type: bool

    Specify whether the font is italic.

.. py:property:: name
    :canonical: br.ok.core.stkobjects.Scenario3dFont.name
    :type: str

    Get or set the font name.

.. py:property:: point_size
    :canonical: br.ok.core.stkobjects.Scenario3dFont.point_size
    :type: Scenario3dPointSize

    Font size in points.


Method detail
-------------




.. py:method:: is_font_available(self, name: str) -> bool
    :canonical: br.ok.core.stkobjects.Scenario3dFont.is_font_available

    Return whether the specified font is installed in the system.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`







