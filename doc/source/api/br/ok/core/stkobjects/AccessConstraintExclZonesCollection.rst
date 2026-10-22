AccessConstraintExclZonesCollection
===================================

.. py:class:: br.ok.core.stkobjects.AccessConstraintExclZonesCollection

   Bases: :py:class:`~br.ok.core.stkobjects.IAccessConstraint`

   Collection of Exclusion Zones used in Exclusion Zone constraint.

.. py:currentmodule:: AccessConstraintExclZonesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.change_exclusion_zone`
              - Update Exclusion Zone data at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.get_exclusion_zone`
              - Return min and max lat/lon values at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.item`
              - Get an AccessConstraintLatitudeLongitudeZone interface using an index.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.remove_all`
              - Remove all items from the collection.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.remove_exclusion_zone`
              - Remove an Exclusion Zone using the min and max lat/lon values. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.remove_index`
              - Remove an item given an index.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.to_array`
              - Return a four-dimensional array of min/max lat/lon values beginning at a given position and having specified number of rows.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection._new_enum`
              - Enumerate the AccessConstraintLatitudeLongitudeZone interfaces.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.constraint_name`
              - Get the constraint name.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.constraint_type`
              - Get the constraint type.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.count`
              - Number of items in the collection.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.enabled`
              - Indicate whether the constraint should be considered (true) or ignored (false) in access computations.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.exclusion_interval`
              - Get or set the ExclInterval.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.is_plugin`
              - Return true if the access constraint is a plugin.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.maximum_relative_motion`
              - Maximum relative motion used in adaptive sampling.
            * - :py:attr:`~br.ok.core.stkobjects.AccessConstraintExclZonesCollection.maximum_time_step`
              - Maximum time step used in adaptive sampling.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AccessConstraintExclZonesCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection._new_enum
    :type: EnumeratorProxy

    Enumerate the AccessConstraintLatitudeLongitudeZone interfaces.

.. py:property:: constraint_name
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.constraint_name
    :type: str

    Get the constraint name.

.. py:property:: constraint_type
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.constraint_type
    :type: AccessConstraintType

    Get the constraint type.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.count
    :type: int

    Number of items in the collection.

.. py:property:: enabled
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.enabled
    :type: bool

    Indicate whether the constraint should be considered (true) or ignored (false) in access computations.

.. py:property:: exclusion_interval
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.exclusion_interval
    :type: bool

    Get or set the ExclInterval.

.. py:property:: is_plugin
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.is_plugin
    :type: bool

    Return true if the access constraint is a plugin.

.. py:property:: maximum_relative_motion
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.maximum_relative_motion
    :type: float

    Maximum relative motion used in adaptive sampling.

.. py:property:: maximum_time_step
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.maximum_time_step
    :type: float

    Maximum time step used in adaptive sampling.


Method detail
-------------

.. py:method:: change_exclusion_zone(self, index: int, min_lat: typing.Any, min_lon: typing.Any, max_lat: typing.Any, max_lon: typing.Any) -> None
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.change_exclusion_zone

    Update Exclusion Zone data at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

        **index** : :obj:`~int`

        **min_lat** : :obj:`~typing.Any`

        **min_lon** : :obj:`~typing.Any`

        **max_lat** : :obj:`~typing.Any`

        **max_lon** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`








.. py:method:: get_exclusion_zone(self, index: int) -> typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.get_exclusion_zone

    Return min and max lat/lon values at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]`


.. py:method:: item(self, index: int) -> AccessConstraintLatitudeLongitudeZone
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.item

    Get an AccessConstraintLatitudeLongitudeZone interface using an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~AccessConstraintLatitudeLongitudeZone`





.. py:method:: remove_all(self) -> None
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.remove_all

    Remove all items from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_exclusion_zone(self, min_lat: typing.Any, min_lon: typing.Any, max_lat: typing.Any, max_lon: typing.Any) -> None
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.remove_exclusion_zone

    Remove an Exclusion Zone using the min and max lat/lon values. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

        **min_lat** : :obj:`~typing.Any`

        **min_lon** : :obj:`~typing.Any`

        **max_lat** : :obj:`~typing.Any`

        **max_lon** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: remove_index(self, index: int) -> None
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.remove_index

    Remove an item given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: to_array(self, index: int, length: int) -> list
    :canonical: br.ok.core.stkobjects.AccessConstraintExclZonesCollection.to_array

    Return a four-dimensional array of min/max lat/lon values beginning at a given position and having specified number of rows.

    :Parameters:

        **index** : :obj:`~int`

        **length** : :obj:`~int`


    :Returns:

        :obj:`~list`


