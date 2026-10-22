VehicleGraphics3DBPlaneTargetPoint
==================================

.. py:class:: br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint

   3D BPlane TargetPoint.

.. py:currentmodule:: VehicleGraphics3DBPlaneTargetPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.is_position_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.set_position_type`
              - Set the position type of the BPlane target point.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.color`
              - Get or set the color of the Target Point.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.position`
              - Return the BPlane target point position.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.position_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.position_type`
              - Get the position type of the BPlane target point.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.show_graphics`
              - Whether the Target Point is displayed.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGraphics3DBPlaneTargetPoint


Property detail
---------------

.. py:property:: color
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.color
    :type: Color

    Get or set the color of the Target Point.

.. py:property:: position
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.position
    :type: IVehicleGraphics3DBPlaneTargetPointPosition

    Return the BPlane target point position.

.. py:property:: position_supported_types
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.position_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: position_type
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.position_type
    :type: VehicleGraphics3DBPlaneTargetPointPosition

    Get the position type of the BPlane target point.

.. py:property:: show_graphics
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.show_graphics
    :type: bool

    Whether the Target Point is displayed.


Method detail
-------------



.. py:method:: is_position_type_supported(self, position: VehicleGraphics3DBPlaneTargetPointPosition) -> bool
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.is_position_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **position** : :obj:`~VehicleGraphics3DBPlaneTargetPointPosition`


    :Returns:

        :obj:`~bool`






.. py:method:: set_position_type(self, position: VehicleGraphics3DBPlaneTargetPointPosition) -> None
    :canonical: br.ok.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint.set_position_type

    Set the position type of the BPlane target point.

    :Parameters:

        **position** : :obj:`~VehicleGraphics3DBPlaneTargetPointPosition`


    :Returns:

        :obj:`~None`

