SceneManagerInitializer
=======================

.. py:class:: br.steak.core.graphics.SceneManagerInitializer

   The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

.. py:currentmodule:: SceneManagerInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.SceneManagerInitializer.render`
              - Render all scenes within an application. To render a specific scene, use the Render method.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.SceneManagerInitializer.frame_rate`
              - Get the frame rate class, which can be used to keep track of how fast scenes are being <see ref='Render'>rendered</see>.
            * - :py:attr:`~br.steak.core.graphics.SceneManagerInitializer.globe_overlay_settings`
              - Get the globe overlay settings, which are used to set global settings for all globe overlays.
            * - :py:attr:`~br.steak.core.graphics.SceneManagerInitializer.primitives`
              - Get the primitive manager, which is used to add primitives to your scenes.
            * - :py:attr:`~br.steak.core.graphics.SceneManagerInitializer.scenes`
              - Get a read-only collection of scenes that are associated with the scene manager.
            * - :py:attr:`~br.steak.core.graphics.SceneManagerInitializer.screen_overlays`
              - Get the screen overlay manager, which is used to add screen overlays to your scenes.
            * - :py:attr:`~br.steak.core.graphics.SceneManagerInitializer.textures`
              - Get the texture 2d factory, which can be used to create textures from various sources.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import SceneManagerInitializer


Property detail
---------------

.. py:property:: frame_rate
    :canonical: br.steak.core.graphics.SceneManagerInitializer.frame_rate
    :type: FrameRate

    Get the frame rate class, which can be used to keep track of how fast scenes are being <see ref='Render'>rendered</see>.

.. py:property:: globe_overlay_settings
    :canonical: br.steak.core.graphics.SceneManagerInitializer.globe_overlay_settings
    :type: GlobeOverlaySettings

    Get the globe overlay settings, which are used to set global settings for all globe overlays.

.. py:property:: primitives
    :canonical: br.steak.core.graphics.SceneManagerInitializer.primitives
    :type: PrimitiveManager

    Get the primitive manager, which is used to add primitives to your scenes.

.. py:property:: scenes
    :canonical: br.steak.core.graphics.SceneManagerInitializer.scenes
    :type: SceneCollection

    Get a read-only collection of scenes that are associated with the scene manager.

.. py:property:: screen_overlays
    :canonical: br.steak.core.graphics.SceneManagerInitializer.screen_overlays
    :type: ScreenOverlayManager

    Get the screen overlay manager, which is used to add screen overlays to your scenes.

.. py:property:: textures
    :canonical: br.steak.core.graphics.SceneManagerInitializer.textures
    :type: Texture2DFactory

    Get the texture 2d factory, which can be used to create textures from various sources.


Method detail
-------------




.. py:method:: render(self) -> None
    :canonical: br.steak.core.graphics.SceneManagerInitializer.render

    Render all scenes within an application. To render a specific scene, use the Render method.

    :Returns:

        :obj:`~None`




