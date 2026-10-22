AttitudeProfileSpinning
=======================

.. py:class:: br.ok.core.stkobjects.AttitudeProfileSpinning

   Bases: :py:class:`~br.ok.core.stkobjects.IVehicleAttitudeProfile`

   Spinning attitude profile.

.. py:currentmodule:: AttitudeProfileSpinning

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AttitudeProfileSpinning.body`
              - Get the spin axis in the body frame.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeProfileSpinning.inertial`
              - Get the spin axis in the inertial frame.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeProfileSpinning.offset`
              - Initial spin offset: an angular measure of the difference between the satellite orientation at the offset epoch from the orientation achieved by orienting the spin axis. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeProfileSpinning.rate`
              - Spin rate: specified in revolutions per minute; positive values indicate rotation in a right-handed sense with respect to the spin axis. Uses AngleRate Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeProfileSpinning.smart_epoch`
              - Epoch of the offset.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AttitudeProfileSpinning


Property detail
---------------

.. py:property:: body
    :canonical: br.ok.core.stkobjects.AttitudeProfileSpinning.body
    :type: IDirection

    Get the spin axis in the body frame.

.. py:property:: inertial
    :canonical: br.ok.core.stkobjects.AttitudeProfileSpinning.inertial
    :type: IDirection

    Get the spin axis in the inertial frame.

.. py:property:: offset
    :canonical: br.ok.core.stkobjects.AttitudeProfileSpinning.offset
    :type: float

    Initial spin offset: an angular measure of the difference between the satellite orientation at the offset epoch from the orientation achieved by orienting the spin axis. Uses Angle Dimension.

.. py:property:: rate
    :canonical: br.ok.core.stkobjects.AttitudeProfileSpinning.rate
    :type: float

    Spin rate: specified in revolutions per minute; positive values indicate rotation in a right-handed sense with respect to the spin axis. Uses AngleRate Dimension.

.. py:property:: smart_epoch
    :canonical: br.ok.core.stkobjects.AttitudeProfileSpinning.smart_epoch
    :type: ITimeToolInstantSmartEpoch

    Epoch of the offset.


