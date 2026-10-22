StochasticModelParameters
=========================

.. py:class:: br.steak.core.stkobjects.astrogator.StochasticModelParameters

   Properties for Stochastic Model Parameters.

.. py:currentmodule:: StochasticModelParameters

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StochasticModelParameters.diffusion_coefficient`
              - Determine the amount of process noise to be added to state covariance used in the Random Walk model.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StochasticModelParameters.error_threshold`
              - Covariance floor for long term mean used in the Vasicek model.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StochasticModelParameters.half_life`
              - Half life value for Gauss Markov stochastic process.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StochasticModelParameters.model_type`
              - Type of stochastic model used for SRP correction.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StochasticModelParameters.process_noise_step`
              - Process noise step when minimum floor is hit used in the Vasicek model.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StochasticModelParameters.sigma`
              - Root variance of the initial error in the nominal value.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StochasticModelParameters.sigma_long_term`
              - Root variance of the initial error in the long term constant value used in the Vasicek model.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import StochasticModelParameters


Property detail
---------------

.. py:property:: diffusion_coefficient
    :canonical: br.steak.core.stkobjects.astrogator.StochasticModelParameters.diffusion_coefficient
    :type: float

    Determine the amount of process noise to be added to state covariance used in the Random Walk model.

.. py:property:: error_threshold
    :canonical: br.steak.core.stkobjects.astrogator.StochasticModelParameters.error_threshold
    :type: float

    Covariance floor for long term mean used in the Vasicek model.

.. py:property:: half_life
    :canonical: br.steak.core.stkobjects.astrogator.StochasticModelParameters.half_life
    :type: float

    Half life value for Gauss Markov stochastic process.

.. py:property:: model_type
    :canonical: br.steak.core.stkobjects.astrogator.StochasticModelParameters.model_type
    :type: StochasticModel

    Type of stochastic model used for SRP correction.

.. py:property:: process_noise_step
    :canonical: br.steak.core.stkobjects.astrogator.StochasticModelParameters.process_noise_step
    :type: float

    Process noise step when minimum floor is hit used in the Vasicek model.

.. py:property:: sigma
    :canonical: br.steak.core.stkobjects.astrogator.StochasticModelParameters.sigma
    :type: float

    Root variance of the initial error in the nominal value.

.. py:property:: sigma_long_term
    :canonical: br.steak.core.stkobjects.astrogator.StochasticModelParameters.sigma_long_term
    :type: float

    Root variance of the initial error in the long term constant value used in the Vasicek model.


