ScheduleTimeCollection
======================

.. py:class:: br.ok.core.stkobjects.ScheduleTimeCollection

   Collection of user-scheduled access times.

.. py:currentmodule:: ScheduleTimeCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTimeCollection.add`
              - Add a schedule time item to the collection. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTimeCollection.deconflict`
              - Deconflicts the schedule time intervals.
            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTimeCollection.item`
              - Retrieve and ScheduleTime interface given an index.
            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTimeCollection.remove_all`
              - Remove all items in the collection.
            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTimeCollection.remove_index`
              - Remove an item given an index.
            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTimeCollection.remove_schedule`
              - Remove an interval using the interval interface. Start/Stop use DateFormat Dimension.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTimeCollection._new_enum`
              - Enumerates through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.ScheduleTimeCollection.count`
              - The number of items in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ScheduleTimeCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.ScheduleTimeCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.ScheduleTimeCollection.count
    :type: int

    The number of items in the collection.


Method detail
-------------

.. py:method:: add(self, start: typing.Any, stop: typing.Any, name: str) -> ScheduleTime
    :canonical: br.ok.core.stkobjects.ScheduleTimeCollection.add

    Add a schedule time item to the collection. Start/Stop use DateFormat Dimension.

    :Parameters:

        **start** : :obj:`~typing.Any`

        **stop** : :obj:`~typing.Any`

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ScheduleTime`


.. py:method:: deconflict(self) -> None
    :canonical: br.ok.core.stkobjects.ScheduleTimeCollection.deconflict

    Deconflicts the schedule time intervals.

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> ScheduleTime
    :canonical: br.ok.core.stkobjects.ScheduleTimeCollection.item

    Retrieve and ScheduleTime interface given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ScheduleTime`

.. py:method:: remove_all(self) -> None
    :canonical: br.ok.core.stkobjects.ScheduleTimeCollection.remove_all

    Remove all items in the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_index(self, index: int) -> None
    :canonical: br.ok.core.stkobjects.ScheduleTimeCollection.remove_index

    Remove an item given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_schedule(self, start: typing.Any, stop: typing.Any, name: str) -> None
    :canonical: br.ok.core.stkobjects.ScheduleTimeCollection.remove_schedule

    Remove an interval using the interval interface. Start/Stop use DateFormat Dimension.

    :Parameters:

        **start** : :obj:`~typing.Any`

        **stop** : :obj:`~typing.Any`

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`


