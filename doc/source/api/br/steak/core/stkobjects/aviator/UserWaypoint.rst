UserWaypoint
============

.. py:class:: br.steak.core.stkobjects.aviator.UserWaypoint

   Bases: :py:class:`~br.steak.core.stkobjects.aviator.ICatalogWaypoint`, :py:class:`~br.steak.core.stkobjects.aviator.ICatalogItem`

   Class defining the user waypoint in the Aviator catalog.

.. py:currentmodule:: UserWaypoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.UserWaypoint.copy_site`
              - Copy the site to the clipboard.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.UserWaypoint.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.UserWaypoint.paste_site`
              - Paste the site to the clipboard.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.UserWaypoint.latitude`
              - Get or set the waypoint latitude.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.UserWaypoint.longitude`
              - Get or set the waypoint longitude.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.aviator import UserWaypoint


Property detail
---------------

.. py:property:: latitude
    :canonical: br.steak.core.stkobjects.aviator.UserWaypoint.latitude
    :type: typing.Any

    Get or set the waypoint latitude.

.. py:property:: longitude
    :canonical: br.steak.core.stkobjects.aviator.UserWaypoint.longitude
    :type: typing.Any

    Get or set the waypoint longitude.


Method detail
-------------

.. py:method:: copy_site(self) -> None
    :canonical: br.steak.core.stkobjects.aviator.UserWaypoint.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: br.steak.core.stkobjects.aviator.UserWaypoint.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`





.. py:method:: paste_site(self) -> None
    :canonical: br.steak.core.stkobjects.aviator.UserWaypoint.paste_site

    Paste the site to the clipboard.

    :Returns:

        :obj:`~None`

