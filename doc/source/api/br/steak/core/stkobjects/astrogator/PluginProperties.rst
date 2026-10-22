PluginProperties
================

.. py:class:: br.steak.core.stkobjects.astrogator.PluginProperties

   The plugin attitude control type.

.. py:currentmodule:: PluginProperties

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.PluginProperties.get_property`
              - Get a property.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.PluginProperties.set_property`
              - Set a property.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.PluginProperties.available_properties`
              - Return an array of all available properties.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import PluginProperties


Property detail
---------------

.. py:property:: available_properties
    :canonical: br.steak.core.stkobjects.astrogator.PluginProperties.available_properties
    :type: list

    Return an array of all available properties.


Method detail
-------------


.. py:method:: get_property(self, path: str) -> typing.Any
    :canonical: br.steak.core.stkobjects.astrogator.PluginProperties.get_property

    Get a property.

    :Parameters:

        **path** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_property(self, path: str, property_value: typing.Any) -> None
    :canonical: br.steak.core.stkobjects.astrogator.PluginProperties.set_property

    Set a property.

    :Parameters:

        **path** : :obj:`~str`

        **property_value** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

