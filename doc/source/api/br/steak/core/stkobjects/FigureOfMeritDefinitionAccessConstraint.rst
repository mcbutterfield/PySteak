FigureOfMeritDefinitionAccessConstraint
=======================================

.. py:class:: br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint

   Bases: :py:class:`~br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute`, :py:class:`~br.steak.core.stkobjects.IFigureOfMeritDefinition`

   Access Constraint Figure of Merit.

.. py:currentmodule:: FigureOfMeritDefinitionAccessConstraint

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint.across_assets`
              - Value of the constraint that is to be selected based on all currently available assets.
            * - :py:attr:`~br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint.constraint`
              - Name of the access constraint.
            * - :py:attr:`~br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint.constraint_name`
              - Name of the access constraint as an enumeration. If the constraint is not in FigureOfMeritConstraintName then use Constraint instead.
            * - :py:attr:`~br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint.time_step`
              - Get or set the value to be used during the sampling of the dynamic definition for use in the static definition.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import FigureOfMeritDefinitionAccessConstraint


Property detail
---------------

.. py:property:: across_assets
    :canonical: br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint.across_assets
    :type: FigureOfMeritAcrossAssets

    Value of the constraint that is to be selected based on all currently available assets.

.. py:property:: constraint
    :canonical: br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint.constraint
    :type: str

    Name of the access constraint.

.. py:property:: constraint_name
    :canonical: br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint.constraint_name
    :type: FigureOfMeritConstraintName

    Name of the access constraint as an enumeration. If the constraint is not in FigureOfMeritConstraintName then use Constraint instead.

.. py:property:: time_step
    :canonical: br.steak.core.stkobjects.FigureOfMeritDefinitionAccessConstraint.time_step
    :type: float

    Get or set the value to be used during the sampling of the dynamic definition for use in the static definition.


