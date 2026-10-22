AircraftExportTools
===================

.. py:class:: br.ok.core.stkobjects.AircraftExportTools

   The Aircraft Export Tools.

.. py:currentmodule:: AircraftExportTools

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AircraftExportTools.get_attitude_export_tool`
              - Return the Attitude export tool.
            * - :py:attr:`~br.ok.core.stkobjects.AircraftExportTools.get_ephemeris_stk_binary_export_tool`
              - Return an Ephemeris file of the STK Binary ephemeris type for export.
            * - :py:attr:`~br.ok.core.stkobjects.AircraftExportTools.get_ephemeris_stk_export_tool`
              - Return the ephemeris export tool.
            * - :py:attr:`~br.ok.core.stkobjects.AircraftExportTools.get_propagator_definition_export_tool`
              - Return the Prop Def export tool.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AircraftExportTools



Method detail
-------------

.. py:method:: get_attitude_export_tool(self) -> VehicleAttitudeExportTool
    :canonical: br.ok.core.stkobjects.AircraftExportTools.get_attitude_export_tool

    Return the Attitude export tool.

    :Returns:

        :obj:`~VehicleAttitudeExportTool`

.. py:method:: get_ephemeris_stk_binary_export_tool(self) -> VehicleEphemerisBinaryExportTool
    :canonical: br.ok.core.stkobjects.AircraftExportTools.get_ephemeris_stk_binary_export_tool

    Return an Ephemeris file of the STK Binary ephemeris type for export.

    :Returns:

        :obj:`~VehicleEphemerisBinaryExportTool`

.. py:method:: get_ephemeris_stk_export_tool(self) -> VehicleEphemerisExportTool
    :canonical: br.ok.core.stkobjects.AircraftExportTools.get_ephemeris_stk_export_tool

    Return the ephemeris export tool.

    :Returns:

        :obj:`~VehicleEphemerisExportTool`

.. py:method:: get_propagator_definition_export_tool(self) -> PropagatorDefinitionExportTool
    :canonical: br.ok.core.stkobjects.AircraftExportTools.get_propagator_definition_export_tool

    Return the Prop Def export tool.

    :Returns:

        :obj:`~PropagatorDefinitionExportTool`

