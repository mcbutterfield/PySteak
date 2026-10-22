KmlFeatureCollection
====================

.. py:class:: br.ok.core.graphics.KmlFeatureCollection

   A collection of KML features.

.. py:currentmodule:: KmlFeatureCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.KmlFeatureCollection.item`
              - Get an element at the specified position in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.KmlFeatureCollection._new_enum`
              - Return an enumerator that iterates through the collection.
            * - :py:attr:`~br.ok.core.graphics.KmlFeatureCollection.count`
              - A total number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import KmlFeatureCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.graphics.KmlFeatureCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.

.. py:property:: count
    :canonical: br.ok.core.graphics.KmlFeatureCollection.count
    :type: int

    A total number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IKmlFeature
    :canonical: br.ok.core.graphics.KmlFeatureCollection.item

    Get an element at the specified position in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IKmlFeature`


