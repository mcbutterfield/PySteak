STKObjectPreDeleteEventArguments
================================

.. py:class:: br.steak.core.stkobjects.STKObjectPreDeleteEventArguments

   Arguments for the OnStkObjectPreDelete event.

.. py:currentmodule:: STKObjectPreDeleteEventArguments

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.STKObjectPreDeleteEventArguments.continue_object_deletion`
              - The status to continue or stop the object deletion.
            * - :py:attr:`~br.steak.core.stkobjects.STKObjectPreDeleteEventArguments.path`
              - Object path.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import STKObjectPreDeleteEventArguments


Property detail
---------------

.. py:property:: continue_object_deletion
    :canonical: br.steak.core.stkobjects.STKObjectPreDeleteEventArguments.continue_object_deletion
    :type: bool

    The status to continue or stop the object deletion.

.. py:property:: path
    :canonical: br.steak.core.stkobjects.STKObjectPreDeleteEventArguments.path
    :type: str

    Object path.


