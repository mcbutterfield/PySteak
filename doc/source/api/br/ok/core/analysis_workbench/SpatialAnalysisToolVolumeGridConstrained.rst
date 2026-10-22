SpatialAnalysisToolVolumeGridConstrained
========================================

.. py:class:: br.ok.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained

   Bases: :py:class:`~br.ok.core.analysis_workbench.ISpatialAnalysisToolVolumeGrid`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume grid constrained interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained.constraint`
              - Get the volume constraint on the grid.
            * - :py:attr:`~br.ok.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained.reference_grid`
              - Get the reference system in which spherical parameters are computed.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import SpatialAnalysisToolVolumeGridConstrained


Property detail
---------------

.. py:property:: constraint
    :canonical: br.ok.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on the grid.

.. py:property:: reference_grid
    :canonical: br.ok.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained.reference_grid
    :type: ISpatialAnalysisToolVolumeGrid

    Get the reference system in which spherical parameters are computed.


