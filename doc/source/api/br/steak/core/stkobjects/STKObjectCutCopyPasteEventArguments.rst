STKObjectCutCopyPasteEventArguments
===================================

.. py:class:: br.steak.core.stkobjects.STKObjectCutCopyPasteEventArguments

   Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

.. py:currentmodule:: STKObjectCutCopyPasteEventArguments

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.STKObjectCutCopyPasteEventArguments.object_paths`
              - Return an array of object paths that are cut, copied or pasted.
            * - :py:attr:`~br.steak.core.stkobjects.STKObjectCutCopyPasteEventArguments.pasted_object_paths`
              - Return an array of object paths that are being pasted. The new object paths corresposnd to the old paths at the same array location in ObjectPaths array.
            * - :py:attr:`~br.steak.core.stkobjects.STKObjectCutCopyPasteEventArguments.selected_object_path`
              - Selected Object path that is being cut, copied or pasted.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import STKObjectCutCopyPasteEventArguments


Property detail
---------------

.. py:property:: object_paths
    :canonical: br.steak.core.stkobjects.STKObjectCutCopyPasteEventArguments.object_paths
    :type: list

    Return an array of object paths that are cut, copied or pasted.

.. py:property:: pasted_object_paths
    :canonical: br.steak.core.stkobjects.STKObjectCutCopyPasteEventArguments.pasted_object_paths
    :type: list

    Return an array of object paths that are being pasted. The new object paths corresposnd to the old paths at the same array location in ObjectPaths array.

.. py:property:: selected_object_path
    :canonical: br.steak.core.stkobjects.STKObjectCutCopyPasteEventArguments.selected_object_path
    :type: str

    Selected Object path that is being cut, copied or pasted.


