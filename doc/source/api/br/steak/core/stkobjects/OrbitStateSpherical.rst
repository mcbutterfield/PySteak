OrbitStateSpherical
===================

.. py:class:: br.steak.core.stkobjects.OrbitStateSpherical

   Bases: :py:class:`~br.steak.core.stkobjects.IOrbitState`

   Spherical coordinate type: defines the path of an orbit using polar coordinates.

.. py:currentmodule:: OrbitStateSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.azimuth`
              - Get or set the angle in the satellite local horizontal plane between the projection of the velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.coordinate_system`
              - Get the coordinate system and coordinate epoch.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.coordinate_system_type`
              - Get or set the coordinate system being used.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.declination`
              - Get or set the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.flight_path_angle`
              - Get the value of the Vertical or Horizontal Flight Path Angle.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.flight_path_angle_type`
              - Get or set the Flight Path Angle type can be Vertical or Horizontal.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.radius`
              - Get or set the magnitude of the satellite position vector. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.right_ascension`
              - Get or set the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.supported_coordinate_system_types`
              - Return an array of supported coordinate system types.
            * - :py:attr:`~br.steak.core.stkobjects.OrbitStateSpherical.velocity`
              - Get or set the magnitude of the velocity vector. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import OrbitStateSpherical


Property detail
---------------

.. py:property:: azimuth
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.azimuth
    :type: float

    Get or set the angle in the satellite local horizontal plane between the projection of the velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.

.. py:property:: coordinate_system
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: coordinate_system_type
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.coordinate_system_type
    :type: CoordinateSystem

    Get or set the coordinate system being used.

.. py:property:: declination
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.declination
    :type: float

    Get or set the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.

.. py:property:: flight_path_angle
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.flight_path_angle
    :type: IFlightPathAngle

    Get the value of the Vertical or Horizontal Flight Path Angle.

.. py:property:: flight_path_angle_type
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.flight_path_angle_type
    :type: SphericalFlightPathAzimuthType

    Get or set the Flight Path Angle type can be Vertical or Horizontal.

.. py:property:: radius
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.radius
    :type: float

    Get or set the magnitude of the satellite position vector. Uses Distance Dimension.

.. py:property:: right_ascension
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.right_ascension
    :type: float

    Get or set the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.

.. py:property:: state_epoch
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.state_epoch
    :type: ITimeToolInstantSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).

.. py:property:: supported_coordinate_system_types
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.supported_coordinate_system_types
    :type: list

    Return an array of supported coordinate system types.

.. py:property:: velocity
    :canonical: br.steak.core.stkobjects.OrbitStateSpherical.velocity
    :type: float

    Get or set the magnitude of the velocity vector. Uses Rate Dimension.


