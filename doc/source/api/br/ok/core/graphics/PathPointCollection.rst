PathPointCollection
===================

.. py:class:: br.ok.core.graphics.PathPointCollection

   A collection of path points.

.. py:currentmodule:: PathPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.PathPointCollection.item`
              - Return a path point at the specified position in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.PathPointCollection._new_enum`
              - Return an enumerator that iterates through the collection.
            * - :py:attr:`~br.ok.core.graphics.PathPointCollection.count`
              - A total number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import PathPointCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.graphics.PathPointCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.

.. py:property:: count
    :canonical: br.ok.core.graphics.PathPointCollection.count
    :type: int

    A total number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> PathPoint
    :canonical: br.ok.core.graphics.PathPointCollection.item

    Return a path point at the specified position in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~PathPoint`


