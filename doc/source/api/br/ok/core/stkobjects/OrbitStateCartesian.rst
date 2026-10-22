OrbitStateCartesian
===================

.. py:class:: br.ok.core.stkobjects.OrbitStateCartesian

   Bases: :py:class:`~br.ok.core.stkobjects.IOrbitState`

   Cartesian coordinate type.

.. py:currentmodule:: OrbitStateCartesian

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.coordinate_system`
              - Get the coordinate system and epoch.
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.coordinate_system_type`
              - Coordinate system being used.
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.supported_coordinate_system_types`
              - Return an array of supported coordinate system types.
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.x_position`
              - X position component.Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.x_velocity`
              - X velocity component. Uses Rate Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.y_position`
              - Y position component. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.y_velocity`
              - Y velocity component. Uses Rate Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.z_position`
              - Z position component. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.OrbitStateCartesian.z_velocity`
              - Z velocity component. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import OrbitStateCartesian


Property detail
---------------

.. py:property:: coordinate_system
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and epoch.

.. py:property:: coordinate_system_type
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.coordinate_system_type
    :type: CoordinateSystem

    Coordinate system being used.

.. py:property:: state_epoch
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.state_epoch
    :type: ITimeToolInstantSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).

.. py:property:: supported_coordinate_system_types
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.supported_coordinate_system_types
    :type: list

    Return an array of supported coordinate system types.

.. py:property:: x_position
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.x_position
    :type: float

    X position component.Uses Distance Dimension.

.. py:property:: x_velocity
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.x_velocity
    :type: float

    X velocity component. Uses Rate Dimension.

.. py:property:: y_position
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.y_position
    :type: float

    Y position component. Uses Distance Dimension.

.. py:property:: y_velocity
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.y_velocity
    :type: float

    Y velocity component. Uses Rate Dimension.

.. py:property:: z_position
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.z_position
    :type: float

    Z position component. Uses Distance Dimension.

.. py:property:: z_velocity
    :canonical: br.ok.core.stkobjects.OrbitStateCartesian.z_velocity
    :type: float

    Z velocity component. Uses Rate Dimension.


