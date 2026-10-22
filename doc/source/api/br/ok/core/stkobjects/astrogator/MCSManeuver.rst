MCSManeuver
===========

.. py:class:: br.ok.core.stkobjects.astrogator.MCSManeuver

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   The Maneuver segment.

.. py:currentmodule:: MCSManeuver

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSManeuver.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSManeuver.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSManeuver.is_control_parameter_enabled`
              - Sees if the specified control is enabled.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSManeuver.set_maneuver_type`
              - Set the maneuver type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSManeuver.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSManeuver.maneuver`
              - Get the Maneuver properties.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.MCSManeuver.maneuver_type`
              - Get the maneuver type.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import MCSManeuver


Property detail
---------------

.. py:property:: control_parameters_available
    :canonical: br.ok.core.stkobjects.astrogator.MCSManeuver.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: maneuver
    :canonical: br.ok.core.stkobjects.astrogator.MCSManeuver.maneuver
    :type: IManeuver

    Get the Maneuver properties.

.. py:property:: maneuver_type
    :canonical: br.ok.core.stkobjects.astrogator.MCSManeuver.maneuver_type
    :type: ManeuverType

    Get the maneuver type.


Method detail
-------------


.. py:method:: disable_control_parameter(self, param: ControlManeuver) -> None
    :canonical: br.ok.core.stkobjects.astrogator.MCSManeuver.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlManeuver`


    :Returns:

        :obj:`~None`

.. py:method:: enable_control_parameter(self, param: ControlManeuver) -> None
    :canonical: br.ok.core.stkobjects.astrogator.MCSManeuver.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlManeuver`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlManeuver) -> bool
    :canonical: br.ok.core.stkobjects.astrogator.MCSManeuver.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlManeuver`


    :Returns:

        :obj:`~bool`



.. py:method:: set_maneuver_type(self, maneuver_type: ManeuverType) -> None
    :canonical: br.ok.core.stkobjects.astrogator.MCSManeuver.set_maneuver_type

    Set the maneuver type.

    :Parameters:

        **maneuver_type** : :obj:`~ManeuverType`


    :Returns:

        :obj:`~None`

