SensorPointingTargetedBoresightTrack
====================================

.. py:class:: br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack

   Bases: :py:class:`~br.steak.core.stkobjects.ISensorPointingTargetedBoresight`

   Class defining a targeted sensor with tracking boresight.

.. py:currentmodule:: SensorPointingTargetedBoresightTrack

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.about_boresight`
              - The orientation of the antenna's X and Y axes with respect to the parent's reference frame. (The Z axis always coincides with its boresight direction and is unambiguously defined by the azimuth and elevation.
            * - :py:attr:`~br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.available_constraint_vectors`
              - Get the available constraint vectors.
            * - :py:attr:`~br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.clock_angle_offset_for_up_vector_boresight`
              - Get or set the clock angle offset for UpVector boresight type. It is an optional value measured in the Sensor Body axes xy-plane, positive about the boresight, locating the direction closest to the ConstraintVector from the Sensor Body x-axis.
            * - :py:attr:`~br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.constraint_vector_for_up_vector_boresight`
              - Get or set the constraint vector for UpVector boresight type.
            * - :py:attr:`~br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.track_mode`
              - The antenna orientation option for the sensor. A member of the TrackMode enumeration.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import SensorPointingTargetedBoresightTrack


Property detail
---------------

.. py:property:: about_boresight
    :canonical: br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.about_boresight
    :type: BoresightType

    The orientation of the antenna's X and Y axes with respect to the parent's reference frame. (The Z axis always coincides with its boresight direction and is unambiguously defined by the azimuth and elevation.

.. py:property:: available_constraint_vectors
    :canonical: br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.available_constraint_vectors
    :type: list

    Get the available constraint vectors.

.. py:property:: clock_angle_offset_for_up_vector_boresight
    :canonical: br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.clock_angle_offset_for_up_vector_boresight
    :type: typing.Any

    Get or set the clock angle offset for UpVector boresight type. It is an optional value measured in the Sensor Body axes xy-plane, positive about the boresight, locating the direction closest to the ConstraintVector from the Sensor Body x-axis.

.. py:property:: constraint_vector_for_up_vector_boresight
    :canonical: br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.constraint_vector_for_up_vector_boresight
    :type: str

    Get or set the constraint vector for UpVector boresight type.

.. py:property:: track_mode
    :canonical: br.steak.core.stkobjects.SensorPointingTargetedBoresightTrack.track_mode
    :type: TrackMode

    The antenna orientation option for the sensor. A member of the TrackMode enumeration.


