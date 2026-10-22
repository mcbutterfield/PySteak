VehicleMethod
=============

.. py:class:: br.steak.core.stkobjects.VehicleMethod

   IntEnum


.. py:currentmodule:: VehicleMethod

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FIXED_STEP`
              - Fixed step: step size will remain constant throughout the integration of the orbit.

            * - :py:attr:`~RELATIVE_ERROR`
              - Relative error: Control the step size based on relative error by providing the error tolerance, and the minimum and maximum integration step sizes to be allowed via relative error control.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleMethod


