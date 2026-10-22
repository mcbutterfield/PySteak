SolarRadiationPressureModelGPS
==============================

.. py:class:: br.ok.core.stkobjects.SolarRadiationPressureModelGPS

   Bases: :py:class:`~br.ok.core.stkobjects.ISRPModelBase`

   GPS Solar Radiation Pressure Model.

.. py:currentmodule:: SolarRadiationPressureModelGPS

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SolarRadiationPressureModelGPS.scale`
              - Multiplicative factor on top of nominal GPS solar pressure model for acceleration in the satellite body fixed X-Z plane, which contains the sun to satellite line. Also known as K1, the nominal value is near 1.0.
            * - :py:attr:`~br.ok.core.stkobjects.SolarRadiationPressureModelGPS.y_bias`
              - Acceleration along the body-fixed Y axis of the satellite. Input is unitless but is multiplied by 1.0e-12 m/s2 to yield an acceleration perpendicular to the sun-to-satellite line. Also known as K2, the nominally value is in the range of -1 < YBias < 1.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import SolarRadiationPressureModelGPS


Property detail
---------------

.. py:property:: scale
    :canonical: br.ok.core.stkobjects.SolarRadiationPressureModelGPS.scale
    :type: float

    Multiplicative factor on top of nominal GPS solar pressure model for acceleration in the satellite body fixed X-Z plane, which contains the sun to satellite line. Also known as K1, the nominal value is near 1.0.

.. py:property:: y_bias
    :canonical: br.ok.core.stkobjects.SolarRadiationPressureModelGPS.y_bias
    :type: float

    Acceleration along the body-fixed Y axis of the satellite. Input is unitless but is multiplied by 1.0e-12 m/s2 to yield an acceleration perpendicular to the sun-to-satellite line. Also known as K2, the nominally value is in the range of -1 < YBias < 1.


