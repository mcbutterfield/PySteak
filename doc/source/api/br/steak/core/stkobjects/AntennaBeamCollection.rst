AntennaBeamCollection
=====================

.. py:class:: br.steak.core.stkobjects.AntennaBeamCollection

   Class defining an antenna beam collection.

.. py:currentmodule:: AntennaBeamCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AntennaBeamCollection.add`
              - Add a new beam to the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaBeamCollection.insert_at`
              - Insert a new beam at the supplied index.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaBeamCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaBeamCollection.remove_at`
              - Remove the layer with the specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AntennaBeamCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaBeamCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AntennaBeamCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.AntennaBeamCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.AntennaBeamCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add(self) -> IAntennaBeam
    :canonical: br.steak.core.stkobjects.AntennaBeamCollection.add

    Add a new beam to the collection.

    :Returns:

        :obj:`~IAntennaBeam`


.. py:method:: insert_at(self, index: int) -> IAntennaBeam
    :canonical: br.steak.core.stkobjects.AntennaBeamCollection.insert_at

    Insert a new beam at the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IAntennaBeam`

.. py:method:: item(self, index: int) -> IAntennaBeam
    :canonical: br.steak.core.stkobjects.AntennaBeamCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IAntennaBeam`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.AntennaBeamCollection.remove_at

    Remove the layer with the specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


