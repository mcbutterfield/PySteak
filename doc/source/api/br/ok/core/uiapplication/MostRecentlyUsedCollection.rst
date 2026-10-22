MostRecentlyUsedCollection
==========================

.. py:class:: br.ok.core.uiapplication.MostRecentlyUsedCollection

   Provide information about most recently used (MRU) list.

.. py:currentmodule:: MostRecentlyUsedCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.uiapplication.MostRecentlyUsedCollection.item`
              - Get the MRU at the specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.uiapplication.MostRecentlyUsedCollection._new_enum`
              - Enumerates through the MRU collection.
            * - :py:attr:`~br.ok.core.uiapplication.MostRecentlyUsedCollection.count`
              - Get the total count of MRUs in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.uiapplication import MostRecentlyUsedCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.uiapplication.MostRecentlyUsedCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the MRU collection.

.. py:property:: count
    :canonical: br.ok.core.uiapplication.MostRecentlyUsedCollection.count
    :type: int

    Get the total count of MRUs in the collection.


Method detail
-------------


.. py:method:: item(self, index: typing.Any) -> str
    :canonical: br.ok.core.uiapplication.MostRecentlyUsedCollection.item

    Get the MRU at the specified index.

    :Parameters:

        **index** : :obj:`~typing.Any`


    :Returns:

        :obj:`~str`


