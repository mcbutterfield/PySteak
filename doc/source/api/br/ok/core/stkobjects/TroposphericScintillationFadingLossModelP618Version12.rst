TroposphericScintillationFadingLossModelP618Version12
=====================================================

.. py:class:: br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12

   Bases: :py:class:`~br.ok.core.stkobjects.ITroposphericScintillationFadingLossModel`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a tropospheric scintillation fading loss P.618-12 model.

.. py:currentmodule:: TroposphericScintillationFadingLossModelP618Version12

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.average_time_choice`
              - Get or set the TropoScintillation average fade time choice.
            * - :py:attr:`~br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.fade_exceeded`
              - Get or set the fade exceeded percent.
            * - :py:attr:`~br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.percent_time_refractivity_gradient`
              - Get or set the percentage of time that the refractivity gradient is less than -100 N units / km.
            * - :py:attr:`~br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.surface_temperature`
              - Get or set the surface temperature.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import TroposphericScintillationFadingLossModelP618Version12


Property detail
---------------

.. py:property:: average_time_choice
    :canonical: br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.average_time_choice
    :type: TroposphericScintillationAverageTimeChoiceType

    Get or set the TropoScintillation average fade time choice.

.. py:property:: fade_exceeded
    :canonical: br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.fade_exceeded
    :type: float

    Get or set the fade exceeded percent.

.. py:property:: percent_time_refractivity_gradient
    :canonical: br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.percent_time_refractivity_gradient
    :type: float

    Get or set the percentage of time that the refractivity gradient is less than -100 N units / km.

.. py:property:: surface_temperature
    :canonical: br.ok.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.surface_temperature
    :type: float

    Get or set the surface temperature.


