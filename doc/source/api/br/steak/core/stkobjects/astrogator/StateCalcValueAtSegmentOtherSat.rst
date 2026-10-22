StateCalcValueAtSegmentOtherSat
===============================

.. py:class:: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   ValueAtSegmentOtherSat Calc objects.

.. py:currentmodule:: StateCalcValueAtSegmentOtherSat

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.calculation_object_name`
              - Get or set the calculation object.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.other_segment_name`
              - Get or set the segment to be compared against.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.reference_satellite`
              - Get the Astrogator satellite on which the segment to be compared exists.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.segment_state_to_use`
              - Get or set the segment state to use in the calculation.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import StateCalcValueAtSegmentOtherSat


Property detail
---------------

.. py:property:: calculation_object_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.calculation_object_name
    :type: str

    Get or set the calculation object.

.. py:property:: other_segment_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.other_segment_name
    :type: str

    Get or set the segment to be compared against.

.. py:property:: reference_satellite
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.reference_satellite
    :type: ILinkToObject

    Get the Astrogator satellite on which the segment to be compared exists.

.. py:property:: segment_state_to_use
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.segment_state_to_use
    :type: SegmentState

    Get or set the segment state to use in the calculation.


