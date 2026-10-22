VolumetricAnalysisInterval
==========================

.. py:class:: br.ok.core.stkobjects.VolumetricAnalysisInterval

   Class defining the volumetric analysis interval.

.. py:currentmodule:: VolumetricAnalysisInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VolumetricAnalysisInterval.set_spatial_calcuation_evaluation_type`
              - Evaluate spatial calculation type, using the VolumetricSpatialCalculationEvaluationType enumeration.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VolumetricAnalysisInterval.analysis_interval`
              - The volume analysis interval or interval list.
            * - :py:attr:`~br.ok.core.stkobjects.VolumetricAnalysisInterval.available_analysis_intervals`
              - Get the available analysis intervals.
            * - :py:attr:`~br.ok.core.stkobjects.VolumetricAnalysisInterval.available_times_from_time_array`
              - Get the available times from time array.
            * - :py:attr:`~br.ok.core.stkobjects.VolumetricAnalysisInterval.evaluation_of_spatial_calculation_type`
              - Get evaluation of spatial calculation type. A member of the VolumetricSpatialCalculationEvaluationType enumeration.
            * - :py:attr:`~br.ok.core.stkobjects.VolumetricAnalysisInterval.step_size`
              - Get or set the step size.
            * - :py:attr:`~br.ok.core.stkobjects.VolumetricAnalysisInterval.time_array`
              - The time array when Evaluation of spatial calculation at times from time array is used.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VolumetricAnalysisInterval


Property detail
---------------

.. py:property:: analysis_interval
    :canonical: br.ok.core.stkobjects.VolumetricAnalysisInterval.analysis_interval
    :type: str

    The volume analysis interval or interval list.

.. py:property:: available_analysis_intervals
    :canonical: br.ok.core.stkobjects.VolumetricAnalysisInterval.available_analysis_intervals
    :type: list

    Get the available analysis intervals.

.. py:property:: available_times_from_time_array
    :canonical: br.ok.core.stkobjects.VolumetricAnalysisInterval.available_times_from_time_array
    :type: list

    Get the available times from time array.

.. py:property:: evaluation_of_spatial_calculation_type
    :canonical: br.ok.core.stkobjects.VolumetricAnalysisInterval.evaluation_of_spatial_calculation_type
    :type: VolumetricSpatialCalculationEvaluationType

    Get evaluation of spatial calculation type. A member of the VolumetricSpatialCalculationEvaluationType enumeration.

.. py:property:: step_size
    :canonical: br.ok.core.stkobjects.VolumetricAnalysisInterval.step_size
    :type: float

    Get or set the step size.

.. py:property:: time_array
    :canonical: br.ok.core.stkobjects.VolumetricAnalysisInterval.time_array
    :type: str

    The time array when Evaluation of spatial calculation at times from time array is used.


Method detail
-------------






.. py:method:: set_spatial_calcuation_evaluation_type(self, spatial_calc_eval_type: VolumetricSpatialCalculationEvaluationType) -> None
    :canonical: br.ok.core.stkobjects.VolumetricAnalysisInterval.set_spatial_calcuation_evaluation_type

    Evaluate spatial calculation type, using the VolumetricSpatialCalculationEvaluationType enumeration.

    :Parameters:

        **spatial_calc_eval_type** : :obj:`~VolumetricSpatialCalculationEvaluationType`


    :Returns:

        :obj:`~None`





