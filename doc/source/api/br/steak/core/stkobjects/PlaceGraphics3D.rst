PlaceGraphics3D
===============

.. py:class:: br.steak.core.stkobjects.PlaceGraphics3D

   Bases: :py:class:`~br.steak.core.stkobjects.IGroundLocationGraphics3D`

   3D Graphics properties of a Place.

.. py:currentmodule:: PlaceGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.az_el_mask`
              - Return the 3D AzElMask properties.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.data_displays`
              - Return the 3D data display properties.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.model`
              - Return the 3D model properties.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.model_pointing`
              - Return 3D model pointing properties used to point parts of a place model toward a place, such as the Sun or Earth.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.offsets`
              - Return the 3D offsets properties.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.range_contours`
              - Return the 3D range contours properties.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.uncertainty_area_label_swap_distance`
              - Area of uncertainty label swap distance.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.vapor_trail`
              - Vapor trail attributes.
            * - :py:attr:`~br.steak.core.stkobjects.PlaceGraphics3D.vector`
              - Return the 3D vectorector properties.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import PlaceGraphics3D


Property detail
---------------

.. py:property:: az_el_mask
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.az_el_mask
    :type: Graphics3DAzElMask

    Return the 3D AzElMask properties.

.. py:property:: data_displays
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.data_displays
    :type: Graphics3DDataDisplayCollection

    Return the 3D data display properties.

.. py:property:: model
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.model
    :type: PointTargetGraphics3DModel

    Return the 3D model properties.

.. py:property:: model_pointing
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.model_pointing
    :type: Graphics3DModelPointing

    Return 3D model pointing properties used to point parts of a place model toward a place, such as the Sun or Earth.

.. py:property:: offsets
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.offsets
    :type: Graphics3DOffset

    Return the 3D offsets properties.

.. py:property:: radar_cross_section
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.radar_cross_section
    :type: RadarCrossSectionGraphics3D

    Get the radar cross section graphics interface.

.. py:property:: range_contours
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.range_contours
    :type: Graphics3DRangeContours

    Return the 3D range contours properties.

.. py:property:: uncertainty_area_label_swap_distance
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.uncertainty_area_label_swap_distance
    :type: Graphics3DLabelSwapDistance

    Area of uncertainty label swap distance.

.. py:property:: vapor_trail
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.vapor_trail
    :type: Graphics3DVaporTrail

    Vapor trail attributes.

.. py:property:: vector
    :canonical: br.steak.core.stkobjects.PlaceGraphics3D.vector
    :type: Graphics3DVector

    Return the 3D vectorector properties.


