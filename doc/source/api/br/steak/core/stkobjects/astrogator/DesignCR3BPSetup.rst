DesignCR3BPSetup
================

.. py:class:: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   CR3BP Setup Tool.

.. py:currentmodule:: DesignCR3BPSetup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.create_calculation_objects`
              - Create the calculation objects for the selected coordinate system.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.create_ideal_secondary_body`
              - Construct the idealized secondary for the three-body system.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.create_propagator`
              - Create the propagator for the primary-secondary CR3BP formulation.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.create_rotating_coordinate_system`
              - Create the coordinate system for the RotatingSystemChoice selection.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.delete_calculation_objects`
              - Delete the calculation objects for the selected coordinate system.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.delete_propagator`
              - Delete the propagator for the primary-secondary CR3BP formulation.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.delete_rotating_coordinate_system`
              - Delete the coordinate system for the RotatingSystemChoice selection.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.reset_ideal_secondary_body`
              - Reset the idealized secondary for the three-body system.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.update_ideal_secondary_cb`
              - Update the idealized secondary for the three-body system.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.associated_objects`
              - Get the list of associated objects.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.central_body_name`
              - Primary central body for the three-body system.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.characteristic_acceleration`
              - Get the characteristic acceleration computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.characteristic_distance`
              - Get the characteristic distance computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.characteristic_time`
              - Get the characteristic time computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.characteristic_velocity`
              - Get the characteristic velocity computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.ideal_orbit_radius`
              - Orbital radius of the idealized secondary definition.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.ideal_secondary_name`
              - Name to be used for the idealized secondary.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.include_stm`
              - Get whether or not the STM propagator function is included on the propagator.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.initial_epoch`
              - Date and time for system construction.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.mass_parameter`
              - Get the mass parameter computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.rotating_system_choice`
              - Get the rotating coordinate system and associated calculation objects to interact with.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.secondary_body_name`
              - Secondary Body.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import DesignCR3BPSetup


Property detail
---------------

.. py:property:: associated_objects
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.associated_objects
    :type: DesignCR3BPObjectCollection

    Get the list of associated objects.

.. py:property:: central_body_name
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.central_body_name
    :type: str

    Primary central body for the three-body system.

.. py:property:: characteristic_acceleration
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.characteristic_acceleration
    :type: float

    Get the characteristic acceleration computed from the primary and secondary bodies.

.. py:property:: characteristic_distance
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.characteristic_distance
    :type: float

    Get the characteristic distance computed from the primary and secondary bodies.

.. py:property:: characteristic_time
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.characteristic_time
    :type: float

    Get the characteristic time computed from the primary and secondary bodies.

.. py:property:: characteristic_velocity
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.characteristic_velocity
    :type: float

    Get the characteristic velocity computed from the primary and secondary bodies.

.. py:property:: ideal_orbit_radius
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.ideal_orbit_radius
    :type: IdealOrbitRadius

    Orbital radius of the idealized secondary definition.

.. py:property:: ideal_secondary_name
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.ideal_secondary_name
    :type: str

    Name to be used for the idealized secondary.

.. py:property:: include_stm
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.include_stm
    :type: bool

    Get whether or not the STM propagator function is included on the propagator.

.. py:property:: initial_epoch
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.initial_epoch
    :type: typing.Any

    Date and time for system construction.

.. py:property:: mass_parameter
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.mass_parameter
    :type: float

    Get the mass parameter computed from the primary and secondary bodies.

.. py:property:: rotating_system_choice
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.rotating_system_choice
    :type: RotatingCoordinateSystem

    Get the rotating coordinate system and associated calculation objects to interact with.

.. py:property:: secondary_body_name
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.secondary_body_name
    :type: str

    Secondary Body.


Method detail
-------------








.. py:method:: create_calculation_objects(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.create_calculation_objects

    Create the calculation objects for the selected coordinate system.

    :Returns:

        :obj:`~None`

.. py:method:: create_ideal_secondary_body(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.create_ideal_secondary_body

    Construct the idealized secondary for the three-body system.

    :Returns:

        :obj:`~None`

.. py:method:: create_propagator(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.create_propagator

    Create the propagator for the primary-secondary CR3BP formulation.

    :Returns:

        :obj:`~None`

.. py:method:: create_rotating_coordinate_system(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.create_rotating_coordinate_system

    Create the coordinate system for the RotatingSystemChoice selection.

    :Returns:

        :obj:`~None`

.. py:method:: delete_calculation_objects(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.delete_calculation_objects

    Delete the calculation objects for the selected coordinate system.

    :Returns:

        :obj:`~None`

.. py:method:: delete_propagator(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.delete_propagator

    Delete the propagator for the primary-secondary CR3BP formulation.

    :Returns:

        :obj:`~None`

.. py:method:: delete_rotating_coordinate_system(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.delete_rotating_coordinate_system

    Delete the coordinate system for the RotatingSystemChoice selection.

    :Returns:

        :obj:`~None`










.. py:method:: reset_ideal_secondary_body(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.reset_ideal_secondary_body

    Reset the idealized secondary for the three-body system.

    :Returns:

        :obj:`~None`





.. py:method:: update_ideal_secondary_cb(self) -> None
    :canonical: br.steak.core.stkobjects.astrogator.DesignCR3BPSetup.update_ideal_secondary_cb

    Update the idealized secondary for the three-body system.

    :Returns:

        :obj:`~None`

