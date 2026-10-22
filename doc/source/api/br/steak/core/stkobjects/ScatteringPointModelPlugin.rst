ScatteringPointModelPlugin
==========================

.. py:class:: br.steak.core.stkobjects.ScatteringPointModelPlugin

   Bases: :py:class:`~br.steak.core.stkobjects.IScatteringPointModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a plugin scattering point model.

.. py:currentmodule:: ScatteringPointModelPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ScatteringPointModelPlugin.plugin_configuration`
              - Get the plugin configuration interface.
            * - :py:attr:`~br.steak.core.stkobjects.ScatteringPointModelPlugin.raw_plugin_object`
              - Get the raw plugin IUnknown interface.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ScatteringPointModelPlugin


Property detail
---------------

.. py:property:: plugin_configuration
    :canonical: br.steak.core.stkobjects.ScatteringPointModelPlugin.plugin_configuration
    :type: CommRadPluginConfiguration

    Get the plugin configuration interface.

.. py:property:: raw_plugin_object
    :canonical: br.steak.core.stkobjects.ScatteringPointModelPlugin.raw_plugin_object
    :type: typing.Any

    Get the raw plugin IUnknown interface.


