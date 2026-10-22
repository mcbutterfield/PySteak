PriorityCollection
==================

.. py:class:: br.ok.core.stkobjects.PriorityCollection

   Class defining a priority data collection.

.. py:currentmodule:: PriorityCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PriorityCollection.item`
              - Given an index, returns the item in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PriorityCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.ok.core.stkobjects.PriorityCollection.count`
              - Return the number of priorities in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import PriorityCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.PriorityCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.PriorityCollection.count
    :type: int

    Return the number of priorities in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> Priority
    :canonical: br.ok.core.stkobjects.PriorityCollection.item

    Given an index, returns the item in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Priority`


