SpaceEnvironmentMagneticField
=============================

.. py:class:: br.ok.core.stkobjects.SpaceEnvironmentMagneticField

   Magnetic field settings.

.. py:currentmodule:: SpaceEnvironmentMagneticField

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticField.compute_b_over_beq`
              - Compute B/Beq (i.e., the ratio of the magnetic field at the vehicle's location to the minimum field intensity along the field line thru the location). Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticField.compute_b_field_as_array`
              - Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the vehicle's location location. Uses DateFormat and MagneticField Dimensions.
            * - :py:attr:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticField.compute_dipole_l_shell`
              - Compute dipole L-shell parameter at the vehicle's location. Uses DateFormat Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticField.compute_mcilwain_l_shell`
              - Compute McIlwain L-shell parameter at the vehicle's location. Uses DateFormat Dimension.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticField.external_field`
              - External magnetic field.
            * - :py:attr:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticField.igrf_update_rate`
              - Duration between updates of IGRF magnetic field model coefficients. Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.SpaceEnvironmentMagneticField.main_field`
              - Get or set the main magnetic field.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import SpaceEnvironmentMagneticField


Property detail
---------------

.. py:property:: external_field
    :canonical: br.ok.core.stkobjects.SpaceEnvironmentMagneticField.external_field
    :type: SpaceEnvironmentMagneticExternalField

    External magnetic field.

.. py:property:: igrf_update_rate
    :canonical: br.ok.core.stkobjects.SpaceEnvironmentMagneticField.igrf_update_rate
    :type: float

    Duration between updates of IGRF magnetic field model coefficients. Uses Time Dimension.

.. py:property:: main_field
    :canonical: br.ok.core.stkobjects.SpaceEnvironmentMagneticField.main_field
    :type: SpaceEnvironmentMagneticMainField

    Get or set the main magnetic field.


Method detail
-------------

.. py:method:: compute_b_over_beq(self, time: typing.Any) -> float
    :canonical: br.ok.core.stkobjects.SpaceEnvironmentMagneticField.compute_b_over_beq

    Compute B/Beq (i.e., the ratio of the magnetic field at the vehicle's location to the minimum field intensity along the field line thru the location). Uses DateFormat Dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~float`

.. py:method:: compute_b_field_as_array(self, time: typing.Any) -> list
    :canonical: br.ok.core.stkobjects.SpaceEnvironmentMagneticField.compute_b_field_as_array

    Compute geomagnetic field in Earth Fixed components, returned as the array (Bx, By, Bz), at the vehicle's location location. Uses DateFormat and MagneticField Dimensions.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: compute_dipole_l_shell(self, time: typing.Any) -> float
    :canonical: br.ok.core.stkobjects.SpaceEnvironmentMagneticField.compute_dipole_l_shell

    Compute dipole L-shell parameter at the vehicle's location. Uses DateFormat Dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~float`

.. py:method:: compute_mcilwain_l_shell(self, time: typing.Any) -> float
    :canonical: br.ok.core.stkobjects.SpaceEnvironmentMagneticField.compute_mcilwain_l_shell

    Compute McIlwain L-shell parameter at the vehicle's location. Uses DateFormat Dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~float`







