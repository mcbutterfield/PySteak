TroposphericScintillationFadingLossModelP618Version8
====================================================

.. py:class:: br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8

   Bases: :py:class:`~br.steak.core.stkobjects.ITroposphericScintillationFadingLossModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a tropospheric scintillation fading loss P.618-8 model.

.. py:currentmodule:: TroposphericScintillationFadingLossModelP618Version8

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8.compute_deep_fade`
              - Get or set the option for computing deep fade.
            * - :py:attr:`~br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8.fade_outage`
              - Get or set the fade outage percent.
            * - :py:attr:`~br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8.percent_time_refractivity_gradient`
              - Get or set the percentage of time the refractivity is gradient is less than -100 N units / km.
            * - :py:attr:`~br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8.surface_temperature`
              - Get or set the surface temperature.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import TroposphericScintillationFadingLossModelP618Version8


Property detail
---------------

.. py:property:: compute_deep_fade
    :canonical: br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8.compute_deep_fade
    :type: bool

    Get or set the option for computing deep fade.

.. py:property:: fade_outage
    :canonical: br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8.fade_outage
    :type: float

    Get or set the fade outage percent.

.. py:property:: percent_time_refractivity_gradient
    :canonical: br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8.percent_time_refractivity_gradient
    :type: float

    Get or set the percentage of time the refractivity is gradient is less than -100 N units / km.

.. py:property:: surface_temperature
    :canonical: br.steak.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8.surface_temperature
    :type: float

    Get or set the surface temperature.


