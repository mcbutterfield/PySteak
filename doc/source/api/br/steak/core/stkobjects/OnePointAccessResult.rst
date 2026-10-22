OnePointAccessResult
====================

.. py:class:: br.steak.core.stkobjects.OnePointAccessResult

   One Point Access Result.

.. py:currentmodule:: OnePointAccessResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.OnePointAccessResult.access_is_satisfied`
              - Indicate whether all constraints are satisfied at this time.
            * - :py:attr:`~br.steak.core.stkobjects.OnePointAccessResult.constraints`
              - List of constraints evaluated at this time.
            * - :py:attr:`~br.steak.core.stkobjects.OnePointAccessResult.time`
              - Get the time of evaluation of the constraints in a OnePointAccess Compute request.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import OnePointAccessResult


Property detail
---------------

.. py:property:: access_is_satisfied
    :canonical: br.steak.core.stkobjects.OnePointAccessResult.access_is_satisfied
    :type: bool

    Indicate whether all constraints are satisfied at this time.

.. py:property:: constraints
    :canonical: br.steak.core.stkobjects.OnePointAccessResult.constraints
    :type: OnePointAccessConstraintCollection

    List of constraints evaluated at this time.

.. py:property:: time
    :canonical: br.steak.core.stkobjects.OnePointAccessResult.time
    :type: typing.Any

    Get the time of evaluation of the constraints in a OnePointAccess Compute request.


