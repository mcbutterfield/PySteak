ScatteringPointCollection
=========================

.. py:class:: br.steak.core.stkobjects.ScatteringPointCollection

   Class defining a collection of scattering points.

.. py:currentmodule:: ScatteringPointCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ScatteringPointCollection.item`
              - Given an index, returns the element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ScatteringPointCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.steak.core.stkobjects.ScatteringPointCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ScatteringPointCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.ScatteringPointCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.ScatteringPointCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ScatteringPointCollectionElement
    :canonical: br.steak.core.stkobjects.ScatteringPointCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ScatteringPointCollectionElement`


