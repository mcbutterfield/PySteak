ExecuteMultipleCommandsResult
=============================

.. py:class:: br.steak.core.stkutil.ExecuteMultipleCommandsResult

   Collection of objects returned by the ExecuteMultipleCommands.

.. py:currentmodule:: ExecuteMultipleCommandsResult

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.ExecuteMultipleCommandsResult.item`
              - Get the element at the specified index (0-based).

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.ExecuteMultipleCommandsResult._new_enum`
              - Return an object that can be used to iterate through all the objects in the collection.
            * - :py:attr:`~br.steak.core.stkutil.ExecuteMultipleCommandsResult.count`
              - Number of elements contained in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkutil import ExecuteMultipleCommandsResult


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkutil.ExecuteMultipleCommandsResult._new_enum
    :type: EnumeratorProxy

    Return an object that can be used to iterate through all the objects in the collection.

.. py:property:: count
    :canonical: br.steak.core.stkutil.ExecuteMultipleCommandsResult.count
    :type: int

    Number of elements contained in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ExecuteCommandResult
    :canonical: br.steak.core.stkutil.ExecuteMultipleCommandsResult.item

    Get the element at the specified index (0-based).

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ExecuteCommandResult`


