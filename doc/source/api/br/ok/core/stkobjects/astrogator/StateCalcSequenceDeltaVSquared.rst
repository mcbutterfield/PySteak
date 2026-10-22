StateCalcSequenceDeltaVSquared
==============================

.. py:class:: br.ok.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   Sequence DeltaV Squared Calc objects.

.. py:currentmodule:: StateCalcSequenceDeltaVSquared

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared.sequence_name`
              - Get or set the sequence whose DeltaV's are to be accumulated.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared.squared_type`
              - Whether the value should be calculated as the sum of the squares of the maneuver Delta-Vs or the square of the sum of the maneuver Delta-Vs.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import StateCalcSequenceDeltaVSquared


Property detail
---------------

.. py:property:: sequence_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared.sequence_name
    :type: str

    Get or set the sequence whose DeltaV's are to be accumulated.

.. py:property:: squared_type
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared.squared_type
    :type: SquaredType

    Whether the value should be calculated as the sum of the squares of the maneuver Delta-Vs or the square of the sum of the maneuver Delta-Vs.


