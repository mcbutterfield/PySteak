ElementCollection
=================

.. py:class:: br.ok.core.stkobjects.ElementCollection

   Class defining a phased array element collection.

.. py:currentmodule:: ElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ElementCollection.item`
              - Given an index, returns the element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ElementCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.ok.core.stkobjects.ElementCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ElementCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.ElementCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.ElementCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> Element
    :canonical: br.ok.core.stkobjects.ElementCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Element`


