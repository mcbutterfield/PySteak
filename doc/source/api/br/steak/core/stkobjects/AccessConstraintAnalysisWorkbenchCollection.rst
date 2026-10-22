AccessConstraintAnalysisWorkbenchCollection
===========================================

.. py:class:: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection

   Bases: :py:class:`~br.steak.core.stkobjects.IAccessConstraint`

   Collection of Analysis Workbench constraints.

.. py:currentmodule:: AccessConstraintAnalysisWorkbenchCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.add_constraint`
              - Add a constraint to the AWB Constraint Collection.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.get_available_references`
              - Return an array of available References.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.item`
              - Get an AccessConstraintAnalysisWorkbench interface using an index.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_all`
              - Remove all items from the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_constraint`
              - Remove a Analysis Workbench using Reference/Component.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_index`
              - Remove an item given an index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection._new_enum`
              - Enumerate the AccessConstraintAnalysisWorkbench interfaces.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.count`
              - Number of items in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AccessConstraintAnalysisWorkbenchCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection._new_enum
    :type: EnumeratorProxy

    Enumerate the AccessConstraintAnalysisWorkbench interfaces.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.count
    :type: int

    Number of items in the collection.


Method detail
-------------

.. py:method:: add_constraint(self, constraint: AnalysisWorkbenchAccessConstraintType, reference: str) -> IAccessConstraint
    :canonical: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.add_constraint

    Add a constraint to the AWB Constraint Collection.

    :Parameters:

        **constraint** : :obj:`~AnalysisWorkbenchAccessConstraintType`

        **reference** : :obj:`~str`


    :Returns:

        :obj:`~IAccessConstraint`


.. py:method:: get_available_references(self, type: AnalysisWorkbenchAccessConstraintType) -> list
    :canonical: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.get_available_references

    Return an array of available References.

    :Parameters:

        **type** : :obj:`~AnalysisWorkbenchAccessConstraintType`


    :Returns:

        :obj:`~list`

.. py:method:: item(self, index: int) -> AccessConstraintAnalysisWorkbench
    :canonical: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.item

    Get an AccessConstraintAnalysisWorkbench interface using an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~AccessConstraintAnalysisWorkbench`

.. py:method:: remove_all(self) -> None
    :canonical: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_all

    Remove all items from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_constraint(self, type: AnalysisWorkbenchAccessConstraintType, reference: str) -> None
    :canonical: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_constraint

    Remove a Analysis Workbench using Reference/Component.

    :Parameters:

        **type** : :obj:`~AnalysisWorkbenchAccessConstraintType`

        **reference** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove_index(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection.remove_index

    Remove an item given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


