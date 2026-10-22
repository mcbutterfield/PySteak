VehicleHPOPCentralBodyGravity
=============================

.. py:class:: br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity

   Class defining Central Body Gravity options for the High Precision Orbit Propagator (HPOP).

.. py:currentmodule:: VehicleHPOPCentralBodyGravity

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.set_maximum_degree_and_order`
              - Set maximum degree and maximum order of geopotential coefficients to be included for Central Body gravity computations. An exception is raised if MaximumDegree is less than MaximumOrder. Both values are dimensionless.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.file`
              - Name of gravity (.grv) file, an ASCII file containing the Central Body geopotential model coefficients.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.maximum_degree`
              - Maximum degree of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.maximum_order`
              - Maximum order of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.solid_tide_type`
              - Solid Tide Type.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.use_ocean_tides`
              - Opt whether to include the perturbation of the gravity field caused by the effects of ocean tides.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.use_secular_variations`
              - Opt whether to include or ignore secular variations defined by the gravity field model.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleHPOPCentralBodyGravity


Property detail
---------------

.. py:property:: file
    :canonical: br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.file
    :type: str

    Name of gravity (.grv) file, an ASCII file containing the Central Body geopotential model coefficients.

.. py:property:: maximum_degree
    :canonical: br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.maximum_degree
    :type: int

    Maximum degree of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.

.. py:property:: maximum_order
    :canonical: br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.maximum_order
    :type: int

    Maximum order of geopotential coefficients to be included for Central Body gravity computations. Dimensionless.

.. py:property:: solid_tide_type
    :canonical: br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.solid_tide_type
    :type: SolidTide

    Solid Tide Type.

.. py:property:: use_ocean_tides
    :canonical: br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.use_ocean_tides
    :type: bool

    Opt whether to include the perturbation of the gravity field caused by the effects of ocean tides.

.. py:property:: use_secular_variations
    :canonical: br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.use_secular_variations
    :type: bool

    Opt whether to include or ignore secular variations defined by the gravity field model.


Method detail
-------------







.. py:method:: set_maximum_degree_and_order(self, maximum_degree: int, maximum_order: int) -> None
    :canonical: br.ok.core.stkobjects.VehicleHPOPCentralBodyGravity.set_maximum_degree_and_order

    Set maximum degree and maximum order of geopotential coefficients to be included for Central Body gravity computations. An exception is raised if MaximumDegree is less than MaximumOrder. Both values are dimensionless.

    :Parameters:

        **maximum_degree** : :obj:`~int`

        **maximum_order** : :obj:`~int`


    :Returns:

        :obj:`~None`







