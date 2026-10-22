SRPGSPM04aeIIR
==============

.. py:class:: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   GSPM04aeIIR SRP propagator function.

.. py:currentmodule:: SRPGSPM04aeIIR

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.atmosphere_altitude`
              - Get or set the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.eclipsing_bodies`
              - Other eclipsing bodies.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.include_boundary_mitigation`
              - True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.k1_stochastic_srp_coefficient`
              - K1 Stochastic SRP Coefficient.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.k2_stochastic_srp_coefficient`
              - K2 Stochastic SRP Coefficient.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.shadow_model`
              - Get or set the shadow model type.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.solar_radius`
              - Get or set the solar radius value to use in eclipse calculations.  Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.sun_position`
              - Get or set the sun position computation.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.use_stochastic_srp_coefficient`
              - True if using a stochastic SRP for propagation or estimation.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.use_sun_central_body_file_values`
              - True if solar radius should come from the Sun.cb file.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import SRPGSPM04aeIIR


Property detail
---------------

.. py:property:: atmosphere_altitude
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.atmosphere_altitude
    :type: float

    Get or set the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.

.. py:property:: eclipsing_bodies
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.eclipsing_bodies
    :type: CentralBodyComponentCollection

    Other eclipsing bodies.

.. py:property:: include_boundary_mitigation
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.include_boundary_mitigation
    :type: bool

    True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.

.. py:property:: k1_stochastic_srp_coefficient
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.k1_stochastic_srp_coefficient
    :type: StochasticModelParameters

    K1 Stochastic SRP Coefficient.

.. py:property:: k2_stochastic_srp_coefficient
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.k2_stochastic_srp_coefficient
    :type: StochasticModelParameters

    K2 Stochastic SRP Coefficient.

.. py:property:: shadow_model
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.shadow_model
    :type: ShadowModel

    Get or set the shadow model type.

.. py:property:: solar_radius
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.solar_radius
    :type: float

    Get or set the solar radius value to use in eclipse calculations.  Uses Distance Dimension.

.. py:property:: sun_position
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.sun_position
    :type: SunPosition

    Get or set the sun position computation.

.. py:property:: use_stochastic_srp_coefficient
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.use_stochastic_srp_coefficient
    :type: bool

    True if using a stochastic SRP for propagation or estimation.

.. py:property:: use_sun_central_body_file_values
    :canonical: br.ok.core.stkobjects.astrogator.SRPGSPM04aeIIR.use_sun_central_body_file_values
    :type: bool

    True if solar radius should come from the Sun.cb file.


