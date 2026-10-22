BurnoutLaunchAzRadius
=====================

.. py:class:: br.steak.core.stkobjects.astrogator.BurnoutLaunchAzRadius

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IBurnout`

   The launch azimuth and radius burnout point.

.. py:currentmodule:: BurnoutLaunchAzRadius

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.BurnoutLaunchAzRadius.azimuth`
              - Get or set the azimuth of the launch trajectory. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.BurnoutLaunchAzRadius.down_range_dist`
              - Get or set the downrange distance of the spacecraft from launch at burnout. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.BurnoutLaunchAzRadius.radius`
              - Get or set the radius of the spacecraft at burnout. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import BurnoutLaunchAzRadius


Property detail
---------------

.. py:property:: azimuth
    :canonical: br.steak.core.stkobjects.astrogator.BurnoutLaunchAzRadius.azimuth
    :type: typing.Any

    Get or set the azimuth of the launch trajectory. Uses Angle Dimension.

.. py:property:: down_range_dist
    :canonical: br.steak.core.stkobjects.astrogator.BurnoutLaunchAzRadius.down_range_dist
    :type: float

    Get or set the downrange distance of the spacecraft from launch at burnout. Uses Distance Dimension.

.. py:property:: radius
    :canonical: br.steak.core.stkobjects.astrogator.BurnoutLaunchAzRadius.radius
    :type: float

    Get or set the radius of the spacecraft at burnout. Uses Distance Dimension.


