DataProviderFixed
=================

.. py:class:: br.steak.core.stkobjects.DataProviderFixed

   Bases: :py:class:`~br.steak.core.stkobjects.IDataProvider`, :py:class:`~br.steak.core.stkobjects.IDataProviderInfo`

   Support for fixed data providers (i.e. non time-dependent like Facility position).

.. py:currentmodule:: DataProviderFixed

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviderFixed.execute`
              - Compute the data; fixed data providers do not require arguments.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviderFixed.execute_elements`
              - Compute the data and returns just the indicated data elements; fixed data providers do not require arguments.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import DataProviderFixed



Method detail
-------------

.. py:method:: execute(self) -> DataProviderResult
    :canonical: br.steak.core.stkobjects.DataProviderFixed.execute

    Compute the data; fixed data providers do not require arguments.

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_elements(self, element_names: list) -> DataProviderResult
    :canonical: br.steak.core.stkobjects.DataProviderFixed.execute_elements

    Compute the data and returns just the indicated data elements; fixed data providers do not require arguments.

    :Parameters:

        **element_names** : :obj:`~list`


    :Returns:

        :obj:`~DataProviderResult`

