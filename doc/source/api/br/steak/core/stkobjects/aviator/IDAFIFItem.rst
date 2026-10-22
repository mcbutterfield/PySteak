IDAFIFItem
==========

.. py:class:: br.steak.core.stkobjects.aviator.IDAFIFItem

   Interface used to access the options for an DAFIF Item found in the Aviator catalog.

.. py:currentmodule:: IDAFIFItem

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.IDAFIFItem.copy_site`
              - Copy the site to the clipboard.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.IDAFIFItem.get_all_fields`
              - Get all the field names.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.IDAFIFItem.get_all_fields_and_values`
              - Get all the field names along with the corresponding value.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.IDAFIFItem.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.IDAFIFItem.get_value`
              - Get the value of the field with the given name.

Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.aviator import IDAFIFItem



Method detail
-------------

.. py:method:: copy_site(self) -> None
    :canonical: br.steak.core.stkobjects.aviator.IDAFIFItem.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: get_all_fields(self) -> list
    :canonical: br.steak.core.stkobjects.aviator.IDAFIFItem.get_all_fields

    Get all the field names.

    :Returns:

        :obj:`~list`

.. py:method:: get_all_fields_and_values(self) -> list
    :canonical: br.steak.core.stkobjects.aviator.IDAFIFItem.get_all_fields_and_values

    Get all the field names along with the corresponding value.

    :Returns:

        :obj:`~list`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: br.steak.core.stkobjects.aviator.IDAFIFItem.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

.. py:method:: get_value(self, field_name: str) -> typing.Any
    :canonical: br.steak.core.stkobjects.aviator.IDAFIFItem.get_value

    Get the value of the field with the given name.

    :Parameters:

        **field_name** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

