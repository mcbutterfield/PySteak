EOIRMaterialElementCollection
=============================

.. py:class:: br.ok.core.stkobjects.EOIRMaterialElementCollection

   Collection of material elements.

.. py:currentmodule:: EOIRMaterialElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.EOIRMaterialElementCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.EOIRMaterialElementCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.EOIRMaterialElementCollection.count`
              - Return the number of elements in a collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import EOIRMaterialElementCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.EOIRMaterialElementCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.EOIRMaterialElementCollection.count
    :type: int

    Return the number of elements in a collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> EOIRMaterialElement
    :canonical: br.ok.core.stkobjects.EOIRMaterialElementCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~EOIRMaterialElement`


