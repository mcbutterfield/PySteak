PropagatorSP3FileCollection
===========================

.. py:class:: br.steak.core.stkobjects.PropagatorSP3FileCollection

   A collection of SP3 files.

.. py:currentmodule:: PropagatorSP3FileCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.PropagatorSP3FileCollection.add`
              - Load an SP3 file using the specified file path and adds the file to a collection of SP3 files.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorSP3FileCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorSP3FileCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorSP3FileCollection.remove_at`
              - Remove an element from the collection using specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.PropagatorSP3FileCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorSP3FileCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import PropagatorSP3FileCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.PropagatorSP3FileCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.PropagatorSP3FileCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: add(self, file_path: str) -> PropagatorSP3File
    :canonical: br.steak.core.stkobjects.PropagatorSP3FileCollection.add

    Load an SP3 file using the specified file path and adds the file to a collection of SP3 files.

    :Parameters:

        **file_path** : :obj:`~str`


    :Returns:

        :obj:`~PropagatorSP3File`


.. py:method:: item(self, index: int) -> PropagatorSP3File
    :canonical: br.steak.core.stkobjects.PropagatorSP3FileCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~PropagatorSP3File`

.. py:method:: remove_all(self) -> None
    :canonical: br.steak.core.stkobjects.PropagatorSP3FileCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.PropagatorSP3FileCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


