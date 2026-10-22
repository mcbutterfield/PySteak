Texture2DFactory
================

.. py:class:: br.ok.core.graphics.Texture2DFactory

   A factory for creating texture 2d objects from various sources.

.. py:currentmodule:: Texture2DFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.Texture2DFactory.from_raster`
              - Create a new texture from a raster.
            * - :py:attr:`~br.ok.core.graphics.Texture2DFactory.load_from_string_uri`
              - Create a new texture from a Uri, which can be a file, HTTP, HTTPS, or FTP source. See raster for a list of supported raster formats.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import Texture2DFactory



Method detail
-------------

.. py:method:: from_raster(self, raster: IRaster) -> RendererTexture2D
    :canonical: br.ok.core.graphics.Texture2DFactory.from_raster

    Create a new texture from a raster.

    :Parameters:

        **raster** : :obj:`~IRaster`


    :Returns:

        :obj:`~RendererTexture2D`

.. py:method:: load_from_string_uri(self, uri: str) -> RendererTexture2D
    :canonical: br.ok.core.graphics.Texture2DFactory.load_from_string_uri

    Create a new texture from a Uri, which can be a file, HTTP, HTTPS, or FTP source. See raster for a list of supported raster formats.

    :Parameters:

        **uri** : :obj:`~str`


    :Returns:

        :obj:`~RendererTexture2D`

