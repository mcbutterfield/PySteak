AttitudeControlFiniteThrustVector
=================================

.. py:class:: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~br.steak.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~br.steak.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The thrust vector attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFiniteThrustVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.attitude_update`
              - How and when the attitude will be updated.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.body_constraint_vector`
              - Define a constraint vector in spacecraft body coordinates to complete the attitude definition.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.thrust_axes_name`
              - Get or set the thrust axes.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.thrust_vector`
              - Define the thrust vector in the reference axes.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import AttitudeControlFiniteThrustVector


Property detail
---------------

.. py:property:: attitude_update
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.attitude_update
    :type: AttitudeUpdate

    How and when the attitude will be updated.

.. py:property:: body_constraint_vector
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.body_constraint_vector
    :type: IDirection

    Define a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: thrust_axes_name
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.thrust_axes_name
    :type: str

    Get or set the thrust axes.

.. py:property:: thrust_vector
    :canonical: br.steak.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.thrust_vector
    :type: IDirection

    Define the thrust vector in the reference axes.


