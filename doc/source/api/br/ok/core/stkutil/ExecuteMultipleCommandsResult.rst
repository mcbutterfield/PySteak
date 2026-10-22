ExecuteMultipleCommandsResult
=============================

.. py:class:: br.ok.core.stkutil.ExecuteMultipleCommandsResult

   Collection of objects returned by the ExecuteMultipleCommands.

.. py:currentmodule:: ExecuteMultipleCommandsResult

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.ExecuteMultipleCommandsResult.item`
              - Get the element at the specified index (0-based).

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.ExecuteMultipleCommandsResult._new_enum`
              - Return an object that can be used to iterate through all the objects in the collection.
            * - :py:attr:`~br.ok.core.stkutil.ExecuteMultipleCommandsResult.count`
              - Number of elements contained in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkutil import ExecuteMultipleCommandsResult


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkutil.ExecuteMultipleCommandsResult._new_enum
    :type: EnumeratorProxy

    Return an object that can be used to iterate through all the objects in the collection.

.. py:property:: count
    :canonical: br.ok.core.stkutil.ExecuteMultipleCommandsResult.count
    :type: int

    Number of elements contained in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ExecuteCommandResult
    :canonical: br.ok.core.stkutil.ExecuteMultipleCommandsResult.item

    Get the element at the specified index (0-based).

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ExecuteCommandResult`


