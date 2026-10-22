ScatteringPointProviderPlugin
=============================

.. py:class:: br.ok.core.stkobjects.ScatteringPointProviderPlugin

   Bases: :py:class:`~br.ok.core.stkobjects.IScatteringPointProvider`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a plugin scattering point provider.

.. py:currentmodule:: ScatteringPointProviderPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ScatteringPointProviderPlugin.plugin_configuration`
              - Get the plugin configuration interface.
            * - :py:attr:`~br.ok.core.stkobjects.ScatteringPointProviderPlugin.raw_plugin_object`
              - Get the raw plugin IUnknown interface.
            * - :py:attr:`~br.ok.core.stkobjects.ScatteringPointProviderPlugin.scattering_point_model`
              - Get the link/embed controller for managing the default scattering point model component.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ScatteringPointProviderPlugin


Property detail
---------------

.. py:property:: plugin_configuration
    :canonical: br.ok.core.stkobjects.ScatteringPointProviderPlugin.plugin_configuration
    :type: CommRadPluginConfiguration

    Get the plugin configuration interface.

.. py:property:: raw_plugin_object
    :canonical: br.ok.core.stkobjects.ScatteringPointProviderPlugin.raw_plugin_object
    :type: typing.Any

    Get the raw plugin IUnknown interface.

.. py:property:: scattering_point_model
    :canonical: br.ok.core.stkobjects.ScatteringPointProviderPlugin.scattering_point_model
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the default scattering point model component.


