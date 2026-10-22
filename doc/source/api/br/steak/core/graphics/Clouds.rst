Clouds
======

.. py:class:: br.steak.core.graphics.Clouds

   Load, show and hide clouds in the scene.

.. py:currentmodule:: Clouds

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.Clouds.altitude`
              - The altitude of the clouds.
            * - :py:attr:`~br.steak.core.graphics.Clouds.clouds_uri`
              - The URI of the clouds index file. A cloud index file is an ascii file that contains a time-ordered list of images that display over the globe.
            * - :py:attr:`~br.steak.core.graphics.Clouds.is_valid`
              - Return whether or not the clouds file is valid.
            * - :py:attr:`~br.steak.core.graphics.Clouds.roundness`
              - The roundness of the clouds.
            * - :py:attr:`~br.steak.core.graphics.Clouds.show`
              - Get or set whether clouds are rendered.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import Clouds


Property detail
---------------

.. py:property:: altitude
    :canonical: br.steak.core.graphics.Clouds.altitude
    :type: float

    The altitude of the clouds.

.. py:property:: clouds_uri
    :canonical: br.steak.core.graphics.Clouds.clouds_uri
    :type: str

    The URI of the clouds index file. A cloud index file is an ascii file that contains a time-ordered list of images that display over the globe.

.. py:property:: is_valid
    :canonical: br.steak.core.graphics.Clouds.is_valid
    :type: bool

    Return whether or not the clouds file is valid.

.. py:property:: roundness
    :canonical: br.steak.core.graphics.Clouds.roundness
    :type: float

    The roundness of the clouds.

.. py:property:: show
    :canonical: br.steak.core.graphics.Clouds.show
    :type: bool

    Get or set whether clouds are rendered.


