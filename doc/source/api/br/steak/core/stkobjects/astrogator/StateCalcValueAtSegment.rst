StateCalcValueAtSegment
=======================

.. py:class:: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegment

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   ValueAtSegment Calc objects.

.. py:currentmodule:: StateCalcValueAtSegment

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcValueAtSegment.calculation_object_name`
              - Get or set the calculation object.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcValueAtSegment.other_segment_name`
              - Get or set the segment to be compared against.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcValueAtSegment.segment_state_to_use`
              - Get or set the segment state to use in the calculation.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import StateCalcValueAtSegment


Property detail
---------------

.. py:property:: calculation_object_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegment.calculation_object_name
    :type: str

    Get or set the calculation object.

.. py:property:: other_segment_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegment.other_segment_name
    :type: str

    Get or set the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegment.segment_state_to_use
    :type: SegmentState

    Get or set the segment state to use in the calculation.


