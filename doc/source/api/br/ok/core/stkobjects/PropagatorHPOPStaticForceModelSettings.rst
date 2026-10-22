PropagatorHPOPStaticForceModelSettings
======================================

.. py:class:: br.ok.core.stkobjects.PropagatorHPOPStaticForceModelSettings

   Class defining static force model options for the HPOP propagator.

.. py:currentmodule:: PropagatorHPOPStaticForceModelSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorHPOPStaticForceModelSettings.include_relativistic_acceleration`
              - Models the effects of general relativity in accordance with IERS Technical Note 32, IERS Conventions (2003).
            * - :py:attr:`~br.ok.core.stkobjects.PropagatorHPOPStaticForceModelSettings.satellite_mass`
              - A value for the satellite's mass to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import PropagatorHPOPStaticForceModelSettings


Property detail
---------------

.. py:property:: include_relativistic_acceleration
    :canonical: br.ok.core.stkobjects.PropagatorHPOPStaticForceModelSettings.include_relativistic_acceleration
    :type: bool

    Models the effects of general relativity in accordance with IERS Technical Note 32, IERS Conventions (2003).

.. py:property:: satellite_mass
    :canonical: br.ok.core.stkobjects.PropagatorHPOPStaticForceModelSettings.satellite_mass
    :type: float

    A value for the satellite's mass to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.


