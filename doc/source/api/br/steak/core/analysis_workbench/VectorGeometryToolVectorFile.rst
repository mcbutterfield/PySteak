VectorGeometryToolVectorFile
============================

.. py:class:: br.steak.core.analysis_workbench.VectorGeometryToolVectorFile

   Bases: :py:class:`~br.steak.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Vector interpolated from tabulated data from file.

.. py:currentmodule:: VectorGeometryToolVectorFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorFile.reload`
              - Reload the file specified with Filename property.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorFile.filename`
              - A path to vector data file.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import VectorGeometryToolVectorFile


Property detail
---------------

.. py:property:: filename
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorFile.filename
    :type: str

    A path to vector data file.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorFile.reload

    Reload the file specified with Filename property.

    :Returns:

        :obj:`~None`

