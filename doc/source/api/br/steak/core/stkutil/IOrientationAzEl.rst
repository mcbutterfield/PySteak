IOrientationAzEl
================

.. py:class:: br.steak.core.stkutil.IOrientationAzEl

   Bases: IOrientation

   Interface for AzEl orientation method.

.. py:currentmodule:: IOrientationAzEl

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.IOrientationAzEl.about_boresight`
              - Determine orientation of the X and Y axes with respect to the parent's reference frame.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationAzEl.azimuth`
              - Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationAzEl.elevation`
              - Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkutil import IOrientationAzEl


Property detail
---------------

.. py:property:: about_boresight
    :canonical: br.steak.core.stkutil.IOrientationAzEl.about_boresight
    :type: AzElAboutBoresight

    Determine orientation of the X and Y axes with respect to the parent's reference frame.

.. py:property:: azimuth
    :canonical: br.steak.core.stkutil.IOrientationAzEl.azimuth
    :type: typing.Any

    Measured in the XY plane of the parent reference frame about its Z axis in the right-handed sense for both vehicle-based sensors and facility-based sensors. Uses Angle Dimension.

.. py:property:: elevation
    :canonical: br.steak.core.stkutil.IOrientationAzEl.elevation
    :type: typing.Any

    Defined as the angle between the XY plane of the parent reference frame and the sensor or antenna boresight measured toward the positive Z axis. Uses Angle Dimension.


