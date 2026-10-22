DistanceToGlobeOverlayDisplayConditionFactory
=============================================

.. py:class:: br.ok.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory

   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

.. py:currentmodule:: DistanceToGlobeOverlayDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory.initialize`
              - Initialize a default distance to globe overlay display condition. With this constructor, an object is always rendered regardless of the camera's distance to the globe overlay.
            * - :py:attr:`~br.ok.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory.initialize_with_distances`
              - Initialize a distance display condition with the globe overlay and the inclusive distance interval [minimumDistance, maximumDistance]...


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import DistanceToGlobeOverlayDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> DistanceToGlobeOverlayDisplayCondition
    :canonical: br.ok.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory.initialize

    Initialize a default distance to globe overlay display condition. With this constructor, an object is always rendered regardless of the camera's distance to the globe overlay.

    :Returns:

        :obj:`~DistanceToGlobeOverlayDisplayCondition`

.. py:method:: initialize_with_distances(self, globe_overlay: IGlobeOverlay, minimum_distance: float, maximum_distance: float) -> DistanceToGlobeOverlayDisplayCondition
    :canonical: br.ok.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory.initialize_with_distances

    Initialize a distance display condition with the globe overlay and the inclusive distance interval [minimumDistance, maximumDistance]...

    :Parameters:

        **globe_overlay** : :obj:`~IGlobeOverlay`

        **minimum_distance** : :obj:`~float`

        **maximum_distance** : :obj:`~float`


    :Returns:

        :obj:`~DistanceToGlobeOverlayDisplayCondition`

