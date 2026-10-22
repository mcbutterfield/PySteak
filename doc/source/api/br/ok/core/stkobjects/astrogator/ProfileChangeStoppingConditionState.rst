ProfileChangeStoppingConditionState
===================================

.. py:class:: br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IProfile`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Change Stopping Condition State profile.

.. py:currentmodule:: ProfileChangeStoppingConditionState

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.set_segment`
              - Set the targeted segment.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.set_trigger`
              - Set the targeted stopping condition.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.segment_name`
              - Get or set the segment that contains the targeted stopping condition.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.state`
              - Get or set the new state of the targeted stopping condition.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.trigger_name`
              - Get or set the name of the targeted stopping condition.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import ProfileChangeStoppingConditionState


Property detail
---------------

.. py:property:: segment_name
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.segment_name
    :type: str

    Get or set the segment that contains the targeted stopping condition.

.. py:property:: state
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.state
    :type: StateType

    Get or set the new state of the targeted stopping condition.

.. py:property:: trigger_name
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.trigger_name
    :type: str

    Get or set the name of the targeted stopping condition.


Method detail
-------------



.. py:method:: set_segment(self, mcs_segment: IMCSSegment) -> None
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.set_segment

    Set the targeted segment.

    :Parameters:

        **mcs_segment** : :obj:`~IMCSSegment`


    :Returns:

        :obj:`~None`

.. py:method:: set_trigger(self, stopping_condition: StoppingCondition) -> None
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangeStoppingConditionState.set_trigger

    Set the targeted stopping condition.

    :Parameters:

        **stopping_condition** : :obj:`~StoppingCondition`


    :Returns:

        :obj:`~None`





