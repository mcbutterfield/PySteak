DisplayTimesTimeComponent
=========================

.. py:class:: br.ok.core.stkobjects.DisplayTimesTimeComponent

   Bases: :py:class:`~br.ok.core.stkobjects.IDisplayTimesData`

   Provide methods to configure the display times using Timeline API components.

.. py:currentmodule:: DisplayTimesTimeComponent

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.DisplayTimesTimeComponent.get_qualified_path`
              - Return the time component' qualified path or null if no component has been configured yet.
            * - :py:attr:`~br.ok.core.stkobjects.DisplayTimesTimeComponent.get_time_component`
              - Return a time component used to configure the display times or null if component has not been configured yet.
            * - :py:attr:`~br.ok.core.stkobjects.DisplayTimesTimeComponent.reset`
              - Remove and resets the display configuration by unsetting currently set time component (if any).
            * - :py:attr:`~br.ok.core.stkobjects.DisplayTimesTimeComponent.set_qualified_path`
              - Configure the display times using the specified time component. Allowed are only intervals and interval lists. QualifiedPath format adheres to the format used throughout VGT API (i.e. ``Scenario/Scenario1 AnalysisInterval EventInterval``).
            * - :py:attr:`~br.ok.core.stkobjects.DisplayTimesTimeComponent.set_time_component`
              - Configure the display times using the specified time component. Allowed are only intervals and interval lists.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import DisplayTimesTimeComponent



Method detail
-------------

.. py:method:: get_qualified_path(self) -> str
    :canonical: br.ok.core.stkobjects.DisplayTimesTimeComponent.get_qualified_path

    Return the time component' qualified path or null if no component has been configured yet.

    :Returns:

        :obj:`~str`

.. py:method:: get_time_component(self) -> IAnalysisWorkbenchComponent
    :canonical: br.ok.core.stkobjects.DisplayTimesTimeComponent.get_time_component

    Return a time component used to configure the display times or null if component has not been configured yet.

    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`

.. py:method:: reset(self) -> None
    :canonical: br.ok.core.stkobjects.DisplayTimesTimeComponent.reset

    Remove and resets the display configuration by unsetting currently set time component (if any).

    :Returns:

        :obj:`~None`

.. py:method:: set_qualified_path(self, qualified_path: str) -> None
    :canonical: br.ok.core.stkobjects.DisplayTimesTimeComponent.set_qualified_path

    Configure the display times using the specified time component. Allowed are only intervals and interval lists. QualifiedPath format adheres to the format used throughout VGT API (i.e. ``Scenario/Scenario1 AnalysisInterval EventInterval``).

    :Parameters:

        **qualified_path** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_time_component(self, component: IAnalysisWorkbenchComponent) -> None
    :canonical: br.ok.core.stkobjects.DisplayTimesTimeComponent.set_time_component

    Configure the display times using the specified time component. Allowed are only intervals and interval lists.

    :Parameters:

        **component** : :obj:`~IAnalysisWorkbenchComponent`


    :Returns:

        :obj:`~None`

