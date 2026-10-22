Constellation
=============

.. py:class:: br.ok.core.stkobjects.Constellation

   Bases: :py:class:`~br.ok.core.stkobjects.ISTKObject`, :py:class:`~br.ok.core.stkobjects.ILifetimeInformation`

   Class represents the STK Constellation.

.. py:currentmodule:: Constellation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Constellation.constraints`
              - Get the constellation's constraints.
            * - :py:attr:`~br.ok.core.stkobjects.Constellation.graphics`
              - Constellation's 2D graphics settings.
            * - :py:attr:`~br.ok.core.stkobjects.Constellation.objects`
              - Get the collection of objects in the chain.
            * - :py:attr:`~br.ok.core.stkobjects.Constellation.routing`
              - Constellation's routing settings.



Examples
--------

Define a constellation

.. code-block:: python

    # STKObjectRoot root: STK Object Model Root
    # Satellite satellite: Satellite object
    constellation = root.current_scenario.children.new(STKObjectType.CONSTELLATION, "MyConstellation")
    constellation.objects.add_object(satellite)
    constellation.objects.add("*/Facility/MyFacility")


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Constellation


Property detail
---------------

.. py:property:: constraints
    :canonical: br.ok.core.stkobjects.Constellation.constraints
    :type: ConstellationConstraints

    Get the constellation's constraints.

.. py:property:: graphics
    :canonical: br.ok.core.stkobjects.Constellation.graphics
    :type: ConstellationGraphics

    Constellation's 2D graphics settings.

.. py:property:: objects
    :canonical: br.ok.core.stkobjects.Constellation.objects
    :type: ObjectLinkCollection

    Get the collection of objects in the chain.

.. py:property:: routing
    :canonical: br.ok.core.stkobjects.Constellation.routing
    :type: ConstellationRouting

    Constellation's routing settings.


