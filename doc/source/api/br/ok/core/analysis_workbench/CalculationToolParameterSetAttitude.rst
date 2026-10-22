CalculationToolParameterSetAttitude
===================================

.. py:class:: br.ok.core.analysis_workbench.CalculationToolParameterSetAttitude

   Bases: :py:class:`~br.ok.core.analysis_workbench.ICalculationToolParameterSet`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Attitude parameter set contains various representations of attitude of one set of axes relative to another.

.. py:currentmodule:: CalculationToolParameterSetAttitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolParameterSetAttitude.axes`
              - Get the axes for which attitude representations are computed.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolParameterSetAttitude.reference_axes`
              - Get the reference axes relative to which attitude representations are computed.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import CalculationToolParameterSetAttitude


Property detail
---------------

.. py:property:: axes
    :canonical: br.ok.core.analysis_workbench.CalculationToolParameterSetAttitude.axes
    :type: IVectorGeometryToolAxes

    Get the axes for which attitude representations are computed.

.. py:property:: reference_axes
    :canonical: br.ok.core.analysis_workbench.CalculationToolParameterSetAttitude.reference_axes
    :type: IVectorGeometryToolAxes

    Get the reference axes relative to which attitude representations are computed.


