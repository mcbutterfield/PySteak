IComponentInfo
==============

.. py:class:: br.ok.core.stkobjects.IComponentInfo

   Interface for a component.

.. py:currentmodule:: IComponentInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IComponentInfo.export`
              - Export the component with default component name as file name and component type as file extension to the scenario directory.
            * - :py:attr:`~br.ok.core.stkobjects.IComponentInfo.export_with_filename_path`
              - Export the component with specified file name and location.
            * - :py:attr:`~br.ok.core.stkobjects.IComponentInfo.is_read_only`
              - Return true if the component is read-only.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IComponentInfo.description`
              - Get the description for this component.
            * - :py:attr:`~br.ok.core.stkobjects.IComponentInfo.name`
              - Get or set the component name.
            * - :py:attr:`~br.ok.core.stkobjects.IComponentInfo.user_comment`
              - Get or set the user comment for this component.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IComponentInfo


Property detail
---------------

.. py:property:: description
    :canonical: br.ok.core.stkobjects.IComponentInfo.description
    :type: str

    Get the description for this component.

.. py:property:: name
    :canonical: br.ok.core.stkobjects.IComponentInfo.name
    :type: str

    Get or set the component name.

.. py:property:: user_comment
    :canonical: br.ok.core.stkobjects.IComponentInfo.user_comment
    :type: str

    Get or set the user comment for this component.


Method detail
-------------


.. py:method:: export(self) -> None
    :canonical: br.ok.core.stkobjects.IComponentInfo.export

    Export the component with default component name as file name and component type as file extension to the scenario directory.

    :Returns:

        :obj:`~None`

.. py:method:: export_with_filename_path(self, filename_path: str) -> None
    :canonical: br.ok.core.stkobjects.IComponentInfo.export_with_filename_path

    Export the component with specified file name and location.

    :Parameters:

        **filename_path** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: is_read_only(self) -> bool
    :canonical: br.ok.core.stkobjects.IComponentInfo.is_read_only

    Return true if the component is read-only.

    :Returns:

        :obj:`~bool`





