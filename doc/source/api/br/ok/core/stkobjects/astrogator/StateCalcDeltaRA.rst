StateCalcDeltaRA
================

.. py:class:: br.ok.core.stkobjects.astrogator.StateCalcDeltaRA

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   DeltaRA Calc objects.

.. py:currentmodule:: StateCalcDeltaRA

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcDeltaRA.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcDeltaRA.reference_body`
              - Get or set the reference body of the component. Read only when the ReferenceType is eVACalcObjectCentralBodyReferenceParent.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcDeltaRA.reference_type`
              - Get or set the central body's reference type.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import StateCalcDeltaRA


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcDeltaRA.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: reference_body
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcDeltaRA.reference_body
    :type: str

    Get or set the reference body of the component. Read only when the ReferenceType is eVACalcObjectCentralBodyReferenceParent.

.. py:property:: reference_type
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcDeltaRA.reference_type
    :type: CalculationObjectCentralBodyReference

    Get or set the central body's reference type.


