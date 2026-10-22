KmlDocumentCollection
=====================

.. py:class:: br.steak.core.graphics.KmlDocumentCollection

   A collection of KML documents.

.. py:currentmodule:: KmlDocumentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.KmlDocumentCollection.item`
              - Get an element at the specified position in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.KmlDocumentCollection._new_enum`
              - Return an enumerator that iterates through the collection.
            * - :py:attr:`~br.steak.core.graphics.KmlDocumentCollection.count`
              - A total number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import KmlDocumentCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.graphics.KmlDocumentCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.

.. py:property:: count
    :canonical: br.steak.core.graphics.KmlDocumentCollection.count
    :type: int

    A total number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> KmlDocument
    :canonical: br.steak.core.graphics.KmlDocumentCollection.item

    Get an element at the specified position in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~KmlDocument`


