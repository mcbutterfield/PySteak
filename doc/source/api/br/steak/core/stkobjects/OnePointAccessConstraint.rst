OnePointAccessConstraint
========================

.. py:class:: br.steak.core.stkobjects.OnePointAccessConstraint

   One Point Access Result.

.. py:currentmodule:: OnePointAccessConstraint

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.OnePointAccessConstraint.constraint`
              - Get the type of the constraint being evaluated.
            * - :py:attr:`~br.steak.core.stkobjects.OnePointAccessConstraint.object_path`
              - Get the object path of the owner of the constraint.
            * - :py:attr:`~br.steak.core.stkobjects.OnePointAccessConstraint.status`
              - An indicator describing the status  of whether the constraint is satisfied or violated at the computed time.
            * - :py:attr:`~br.steak.core.stkobjects.OnePointAccessConstraint.value`
              - Get the value of the constraint at the computed time, in internal units.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import OnePointAccessConstraint


Property detail
---------------

.. py:property:: constraint
    :canonical: br.steak.core.stkobjects.OnePointAccessConstraint.constraint
    :type: AccessConstraintType

    Get the type of the constraint being evaluated.

.. py:property:: object_path
    :canonical: br.steak.core.stkobjects.OnePointAccessConstraint.object_path
    :type: str

    Get the object path of the owner of the constraint.

.. py:property:: status
    :canonical: br.steak.core.stkobjects.OnePointAccessConstraint.status
    :type: OnePointAccessStatus

    An indicator describing the status  of whether the constraint is satisfied or violated at the computed time.

.. py:property:: value
    :canonical: br.steak.core.stkobjects.OnePointAccessConstraint.value
    :type: float

    Get the value of the constraint at the computed time, in internal units.


