TimeToolInstantStartStopTime
============================

.. py:class:: br.ok.core.analysis_workbench.TimeToolInstantStartStopTime

   Bases: :py:class:`~br.ok.core.analysis_workbench.ITimeToolInstant`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Event is either start or stop time selected from a reference interval.

.. py:currentmodule:: TimeToolInstantStartStopTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolInstantStartStopTime.reference_interval`
              - The reference interval.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolInstantStartStopTime.use_start`
              - Indicate whether to use start (true) or stop (false).



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import TimeToolInstantStartStopTime


Property detail
---------------

.. py:property:: reference_interval
    :canonical: br.ok.core.analysis_workbench.TimeToolInstantStartStopTime.reference_interval
    :type: ITimeToolTimeInterval

    The reference interval.

.. py:property:: use_start
    :canonical: br.ok.core.analysis_workbench.TimeToolInstantStartStopTime.use_start
    :type: bool

    Indicate whether to use start (true) or stop (false).


