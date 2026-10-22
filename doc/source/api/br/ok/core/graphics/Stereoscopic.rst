Stereoscopic
============

.. py:class:: br.ok.core.graphics.Stereoscopic

   Get the stereoscopic options for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

.. py:currentmodule:: Stereoscopic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.Stereoscopic.display_mode`
              - Get or set the stereoscopic display mode for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.
            * - :py:attr:`~br.ok.core.graphics.Stereoscopic.eye_separation_factor`
              - Get or set the eye separation factor.
            * - :py:attr:`~br.ok.core.graphics.Stereoscopic.projection_distance`
              - Get or set the projection distance. If projection mode is set to eStkGraphicsStereoProjectionAutomatic, the value of this property will be ignored.
            * - :py:attr:`~br.ok.core.graphics.Stereoscopic.projection_mode`
              - Get or set whether the type of stereo projection that will be used.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import Stereoscopic


Property detail
---------------

.. py:property:: display_mode
    :canonical: br.ok.core.graphics.Stereoscopic.display_mode
    :type: StereoscopicDisplayMode

    Get or set the stereoscopic display mode for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

.. py:property:: eye_separation_factor
    :canonical: br.ok.core.graphics.Stereoscopic.eye_separation_factor
    :type: float

    Get or set the eye separation factor.

.. py:property:: projection_distance
    :canonical: br.ok.core.graphics.Stereoscopic.projection_distance
    :type: float

    Get or set the projection distance. If projection mode is set to eStkGraphicsStereoProjectionAutomatic, the value of this property will be ignored.

.. py:property:: projection_mode
    :canonical: br.ok.core.graphics.Stereoscopic.projection_mode
    :type: StereoProjectionMode

    Get or set whether the type of stereo projection that will be used.


