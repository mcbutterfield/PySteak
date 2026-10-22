AttitudeControlFinitePlugin
===========================

.. py:class:: br.steak.core.stkobjects.astrogator.AttitudeControlFinitePlugin

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~br.steak.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~br.steak.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The plugin attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFinitePlugin

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFinitePlugin.select_plugin_by_name`
              - Select plugin using the plugin name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFinitePlugin.plugin_config`
              - Get the properties of the selected plugin.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFinitePlugin.plugin_name`
              - Get the selected plugin's name.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import AttitudeControlFinitePlugin


Property detail
---------------

.. py:property:: plugin_config
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFinitePlugin.plugin_config
    :type: PluginProperties

    Get the properties of the selected plugin.

.. py:property:: plugin_name
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFinitePlugin.plugin_name
    :type: str

    Get the selected plugin's name.


Method detail
-------------



.. py:method:: select_plugin_by_name(self, name: str) -> None
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFinitePlugin.select_plugin_by_name

    Select plugin using the plugin name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`

