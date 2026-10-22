AnalysisWorkbenchAngleFindAngleWithRateResult
=============================================

.. py:class:: br.steak.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleWithRateResult

   Bases: :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAngle.FindAngleWithRate method.

.. py:currentmodule:: AnalysisWorkbenchAngleFindAngleWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleWithRateResult.angle`
              - The computed angle. The value of the angle is in ``AngleUnit`` dimension.
            * - :py:attr:`~br.steak.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleWithRateResult.angle_rate`
              - The computed angle rate. The value of the angle rate is in ``AngleRateUnit`` dimension.
            * - :py:attr:`~br.steak.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleWithRateResult.is_valid`
              - Indicate whether the result object is valid.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import AnalysisWorkbenchAngleFindAngleWithRateResult


Property detail
---------------

.. py:property:: angle
    :canonical: br.steak.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleWithRateResult.angle
    :type: typing.Any

    The computed angle. The value of the angle is in ``AngleUnit`` dimension.

.. py:property:: angle_rate
    :canonical: br.steak.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleWithRateResult.angle_rate
    :type: typing.Any

    The computed angle rate. The value of the angle rate is in ``AngleRateUnit`` dimension.

.. py:property:: is_valid
    :canonical: br.steak.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleWithRateResult.is_valid
    :type: bool

    Indicate whether the result object is valid.


