CommSystemAccessEventDetectionSubsample
=======================================

.. py:class:: br.ok.core.stkobjects.CommSystemAccessEventDetectionSubsample

   Bases: :py:class:`~br.ok.core.stkobjects.ICommSystemAccessEventDetection`

   Class defining a CommSystem access options.

.. py:currentmodule:: CommSystemAccessEventDetectionSubsample

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.CommSystemAccessEventDetectionSubsample.absolute_tolerance`
              - Get or set the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.
            * - :py:attr:`~br.ok.core.stkobjects.CommSystemAccessEventDetectionSubsample.relative_tolerance`
              - An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.
            * - :py:attr:`~br.ok.core.stkobjects.CommSystemAccessEventDetectionSubsample.time_convergence`
              - Get or set the time convergence value for Access. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import CommSystemAccessEventDetectionSubsample


Property detail
---------------

.. py:property:: absolute_tolerance
    :canonical: br.ok.core.stkobjects.CommSystemAccessEventDetectionSubsample.absolute_tolerance
    :type: float

    Get or set the criterion used for convergence in value for values near 0. An event is said to be detected when a constraint value's difference compared to the previous sample is within this tolerance: (value - previousValue) < absoluteTolerance.

.. py:property:: relative_tolerance
    :canonical: br.ok.core.stkobjects.CommSystemAccessEventDetectionSubsample.relative_tolerance
    :type: float

    An event is said to be detected when a constraint value's relative difference compared to the previous sample is within this tolerance: (value - previousValue) / value < relativeTolerance.

.. py:property:: time_convergence
    :canonical: br.ok.core.stkobjects.CommSystemAccessEventDetectionSubsample.time_convergence
    :type: float

    Get or set the time convergence value for Access. Uses Time Dimension.


