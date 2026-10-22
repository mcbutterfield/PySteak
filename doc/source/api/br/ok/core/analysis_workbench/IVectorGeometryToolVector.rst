IVectorGeometryToolVector
=========================

.. py:class:: br.ok.core.analysis_workbench.IVectorGeometryToolVector

   The interface defines methods and properties common to all vectors.

.. py:currentmodule:: IVectorGeometryToolVector

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector.find_in_axes`
              - Compute the vector in the specified axes.
            * - :py:attr:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector.find_in_axes_with_rate`
              - Compute the vector and its rate in the specified axes.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.IVectorGeometryToolVector.type`
              - Return a type of the vector object.


Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import IVectorGeometryToolVector


Property detail
---------------

.. py:property:: type
    :canonical: br.ok.core.analysis_workbench.IVectorGeometryToolVector.type
    :type: VectorType

    Return a type of the vector object.


Method detail
-------------

.. py:method:: find_in_axes(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchVectorFindInAxesResult
    :canonical: br.ok.core.analysis_workbench.IVectorGeometryToolVector.find_in_axes

    Compute the vector in the specified axes.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **axes** : :obj:`~IVectorGeometryToolAxes`


    :Returns:

        :obj:`~AnalysisWorkbenchVectorFindInAxesResult`

.. py:method:: find_in_axes_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchVectorFindInAxesWithRateResult
    :canonical: br.ok.core.analysis_workbench.IVectorGeometryToolVector.find_in_axes_with_rate

    Compute the vector and its rate in the specified axes.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **axes** : :obj:`~IVectorGeometryToolAxes`


    :Returns:

        :obj:`~AnalysisWorkbenchVectorFindInAxesWithRateResult`


