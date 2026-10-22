RuntimeTypeInfo
===============

.. py:class:: br.ok.core.stkutil.RuntimeTypeInfo

   Runtime Type info coclass.

.. py:currentmodule:: RuntimeTypeInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.RuntimeTypeInfo.get_item`
              - Return the property of the collection at the given index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.RuntimeTypeInfo.count`
              - If the interface is a collection, returns the collection count.
            * - :py:attr:`~br.ok.core.stkutil.RuntimeTypeInfo.is_collection`
              - Determine if the interface is a collection.
            * - :py:attr:`~br.ok.core.stkutil.RuntimeTypeInfo.properties`
              - Get the collection of properties.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkutil import RuntimeTypeInfo


Property detail
---------------

.. py:property:: count
    :canonical: br.ok.core.stkutil.RuntimeTypeInfo.count
    :type: int

    If the interface is a collection, returns the collection count.

.. py:property:: is_collection
    :canonical: br.ok.core.stkutil.RuntimeTypeInfo.is_collection
    :type: bool

    Determine if the interface is a collection.

.. py:property:: properties
    :canonical: br.ok.core.stkutil.RuntimeTypeInfo.properties
    :type: PropertyInfoCollection

    Get the collection of properties.


Method detail
-------------


.. py:method:: get_item(self, index: int) -> PropertyInfo
    :canonical: br.ok.core.stkutil.RuntimeTypeInfo.get_item

    Return the property of the collection at the given index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~PropertyInfo`



