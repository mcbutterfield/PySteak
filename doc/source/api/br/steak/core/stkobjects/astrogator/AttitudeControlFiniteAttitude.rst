AttitudeControlFiniteAttitude
=============================

.. py:class:: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteAttitude

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~br.steak.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~br.steak.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The attitude attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFiniteAttitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.attitude_update`
              - How and when the attitude will be updated.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.orientation`
              - Get the orientation of the attitude.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.reference_axes_name`
              - Ref Axes - the reference axes to be used in modeling this maneuver.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import AttitudeControlFiniteAttitude


Property detail
---------------

.. py:property:: attitude_update
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.attitude_update
    :type: AttitudeUpdate

    How and when the attitude will be updated.

.. py:property:: orientation
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.orientation
    :type: IOrientation

    Get the orientation of the attitude.

.. py:property:: reference_axes_name
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.reference_axes_name
    :type: str

    Ref Axes - the reference axes to be used in modeling this maneuver.


