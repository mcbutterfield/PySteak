TimeToolPointSamplingInterval
=============================

.. py:class:: br.ok.core.analysis_workbench.TimeToolPointSamplingInterval

   The interface represents an interval with the time, position and velocity arrays.

.. py:currentmodule:: TimeToolPointSamplingInterval

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.positions`
              - An array of 3-tuples each tuple representing the point's cartesian position (x,y,z).
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.start`
              - The start time of the interval.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.stop`
              - The stop time of the interval.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.times`
              - A time array associated with the interval.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.velocities`
              - An array of velocities.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import TimeToolPointSamplingInterval


Property detail
---------------

.. py:property:: positions
    :canonical: br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.positions
    :type: list

    An array of 3-tuples each tuple representing the point's cartesian position (x,y,z).

.. py:property:: start
    :canonical: br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.start
    :type: typing.Any

    The start time of the interval.

.. py:property:: stop
    :canonical: br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.stop
    :type: typing.Any

    The stop time of the interval.

.. py:property:: times
    :canonical: br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.times
    :type: list

    A time array associated with the interval.

.. py:property:: velocities
    :canonical: br.ok.core.analysis_workbench.TimeToolPointSamplingInterval.velocities
    :type: list

    An array of velocities.


