CoverageBoundsCustomBoundary
============================

.. py:class:: br.steak.core.stkobjects.CoverageBoundsCustomBoundary

   Bases: :py:class:`~br.steak.core.stkobjects.ICoverageBounds`

   Custom Boundary.

.. py:currentmodule:: CoverageBoundsCustomBoundary

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.CoverageBoundsCustomBoundary.boundary_objects`
              - A list of STK Objects to be used as part of the coverage area.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageBoundsCustomBoundary.region_files`
              - File containing user-defined points defining a specific grid region.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import CoverageBoundsCustomBoundary


Property detail
---------------

.. py:property:: boundary_objects
    :canonical: br.steak.core.stkobjects.CoverageBoundsCustomBoundary.boundary_objects
    :type: ObjectLinkCollection

    A list of STK Objects to be used as part of the coverage area.

.. py:property:: region_files
    :canonical: br.steak.core.stkobjects.CoverageBoundsCustomBoundary.region_files
    :type: CoverageRegionFilesCollection

    File containing user-defined points defining a specific grid region.


