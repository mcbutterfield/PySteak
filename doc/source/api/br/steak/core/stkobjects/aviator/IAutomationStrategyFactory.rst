IAutomationStrategyFactory
==========================

.. py:class:: br.steak.core.stkobjects.aviator.IAutomationStrategyFactory

   Interface used to send connect commands to Aviator objects.

.. py:currentmodule:: IAutomationStrategyFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.IAutomationStrategyFactory.construct_strategy`
              - Construct the strategy.

Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.aviator import IAutomationStrategyFactory



Method detail
-------------

.. py:method:: construct_strategy(self, obj: IUnknown) -> IBasicManeuverStrategy
    :canonical: br.steak.core.stkobjects.aviator.IAutomationStrategyFactory.construct_strategy

    Construct the strategy.

    :Parameters:

        **obj** : :obj:`~IUnknown`


    :Returns:

        :obj:`~IBasicManeuverStrategy`

