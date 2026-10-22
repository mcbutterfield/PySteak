ProfileScriptingTool
====================

.. py:class:: br.ok.core.stkobjects.astrogator.ProfileScriptingTool

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IProfile`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Scripting Tool profile.

.. py:currentmodule:: ProfileScriptingTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileScriptingTool.copy_to_clipboard`
              - Copy entire scripting tool to clipboard.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileScriptingTool.paste_from_clipboard`
              - Replace entire scripting tool with scripting tool in clipboard.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileScriptingTool.script_text`
              - Injects the script into the scripting tool.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileScriptingTool.calculation_objects`
              - Return the collection of the calc objects.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileScriptingTool.enable`
              - If true, the scripting tool will be used.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileScriptingTool.language_type`
              - Get or set the scripting language being used.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileScriptingTool.parameters`
              - Return the collection of parameters.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileScriptingTool.segment_properties`
              - Return the collection of the segment properties.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import ProfileScriptingTool


Property detail
---------------

.. py:property:: calculation_objects
    :canonical: br.ok.core.stkobjects.astrogator.ProfileScriptingTool.calculation_objects
    :type: ScriptingCalculationObjectCollection

    Return the collection of the calc objects.

.. py:property:: enable
    :canonical: br.ok.core.stkobjects.astrogator.ProfileScriptingTool.enable
    :type: bool

    If true, the scripting tool will be used.

.. py:property:: language_type
    :canonical: br.ok.core.stkobjects.astrogator.ProfileScriptingTool.language_type
    :type: Language

    Get or set the scripting language being used.

.. py:property:: parameters
    :canonical: br.ok.core.stkobjects.astrogator.ProfileScriptingTool.parameters
    :type: ScriptingParameterCollection

    Return the collection of parameters.

.. py:property:: segment_properties
    :canonical: br.ok.core.stkobjects.astrogator.ProfileScriptingTool.segment_properties
    :type: ScriptingSegmentCollection

    Return the collection of the segment properties.


Method detail
-------------


.. py:method:: copy_to_clipboard(self) -> None
    :canonical: br.ok.core.stkobjects.astrogator.ProfileScriptingTool.copy_to_clipboard

    Copy entire scripting tool to clipboard.

    :Returns:

        :obj:`~None`






.. py:method:: paste_from_clipboard(self) -> None
    :canonical: br.ok.core.stkobjects.astrogator.ProfileScriptingTool.paste_from_clipboard

    Replace entire scripting tool with scripting tool in clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: script_text(self, script: str) -> None
    :canonical: br.ok.core.stkobjects.astrogator.ProfileScriptingTool.script_text

    Injects the script into the scripting tool.

    :Parameters:

        **script** : :obj:`~str`


    :Returns:

        :obj:`~None`


