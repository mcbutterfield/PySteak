SiteSTKStaticObject
===================

.. py:class:: br.steak.core.stkobjects.aviator.SiteSTKStaticObject

   Bases: :py:class:`~br.steak.core.stkobjects.aviator.ISite`

   Class defining a STK Static Object site.

.. py:currentmodule:: SiteSTKStaticObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.SiteSTKStaticObject.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.SiteSTKStaticObject.object_name`
              - Get or set the object name to link to.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.SiteSTKStaticObject.valid_object_names`
              - Return the valid object names.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.aviator import SiteSTKStaticObject


Property detail
---------------

.. py:property:: object_name
    :canonical: br.steak.core.stkobjects.aviator.SiteSTKStaticObject.object_name
    :type: str

    Get or set the object name to link to.

.. py:property:: valid_object_names
    :canonical: br.steak.core.stkobjects.aviator.SiteSTKStaticObject.valid_object_names
    :type: list

    Return the valid object names.


Method detail
-------------

.. py:method:: get_as_site(self) -> ISite
    :canonical: br.steak.core.stkobjects.aviator.SiteSTKStaticObject.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`




