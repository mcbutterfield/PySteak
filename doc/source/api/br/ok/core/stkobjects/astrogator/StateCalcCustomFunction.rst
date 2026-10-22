StateCalcCustomFunction
=======================

.. py:class:: br.ok.core.stkobjects.astrogator.StateCalcCustomFunction

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   Do not use this class, as it is deprecated. Custom Function Calc objects.

.. py:currentmodule:: StateCalcCustomFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcCustomFunction.eval_function_name`
              - Get or set the custom function used to calculate this object's value.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcCustomFunction.reset_function_name`
              - Get or set the custom function called before computing, before each segment runs, and before reporting.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcCustomFunction.unit_dimension`
              - Get or set the unit dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import StateCalcCustomFunction


Property detail
---------------

.. py:property:: eval_function_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcCustomFunction.eval_function_name
    :type: str

    Get or set the custom function used to calculate this object's value.

.. py:property:: reset_function_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcCustomFunction.reset_function_name
    :type: str

    Get or set the custom function called before computing, before each segment runs, and before reporting.

.. py:property:: unit_dimension
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcCustomFunction.unit_dimension
    :type: str

    Get or set the unit dimension.


