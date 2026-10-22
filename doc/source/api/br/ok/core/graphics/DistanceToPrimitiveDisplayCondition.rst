DistanceToPrimitiveDisplayCondition
===================================

.. py:class:: br.ok.core.graphics.DistanceToPrimitiveDisplayCondition

   Bases: :py:class:`~br.ok.core.graphics.IDisplayCondition`

   Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

.. py:currentmodule:: DistanceToPrimitiveDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.maximum_distance`
              - Get or set the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.
            * - :py:attr:`~br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.maximum_distance_squared`
              - Get the squared maximum distance of the inclusive distance interval.
            * - :py:attr:`~br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.minimum_distance`
              - Get or set the minimum distance of the inclusive distance interval.
            * - :py:attr:`~br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.minimum_distance_squared`
              - Get the squared minimum distance of the inclusive distance interval.
            * - :py:attr:`~br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.primitive`
              - Get or set the primitive associated with this instance.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import DistanceToPrimitiveDisplayCondition


Property detail
---------------

.. py:property:: maximum_distance
    :canonical: br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.maximum_distance
    :type: float

    Get or set the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.

.. py:property:: maximum_distance_squared
    :canonical: br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.maximum_distance_squared
    :type: float

    Get the squared maximum distance of the inclusive distance interval.

.. py:property:: minimum_distance
    :canonical: br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.minimum_distance
    :type: float

    Get or set the minimum distance of the inclusive distance interval.

.. py:property:: minimum_distance_squared
    :canonical: br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.minimum_distance_squared
    :type: float

    Get the squared minimum distance of the inclusive distance interval.

.. py:property:: primitive
    :canonical: br.ok.core.graphics.DistanceToPrimitiveDisplayCondition.primitive
    :type: IPrimitive

    Get or set the primitive associated with this instance.


