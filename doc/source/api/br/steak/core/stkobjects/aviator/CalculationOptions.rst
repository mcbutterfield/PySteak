CalculationOptions
==================

.. py:class:: br.steak.core.stkobjects.aviator.CalculationOptions

   Class defining the calculation options for a procedure or phase.

.. py:currentmodule:: CalculationOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.CalculationOptions.integrator_type`
              - Get or set the integrator type.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.CalculationOptions.integrator_type_string`
              - Get or set the integrator type as a string value. Use this for custom integrators.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.CalculationOptions.max_bad_steps`
              - Get or set the maximum number of bad steps Aviator will allow before ceasing calculation.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.CalculationOptions.max_iterations`
              - Get or set the maximum number of iterations per time step Aviator will attempt.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.CalculationOptions.max_relative_motion_factor`
              - Get or set the maximum motion allowed between sampling points.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.CalculationOptions.state_cache_time_interval`
              - Get or set the time interval used to store the state information.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.CalculationOptions.time_resolution`
              - Get or set the tolerance for resolving time calculations.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.aviator import CalculationOptions


Property detail
---------------

.. py:property:: integrator_type
    :canonical: br.steak.core.stkobjects.aviator.CalculationOptions.integrator_type
    :type: AviatorNumericalIntegrator

    Get or set the integrator type.

.. py:property:: integrator_type_string
    :canonical: br.steak.core.stkobjects.aviator.CalculationOptions.integrator_type_string
    :type: str

    Get or set the integrator type as a string value. Use this for custom integrators.

.. py:property:: max_bad_steps
    :canonical: br.steak.core.stkobjects.aviator.CalculationOptions.max_bad_steps
    :type: int

    Get or set the maximum number of bad steps Aviator will allow before ceasing calculation.

.. py:property:: max_iterations
    :canonical: br.steak.core.stkobjects.aviator.CalculationOptions.max_iterations
    :type: int

    Get or set the maximum number of iterations per time step Aviator will attempt.

.. py:property:: max_relative_motion_factor
    :canonical: br.steak.core.stkobjects.aviator.CalculationOptions.max_relative_motion_factor
    :type: float

    Get or set the maximum motion allowed between sampling points.

.. py:property:: state_cache_time_interval
    :canonical: br.steak.core.stkobjects.aviator.CalculationOptions.state_cache_time_interval
    :type: float

    Get or set the time interval used to store the state information.

.. py:property:: time_resolution
    :canonical: br.steak.core.stkobjects.aviator.CalculationOptions.time_resolution
    :type: float

    Get or set the tolerance for resolving time calculations.


