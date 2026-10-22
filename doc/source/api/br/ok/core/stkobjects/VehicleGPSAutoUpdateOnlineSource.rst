VehicleGPSAutoUpdateOnlineSource
================================

.. py:class:: br.ok.core.stkobjects.VehicleGPSAutoUpdateOnlineSource

   GPS automatic updates using online source (AGI server).

.. py:currentmodule:: VehicleGPSAutoUpdateOnlineSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGPSAutoUpdateOnlineSource.preview`
              - Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGPSAutoUpdateOnlineSource



Method detail
-------------

.. py:method:: preview(self) -> VehicleGPSElementCollection
    :canonical: br.ok.core.stkobjects.VehicleGPSAutoUpdateOnlineSource.preview

    Preview the GPS elements in the almanac. Only records associated with the current PRN are returned.

    :Returns:

        :obj:`~VehicleGPSElementCollection`

