CustomImageGlobeOverlayPluginActivator
======================================

.. py:class:: br.steak.core.graphics.CustomImageGlobeOverlayPluginActivator

   The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

.. py:currentmodule:: CustomImageGlobeOverlayPluginActivator

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlayPluginActivator.create_from_display_name`
              - Load a custom image globe overlay COM plugin associated with the specified display name and returns a proxy object that allows accessing the custom image globe overlays implemented by the plugin.
            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlayPluginActivator.get_available_display_names`
              - Get a list of available custom image globe overlay Display Names (Programmatic Identifiers).


Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import CustomImageGlobeOverlayPluginActivator



Method detail
-------------

.. py:method:: create_from_display_name(self, display_name: str) -> CustomImageGlobeOverlayPluginProxy
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlayPluginActivator.create_from_display_name

    Load a custom image globe overlay COM plugin associated with the specified display name and returns a proxy object that allows accessing the custom image globe overlays implemented by the plugin.

    :Parameters:

        **display_name** : :obj:`~str`


    :Returns:

        :obj:`~CustomImageGlobeOverlayPluginProxy`

.. py:method:: get_available_display_names(self) -> list
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlayPluginActivator.get_available_display_names

    Get a list of available custom image globe overlay Display Names (Programmatic Identifiers).

    :Returns:

        :obj:`~list`

