IConnect
========

.. py:class:: br.ok.core.stkobjects.aviator.IConnect

   Interface used to send connect commands to Aviator objects.

.. py:currentmodule:: IConnect

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.IConnect.execute_command`
              - Send a connect command to an Aviator object.

Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import IConnect



Method detail
-------------

.. py:method:: execute_command(self, command: str) -> typing.Any
    :canonical: br.ok.core.stkobjects.aviator.IConnect.execute_command

    Send a connect command to an Aviator object.

    :Parameters:

        **command** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

