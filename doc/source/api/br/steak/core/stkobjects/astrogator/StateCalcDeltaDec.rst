StateCalcDeltaDec
=================

.. py:class:: br.steak.core.stkobjects.astrogator.StateCalcDeltaDec

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   DeltaDec Calc objects.

.. py:currentmodule:: StateCalcDeltaDec

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcDeltaDec.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcDeltaDec.reference_body`
              - Get or set the reference body of the component. Read only when the ReferenceType is eVACalcObjectCentralBodyReferenceParent.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcDeltaDec.reference_type`
              - Get or set the central body's reference type.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import StateCalcDeltaDec


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcDeltaDec.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: reference_body
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcDeltaDec.reference_body
    :type: str

    Get or set the reference body of the component. Read only when the ReferenceType is eVACalcObjectCentralBodyReferenceParent.

.. py:property:: reference_type
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcDeltaDec.reference_type
    :type: CalculationObjectCentralBodyReference

    Get or set the central body's reference type.


