VehicleGraphics2DAttributesRealtime
===================================

.. py:class:: br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime

   Bases: :py:class:`~br.ok.core.stkobjects.IVehicleGraphics2DAttributes`

   2D Graphics attributes for a vehicle based on real time data state.

.. py:currentmodule:: VehicleGraphics2DAttributesRealtime

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime.drop_out`
              - Get the drop out, i.e. data that is outside the time out gap.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime.history`
              - Get the historical data, consisting of all data points received from the time of the most current data point back to the last point within the look behind duration.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime.look_ahead`
              - Get the look ahead data, calculated on the basis of the last received data point.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime.spline`
              - Get the spline between the last point received and the new point.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleGraphics2DAttributesRealtime


Property detail
---------------

.. py:property:: drop_out
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime.drop_out
    :type: IVehicleGraphics2DAttributesBasic

    Get the drop out, i.e. data that is outside the time out gap.

.. py:property:: history
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime.history
    :type: IVehicleGraphics2DAttributesBasic

    Get the historical data, consisting of all data points received from the time of the most current data point back to the last point within the look behind duration.

.. py:property:: look_ahead
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime.look_ahead
    :type: IVehicleGraphics2DAttributesBasic

    Get the look ahead data, calculated on the basis of the last received data point.

.. py:property:: spline
    :canonical: br.ok.core.stkobjects.VehicleGraphics2DAttributesRealtime.spline
    :type: IVehicleGraphics2DAttributesBasic

    Get the spline between the last point received and the new point.


