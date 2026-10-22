ScenarioDatabaseCollection
==========================

.. py:class:: br.steak.core.stkobjects.ScenarioDatabaseCollection

   Collection of Scenario database settings.

.. py:currentmodule:: ScenarioDatabaseCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ScenarioDatabaseCollection.item`
              - Return scenario database settings at a specified position.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ScenarioDatabaseCollection._new_enum`
              - Enumerates the elements in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.ScenarioDatabaseCollection.count`
              - Return a number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ScenarioDatabaseCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.ScenarioDatabaseCollection._new_enum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.ScenarioDatabaseCollection.count
    :type: int

    Return a number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ScenarioDatabase
    :canonical: br.steak.core.stkobjects.ScenarioDatabaseCollection.item

    Return scenario database settings at a specified position.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ScenarioDatabase`


