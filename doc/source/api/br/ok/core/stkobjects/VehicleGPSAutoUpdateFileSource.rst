VehicleGPSAutoUpdateFileSource
==============================

.. py:class:: br.ok.core.stkobjects.VehicleGPSAutoUpdateFileSource

   GPS automatic updates using almanac file(s).

.. py:currentmodule:: VehicleGPSAutoUpdateFileSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGPSAutoUpdateFileSource.preview`
              - Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGPSAutoUpdateFileSource.filename`
              - Get or set the name of the source file.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGPSAutoUpdateFileSource


Property detail
---------------

.. py:property:: filename
    :canonical: br.ok.core.stkobjects.VehicleGPSAutoUpdateFileSource.filename
    :type: str

    Get or set the name of the source file.


Method detail
-------------



.. py:method:: preview(self) -> VehicleGPSElementCollection
    :canonical: br.ok.core.stkobjects.VehicleGPSAutoUpdateFileSource.preview

    Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    :Returns:

        :obj:`~VehicleGPSElementCollection`

