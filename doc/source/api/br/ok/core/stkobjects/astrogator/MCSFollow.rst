MCSFollow
=========

.. py:class:: br.ok.core.stkobjects.astrogator.MCSFollow

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   The Follow segment.

.. py:currentmodule:: MCSFollow

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.fuel_tank`
              - Get the spacecraft's fuel tank properties.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.joining_conditions`
              - If joining conditions are specified, the list of joining conditions.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.joining_type`
              - Get or set the joining type.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.leader`
              - Get the leader object.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.separation_conditions`
              - If separation conditions are specified, the list of separation conditions.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.separation_type`
              - Get or set the separation type.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.spacecraft_and_fuel_tank_type`
              - Get or set the spacecraft snd fuel tank configuration type.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.spacecraft_parameters`
              - Get the spacecraft's physical properties.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.user_variables`
              - Interface used to modify user variables for the follow segment.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.x_offset`
              - Get or set the distance that the spacecraft will be offset from the leader's body frame along the X axis. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.y_offset`
              - Get or set the distance that the spacecraft will be offset from the leader's body frame along the Y axis. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSFollow.z_offset`
              - Get or set the distance that the spacecraft will be offset from the leader's body frame along the Z axis. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import MCSFollow


Property detail
---------------

.. py:property:: control_parameters_available
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: fuel_tank
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.fuel_tank
    :type: FuelTank

    Get the spacecraft's fuel tank properties.

.. py:property:: joining_conditions
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.joining_conditions
    :type: StoppingConditionCollection

    If joining conditions are specified, the list of joining conditions.

.. py:property:: joining_type
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.joining_type
    :type: FollowJoin

    Get or set the joining type.

.. py:property:: leader
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.leader
    :type: ILinkToObject

    Get the leader object.

.. py:property:: separation_conditions
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.separation_conditions
    :type: StoppingConditionCollection

    If separation conditions are specified, the list of separation conditions.

.. py:property:: separation_type
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.separation_type
    :type: FollowSeparation

    Get or set the separation type.

.. py:property:: spacecraft_and_fuel_tank_type
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.spacecraft_and_fuel_tank_type
    :type: FollowSpacecraftAndFuelTank

    Get or set the spacecraft snd fuel tank configuration type.

.. py:property:: spacecraft_parameters
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.spacecraft_parameters
    :type: SpacecraftParameters

    Get the spacecraft's physical properties.

.. py:property:: user_variables
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.user_variables
    :type: UserVariableCollection

    Interface used to modify user variables for the follow segment.

.. py:property:: x_offset
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.x_offset
    :type: float

    Get or set the distance that the spacecraft will be offset from the leader's body frame along the X axis. Uses Distance Dimension.

.. py:property:: y_offset
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.y_offset
    :type: float

    Get or set the distance that the spacecraft will be offset from the leader's body frame along the Y axis. Uses Distance Dimension.

.. py:property:: z_offset
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.z_offset
    :type: float

    Get or set the distance that the spacecraft will be offset from the leader's body frame along the Z axis. Uses Distance Dimension.


Method detail
-------------


.. py:method:: disable_control_parameter(self, param: ControlFollow) -> None
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlFollow`


    :Returns:

        :obj:`~None`

.. py:method:: enable_control_parameter(self, param: ControlFollow) -> None
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlFollow`


    :Returns:

        :obj:`~None`


.. py:method:: is_control_parameter_enabled(self, param: ControlFollow) -> bool
    :canonical: br.ok.core.stkobjects.astrogator.MCSFollow.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlFollow`


    :Returns:

        :obj:`~bool`


















