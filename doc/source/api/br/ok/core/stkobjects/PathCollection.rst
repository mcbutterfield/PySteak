PathCollection
==============

.. py:class:: br.ok.core.stkobjects.PathCollection

   Allow adding and removing of paths.

.. py:currentmodule:: PathCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PathCollection.add`
              - Add a new element to the collection. Must be the full path to the file.
            * - :py:attr:`~br.ok.core.stkobjects.PathCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.ok.core.stkobjects.PathCollection.remove`
              - Remove an element from the collection given a filename.
            * - :py:attr:`~br.ok.core.stkobjects.PathCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~br.ok.core.stkobjects.PathCollection.remove_at`
              - Remove an element from the collection using specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PathCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.PathCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import PathCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.PathCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.PathCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self, filename: str) -> None
    :canonical: br.ok.core.stkobjects.PathCollection.add

    Add a new element to the collection. Must be the full path to the file.

    :Parameters:

        **filename** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: item(self, index: int) -> str
    :canonical: br.ok.core.stkobjects.PathCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~str`

.. py:method:: remove(self, filename: str) -> None
    :canonical: br.ok.core.stkobjects.PathCollection.remove

    Remove an element from the collection given a filename.

    :Parameters:

        **filename** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: br.ok.core.stkobjects.PathCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.ok.core.stkobjects.PathCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


