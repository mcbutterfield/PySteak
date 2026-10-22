TimeToolTimeArrayFindTimesResult
================================

.. py:class:: br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult

   Return a collection of intervals and an array of times.

.. py:currentmodule:: TimeToolTimeArrayFindTimesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.intervals`
              - A collection of found intervals.
            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.is_valid`
              - Indicate whether the result object is valid.
            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.start`
              - The start time of the entire interval span.
            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.stop`
              - The stop time of the entire interval span.
            * - :py:attr:`~br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.times`
              - An array of found times.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import TimeToolTimeArrayFindTimesResult


Property detail
---------------

.. py:property:: intervals
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.intervals
    :type: TimeToolIntervalCollection

    A collection of found intervals.

.. py:property:: is_valid
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.is_valid
    :type: bool

    Indicate whether the result object is valid.

.. py:property:: start
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.start
    :type: typing.Any

    The start time of the entire interval span.

.. py:property:: stop
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.stop
    :type: typing.Any

    The stop time of the entire interval span.

.. py:property:: times
    :canonical: br.steak.core.analysis_workbench.TimeToolTimeArrayFindTimesResult.times
    :type: list

    An array of found times.


