Volumetric
==========

.. py:class:: br.ok.core.stkobjects.Volumetric

   Bases: :py:class:`~br.ok.core.stkobjects.ISTKObject`, :py:class:`~br.ok.core.stkobjects.ILifetimeInformation`

   The Volumetric class.

.. py:currentmodule:: Volumetric

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.clear`
              - Clear computations for Volumetric.
            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.compute`
              - Compute computations for Volumetric.
            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.compute_in_parallel`
              - Compute computations in parallel for Volumetric.
            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.get_volumetric_export_tool`
              - Volumetric export tool.
            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.set_volume_grid_definition_type`
              - Set volume grid definition type, using the VolumetricDefinitionType enumeration.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.advanced`
              - Get Advanced options.
            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.graphics_3d`
              - Get the 3D Graphics properties for the volumetric object.
            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.volume_analysis_interval`
              - Get Volume Analysis Interval.
            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.volume_grid_definition`
              - Get Volume Grid definition.
            * - :py:attr:`~br.ok.core.stkobjects.Volumetric.volume_grid_definition_type`
              - Get Volume Grid definition type. A member of the VolumetricDefinitionType enumeration.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Volumetric


Property detail
---------------

.. py:property:: advanced
    :canonical: br.ok.core.stkobjects.Volumetric.advanced
    :type: VolumetricAdvancedSettings

    Get Advanced options.

.. py:property:: graphics_3d
    :canonical: br.ok.core.stkobjects.Volumetric.graphics_3d
    :type: VolumetricGraphics3D

    Get the 3D Graphics properties for the volumetric object.

.. py:property:: volume_analysis_interval
    :canonical: br.ok.core.stkobjects.Volumetric.volume_analysis_interval
    :type: VolumetricAnalysisInterval

    Get Volume Analysis Interval.

.. py:property:: volume_grid_definition
    :canonical: br.ok.core.stkobjects.Volumetric.volume_grid_definition
    :type: IVolumetricGridDefinition

    Get Volume Grid definition.

.. py:property:: volume_grid_definition_type
    :canonical: br.ok.core.stkobjects.Volumetric.volume_grid_definition_type
    :type: VolumetricDefinitionType

    Get Volume Grid definition type. A member of the VolumetricDefinitionType enumeration.


Method detail
-------------


.. py:method:: clear(self) -> None
    :canonical: br.ok.core.stkobjects.Volumetric.clear

    Clear computations for Volumetric.

    :Returns:

        :obj:`~None`

.. py:method:: compute(self) -> None
    :canonical: br.ok.core.stkobjects.Volumetric.compute

    Compute computations for Volumetric.

    :Returns:

        :obj:`~None`

.. py:method:: compute_in_parallel(self) -> None
    :canonical: br.ok.core.stkobjects.Volumetric.compute_in_parallel

    Compute computations in parallel for Volumetric.

    :Returns:

        :obj:`~None`

.. py:method:: get_volumetric_export_tool(self) -> VolumetricExportTool
    :canonical: br.ok.core.stkobjects.Volumetric.get_volumetric_export_tool

    Volumetric export tool.

    :Returns:

        :obj:`~VolumetricExportTool`

.. py:method:: set_volume_grid_definition_type(self, vm_grid_calc_type: VolumetricDefinitionType) -> None
    :canonical: br.ok.core.stkobjects.Volumetric.set_volume_grid_definition_type

    Set volume grid definition type, using the VolumetricDefinitionType enumeration.

    :Parameters:

        **vm_grid_calc_type** : :obj:`~VolumetricDefinitionType`


    :Returns:

        :obj:`~None`





