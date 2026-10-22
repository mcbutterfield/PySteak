AtmosphericAbsorptionModelITURP676Version13
===========================================

.. py:class:: br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13

   Bases: :py:class:`~br.steak.core.stkobjects.IAtmosphericAbsorptionModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining an atmospheric absorption model.

.. py:currentmodule:: AtmosphericAbsorptionModelITURP676Version13

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13.atmosphere_data_type`
              - Get or set the atmosphere data type.
            * - :py:attr:`~br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13.fast_approximation_method`
              - Get or set the option for using the fast approximation method.
            * - :py:attr:`~br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13.use_water_vapor_from_section2_2`
              - Get or set the use of P.676-13 Section 2.2 for water vapor computations.
            * - :py:attr:`~br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13.user_profile_filename`
              - Get or set the atmosphere profile file.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AtmosphericAbsorptionModelITURP676Version13


Property detail
---------------

.. py:property:: atmosphere_data_type
    :canonical: br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13.atmosphere_data_type
    :type: ITURP676AtmosphereDataType

    Get or set the atmosphere data type.

.. py:property:: fast_approximation_method
    :canonical: br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13.fast_approximation_method
    :type: bool

    Get or set the option for using the fast approximation method.

.. py:property:: use_water_vapor_from_section2_2
    :canonical: br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13.use_water_vapor_from_section2_2
    :type: bool

    Get or set the use of P.676-13 Section 2.2 for water vapor computations.

.. py:property:: user_profile_filename
    :canonical: br.steak.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13.user_profile_filename
    :type: str

    Get or set the atmosphere profile file.


