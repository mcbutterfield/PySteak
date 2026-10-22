CustomImageGlobeOverlay
=======================

.. py:class:: br.steak.core.graphics.CustomImageGlobeOverlay

   Bases: :py:class:`~br.steak.core.graphics.IGlobeImageOverlay`, :py:class:`~br.steak.core.graphics.IGlobeOverlay`

   A globe image overlay that allows for a user defined image to be specified.

.. py:currentmodule:: CustomImageGlobeOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlay.clear_cache`
              - Clear the image data cache associated with this instance. This is equivalent to deleting and re-adding the overlay.
            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlay.read`
              - Read a tile from the specified extent, scales it to and stores the result in image.
            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlay.reload`
              - Reload the image data associated with this instance. Preserves the current image data until new image data replaces it.
            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlay.shut_down`
              - Initiate shutdown when imagery is being removed from the globe.
            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlay.start_up`
              - Initiate start-up when imagery is being added to the globe.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlay.is_translucent`
              - Get whether the overlay contains translucent imagery.
            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlay.maximum_meters_per_pixel`
              - Get the maximum resolution of the inlay in meters per pixel.
            * - :py:attr:`~br.steak.core.graphics.CustomImageGlobeOverlay.projection`
              - Get the map projection. Valid values are mercator and equidistant cylindrical.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import CustomImageGlobeOverlay


Property detail
---------------

.. py:property:: is_translucent
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlay.is_translucent
    :type: bool

    Get whether the overlay contains translucent imagery.

.. py:property:: maximum_meters_per_pixel
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlay.maximum_meters_per_pixel
    :type: float

    Get the maximum resolution of the inlay in meters per pixel.

.. py:property:: projection
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlay.projection
    :type: MapProjection

    Get the map projection. Valid values are mercator and equidistant cylindrical.


Method detail
-------------

.. py:method:: clear_cache(self) -> None
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlay.clear_cache

    Clear the image data cache associated with this instance. This is equivalent to deleting and re-adding the overlay.

    :Returns:

        :obj:`~None`




.. py:method:: read(self, extent: list, user_tile_data: typing.Any, image: IPictureDisp) -> bool
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlay.read

    Read a tile from the specified extent, scales it to and stores the result in image.

    :Parameters:

        **extent** : :obj:`~list`

        **user_tile_data** : :obj:`~typing.Any`

        **image** : :obj:`~IPictureDisp`


    :Returns:

        :obj:`~bool`

.. py:method:: reload(self) -> None
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlay.reload

    Reload the image data associated with this instance. Preserves the current image data until new image data replaces it.

    :Returns:

        :obj:`~None`

.. py:method:: shut_down(self, scene: Scene) -> None
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlay.shut_down

    Initiate shutdown when imagery is being removed from the globe.

    :Parameters:

        **scene** : :obj:`~Scene`


    :Returns:

        :obj:`~None`

.. py:method:: start_up(self, scene: Scene) -> None
    :canonical: br.steak.core.graphics.CustomImageGlobeOverlay.start_up

    Initiate start-up when imagery is being added to the globe.

    :Parameters:

        **scene** : :obj:`~Scene`


    :Returns:

        :obj:`~None`

