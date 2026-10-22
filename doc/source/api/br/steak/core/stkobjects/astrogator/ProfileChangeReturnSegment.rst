ProfileChangeReturnSegment
==========================

.. py:class:: br.steak.core.stkobjects.astrogator.ProfileChangeReturnSegment

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IProfile`, :py:class:`~br.steak.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Change Return Segment profile.

.. py:currentmodule:: ProfileChangeReturnSegment

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileChangeReturnSegment.set_segment`
              - Set the return segment to target.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileChangeReturnSegment.segment_name`
              - Get or set the targeted return segment.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileChangeReturnSegment.state`
              - Get or set the new state for the targeted return segment.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import ProfileChangeReturnSegment


Property detail
---------------

.. py:property:: segment_name
    :canonical: br.steak.core.stkobjects.astrogator.ProfileChangeReturnSegment.segment_name
    :type: str

    Get or set the targeted return segment.

.. py:property:: state
    :canonical: br.steak.core.stkobjects.astrogator.ProfileChangeReturnSegment.state
    :type: ReturnControl

    Get or set the new state for the targeted return segment.


Method detail
-------------



.. py:method:: set_segment(self, mcs_return: MCSReturn) -> None
    :canonical: br.steak.core.stkobjects.astrogator.ProfileChangeReturnSegment.set_segment

    Set the return segment to target.

    :Parameters:

        **mcs_return** : :obj:`~MCSReturn`


    :Returns:

        :obj:`~None`



