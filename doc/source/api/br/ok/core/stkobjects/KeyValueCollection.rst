KeyValueCollection
==================

.. py:class:: br.ok.core.stkobjects.KeyValueCollection

   A collection of keys and values associated with the keys.

.. py:currentmodule:: KeyValueCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.contains`
              - Determine whether the collection contains the specified key.
            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.get_read_only`
              - Given a key, returns read-only flag.
            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.item`
              - Given a key, returns associated element.
            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.remove_all`
              - Remove all elements.
            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.remove_key`
              - Remove an element associated with specified key.
            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.set`
              - Set the value associated with specified key.
            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.set_read_only`
              - Given a key, sets read-only flag.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection._new_enum`
              - Return an enumerator containing the keys in the collection.
            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~br.ok.core.stkobjects.KeyValueCollection.keys`
              - Return an array of keys of the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import KeyValueCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.KeyValueCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator containing the keys in the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.KeyValueCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: keys
    :canonical: br.ok.core.stkobjects.KeyValueCollection.keys
    :type: list

    Return an array of keys of the collection.


Method detail
-------------

.. py:method:: contains(self, key: str) -> bool
    :canonical: br.ok.core.stkobjects.KeyValueCollection.contains

    Determine whether the collection contains the specified key.

    :Parameters:

        **key** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: get_read_only(self, key: str) -> bool
    :canonical: br.ok.core.stkobjects.KeyValueCollection.get_read_only

    Given a key, returns read-only flag.

    :Parameters:

        **key** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: item(self, key: str) -> str
    :canonical: br.ok.core.stkobjects.KeyValueCollection.item

    Given a key, returns associated element.

    :Parameters:

        **key** : :obj:`~str`


    :Returns:

        :obj:`~str`


.. py:method:: remove_all(self) -> None
    :canonical: br.ok.core.stkobjects.KeyValueCollection.remove_all

    Remove all elements.

    :Returns:

        :obj:`~None`

.. py:method:: remove_key(self, key: str) -> bool
    :canonical: br.ok.core.stkobjects.KeyValueCollection.remove_key

    Remove an element associated with specified key.

    :Parameters:

        **key** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: set(self, key: str, value: str) -> None
    :canonical: br.ok.core.stkobjects.KeyValueCollection.set

    Set the value associated with specified key.

    :Parameters:

        **key** : :obj:`~str`

        **value** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_read_only(self, key: str, is_read_only: bool) -> None
    :canonical: br.ok.core.stkobjects.KeyValueCollection.set_read_only

    Given a key, sets read-only flag.

    :Parameters:

        **key** : :obj:`~str`

        **is_read_only** : :obj:`~bool`


    :Returns:

        :obj:`~None`


