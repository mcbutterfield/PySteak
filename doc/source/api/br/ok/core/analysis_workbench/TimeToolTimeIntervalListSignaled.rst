TimeToolTimeIntervalListSignaled
================================

.. py:class:: br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled

   Bases: :py:class:`~br.ok.core.analysis_workbench.ITimeToolTimeIntervalList`, :py:class:`~br.ok.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

.. py:currentmodule:: TimeToolTimeIntervalListSignaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.base_clock_location`
              - The base clock location, which is a point from VGT.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.original_intervals`
              - The original time interval list.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.signal_delay`
              - The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.signal_sense`
              - The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.target_clock_location`
              - The target clock location, which is a point from VGT.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import TimeToolTimeIntervalListSignaled


Property detail
---------------

.. py:property:: base_clock_location
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.base_clock_location
    :type: IVectorGeometryToolPoint

    The base clock location, which is a point from VGT.

.. py:property:: original_intervals
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.original_intervals
    :type: ITimeToolTimeIntervalList

    The original time interval list.

.. py:property:: signal_delay
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.signal_delay
    :type: IAnalysisWorkbenchSignalDelay

    The Signal delay definition, which includes signal transmission, time delay convergence and signal path reference system.

.. py:property:: signal_sense
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.signal_sense
    :type: SignalDirectionType

    The direction of the signal, whether you are Transmitting or Receiving from the Base Clock Location.

.. py:property:: target_clock_location
    :canonical: br.ok.core.analysis_workbench.TimeToolTimeIntervalListSignaled.target_clock_location
    :type: IVectorGeometryToolPoint

    The target clock location, which is a point from VGT.


