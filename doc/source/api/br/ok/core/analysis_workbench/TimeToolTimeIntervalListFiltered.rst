TimeToolTimeIntervalListFiltered
================================

.. py:class:: br.ok.core.analysis_workbench.TimeToolTimeIntervalListFiltered

   Bases: :py:class:`~br.ok.core.analysis_workbench.ITimeToolTimeIntervalList`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by filtering intervals from original interval list using specified filtering method.

.. py:currentmodule:: TimeToolTimeIntervalListFiltered

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalListFiltered.filter`
              - The pruning filter.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalListFiltered.filter_factory`
              - Get the prune filter factory.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalListFiltered.original_intervals`
              - The original interval list.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import TimeToolTimeIntervalListFiltered


Property detail
---------------

.. py:property:: filter
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalListFiltered.filter
    :type: ITimeToolPruneFilter

    The pruning filter.

.. py:property:: filter_factory
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalListFiltered.filter_factory
    :type: TimeToolPruneFilterFactory

    Get the prune filter factory.

.. py:property:: original_intervals
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalListFiltered.original_intervals
    :type: ITimeToolTimeIntervalList

    The original interval list.


