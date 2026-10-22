ProfileChangeStopSegment
========================

.. py:class:: br.ok.core.stkobjects.astrogator.ProfileChangeStopSegment

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IProfile`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Change Stop Segment profile.

.. py:currentmodule:: ProfileChangeStopSegment

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangeStopSegment.set_segment`
              - Set the stop segment to target.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangeStopSegment.segment_name`
              - Get or set the targeted stop segment.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangeStopSegment.state`
              - Get or set the new state of the targeted stop segment.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import ProfileChangeStopSegment


Property detail
---------------

.. py:property:: segment_name
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangeStopSegment.segment_name
    :type: str

    Get or set the targeted stop segment.

.. py:property:: state
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangeStopSegment.state
    :type: StateType

    Get or set the new state of the targeted stop segment.


Method detail
-------------



.. py:method:: set_segment(self, mcs_stop: MCSStop) -> None
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangeStopSegment.set_segment

    Set the stop segment to target.

    :Parameters:

        **mcs_stop** : :obj:`~MCSStop`


    :Returns:

        :obj:`~None`



