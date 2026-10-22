UnitPreferencesUnitCollection
=============================

.. py:class:: br.ok.core.stkutil.UnitPreferencesUnitCollection

   Object that contains a collection of UnitPreferencesUnit.

.. py:currentmodule:: UnitPreferencesUnitCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.UnitPreferencesUnitCollection.get_item_by_index`
              - Retrieve a unit from the collection by index.
            * - :py:attr:`~br.ok.core.stkutil.UnitPreferencesUnitCollection.get_item_by_name`
              - Retrieve a unit from the collection by name.
            * - :py:attr:`~br.ok.core.stkutil.UnitPreferencesUnitCollection.item`
              - Return the specific item in the collection given a unit identifier or an index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.UnitPreferencesUnitCollection._new_enum`
              - Return an enumeration of UnitPreferencesUnit.
            * - :py:attr:`~br.ok.core.stkutil.UnitPreferencesUnitCollection.count`
              - Return the number of items in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkutil import UnitPreferencesUnitCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkutil.UnitPreferencesUnitCollection._new_enum
    :type: EnumeratorProxy

    Return an enumeration of UnitPreferencesUnit.

.. py:property:: count
    :canonical: br.ok.core.stkutil.UnitPreferencesUnitCollection.count
    :type: int

    Return the number of items in the collection.


Method detail
-------------


.. py:method:: get_item_by_index(self, index: int) -> UnitPreferencesUnit
    :canonical: br.ok.core.stkutil.UnitPreferencesUnitCollection.get_item_by_index

    Retrieve a unit from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~UnitPreferencesUnit`

.. py:method:: get_item_by_name(self, name: str) -> UnitPreferencesUnit
    :canonical: br.ok.core.stkutil.UnitPreferencesUnitCollection.get_item_by_name

    Retrieve a unit from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UnitPreferencesUnit`

.. py:method:: item(self, index_or_name: typing.Any) -> UnitPreferencesUnit
    :canonical: br.ok.core.stkutil.UnitPreferencesUnitCollection.item

    Return the specific item in the collection given a unit identifier or an index.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~UnitPreferencesUnit`


