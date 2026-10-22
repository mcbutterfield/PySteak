IAnalysisWorkbenchComponentContext
==================================

.. py:class:: br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentContext

   The interface represents a context associated with a VGT component. All VGT components are associated with a valid context. A context can represent a VGT instance or a VGT template.

.. py:currentmodule:: IAnalysisWorkbenchComponentContext

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentContext.is_template`
              - Return whether the current instance is a VGT template.


Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import IAnalysisWorkbenchComponentContext


Property detail
---------------

.. py:property:: is_template
    :canonical: br.steak.core.analysis_workbench.IAnalysisWorkbenchComponentContext.is_template
    :type: bool

    Return whether the current instance is a VGT template.


