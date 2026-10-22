ScriptingTool
=============

.. py:class:: br.steak.core.stkobjects.astrogator.ScriptingTool

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Scripting Tool.

.. py:currentmodule:: ScriptingTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.copy_to_clipboard`
              - Copy entire scripting tool to clipboard.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.paste_from_clipboard`
              - Replace entire scripting tool with scripting tool in clipboard.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.script_text`
              - Injects the script into the scripting tool.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.calculation_objects`
              - Return the collection of the calculation objects.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.enable`
              - If true, the scripting tool is enabled.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.language_type`
              - Get or set the scripting language being used.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.parameters`
              - Return the collection of parameters.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.pre_iterate`
              - If true, the sequence will run once before executing the script.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ScriptingTool.segment_properties`
              - Return the collection of the segment properties.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import ScriptingTool


Property detail
---------------

.. py:property:: calculation_objects
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.calculation_objects
    :type: ScriptingCalculationObjectCollection

    Return the collection of the calculation objects.

.. py:property:: enable
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.enable
    :type: bool

    If true, the scripting tool is enabled.

.. py:property:: language_type
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.language_type
    :type: Language

    Get or set the scripting language being used.

.. py:property:: parameters
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.parameters
    :type: ScriptingParameterCollection

    Return the collection of parameters.

.. py:property:: pre_iterate
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.pre_iterate
    :type: bool

    If true, the sequence will run once before executing the script.

.. py:property:: segment_properties
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.segment_properties
    :type: ScriptingSegmentCollection

    Return the collection of the segment properties.


Method detail
-------------


.. py:method:: copy_to_clipboard(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.copy_to_clipboard

    Copy entire scripting tool to clipboard.

    :Returns:

        :obj:`~None`






.. py:method:: paste_from_clipboard(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.paste_from_clipboard

    Replace entire scripting tool with scripting tool in clipboard.

    :Returns:

        :obj:`~None`



.. py:method:: script_text(self, script: str) -> None
    :canonical: br.steak.core.stkobjects.astrogator.ScriptingTool.script_text

    Injects the script into the scripting tool.

    :Parameters:

        **script** : :obj:`~str`


    :Returns:

        :obj:`~None`


