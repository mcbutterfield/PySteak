ICelestialBodyInformationCollection
===================================

.. py:class:: br.ok.core.stkobjects.ICelestialBodyInformationCollection

   Represents a collection of celestial bodies.

.. py:currentmodule:: ICelestialBodyInformationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ICelestialBodyInformationCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ICelestialBodyInformationCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.ICelestialBodyInformationCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~br.ok.core.stkobjects.ICelestialBodyInformationCollection.recycle`
              - Control whether to reuse the same celestial info object when accessing the elements of the collection.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ICelestialBodyInformationCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.ICelestialBodyInformationCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.ICelestialBodyInformationCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: recycle
    :canonical: br.ok.core.stkobjects.ICelestialBodyInformationCollection.recycle
    :type: bool

    Control whether to reuse the same celestial info object when accessing the elements of the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ICelestialBodyInformation
    :canonical: br.ok.core.stkobjects.ICelestialBodyInformationCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ICelestialBodyInformation`




