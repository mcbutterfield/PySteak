EngineConstant
==============

.. py:class:: br.steak.core.stkobjects.astrogator.EngineConstant

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   Constant Thrust engine model.

.. py:currentmodule:: EngineConstant

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EngineConstant.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EngineConstant.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EngineConstant.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EngineConstant.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EngineConstant.g`
              - Get or set the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EngineConstant.isp`
              - Get or set the specific impulse for this engine. Uses SpecificImpulse Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.EngineConstant.thrust`
              - Get or set the thrust for this engine. Uses Force Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import EngineConstant


Property detail
---------------

.. py:property:: control_parameters_available
    :canonical: br.steak.core.stkobjects.astrogator.EngineConstant.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: g
    :canonical: br.steak.core.stkobjects.astrogator.EngineConstant.g
    :type: float

    Get or set the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: isp
    :canonical: br.steak.core.stkobjects.astrogator.EngineConstant.isp
    :type: float

    Get or set the specific impulse for this engine. Uses SpecificImpulse Dimension.

.. py:property:: thrust
    :canonical: br.steak.core.stkobjects.astrogator.EngineConstant.thrust
    :type: float

    Get or set the thrust for this engine. Uses Force Dimension.


Method detail
-------------


.. py:method:: disable_control_parameter(self, param: ControlEngineConstant) -> None
    :canonical: br.steak.core.stkobjects.astrogator.EngineConstant.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlEngineConstant`


    :Returns:

        :obj:`~None`

.. py:method:: enable_control_parameter(self, param: ControlEngineConstant) -> None
    :canonical: br.steak.core.stkobjects.astrogator.EngineConstant.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlEngineConstant`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlEngineConstant) -> bool
    :canonical: br.steak.core.stkobjects.astrogator.EngineConstant.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlEngineConstant`


    :Returns:

        :obj:`~bool`







