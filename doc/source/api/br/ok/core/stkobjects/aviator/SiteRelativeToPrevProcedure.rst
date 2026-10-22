SiteRelativeToPrevProcedure
===========================

.. py:class:: br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure

   Bases: :py:class:`~br.ok.core.stkobjects.aviator.ISite`

   Class defining a Relative to Previous Procedure site.

.. py:currentmodule:: SiteRelativeToPrevProcedure

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure.bearing`
              - Get or set the bearing to define the site.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure.bearing_mode`
              - Get or set the bearing reference.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure.range`
              - Get or set the range from the previous procedure.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import SiteRelativeToPrevProcedure


Property detail
---------------

.. py:property:: bearing
    :canonical: br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure.bearing
    :type: typing.Any

    Get or set the bearing to define the site.

.. py:property:: bearing_mode
    :canonical: br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure.bearing_mode
    :type: RelativeAbsoluteBearing

    Get or set the bearing reference.

.. py:property:: range
    :canonical: br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure.range
    :type: float

    Get or set the range from the previous procedure.


Method detail
-------------





.. py:method:: get_as_site(self) -> ISite
    :canonical: br.ok.core.stkobjects.aviator.SiteRelativeToPrevProcedure.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`



