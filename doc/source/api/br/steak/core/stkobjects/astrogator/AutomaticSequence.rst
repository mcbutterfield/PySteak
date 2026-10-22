AutomaticSequence
=================

.. py:class:: br.steak.core.stkobjects.astrogator.AutomaticSequence

   Automatic Sequence.

.. py:currentmodule:: AutomaticSequence

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequence.make_copy`
              - Make a copy of the sequence.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequence.name`
              - Get or set the name of the sequence.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequence.sequence`
              - Return the segment collection of the sequence.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AutomaticSequence.user_comment`
              - Get or set the user comment.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import AutomaticSequence


Property detail
---------------

.. py:property:: name
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequence.name
    :type: str

    Get or set the name of the sequence.

.. py:property:: sequence
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequence.sequence
    :type: MCSSegmentCollection

    Return the segment collection of the sequence.

.. py:property:: user_comment
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequence.user_comment
    :type: str

    Get or set the user comment.


Method detail
-------------

.. py:method:: make_copy(self, unique_name: str) -> AutomaticSequence
    :canonical: br.steak.core.stkobjects.astrogator.AutomaticSequence.make_copy

    Make a copy of the sequence.

    :Parameters:

        **unique_name** : :obj:`~str`


    :Returns:

        :obj:`~AutomaticSequence`






