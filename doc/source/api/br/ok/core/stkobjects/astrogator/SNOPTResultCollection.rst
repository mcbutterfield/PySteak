SNOPTResultCollection
=====================

.. py:class:: br.ok.core.stkobjects.astrogator.SNOPTResultCollection

   SNOPT result collection.

.. py:currentmodule:: SNOPTResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SNOPTResultCollection.get_result_by_paths`
              - Return the result specified by the object/result names.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SNOPTResultCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SNOPTResultCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SNOPTResultCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import SNOPTResultCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.astrogator.SNOPTResultCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.astrogator.SNOPTResultCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------


.. py:method:: get_result_by_paths(self, object_path: str, result_path: str) -> SNOPTResult
    :canonical: br.ok.core.stkobjects.astrogator.SNOPTResultCollection.get_result_by_paths

    Return the result specified by the object/result names.

    :Parameters:

        **object_path** : :obj:`~str`

        **result_path** : :obj:`~str`


    :Returns:

        :obj:`~SNOPTResult`

.. py:method:: item(self, index: int) -> SNOPTResult
    :canonical: br.ok.core.stkobjects.astrogator.SNOPTResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SNOPTResult`


