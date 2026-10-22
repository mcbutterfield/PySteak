ObjectCollection
================

.. py:class:: br.steak.core.graphics.ObjectCollection

   A collection of objects.

.. py:currentmodule:: ObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.ObjectCollection.item`
              - Return an item in the collection at the specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.ObjectCollection._new_enum`
              - Return an enumerator that iterates through the collection.
            * - :py:attr:`~br.steak.core.graphics.ObjectCollection.count`
              - A total number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import ObjectCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.graphics.ObjectCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.

.. py:property:: count
    :canonical: br.steak.core.graphics.ObjectCollection.count
    :type: int

    A total number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> typing.Any
    :canonical: br.steak.core.graphics.ObjectCollection.item

    Return an item in the collection at the specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~typing.Any`


