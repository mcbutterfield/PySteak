EnginePlugin
============

.. py:class:: br.steak.core.stkobjects.astrogator.EnginePlugin

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   Plugin engine model.

.. py:currentmodule:: EnginePlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EnginePlugin.g`
              - Get or set the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EnginePlugin.plugin_config`
              - Get the properties of the plugin.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EnginePlugin.plugin_identifier`
              - Get or set the PluginIdentifier - the ProgID of the COM component you are using for this model.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import EnginePlugin


Property detail
---------------

.. py:property:: g
    :canonical: br.steak.core.stkobjects.astrogator.EnginePlugin.g
    :type: float

    Get or set the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: plugin_config
    :canonical: br.steak.core.stkobjects.astrogator.EnginePlugin.plugin_config
    :type: PluginProperties

    Get the properties of the plugin.

.. py:property:: plugin_identifier
    :canonical: br.steak.core.stkobjects.astrogator.EnginePlugin.plugin_identifier
    :type: str

    Get or set the PluginIdentifier - the ProgID of the COM component you are using for this model.


