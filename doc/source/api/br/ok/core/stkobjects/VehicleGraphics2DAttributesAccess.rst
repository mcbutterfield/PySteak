VehicleGraphics2DAttributesAccess
=================================

.. py:class:: br.ok.core.stkobjects.VehicleGraphics2DAttributesAccess

   Bases: :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DAttributes`, :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DAttributesDisplayState`

   Vehicle 2D Graphics display based on access intervals.

.. py:currentmodule:: VehicleGraphics2DAttributesAccess

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesAccess.access_objects`
              - Return the collection of objects used for the access.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesAccess.during_access`
              - Return the collection of gfx attributes used during the access.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesAccess.no_access`
              - Return the collection of gfx attributes used when there is no access.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGraphics2DAttributesAccess


Property detail
---------------

.. py:property:: access_objects
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DAttributesAccess.access_objects
    :type: ObjectLinkCollection

    Return the collection of objects used for the access.

.. py:property:: during_access
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DAttributesAccess.during_access
    :type: IVehicleGraphics2DAttributesBasic

    Return the collection of gfx attributes used during the access.

.. py:property:: no_access
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DAttributesAccess.no_access
    :type: IVehicleGraphics2DAttributesBasic

    Return the collection of gfx attributes used when there is no access.


