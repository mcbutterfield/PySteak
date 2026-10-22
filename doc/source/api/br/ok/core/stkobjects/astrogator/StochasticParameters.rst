StochasticParameters
====================

.. py:class:: br.ok.core.stkobjects.astrogator.StochasticParameters

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Stochastic Parameters.

.. py:currentmodule:: StochasticParameters

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.ballistic_coefficient`
              - Get the ballistic coefficient.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.cr_a_over_m`
              - Get the Cr A / M
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.density_model_initial_correction`
              - Get or set the density model initial correction.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.drag_initial_correction`
              - Get or set the drag initial correction.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.drag_long_term_initial_correction`
              - Get or set the drag long term initial correction.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.drag_n_plate_stochastic_correction_parameters`
              - Drag NPlate Stochastic Correction Parameters.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.srp_initial_correction`
              - Get or set the Solar Radiation Pressure initial correction.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.srp_long_term_initial_correction`
              - Get or set the Solar Radiation Pressure long term initial correction.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StochasticParameters.srp_n_plate_stochastic_correction_parameters`
              - SRP NPlate Stochastic Correction Parameters.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import StochasticParameters


Property detail
---------------

.. py:property:: ballistic_coefficient
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.ballistic_coefficient
    :type: float

    Get the ballistic coefficient.

.. py:property:: cr_a_over_m
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.cr_a_over_m
    :type: float

    Get the Cr A / M

.. py:property:: density_model_initial_correction
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.density_model_initial_correction
    :type: float

    Get or set the density model initial correction.

.. py:property:: drag_initial_correction
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.drag_initial_correction
    :type: float

    Get or set the drag initial correction.

.. py:property:: drag_long_term_initial_correction
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.drag_long_term_initial_correction
    :type: float

    Get or set the drag long term initial correction.

.. py:property:: drag_n_plate_stochastic_correction_parameters
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.drag_n_plate_stochastic_correction_parameters
    :type: NPlateStochasticCorrectionParametersCollection

    Drag NPlate Stochastic Correction Parameters.

.. py:property:: srp_initial_correction
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.srp_initial_correction
    :type: float

    Get or set the Solar Radiation Pressure initial correction.

.. py:property:: srp_long_term_initial_correction
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.srp_long_term_initial_correction
    :type: float

    Get or set the Solar Radiation Pressure long term initial correction.

.. py:property:: srp_n_plate_stochastic_correction_parameters
    :canonical: br.ok.core.stkobjects.astrogator.StochasticParameters.srp_n_plate_stochastic_correction_parameters
    :type: NPlateStochasticCorrectionParametersCollection

    SRP NPlate Stochastic Correction Parameters.


