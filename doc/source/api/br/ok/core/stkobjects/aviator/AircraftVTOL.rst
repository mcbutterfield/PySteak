AircraftVTOL
============

.. py:class:: br.ok.core.stkobjects.aviator.AircraftVTOL

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.ICatalogItem`

   Class defining the VTOL category of an Aviator aircraft.

.. py:currentmodule:: AircraftVTOL

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftVTOL.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.AircraftVTOL.get_vtol_by_name`
              - Get the VTOL model with the given name.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import AircraftVTOL



Method detail
-------------

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: br.ok.core.stkobjects.aviator.AircraftVTOL.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

.. py:method:: get_vtol_by_name(self, name: str) -> AircraftVTOLModel
    :canonical: br.ok.core.stkobjects.aviator.AircraftVTOL.get_vtol_by_name

    Get the VTOL model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftVTOLModel`

