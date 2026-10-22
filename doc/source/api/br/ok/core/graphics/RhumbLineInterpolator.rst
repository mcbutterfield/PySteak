RhumbLineInterpolator
=====================

.. py:class:: br.ok.core.graphics.RhumbLineInterpolator

   Bases: :py:class:`~br.ok.core.graphics.IPositionInterpolator`

   The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

.. py:currentmodule:: RhumbLineInterpolator

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.RhumbLineInterpolator.central_body`
              - Get or set the central body used when interpolating with interpolate.
            * - :py:attr:`~br.ok.core.graphics.RhumbLineInterpolator.granularity`
              - Get or set the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import RhumbLineInterpolator


Property detail
---------------

.. py:property:: central_body
    :canonical: br.ok.core.graphics.RhumbLineInterpolator.central_body
    :type: str

    Get or set the central body used when interpolating with interpolate.

.. py:property:: granularity
    :canonical: br.ok.core.graphics.RhumbLineInterpolator.granularity
    :type: float

    Get or set the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.


