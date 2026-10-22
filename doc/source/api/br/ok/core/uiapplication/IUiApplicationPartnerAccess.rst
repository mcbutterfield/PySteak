IUiApplicationPartnerAccess
===========================

.. py:class:: br.ok.core.uiapplication.IUiApplicationPartnerAccess

   Access to the application object model for business partners.

.. py:currentmodule:: IUiApplicationPartnerAccess

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.uiapplication.IUiApplicationPartnerAccess.grant_partner_access`
              - Provide object model root for authorized business partners.

Import detail
-------------

.. code-block:: python

    from br.ok.core.uiapplication import IUiApplicationPartnerAccess



Method detail
-------------

.. py:method:: grant_partner_access(self, vendor: str, product: str, key: str) -> typing.Any
    :canonical: br.ok.core.uiapplication.IUiApplicationPartnerAccess.grant_partner_access

    Provide object model root for authorized business partners.

    :Parameters:

        **vendor** : :obj:`~str`

        **product** : :obj:`~str`

        **key** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

