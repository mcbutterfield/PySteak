ExternalFileMessageLevelType
============================

.. py:class:: br.steak.core.stkobjects.ExternalFileMessageLevelType

   IntEnum


.. py:currentmodule:: ExternalFileMessageLevelType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported message level.

            * - :py:attr:`~ERRORS`
              - Message level to report only errors found during file loading.

            * - :py:attr:`~WARNINGS`
              - Message level to report errors and warnings found during file loading.

            * - :py:attr:`~VERBOSE`
              - Message level to report errors and warnings found during file loading and provide a success message when finding no issues.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ExternalFileMessageLevelType


