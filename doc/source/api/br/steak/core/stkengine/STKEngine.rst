STKEngine
=========

.. py:class:: br.steak.core.stkengine.STKEngine

   object

   Initialize and manage the STK Engine application.

.. py:currentmodule:: STKEngine


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkengine.STKEngine.start_application`
              - Initialize STK Engine in-process and return the instance.

                Must only be used once per Python process.
                Specify no_graphics = True to start the application in no-graphics mode.

Import detail
-------------

.. code-block:: python

    from br.steak.core.stkengine import STKEngine


Method detail
-------------

.. py:method:: start_application(no_graphics: bool = True) -> STKEngineApplication
    :canonical: br.steak.core.stkengine.STKEngine.start_application

    Initialize STK Engine in-process and return the instance.

    Must only be used once per Python process.
    Specify no_graphics = True to start the application in no-graphics mode.

    :Parameters:

        **no_graphics** : :obj:`~bool`


    :Returns:

        :obj:`~STKEngineApplication`


