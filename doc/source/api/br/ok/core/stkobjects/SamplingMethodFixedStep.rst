SamplingMethodFixedStep
=======================

.. py:class:: br.ok.core.stkobjects.SamplingMethodFixedStep

   Bases: :py:class:`~br.ok.core.stkobjects.ISamplingMethodStrategy`

   Define a fixed time-step sampling method.

.. py:currentmodule:: SamplingMethodFixedStep

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.SamplingMethodFixedStep.fixed_time_step`
              - Fixed sampling time step. Uses Time Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.SamplingMethodFixedStep.time_bound`
              - Duration used to align sample times with UTC. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import SamplingMethodFixedStep


Property detail
---------------

.. py:property:: fixed_time_step
    :canonical: br.ok.core.stkobjects.SamplingMethodFixedStep.fixed_time_step
    :type: float

    Fixed sampling time step. Uses Time Dimension.

.. py:property:: time_bound
    :canonical: br.ok.core.stkobjects.SamplingMethodFixedStep.time_bound
    :type: float

    Duration used to align sample times with UTC. Uses Time Dimension.


