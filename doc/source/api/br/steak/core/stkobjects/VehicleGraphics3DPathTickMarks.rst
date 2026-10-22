VehicleGraphics3DPathTickMarks
==============================

.. py:class:: br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks

   Tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

.. py:currentmodule:: VehicleGraphics3DPathTickMarks

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.is_tick_data_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.set_tick_data_type`
              - Set the type of tick marks to display.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.show_graphics`
              - Opt whether to display tick marks.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data`
              - Get the tick mark data.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data_type`
              - Get the type of tick marks to display.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleGraphics3DPathTickMarks


Property detail
---------------

.. py:property:: show_graphics
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.show_graphics
    :type: bool

    Opt whether to display tick marks.

.. py:property:: tick_data
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data
    :type: IVehicleGraphics3DTickData

    Get the tick mark data.

.. py:property:: tick_data_supported_types
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: tick_data_type
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data_type
    :type: TickData

    Get the type of tick marks to display.


Method detail
-------------

.. py:method:: is_tick_data_type_supported(self, tick_data: TickData) -> bool
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.is_tick_data_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **tick_data** : :obj:`~TickData`


    :Returns:

        :obj:`~bool`



.. py:method:: set_tick_data_type(self, tick_data: TickData) -> None
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DPathTickMarks.set_tick_data_type

    Set the type of tick marks to display.

    :Parameters:

        **tick_data** : :obj:`~TickData`


    :Returns:

        :obj:`~None`




