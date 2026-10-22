IProvideSpatialInfo
===================

.. py:class:: br.ok.core.stkobjects.IProvideSpatialInfo

   Provide methods for accessing spatial information for an object.

.. py:currentmodule:: IProvideSpatialInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IProvideSpatialInfo.get_spatial_information`
              - Return the spatial information for an object.

Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IProvideSpatialInfo



Method detail
-------------

.. py:method:: get_spatial_information(self, recycle: bool) -> VehicleSpatialInformation
    :canonical: br.ok.core.stkobjects.IProvideSpatialInfo.get_spatial_information

    Return the spatial information for an object.

    :Parameters:

        **recycle** : :obj:`~bool`


    :Returns:

        :obj:`~VehicleSpatialInformation`

