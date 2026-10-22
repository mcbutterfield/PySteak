IComponentLinkEmbedControl
==========================

.. py:class:: br.steak.core.stkobjects.IComponentLinkEmbedControl

   Interface for a control which manages the linking or embedding of a component from the component browser.

.. py:currentmodule:: IComponentLinkEmbedControl

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.IComponentLinkEmbedControl.set_component`
              - Set the component by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.IComponentLinkEmbedControl.component`
              - Get the component interface.
            * - :py:attr:`~br.steak.core.stkobjects.IComponentLinkEmbedControl.reference_type`
              - Get or set the component reference type.
            * - :py:attr:`~br.steak.core.stkobjects.IComponentLinkEmbedControl.supported_components`
              - Get the list of supported component names.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import IComponentLinkEmbedControl


Property detail
---------------

.. py:property:: component
    :canonical: br.steak.core.stkobjects.IComponentLinkEmbedControl.component
    :type: IComponentInfo

    Get the component interface.

.. py:property:: reference_type
    :canonical: br.steak.core.stkobjects.IComponentLinkEmbedControl.reference_type
    :type: ComponentLinkEmbedControlReferenceType

    Get or set the component reference type.

.. py:property:: supported_components
    :canonical: br.steak.core.stkobjects.IComponentLinkEmbedControl.supported_components
    :type: list

    Get the list of supported component names.


Method detail
-------------




.. py:method:: set_component(self, component_name: str) -> None
    :canonical: br.steak.core.stkobjects.IComponentLinkEmbedControl.set_component

    Set the component by name.

    :Parameters:

        **component_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


