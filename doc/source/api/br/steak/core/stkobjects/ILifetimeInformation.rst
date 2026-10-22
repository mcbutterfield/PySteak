ILifetimeInformation
====================

.. py:class:: br.steak.core.stkobjects.ILifetimeInformation

   Provide the information about the lifetime of the object.

.. py:currentmodule:: ILifetimeInformation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ILifetimeInformation.has_been_deleted`
              - Determine if the object has been deleted or has become invalid due to some other modifications to its internal state.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ILifetimeInformation


Property detail
---------------

.. py:property:: has_been_deleted
    :canonical: br.steak.core.stkobjects.ILifetimeInformation.has_been_deleted
    :type: bool

    Determine if the object has been deleted or has become invalid due to some other modifications to its internal state.


