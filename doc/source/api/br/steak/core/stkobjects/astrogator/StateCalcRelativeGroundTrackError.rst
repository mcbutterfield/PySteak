StateCalcRelativeGroundTrackError
=================================

.. py:class:: br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   RelGroundTrackError Calc objects.

.. py:currentmodule:: StateCalcRelativeGroundTrackError

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.direction`
              - Get or set the direction to search for the desired value.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.reference`
              - Get the reference object.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.reference_selection`
              - Get or set the reference object selection.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.signed`
              - True if signed based on RxV.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import StateCalcRelativeGroundTrackError


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: direction
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.direction
    :type: CalculationObjectDirection

    Get or set the direction to search for the desired value.

.. py:property:: reference
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: reference_selection
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.reference_selection
    :type: CalculationObjectReference

    Get or set the reference object selection.

.. py:property:: signed
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError.signed
    :type: bool

    True if signed based on RxV.


