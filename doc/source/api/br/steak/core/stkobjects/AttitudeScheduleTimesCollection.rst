AttitudeScheduleTimesCollection
===============================

.. py:class:: br.steak.core.stkobjects.AttitudeScheduleTimesCollection

   List of scheduled accesses.

.. py:currentmodule:: AttitudeScheduleTimesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AttitudeScheduleTimesCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AttitudeScheduleTimesCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AttitudeScheduleTimesCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AttitudeScheduleTimesCollection.remove_at`
              - Remove an element from the collection using specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AttitudeScheduleTimesCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AttitudeScheduleTimesCollection.available_targets`
              - Return a list of available targets.
            * - :py:attr:`~br.steak.core.stkobjects.AttitudeScheduleTimesCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AttitudeScheduleTimesCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.AttitudeScheduleTimesCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: available_targets
    :canonical: br.steak.core.stkobjects.AttitudeScheduleTimesCollection.available_targets
    :type: list

    Return a list of available targets.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.AttitudeScheduleTimesCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self, target_path: str) -> AttitudeScheduleTimesElement
    :canonical: br.steak.core.stkobjects.AttitudeScheduleTimesCollection.add

    Add a new element to the collection.

    :Parameters:

        **target_path** : :obj:`~str`


    :Returns:

        :obj:`~AttitudeScheduleTimesElement`



.. py:method:: item(self, index: int) -> AttitudeScheduleTimesElement
    :canonical: br.steak.core.stkobjects.AttitudeScheduleTimesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~AttitudeScheduleTimesElement`

.. py:method:: remove_all(self) -> None
    :canonical: br.steak.core.stkobjects.AttitudeScheduleTimesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.AttitudeScheduleTimesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


