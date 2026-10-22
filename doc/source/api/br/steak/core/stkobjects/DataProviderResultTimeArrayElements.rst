DataProviderResultTimeArrayElements
===================================

.. py:class:: br.steak.core.stkobjects.DataProviderResultTimeArrayElements

   Provide a array result of element values for each time array value.

.. py:currentmodule:: DataProviderResultTimeArrayElements

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultTimeArrayElements.get_array`
              - Return an array of values at the specified index.  Valid values of index range from 0 to Count-1.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultTimeArrayElements.count`
              - Get the number of arrays in the result.
            * - :py:attr:`~br.steak.core.stkobjects.DataProviderResultTimeArrayElements.valid`
              - Return true if the result is valid, false otherwise.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import DataProviderResultTimeArrayElements


Property detail
---------------

.. py:property:: count
    :canonical: br.steak.core.stkobjects.DataProviderResultTimeArrayElements.count
    :type: int

    Get the number of arrays in the result.

.. py:property:: valid
    :canonical: br.steak.core.stkobjects.DataProviderResultTimeArrayElements.valid
    :type: bool

    Return true if the result is valid, false otherwise.


Method detail
-------------


.. py:method:: get_array(self, index_or_name: typing.Any) -> list
    :canonical: br.steak.core.stkobjects.DataProviderResultTimeArrayElements.get_array

    Return an array of values at the specified index.  Valid values of index range from 0 to Count-1.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`


