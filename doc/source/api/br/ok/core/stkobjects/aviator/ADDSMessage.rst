ADDSMessage
===========

.. py:class:: br.ok.core.stkobjects.aviator.ADDSMessage

   Class defining a message from the NOAA ADDS service.

.. py:currentmodule:: ADDSMessage

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.ADDSMessage.message_time`
              - Get the message time for the ADDS message.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ADDSMessage.source`
              - Get the ADDS message source.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ADDSMessage.start_time`
              - Valid start time for the ADDS message.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ADDSMessage.stop_time`
              - Valid stop time for the ADDS message.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.ADDSMessage.type`
              - Get the ADDS message type.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import ADDSMessage


Property detail
---------------

.. py:property:: message_time
    :canonical: br.ok.core.stkobjects.aviator.ADDSMessage.message_time
    :type: typing.Any

    Get the message time for the ADDS message.

.. py:property:: source
    :canonical: br.ok.core.stkobjects.aviator.ADDSMessage.source
    :type: str

    Get the ADDS message source.

.. py:property:: start_time
    :canonical: br.ok.core.stkobjects.aviator.ADDSMessage.start_time
    :type: typing.Any

    Valid start time for the ADDS message.

.. py:property:: stop_time
    :canonical: br.ok.core.stkobjects.aviator.ADDSMessage.stop_time
    :type: typing.Any

    Valid stop time for the ADDS message.

.. py:property:: type
    :canonical: br.ok.core.stkobjects.aviator.ADDSMessage.type
    :type: ADDSForecastType

    Get the ADDS message type.


