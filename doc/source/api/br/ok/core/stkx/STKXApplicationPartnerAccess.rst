STKXApplicationPartnerAccess
============================

.. py:class:: br.ok.core.stkx.STKXApplicationPartnerAccess

   STK X Application Partner Access object.

.. py:currentmodule:: STKXApplicationPartnerAccess

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkx.STKXApplicationPartnerAccess.grant_partner_access`
              - Provide object model root for authorized business partners.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkx import STKXApplicationPartnerAccess



Method detail
-------------

.. py:method:: grant_partner_access(self, vendor: str, product: str, key: str) -> STKXApplication
    :canonical: br.ok.core.stkx.STKXApplicationPartnerAccess.grant_partner_access

    Provide object model root for authorized business partners.

    :Parameters:

        **vendor** : :obj:`~str`

        **product** : :obj:`~str`

        **key** : :obj:`~str`


    :Returns:

        :obj:`~STKXApplication`

