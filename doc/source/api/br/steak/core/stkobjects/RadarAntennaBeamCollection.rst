RadarAntennaBeamCollection
==========================

.. py:class:: br.steak.core.stkobjects.RadarAntennaBeamCollection

   Class defining an radar antenna beam collection.

.. py:currentmodule:: RadarAntennaBeamCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarAntennaBeamCollection.add`
              - Add a new beam to the collection.
            * - :py:attr:`~br.steak.core.stkobjects.RadarAntennaBeamCollection.duplicate_beam`
              - Duplicates the beam at the specified index.
            * - :py:attr:`~br.steak.core.stkobjects.RadarAntennaBeamCollection.insert_at`
              - Insert a new beam at the supplied index.
            * - :py:attr:`~br.steak.core.stkobjects.RadarAntennaBeamCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~br.steak.core.stkobjects.RadarAntennaBeamCollection.remove_at`
              - Remove the layer with the specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarAntennaBeamCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.steak.core.stkobjects.RadarAntennaBeamCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RadarAntennaBeamCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.RadarAntennaBeamCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.RadarAntennaBeamCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add(self) -> RadarAntennaBeam
    :canonical: br.steak.core.stkobjects.RadarAntennaBeamCollection.add

    Add a new beam to the collection.

    :Returns:

        :obj:`~RadarAntennaBeam`


.. py:method:: duplicate_beam(self, index: int) -> RadarAntennaBeam
    :canonical: br.steak.core.stkobjects.RadarAntennaBeamCollection.duplicate_beam

    Duplicates the beam at the specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~RadarAntennaBeam`

.. py:method:: insert_at(self, index: int) -> RadarAntennaBeam
    :canonical: br.steak.core.stkobjects.RadarAntennaBeamCollection.insert_at

    Insert a new beam at the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~RadarAntennaBeam`

.. py:method:: item(self, index: int) -> RadarAntennaBeam
    :canonical: br.steak.core.stkobjects.RadarAntennaBeamCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~RadarAntennaBeam`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.RadarAntennaBeamCollection.remove_at

    Remove the layer with the specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


