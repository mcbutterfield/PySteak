ProfileSearchPlugin
===================

.. py:class:: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IProfile`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The plugin search profile.

.. py:currentmodule:: ProfileSearchPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.controls`
              - Get the selected control parameters.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.log_file`
              - Name of the log file for this profile.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.plugin_config`
              - Get the properties of the selected plugin.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.plugin_identifier`
              - Get the plugin identifier.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.reset_controls_before_run`
              - Reset controls before each run.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.results`
              - Get the selected equality constraints.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.scripting_tool`
              - Return the Scripting tool for the sequence.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.targeter_graphs`
              - Graphs.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import ProfileSearchPlugin


Property detail
---------------

.. py:property:: controls
    :canonical: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.controls
    :type: SearchPluginControlCollection

    Get the selected control parameters.

.. py:property:: log_file
    :canonical: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.log_file
    :type: str

    Name of the log file for this profile.

.. py:property:: plugin_config
    :canonical: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.plugin_config
    :type: PluginProperties

    Get the properties of the selected plugin.

.. py:property:: plugin_identifier
    :canonical: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.plugin_identifier
    :type: str

    Get the plugin identifier.

.. py:property:: reset_controls_before_run
    :canonical: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: results
    :canonical: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.results
    :type: SearchPluginResultCollection

    Get the selected equality constraints.

.. py:property:: scripting_tool
    :canonical: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.scripting_tool
    :type: ScriptingTool

    Return the Scripting tool for the sequence.

.. py:property:: targeter_graphs
    :canonical: br.ok.core.stkobjects.astrogator.ProfileSearchPlugin.targeter_graphs
    :type: TargeterGraphCollection

    Graphs.


