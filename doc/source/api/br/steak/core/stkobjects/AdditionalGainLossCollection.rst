AdditionalGainLossCollection
============================

.. py:class:: br.steak.core.stkobjects.AdditionalGainLossCollection

   Class defining a collection of additional gains and losses.

.. py:currentmodule:: AdditionalGainLossCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AdditionalGainLossCollection.add`
              - Add and returns a new gain with the corresponding value.
            * - :py:attr:`~br.steak.core.stkobjects.AdditionalGainLossCollection.clear`
              - Clear all gain values from the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AdditionalGainLossCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AdditionalGainLossCollection.remove_at`
              - Remove the gain with the supplied index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AdditionalGainLossCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AdditionalGainLossCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AdditionalGainLossCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.AdditionalGainLossCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.AdditionalGainLossCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add(self, value: float) -> AdditionalGainLoss
    :canonical: br.steak.core.stkobjects.AdditionalGainLossCollection.add

    Add and returns a new gain with the corresponding value.

    :Parameters:

        **value** : :obj:`~float`


    :Returns:

        :obj:`~AdditionalGainLoss`

.. py:method:: clear(self) -> None
    :canonical: br.steak.core.stkobjects.AdditionalGainLossCollection.clear

    Clear all gain values from the collection.

    :Returns:

        :obj:`~None`


.. py:method:: item(self, index: int) -> AdditionalGainLoss
    :canonical: br.steak.core.stkobjects.AdditionalGainLossCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~AdditionalGainLoss`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.AdditionalGainLossCollection.remove_at

    Remove the gain with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


