ObjectPathCollection
====================

.. py:class:: br.steak.core.stkx.ObjectPathCollection

   Collection of object paths.

.. py:currentmodule:: ObjectPathCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkx.ObjectPathCollection.item`
              - Get the element at the specified index (0-based).
            * - :py:attr:`~br.steak.core.stkx.ObjectPathCollection.range`
              - Return the elements within the specified range.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkx.ObjectPathCollection._new_enum`
              - Return an object that can be used to iterate through all the object paths in the collection.
            * - :py:attr:`~br.steak.core.stkx.ObjectPathCollection.count`
              - Number of elements contained in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkx import ObjectPathCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkx.ObjectPathCollection._new_enum
    :type: EnumeratorProxy

    Return an object that can be used to iterate through all the object paths in the collection.

.. py:property:: count
    :canonical: br.steak.core.stkx.ObjectPathCollection.count
    :type: int

    Number of elements contained in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: br.steak.core.stkx.ObjectPathCollection.item

    Get the element at the specified index (0-based).

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~str`

.. py:method:: range(self, start_index: int, stop_index: int) -> list
    :canonical: br.steak.core.stkx.ObjectPathCollection.range

    Return the elements within the specified range.

    :Parameters:

        **start_index** : :obj:`~int`

        **stop_index** : :obj:`~int`


    :Returns:

        :obj:`~list`


