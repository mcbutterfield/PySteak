AttitudeControlOptimalFiniteLagrange
====================================

.. py:class:: br.ok.core.stkobjects.astrogator.AttitudeControlOptimalFiniteLagrange

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IAttitudeControlOptimalFinite`, :py:class:`~br.ok.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Lagrange Interpolation attitude control for a optimal finite maneuver.

.. py:currentmodule:: AttitudeControlOptimalFiniteLagrange

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlOptimalFiniteLagrange.body_constraint_vector`
              - Define a constraint vector in spacecraft body coordinates to complete the attitude definition.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import AttitudeControlOptimalFiniteLagrange


Property detail
---------------

.. py:property:: body_constraint_vector
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlOptimalFiniteLagrange.body_constraint_vector
    :type: IDirection

    Define a constraint vector in spacecraft body coordinates to complete the attitude definition.


