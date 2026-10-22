STKObjectModelContext
=====================

.. py:class:: br.ok.core.stkobjects.STKObjectModelContext

   STKObjectModelContext class provides methods to create instance of STKObjectRoot class.

.. py:currentmodule:: STKObjectModelContext

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.STKObjectModelContext.create`
              - Create a non-restrictive root object.
            * - :py:attr:`~br.ok.core.stkobjects.STKObjectModelContext.create_restrictive`
              - Create a restrictive root object.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import STKObjectModelContext



Method detail
-------------

.. py:method:: create(self) -> STKObjectRoot
    :canonical: br.ok.core.stkobjects.STKObjectModelContext.create

    Create a non-restrictive root object.

    :Returns:

        :obj:`~STKObjectRoot`

.. py:method:: create_restrictive(self) -> STKObjectRoot
    :canonical: br.ok.core.stkobjects.STKObjectModelContext.create_restrictive

    Create a restrictive root object.

    :Returns:

        :obj:`~STKObjectRoot`

