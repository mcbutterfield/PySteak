StateCalcInclinationY
=====================

.. py:class:: br.steak.core.stkobjects.astrogator.StateCalcInclinationY

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   InclinationY Calc objects.

.. py:currentmodule:: StateCalcInclinationY

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcInclinationY.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcInclinationY.inclination_magnitude_type`
              - Magnitude to use when computing the inclination vector.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import StateCalcInclinationY


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcInclinationY.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: inclination_magnitude_type
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcInclinationY.inclination_magnitude_type
    :type: GeoStationaryInclinationMagnitude

    Magnitude to use when computing the inclination vector.


