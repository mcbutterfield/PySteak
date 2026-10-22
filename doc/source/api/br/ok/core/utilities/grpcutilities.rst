The ``grpcutilities`` module
============================

.. py:module:: br.ok.core.utilities.grpcutilities

Summary
-------

.. tab-set::

    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:class:`~br.ok.core.utilities.grpcutilities.GrpcAuthenticationMode`
              - Specify the method of client-server authentication to use for gRPC.

            * - :py:class:`~br.ok.core.utilities.grpcutilities.GrpcCallBatcher`
              - A class used to batch together API calls to optimize performance.



Description
-----------

Optimize performance of gRPC communications.

GrpcCallBatcher may be used to reduce the number of remote communications
by batching together API commands that do not require return values.

.. py:currentmodule:: br.ok.core.utilities.grpcutilities

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     GrpcAuthenticationMode<grpcutilities/GrpcAuthenticationMode>
     GrpcCallBatcher<grpcutilities/GrpcCallBatcher>


