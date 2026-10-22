VectorGeometryToolAxesPlugin
============================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolAxes`

   A VGT axes plugin.

.. py:currentmodule:: VectorGeometryToolAxesPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.get_property`
              - Read a value of the specified plugin property. This method throws an exception if the property does not exist.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.reset`
              - Reset the plugin.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.set_property`
              - Set the plugin properties. This method throws an exception if the specified property does not exist, invalid value was specified or the specified property is read-only.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.available_properties`
              - An array of names of the properties that can be used to configure the plugin.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.display_name`
              - Plugin's Display Name associated with the COM plugin.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.prog_id`
              - A programmatic ID associated with the component.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolAxesPlugin


Property detail
---------------

.. py:property:: available_properties
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.available_properties
    :type: list

    An array of names of the properties that can be used to configure the plugin.

.. py:property:: display_name
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.display_name
    :type: str

    Plugin's Display Name associated with the COM plugin.

.. py:property:: prog_id
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.prog_id
    :type: str

    A programmatic ID associated with the component.


Method detail
-------------



.. py:method:: get_property(self, name: str) -> str
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.get_property

    Read a value of the specified plugin property. This method throws an exception if the property does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~str`


.. py:method:: reset(self) -> None
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.reset

    Reset the plugin.

    :Returns:

        :obj:`~None`

.. py:method:: set_property(self, name: str, value: str) -> None
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolAxesPlugin.set_property

    Set the plugin properties. This method throws an exception if the specified property does not exist, invalid value was specified or the specified property is read-only.

    :Parameters:

        **name** : :obj:`~str`

        **value** : :obj:`~str`


    :Returns:

        :obj:`~None`

