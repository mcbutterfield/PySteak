RFInterference
==============

.. py:class:: br.steak.core.stkobjects.RFInterference

   Class defining radar jamming.

.. py:currentmodule:: RFInterference

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RFInterference.emitters`
              - Get the interference emitters collection.
            * - :py:attr:`~br.steak.core.stkobjects.RFInterference.enabled`
              - Get or set whether the interference is enabled or disabled.
            * - :py:attr:`~br.steak.core.stkobjects.RFInterference.include_active_comm_system_interference_emitters`
              - Get or set whether the emitters from the active CommSystem object are included in their interference computation.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RFInterference


Property detail
---------------

.. py:property:: emitters
    :canonical: br.steak.core.stkobjects.RFInterference.emitters
    :type: ObjectLinkCollection

    Get the interference emitters collection.

.. py:property:: enabled
    :canonical: br.steak.core.stkobjects.RFInterference.enabled
    :type: bool

    Get or set whether the interference is enabled or disabled.

.. py:property:: include_active_comm_system_interference_emitters
    :canonical: br.steak.core.stkobjects.RFInterference.include_active_comm_system_interference_emitters
    :type: bool

    Get or set whether the emitters from the active CommSystem object are included in their interference computation.


