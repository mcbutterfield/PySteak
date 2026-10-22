StateCalcSTMEigenvecElem
========================

.. py:class:: br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   Cartesian STM Eigenvector Calc objects.

.. py:currentmodule:: StateCalcSTMEigenvecElem

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem.coord_system_name`
              - Get or set the coordinate system within which the element is defined.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem.eigenvector_complex_part`
              - Whether this value represents the real or imaginary part of an Eigenvector element.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem.eigenvector_number`
              - Get or set the number identifying one of the six Eigenvectors.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem.state_variable`
              - Get or set the variable identifying the component within an Eigenvector.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import StateCalcSTMEigenvecElem


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem.coord_system_name
    :type: str

    Get or set the coordinate system within which the element is defined.

.. py:property:: eigenvector_complex_part
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem.eigenvector_complex_part
    :type: ComplexNumber

    Whether this value represents the real or imaginary part of an Eigenvector element.

.. py:property:: eigenvector_number
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem.eigenvector_number
    :type: STMEigenNumber

    Get or set the number identifying one of the six Eigenvectors.

.. py:property:: state_variable
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcSTMEigenvecElem.state_variable
    :type: STMPerturbationVariables

    Get or set the variable identifying the component within an Eigenvector.


