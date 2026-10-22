AnalysisWorkbenchPointLocateInSystemResult
==========================================

.. py:class:: br.ok.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemResult

   Bases: :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolPlane.FindInSystemWithRate method.

.. py:currentmodule:: AnalysisWorkbenchPointLocateInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~br.ok.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemResult.position`
              - The point position in the specified coordinate system.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import AnalysisWorkbenchPointLocateInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: br.ok.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemResult.position
    :type: ICartesian3Vector

    The point position in the specified coordinate system.


