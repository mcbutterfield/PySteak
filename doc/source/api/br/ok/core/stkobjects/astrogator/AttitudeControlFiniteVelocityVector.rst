AttitudeControlFiniteVelocityVector
===================================

.. py:class:: br.ok.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~br.ok.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The velocity vector attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFiniteVelocityVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector.attitude_update`
              - How and when the attitude will be updated.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector.body_constraint_vector`
              - Define a constraint vector in spacecraft body coordinates to complete the attitude definition.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import AttitudeControlFiniteVelocityVector


Property detail
---------------

.. py:property:: attitude_update
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector.attitude_update
    :type: AttitudeUpdate

    How and when the attitude will be updated.

.. py:property:: body_constraint_vector
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector.body_constraint_vector
    :type: IDirection

    Define a constraint vector in spacecraft body coordinates to complete the attitude definition.


