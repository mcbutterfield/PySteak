BulirschStoerIntegrator
=======================

.. py:class:: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.INumericalIntegrator`

   Bulirsch-Stoer Numerical Integrator.

.. py:currentmodule:: BulirschStoerIntegrator

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.first_safety_coefficient`
              - Get or set the first safety coefficient. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.initial_step`
              - Get or set the initial step. Uses time dimension.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.max_iterations`
              - Get or set the maximum number of iterations. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.max_relative_err`
              - Get or set the maximum relative error used to control step size. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.max_sequences`
              - Get or set the maximum number of sequences. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.max_step`
              - Get or set the maximum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.min_step`
              - Get or set the minimum step size to allow (absolute value). Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.second_safety_coefficient`
              - Get or set the second safety coefficient. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.tolerance`
              - Get or set the error tolerance for step size control. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.use_fixed_step`
              - True if running in fixed-step mode.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.use_max_step`
              - Whether or not to enforce the maximum step.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.use_min_step`
              - Whether or not to enforce the minimum step.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import BulirschStoerIntegrator


Property detail
---------------

.. py:property:: first_safety_coefficient
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.first_safety_coefficient
    :type: float

    Get or set the first safety coefficient. Dimensionless.

.. py:property:: initial_step
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.initial_step
    :type: float

    Get or set the initial step. Uses time dimension.

.. py:property:: max_iterations
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.max_iterations
    :type: int

    Get or set the maximum number of iterations. Dimensionless.

.. py:property:: max_relative_err
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.max_relative_err
    :type: float

    Get or set the maximum relative error used to control step size. Dimensionless.

.. py:property:: max_sequences
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.max_sequences
    :type: int

    Get or set the maximum number of sequences. Dimensionless.

.. py:property:: max_step
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.max_step
    :type: float

    Get or set the maximum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: min_step
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.min_step
    :type: float

    Get or set the minimum step size to allow (absolute value). Uses Time Dimension.

.. py:property:: second_safety_coefficient
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.second_safety_coefficient
    :type: float

    Get or set the second safety coefficient. Dimensionless.

.. py:property:: tolerance
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.tolerance
    :type: float

    Get or set the error tolerance for step size control. Dimensionless.

.. py:property:: use_fixed_step
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.use_fixed_step
    :type: bool

    True if running in fixed-step mode.

.. py:property:: use_max_step
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.use_max_step
    :type: bool

    Whether or not to enforce the maximum step.

.. py:property:: use_min_step
    :canonical: br.ok.core.stkobjects.astrogator.BulirschStoerIntegrator.use_min_step
    :type: bool

    Whether or not to enforce the minimum step.


