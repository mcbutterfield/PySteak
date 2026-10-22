DirectionProviderObject
=======================

.. py:class:: br.steak.core.stkobjects.DirectionProviderObject

   Bases: :py:class:`~br.steak.core.stkobjects.IDirectionProvider`

   Class defining an object direction provider.

.. py:currentmodule:: DirectionProviderObject

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.azimuth_steering_limit_a`
              - Get or set Azimuth Steering Limit A.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.azimuth_steering_limit_b`
              - Get or set Azimuth Steering Limit B.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.directions`
              - Get the beam steering list.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.elevation_steering_limit_a`
              - Get or set Elevation Steering Limit A.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.elevation_steering_limit_b`
              - Get or set Elevation Steering Limit B.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.enabled`
              - Get or set the option for enabling steering.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.limits_exceeded_behavior_type`
              - Get or set the Limits Exceeded Behavior type.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.maximum_selection_count`
              - Get or set the maximum number of targets to select for beam steering.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.target_selection_method`
              - Get the target selection method.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.target_selection_method_type`
              - Get or set the method type used to determine which targets are selected for steering.
            * - :py:attr:`~br.steak.core.stkobjects.DirectionProviderObject.use_default_direction`
              - Get or set the option to use default direction when there are zero objects in the field of view.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import DirectionProviderObject


Property detail
---------------

.. py:property:: azimuth_steering_limit_a
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.azimuth_steering_limit_a
    :type: float

    Get or set Azimuth Steering Limit A.

.. py:property:: azimuth_steering_limit_b
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.azimuth_steering_limit_b
    :type: float

    Get or set Azimuth Steering Limit B.

.. py:property:: directions
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.directions
    :type: ObjectLinkCollection

    Get the beam steering list.

.. py:property:: elevation_steering_limit_a
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.elevation_steering_limit_a
    :type: float

    Get or set Elevation Steering Limit A.

.. py:property:: elevation_steering_limit_b
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.elevation_steering_limit_b
    :type: float

    Get or set Elevation Steering Limit B.

.. py:property:: enabled
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.enabled
    :type: bool

    Get or set the option for enabling steering.

.. py:property:: limits_exceeded_behavior_type
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.limits_exceeded_behavior_type
    :type: LimitsExceededBehaviorType

    Get or set the Limits Exceeded Behavior type.

.. py:property:: maximum_selection_count
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.maximum_selection_count
    :type: int

    Get or set the maximum number of targets to select for beam steering.

.. py:property:: target_selection_method
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.target_selection_method
    :type: ITargetSelectionMethod

    Get the target selection method.

.. py:property:: target_selection_method_type
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.target_selection_method_type
    :type: TargetSelectionMethod

    Get or set the method type used to determine which targets are selected for steering.

.. py:property:: use_default_direction
    :canonical: br.steak.core.stkobjects.DirectionProviderObject.use_default_direction
    :type: bool

    Get or set the option to use default direction when there are zero objects in the field of view.


