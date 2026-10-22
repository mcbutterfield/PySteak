ITimeToolTimeInterval
=====================

.. py:class:: br.steak.core.analysis_workbench.ITimeToolTimeInterval

   A single time interval.

.. py:currentmodule:: ITimeToolTimeInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.ITimeToolTimeInterval.find_interval`
              - Return computed interval if it exists.
            * - :py:attr:`~br.steak.core.analysis_workbench.ITimeToolTimeInterval.occurred`
              - Determine if specified time falls within computed interval if it exists.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.ITimeToolTimeInterval.label_start`
              - A label associated with the interval start.
            * - :py:attr:`~br.steak.core.analysis_workbench.ITimeToolTimeInterval.label_start_description`
              - The start description.
            * - :py:attr:`~br.steak.core.analysis_workbench.ITimeToolTimeInterval.label_stop`
              - A label associated with the interval stop.
            * - :py:attr:`~br.steak.core.analysis_workbench.ITimeToolTimeInterval.label_stop_description`
              - The stop description.
            * - :py:attr:`~br.steak.core.analysis_workbench.ITimeToolTimeInterval.type`
              - Return the type of interval.


Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import ITimeToolTimeInterval


Property detail
---------------

.. py:property:: label_start
    :canonical: br.steak.core.analysis_workbench.ITimeToolTimeInterval.label_start
    :type: str

    A label associated with the interval start.

.. py:property:: label_start_description
    :canonical: br.steak.core.analysis_workbench.ITimeToolTimeInterval.label_start_description
    :type: str

    The start description.

.. py:property:: label_stop
    :canonical: br.steak.core.analysis_workbench.ITimeToolTimeInterval.label_stop
    :type: str

    A label associated with the interval stop.

.. py:property:: label_stop_description
    :canonical: br.steak.core.analysis_workbench.ITimeToolTimeInterval.label_stop_description
    :type: str

    The stop description.

.. py:property:: type
    :canonical: br.steak.core.analysis_workbench.ITimeToolTimeInterval.type
    :type: EventIntervalType

    Return the type of interval.


Method detail
-------------

.. py:method:: find_interval(self) -> TimeToolTimeIntervalResult
    :canonical: br.steak.core.analysis_workbench.ITimeToolTimeInterval.find_interval

    Return computed interval if it exists.

    :Returns:

        :obj:`~TimeToolTimeIntervalResult`





.. py:method:: occurred(self, epoch: typing.Any) -> bool
    :canonical: br.steak.core.analysis_workbench.ITimeToolTimeInterval.occurred

    Determine if specified time falls within computed interval if it exists.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~bool`


