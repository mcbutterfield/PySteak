GridSearchResultCollection
==========================

.. py:class:: br.ok.core.stkobjects.astrogator.GridSearchResultCollection

   Properties for the list of Grid Search result parameters.

.. py:currentmodule:: GridSearchResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.GridSearchResultCollection.get_result_by_paths`
              - Return the result specified by the object/result path.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.GridSearchResultCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.GridSearchResultCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.GridSearchResultCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import GridSearchResultCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.astrogator.GridSearchResultCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.astrogator.GridSearchResultCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------


.. py:method:: get_result_by_paths(self, object_path: str, result_path: str) -> GridSearchResult
    :canonical: br.ok.core.stkobjects.astrogator.GridSearchResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

        **object_path** : :obj:`~str`

        **result_path** : :obj:`~str`


    :Returns:

        :obj:`~GridSearchResult`

.. py:method:: item(self, index: int) -> GridSearchResult
    :canonical: br.ok.core.stkobjects.astrogator.GridSearchResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~GridSearchResult`


