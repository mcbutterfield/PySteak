STKDesktopApplication
=====================

.. py:class:: br.steak.core.stkdesktop.STKDesktopApplication

   UiApplication

   Interact with an STK Desktop application.

   Use STKDesktop.StartApplication() or STKDesktop.AttachToApplication()
   to obtain an initialized STKDesktopApplication object.

.. py:currentmodule:: STKDesktopApplication


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkdesktop.STKDesktopApplication.new_grpc_call_batcher`
              - Construct a GrpcCallBatcher linked to this gRPC client that may be used to improve API performance.

                If gRPC is not active, the batcher will be disabled.
                max_batch is the maximum number of calls to batch together.
                Set disable_batching=True to disable batching operations for this batcher.
                See grpcutilities module for more information.
            * - :py:attr:`~br.steak.core.stkdesktop.STKDesktopApplication.new_object_model_context`
              - Create a new object model context for the STK Desktop application.
            * - :py:attr:`~br.steak.core.stkdesktop.STKDesktopApplication.set_grpc_options`
              - Set advanced-usage options for the gRPC client.

                Available options include:
                { "collection iteration batch size" : int }. Number of items to preload while iterating
                through a collection object. Default is 100. Use 0 to indicate no limit (load entire collection).
                { "disable batching" : bool }. Disable all batching operations.
                { "release batch size" : int }. Number of interfaces to be garbage collected before
                sending the entire batch to STK to be released. Default value is 12.
            * - :py:attr:`~br.steak.core.stkdesktop.STKDesktopApplication.shutdown`
              - Close this STK Desktop instance (or detach if the instance was obtained through STKDesktop.AttachToApplication()).

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkdesktop.STKDesktopApplication.root`
              - Get the object model root associated with this instance of STK Desktop application.

Import detail
-------------

.. code-block:: python

    from br.steak.core.stkdesktop import STKDesktopApplication


Property detail
---------------

.. py:property:: root
    :canonical: br.steak.core.stkdesktop.STKDesktopApplication.root
    :type: STKObjectRoot

    Get the object model root associated with this instance of STK Desktop application.


Method detail
-------------

.. py:method:: new_grpc_call_batcher(self, max_batch: int = None, disable_batching: bool = False) -> GrpcCallBatcher
    :canonical: br.steak.core.stkdesktop.STKDesktopApplication.new_grpc_call_batcher

    Construct a GrpcCallBatcher linked to this gRPC client that may be used to improve API performance.

    If gRPC is not active, the batcher will be disabled.
    max_batch is the maximum number of calls to batch together.
    Set disable_batching=True to disable batching operations for this batcher.
    See grpcutilities module for more information.

    :Parameters:

        **max_batch** : :obj:`~int`

        **disable_batching** : :obj:`~bool`


    :Returns:

        :obj:`~GrpcCallBatcher`

.. py:method:: new_object_model_context(self) -> STKObjectModelContext
    :canonical: br.steak.core.stkdesktop.STKDesktopApplication.new_object_model_context

    Create a new object model context for the STK Desktop application.

    :Returns:

        :obj:`~STKObjectModelContext`

.. py:method:: set_grpc_options(self, options: dict) -> None
    :canonical: br.steak.core.stkdesktop.STKDesktopApplication.set_grpc_options

    Set advanced-usage options for the gRPC client.

    Available options include:
    { "collection iteration batch size" : int }. Number of items to preload while iterating
    through a collection object. Default is 100. Use 0 to indicate no limit (load entire collection).
    { "disable batching" : bool }. Disable all batching operations.
    { "release batch size" : int }. Number of interfaces to be garbage collected before
    sending the entire batch to STK to be released. Default value is 12.

    :Parameters:

        **options** : :obj:`~dict`


    :Returns:

        :obj:`~None`

.. py:method:: shutdown(self) -> None
    :canonical: br.steak.core.stkdesktop.STKDesktopApplication.shutdown

    Close this STK Desktop instance (or detach if the instance was obtained through STKDesktop.AttachToApplication()).

    :Returns:

        :obj:`~None`


