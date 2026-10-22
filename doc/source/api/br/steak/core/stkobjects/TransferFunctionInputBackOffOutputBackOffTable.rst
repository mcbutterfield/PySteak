TransferFunctionInputBackOffOutputBackOffTable
==============================================

.. py:class:: br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable

   Class defining an input back off vs output back off table.

.. py:currentmodule:: TransferFunctionInputBackOffOutputBackOffTable

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.add`
              - Add and returns a new row.
            * - :py:attr:`~br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.insert_at`
              - Insert and returns a new row at the supplied index.
            * - :py:attr:`~br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.remove_at`
              - Remove the row with the supplied index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import TransferFunctionInputBackOffOutputBackOffTable


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add(self, input_back_off: float, output_back_off: float) -> TransferFunctionInputBackOffOutputBackOffTableRow
    :canonical: br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.add

    Add and returns a new row.

    :Parameters:

        **input_back_off** : :obj:`~float`

        **output_back_off** : :obj:`~float`


    :Returns:

        :obj:`~TransferFunctionInputBackOffOutputBackOffTableRow`


.. py:method:: insert_at(self, index: int, input_back_off: float, output_back_off: float) -> TransferFunctionInputBackOffOutputBackOffTableRow
    :canonical: br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.insert_at

    Insert and returns a new row at the supplied index.

    :Parameters:

        **index** : :obj:`~int`

        **input_back_off** : :obj:`~float`

        **output_back_off** : :obj:`~float`


    :Returns:

        :obj:`~TransferFunctionInputBackOffOutputBackOffTableRow`

.. py:method:: item(self, index: int) -> TransferFunctionInputBackOffOutputBackOffTableRow
    :canonical: br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~TransferFunctionInputBackOffOutputBackOffTableRow`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.remove_at

    Remove the row with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


