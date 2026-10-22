IAccessAdvanced
===============

.. py:class:: br.steak.core.stkobjects.IAccessAdvanced

   Interface for configuring advanced targeting access computation properties.

.. py:currentmodule:: IAccessAdvanced

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.IAccessAdvanced.aberration_type`
              - Model used for including aberration in apparent direction computations.
            * - :py:attr:`~br.steak.core.stkobjects.IAccessAdvanced.event_detection`
              - Event detection strategy used in access calculations.
            * - :py:attr:`~br.steak.core.stkobjects.IAccessAdvanced.sampling`
              - Sampling method used in access calculations.
            * - :py:attr:`~br.steak.core.stkobjects.IAccessAdvanced.time_delay_convergence`
              - Time delay convergence tolerance. Uses Time Dimension.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import IAccessAdvanced


Property detail
---------------

.. py:property:: aberration_type
    :canonical: br.steak.core.stkobjects.IAccessAdvanced.aberration_type
    :type: AberrationType

    Model used for including aberration in apparent direction computations.

.. py:property:: event_detection
    :canonical: br.steak.core.stkobjects.IAccessAdvanced.event_detection
    :type: AccessEventDetection

    Event detection strategy used in access calculations.

.. py:property:: sampling
    :canonical: br.steak.core.stkobjects.IAccessAdvanced.sampling
    :type: AccessSampling

    Sampling method used in access calculations.

.. py:property:: time_delay_convergence
    :canonical: br.steak.core.stkobjects.IAccessAdvanced.time_delay_convergence
    :type: float

    Time delay convergence tolerance. Uses Time Dimension.


