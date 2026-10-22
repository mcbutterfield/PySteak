VectorGeometryToolVectorCustomScript
====================================

.. py:class:: br.ok.core.analysis_workbench.VectorGeometryToolVectorCustomScript

   Bases: :py:class:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Customized vector components defined with respect to reference axes.

.. py:currentmodule:: VectorGeometryToolVectorCustomScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorCustomScript.initialization_script_file`
              - Specify an initialization script file (optional). The initialization script is run once, at the beginning of the calculation.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorCustomScript.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~br.ok.core.analysis_workbench.VectorGeometryToolVectorCustomScript.script_file`
              - Specify a script file.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import VectorGeometryToolVectorCustomScript


Property detail
---------------

.. py:property:: initialization_script_file
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorCustomScript.initialization_script_file
    :type: str

    Specify an initialization script file (optional). The initialization script is run once, at the beginning of the calculation.

.. py:property:: reference_axes
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorCustomScript.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: script_file
    :canonical: br.ok.core.analysis_workbench.VectorGeometryToolVectorCustomScript.script_file
    :type: str

    Specify a script file.


