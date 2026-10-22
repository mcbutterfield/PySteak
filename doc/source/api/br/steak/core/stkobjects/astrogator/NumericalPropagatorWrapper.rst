NumericalPropagatorWrapper
==========================

.. py:class:: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   Numerical Propagator.

.. py:currentmodule:: NumericalPropagatorWrapper

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.set_numerical_integrator`
              - Change the single step integrator.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.central_body_name`
              - Get or set the central body for Propagation.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.numerical_integrator`
              - Get the numerical integrator.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.numerical_integrator_type`
              - Get the single step integrator type.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.propagator_functions`
              - Get the list of propagator functions.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.regularized_time_exponent`
              - Get or set the exponent to use in regularized time; related to numerical integrator. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.regularized_time_steps_per_orbit`
              - Get or set the steps per orbit used in regularized time; related to numerical integrator. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.use_regularized_time`
              - Whether or not to use regularized time; related to numerical integrator.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.use_variation_of_parameters`
              - Whether or not to use a variation of parameters(VOP) in universal variables formulation of the equations of motion; related to numerical integrator.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import NumericalPropagatorWrapper


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.central_body_name
    :type: str

    Get or set the central body for Propagation.

.. py:property:: numerical_integrator
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.numerical_integrator
    :type: INumericalIntegrator

    Get the numerical integrator.

.. py:property:: numerical_integrator_type
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.numerical_integrator_type
    :type: NumericalIntegrator

    Get the single step integrator type.

.. py:property:: propagator_functions
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.propagator_functions
    :type: PropagatorFunctionCollection

    Get the list of propagator functions.

.. py:property:: regularized_time_exponent
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.regularized_time_exponent
    :type: float

    Get or set the exponent to use in regularized time; related to numerical integrator. Dimensionless.

.. py:property:: regularized_time_steps_per_orbit
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.regularized_time_steps_per_orbit
    :type: int

    Get or set the steps per orbit used in regularized time; related to numerical integrator. Dimensionless.

.. py:property:: use_regularized_time
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.use_regularized_time
    :type: bool

    Whether or not to use regularized time; related to numerical integrator.

.. py:property:: use_variation_of_parameters
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.use_variation_of_parameters
    :type: bool

    Whether or not to use a variation of parameters(VOP) in universal variables formulation of the equations of motion; related to numerical integrator.


Method detail
-------------










.. py:method:: set_numerical_integrator(self, integrator: NumericalIntegrator) -> None
    :canonical: br.steak.core.stkobjects.astrogator.NumericalPropagatorWrapper.set_numerical_integrator

    Change the single step integrator.

    :Parameters:

        **integrator** : :obj:`~NumericalIntegrator`


    :Returns:

        :obj:`~None`





