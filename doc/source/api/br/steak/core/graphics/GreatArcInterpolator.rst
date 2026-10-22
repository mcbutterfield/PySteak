GreatArcInterpolator
====================

.. py:class:: br.steak.core.graphics.GreatArcInterpolator

   Bases: :py:class:`~br.steak.core.graphics.IPositionInterpolator`

   The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

.. py:currentmodule:: GreatArcInterpolator

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.GreatArcInterpolator.central_body`
              - Get or set the central body used when interpolating with interpolate.
            * - :py:attr:`~br.steak.core.graphics.GreatArcInterpolator.granularity`
              - Get or set the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import GreatArcInterpolator


Property detail
---------------

.. py:property:: central_body
    :canonical: br.steak.core.graphics.GreatArcInterpolator.central_body
    :type: str

    Get or set the central body used when interpolating with interpolate.

.. py:property:: granularity
    :canonical: br.steak.core.graphics.GreatArcInterpolator.granularity
    :type: float

    Get or set the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.


