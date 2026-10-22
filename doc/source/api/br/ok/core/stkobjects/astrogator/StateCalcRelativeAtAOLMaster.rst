StateCalcRelativeAtAOLMaster
============================

.. py:class:: br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   RelAOLMaster Calc objects.

.. py:currentmodule:: StateCalcRelativeAtAOLMaster

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.calculation_object_name`
              - Get or set the calculation object of interest.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.direction`
              - Get or set the direction to search for the desired value.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.reference`
              - Get the reference object.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.reference_selection`
              - Get or set the reference object selection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import StateCalcRelativeAtAOLMaster


Property detail
---------------

.. py:property:: calculation_object_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.calculation_object_name
    :type: str

    Get or set the calculation object of interest.

.. py:property:: central_body_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: direction
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.direction
    :type: CalculationObjectDirection

    Get or set the direction to search for the desired value.

.. py:property:: reference
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: reference_selection
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.reference_selection
    :type: CalculationObjectReference

    Get or set the reference object selection.


