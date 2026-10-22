RadarSarImageLocationCollection
===============================

.. py:class:: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection

   A collection of image location information.

.. py:currentmodule:: RadarSarImageLocationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.add_new`
              - Add and returns a new SAR image location.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.contains`
              - Check to see if a given SAR image location exists in the collection.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.find`
              - Find a SAR image location by name. Returns Null if the image location name does not exist in the collection.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.remove`
              - Remove the supplied SAR image location from the collection.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.remove_all`
              - Clear all SAR image locations from the collection.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.remove_at`
              - Remove the SAR image location with the supplied index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkrfchannelmodeler import RadarSarImageLocationCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add_new(self) -> RadarSarImageLocation
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.add_new

    Add and returns a new SAR image location.

    :Returns:

        :obj:`~RadarSarImageLocation`

.. py:method:: contains(self, name_str: str) -> bool
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.contains

    Check to see if a given SAR image location exists in the collection.

    :Parameters:

        **name_str** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: find(self, name_str: str) -> RadarSarImageLocation
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.find

    Find a SAR image location by name. Returns Null if the image location name does not exist in the collection.

    :Parameters:

        **name_str** : :obj:`~str`


    :Returns:

        :obj:`~RadarSarImageLocation`

.. py:method:: item(self, index: int) -> RadarSarImageLocation
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~RadarSarImageLocation`

.. py:method:: remove(self, name_str: str) -> None
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.remove

    Remove the supplied SAR image location from the collection.

    :Parameters:

        **name_str** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.remove_all

    Clear all SAR image locations from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.steak.core.stkrfchannelmodeler.RadarSarImageLocationCollection.remove_at

    Remove the SAR image location with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


