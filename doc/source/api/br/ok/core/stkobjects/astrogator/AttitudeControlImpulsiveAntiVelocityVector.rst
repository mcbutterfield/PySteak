AttitudeControlImpulsiveAntiVelocityVector
==========================================

.. py:class:: br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveAntiVelocityVector

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IAttitudeControlImpulsive`, :py:class:`~br.ok.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The anti-velocity vector attitude control for an impulsive maneuver.

.. py:currentmodule:: AttitudeControlImpulsiveAntiVelocityVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveAntiVelocityVector.body_constraint_vector`
              - Define a constraint vector in spacecraft body coordinates to complete the attitude definition.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveAntiVelocityVector.delta_v_magnitude`
              - Get or set the size of the delta-V to be applied to the orbit along the velocity vector. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import AttitudeControlImpulsiveAntiVelocityVector


Property detail
---------------

.. py:property:: body_constraint_vector
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveAntiVelocityVector.body_constraint_vector
    :type: IDirection

    Define a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: delta_v_magnitude
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveAntiVelocityVector.delta_v_magnitude
    :type: float

    Get or set the size of the delta-V to be applied to the orbit along the velocity vector. Uses Rate Dimension.


