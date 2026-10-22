RefractionModelEffectiveRadiusMethod
====================================

.. py:class:: br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod

   Effective Radius Method.

.. py:currentmodule:: RefractionModelEffectiveRadiusMethod

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod.ceiling`
              - Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod.effective_radius`
              - Effective radius used to compute refracted elevation. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod.maximum_target_altitude`
              - Maximum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod.use_extrapolation`
              - Flag controls whether extrapolation is used past the maximum target altitude.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RefractionModelEffectiveRadiusMethod


Property detail
---------------

.. py:property:: ceiling
    :canonical: br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod.ceiling
    :type: float

    Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.

.. py:property:: effective_radius
    :canonical: br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod.effective_radius
    :type: float

    Effective radius used to compute refracted elevation. Dimensionless.

.. py:property:: maximum_target_altitude
    :canonical: br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod.maximum_target_altitude
    :type: float

    Maximum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.

.. py:property:: use_extrapolation
    :canonical: br.steak.core.stkobjects.RefractionModelEffectiveRadiusMethod.use_extrapolation
    :type: bool

    Flag controls whether extrapolation is used past the maximum target altitude.


