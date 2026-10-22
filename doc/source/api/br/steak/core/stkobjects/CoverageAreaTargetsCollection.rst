CoverageAreaTargetsCollection
=============================

.. py:class:: br.steak.core.stkobjects.CoverageAreaTargetsCollection

   Collection of Area Targets.

.. py:currentmodule:: CoverageAreaTargetsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.CoverageAreaTargetsCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageAreaTargetsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageAreaTargetsCollection.remove`
              - Remove an element from the collection given a Target name.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageAreaTargetsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageAreaTargetsCollection.remove_at`
              - Remove an element from the collection using specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.CoverageAreaTargetsCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageAreaTargetsCollection.available_area_targets`
              - Get the available area targets.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageAreaTargetsCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import CoverageAreaTargetsCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.CoverageAreaTargetsCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: available_area_targets
    :canonical: br.steak.core.stkobjects.CoverageAreaTargetsCollection.available_area_targets
    :type: list

    Get the available area targets.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.CoverageAreaTargetsCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self, target_name: str) -> None
    :canonical: br.steak.core.stkobjects.CoverageAreaTargetsCollection.add

    Add a new element to the collection.

    :Parameters:

        **target_name** : :obj:`~str`


    :Returns:

        :obj:`~None`



.. py:method:: item(self, index: int) -> str
    :canonical: br.steak.core.stkobjects.CoverageAreaTargetsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~str`

.. py:method:: remove(self, target_name: str) -> None
    :canonical: br.steak.core.stkobjects.CoverageAreaTargetsCollection.remove

    Remove an element from the collection given a Target name.

    :Parameters:

        **target_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: br.steak.core.stkobjects.CoverageAreaTargetsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.CoverageAreaTargetsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


