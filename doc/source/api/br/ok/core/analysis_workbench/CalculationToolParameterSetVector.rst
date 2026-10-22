CalculationToolParameterSetVector
=================================

.. py:class:: br.ok.core.analysis_workbench.CalculationToolParameterSetVector

   Bases: :py:class:`~br.ok.core.analysis_workbench.ICalculationToolParameterSet`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Vector parameter set contains various representations of a vector in a reference set of axes.

.. py:currentmodule:: CalculationToolParameterSetVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolParameterSetVector.reference_axes`
              - Get the reference axes relative to which representations are computed.
            * - :py:attr:`~br.ok.core.analysis_workbench.CalculationToolParameterSetVector.vector`
              - Get the vector for which representations are computed.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import CalculationToolParameterSetVector


Property detail
---------------

.. py:property:: reference_axes
    :canonical: br.ok.core.analysis_workbench.CalculationToolParameterSetVector.reference_axes
    :type: IVectorGeometryToolAxes

    Get the reference axes relative to which representations are computed.

.. py:property:: vector
    :canonical: br.ok.core.analysis_workbench.CalculationToolParameterSetVector.vector
    :type: IVectorGeometryToolVector

    Get the vector for which representations are computed.


