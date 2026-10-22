ADDSMessageCollection
=====================

.. py:class:: br.steak.core.stkobjects.aviator.ADDSMessageCollection

   Class defining a collection of messages from the NOAA ADDS service.

.. py:currentmodule:: ADDSMessageCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.ADDSMessageCollection.clear_messages`
              - Clear all of the messages in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ADDSMessageCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ADDSMessageCollection.remove_message`
              - Remove this message from the forecast.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.ADDSMessageCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.ADDSMessageCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.aviator import ADDSMessageCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.aviator.ADDSMessageCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.aviator.ADDSMessageCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------

.. py:method:: clear_messages(self) -> None
    :canonical: br.steak.core.stkobjects.aviator.ADDSMessageCollection.clear_messages

    Clear all of the messages in the collection.

    :Returns:

        :obj:`~None`


.. py:method:: item(self, index: int) -> ADDSMessage
    :canonical: br.steak.core.stkobjects.aviator.ADDSMessageCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ADDSMessage`

.. py:method:: remove_message(self, message: ADDSMessage) -> None
    :canonical: br.steak.core.stkobjects.aviator.ADDSMessageCollection.remove_message

    Remove this message from the forecast.

    :Parameters:

        **message** : :obj:`~ADDSMessage`


    :Returns:

        :obj:`~None`


