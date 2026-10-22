ITimeToolInstant
================

.. py:class:: br.ok.core.analysis_workbench.ITimeToolInstant

   Define an event (time instant).

.. py:currentmodule:: ITimeToolInstant

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.ITimeToolInstant.find_occurrence`
              - Return computed time instance if it occurs.
            * - :py:attr:`~br.ok.core.analysis_workbench.ITimeToolInstant.occurs_before`
              - Return true if computed time instance occurs before or at specified time, return false otherwise.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.analysis_workbench.ITimeToolInstant.noon_today`
              - Return time instant that corresponds to today's GMT noon.
            * - :py:attr:`~br.ok.core.analysis_workbench.ITimeToolInstant.noon_tomorrow`
              - Return time instant that corresponds to tomorrow's GMT noon.
            * - :py:attr:`~br.ok.core.analysis_workbench.ITimeToolInstant.today`
              - Return time instant that corresponds to today's GMT midnight.
            * - :py:attr:`~br.ok.core.analysis_workbench.ITimeToolInstant.tomorrow`
              - Return time instant that corresponds to tomorrow's GMT midnight.
            * - :py:attr:`~br.ok.core.analysis_workbench.ITimeToolInstant.type`
              - Return the type of time instant.


Import detail
-------------

.. code-block:: python

    from br.ok.core.analysis_workbench import ITimeToolInstant


Property detail
---------------

.. py:property:: noon_today
    :canonical: br.ok.core.analysis_workbench.ITimeToolInstant.noon_today
    :type: ITimeToolInstant

    Return time instant that corresponds to today's GMT noon.

.. py:property:: noon_tomorrow
    :canonical: br.ok.core.analysis_workbench.ITimeToolInstant.noon_tomorrow
    :type: ITimeToolInstant

    Return time instant that corresponds to tomorrow's GMT noon.

.. py:property:: today
    :canonical: br.ok.core.analysis_workbench.ITimeToolInstant.today
    :type: ITimeToolInstant

    Return time instant that corresponds to today's GMT midnight.

.. py:property:: tomorrow
    :canonical: br.ok.core.analysis_workbench.ITimeToolInstant.tomorrow
    :type: ITimeToolInstant

    Return time instant that corresponds to tomorrow's GMT midnight.

.. py:property:: type
    :canonical: br.ok.core.analysis_workbench.ITimeToolInstant.type
    :type: TimeEventType

    Return the type of time instant.


Method detail
-------------

.. py:method:: find_occurrence(self) -> TimeToolInstantOccurrenceResult
    :canonical: br.ok.core.analysis_workbench.ITimeToolInstant.find_occurrence

    Return computed time instance if it occurs.

    :Returns:

        :obj:`~TimeToolInstantOccurrenceResult`



.. py:method:: occurs_before(self, epoch: typing.Any) -> bool
    :canonical: br.ok.core.analysis_workbench.ITimeToolInstant.occurs_before

    Return true if computed time instance occurs before or at specified time, return false otherwise.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~bool`




