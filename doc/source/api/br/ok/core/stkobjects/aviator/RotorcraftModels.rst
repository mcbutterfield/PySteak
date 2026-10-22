RotorcraftModels
================

.. py:class:: br.ok.core.stkobjects.aviator.RotorcraftModels

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.ICatalogSource`

   Class defining the User Rotorcraft Models in the Aviator Catalog.

.. py:currentmodule:: RotorcraftModels

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.RotorcraftModels.add_rotorcraft`
              - Create a new rotorcraft with the given name.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.RotorcraftModels.get_as_catalog_source`
              - Get the catalog source interface for this object.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.RotorcraftModels.get_rotorcraft`
              - Get the rotorcraft with the given name.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import RotorcraftModels



Method detail
-------------

.. py:method:: add_rotorcraft(self, name: str) -> RotorcraftModel
    :canonical: br.ok.core.stkobjects.aviator.RotorcraftModels.add_rotorcraft

    Create a new rotorcraft with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~RotorcraftModel`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: br.ok.core.stkobjects.aviator.RotorcraftModels.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

.. py:method:: get_rotorcraft(self, name: str) -> RotorcraftModel
    :canonical: br.ok.core.stkobjects.aviator.RotorcraftModels.get_rotorcraft

    Get the rotorcraft with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~RotorcraftModel`

