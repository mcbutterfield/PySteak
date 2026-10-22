IAccessAdvanced
===============

.. py:class:: br.ok.core.stkobjects.IAccessAdvanced

   Interface for configuring advanced targeting access computation properties.

.. py:currentmodule:: IAccessAdvanced

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IAccessAdvanced.aberration_type`
              - Model used for including aberration in apparent direction computations.
            * - :py:attr:`~br.ok.core.stkobjects.IAccessAdvanced.event_detection`
              - Event detection strategy used in access calculations.
            * - :py:attr:`~br.ok.core.stkobjects.IAccessAdvanced.sampling`
              - Sampling method used in access calculations.
            * - :py:attr:`~br.ok.core.stkobjects.IAccessAdvanced.time_delay_convergence`
              - Time delay convergence tolerance. Uses Time Dimension.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IAccessAdvanced


Property detail
---------------

.. py:property:: aberration_type
    :canonical: br.ok.core.stkobjects.IAccessAdvanced.aberration_type
    :type: AberrationType

    Model used for including aberration in apparent direction computations.

.. py:property:: event_detection
    :canonical: br.ok.core.stkobjects.IAccessAdvanced.event_detection
    :type: AccessEventDetection

    Event detection strategy used in access calculations.

.. py:property:: sampling
    :canonical: br.ok.core.stkobjects.IAccessAdvanced.sampling
    :type: AccessSampling

    Sampling method used in access calculations.

.. py:property:: time_delay_convergence
    :canonical: br.ok.core.stkobjects.IAccessAdvanced.time_delay_convergence
    :type: float

    Time delay convergence tolerance. Uses Time Dimension.


