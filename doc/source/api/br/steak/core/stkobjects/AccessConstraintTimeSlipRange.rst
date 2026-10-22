AccessConstraintTimeSlipRange
=============================

.. py:class:: br.steak.core.stkobjects.AccessConstraintTimeSlipRange

   Bases: :py:class:`~br.steak.core.stkobjects.IAccessConstraint`

   Class for controlling the use the Time Slip constraint for a missile or launch vehicle, used with the Close Approach Tool.

.. py:currentmodule:: AccessConstraintTimeSlipRange

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintTimeSlipRange.launch_window_end`
              - Launch Window End time. Uses DateFormat Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintTimeSlipRange.launch_window_start`
              - Launch Window Start time. Uses DateFormat Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintTimeSlipRange.range`
              - Range of the launch window. When available, uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AccessConstraintTimeSlipRange


Property detail
---------------

.. py:property:: launch_window_end
    :canonical: br.steak.core.stkobjects.AccessConstraintTimeSlipRange.launch_window_end
    :type: typing.Any

    Launch Window End time. Uses DateFormat Dimension.

.. py:property:: launch_window_start
    :canonical: br.steak.core.stkobjects.AccessConstraintTimeSlipRange.launch_window_start
    :type: typing.Any

    Launch Window Start time. Uses DateFormat Dimension.

.. py:property:: range
    :canonical: br.steak.core.stkobjects.AccessConstraintTimeSlipRange.range
    :type: float

    Range of the launch window. When available, uses Distance Dimension.


