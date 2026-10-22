AttitudeStandardBasic
=====================

.. py:class:: br.ok.core.stkobjects.AttitudeStandardBasic

   Basic attitude profile.

.. py:currentmodule:: AttitudeStandardBasic

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardBasic.is_profile_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardBasic.set_profile_type`
              - Set basic attitude profile type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardBasic.profile`
              - Return the profile interface.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardBasic.profile_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeStandardBasic.profile_type`
              - Get basic attitude profile type.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AttitudeStandardBasic


Property detail
---------------

.. py:property:: profile
    :canonical: br.ok.core.stkobjects.AttitudeStandardBasic.profile
    :type: IVehicleAttitudeProfile

    Return the profile interface.

.. py:property:: profile_supported_types
    :canonical: br.ok.core.stkobjects.AttitudeStandardBasic.profile_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: profile_type
    :canonical: br.ok.core.stkobjects.AttitudeStandardBasic.profile_type
    :type: AttitudeProfile

    Get basic attitude profile type.


Method detail
-------------

.. py:method:: is_profile_type_supported(self, profile: AttitudeProfile) -> bool
    :canonical: br.ok.core.stkobjects.AttitudeStandardBasic.is_profile_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **profile** : :obj:`~AttitudeProfile`


    :Returns:

        :obj:`~bool`




.. py:method:: set_profile_type(self, profile: AttitudeProfile) -> None
    :canonical: br.ok.core.stkobjects.AttitudeStandardBasic.set_profile_type

    Set basic attitude profile type.

    :Parameters:

        **profile** : :obj:`~AttitudeProfile`


    :Returns:

        :obj:`~None`

