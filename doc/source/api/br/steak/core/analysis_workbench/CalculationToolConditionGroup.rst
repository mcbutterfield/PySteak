CalculationToolConditionGroup
=============================

.. py:class:: br.steak.core.analysis_workbench.CalculationToolConditionGroup

   Access or create VGT conditions associated with an object or a central body.

.. py:currentmodule:: CalculationToolConditionGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup.get_item_by_index`
              - Retrieve a condition from the collection by index.
            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup.get_item_by_name`
              - Retrieve a condition from the collection by name.
            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup.remove`
              - Remove a specified element.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup._new_enum`
              - Return a COM enumerator.
            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~br.steak.core.analysis_workbench.CalculationToolConditionGroup.factory`
              - Return a factory object used to create calc scalar components.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import CalculationToolConditionGroup


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.

.. py:property:: context
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup.factory
    :type: CalculationToolConditionFactory

    Return a factory object used to create calc scalar components.


Method detail
-------------

.. py:method:: contains(self, name: str) -> bool
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`




.. py:method:: get_item_by_index(self, index: int) -> ICalculationToolCondition
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup.get_item_by_index

    Retrieve a condition from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: get_item_by_name(self, name: str) -> ICalculationToolCondition
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup.get_item_by_name

    Retrieve a condition from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: item(self, index_or_name: typing.Any) -> ICalculationToolCondition
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup.item

    Return an element by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: remove(self, event_name: str) -> None
    :canonical: br.steak.core.analysis_workbench.CalculationToolConditionGroup.remove

    Remove a specified element.

    :Parameters:

        **event_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


