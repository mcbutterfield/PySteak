TimeToolAxesSamplingInterval
============================

.. py:class:: br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval

   The interface represents an interval with the time, orientation and velocity arrays.

.. py:currentmodule:: TimeToolAxesSamplingInterval

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.quaternions`
              - An array of 4-tuples each tuple representing the orientation of the axes as a quaternion (q1,q2,q3,q4).
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.start`
              - The start time of the interval.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.stop`
              - The stop time of the interval.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.times`
              - A time array associated with the interval.
            * - :py:attr:`~br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.velocities`
              - An array of angular velocities.



Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import TimeToolAxesSamplingInterval


Property detail
---------------

.. py:property:: quaternions
    :canonical: br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.quaternions
    :type: list

    An array of 4-tuples each tuple representing the orientation of the axes as a quaternion (q1,q2,q3,q4).

.. py:property:: start
    :canonical: br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.start
    :type: typing.Any

    The start time of the interval.

.. py:property:: stop
    :canonical: br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.stop
    :type: typing.Any

    The stop time of the interval.

.. py:property:: times
    :canonical: br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.times
    :type: list

    A time array associated with the interval.

.. py:property:: velocities
    :canonical: br.ok.core.analysis_workbench.TimeToolAxesSamplingInterval.velocities
    :type: list

    An array of angular velocities.


