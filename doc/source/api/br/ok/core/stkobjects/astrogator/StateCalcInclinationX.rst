StateCalcInclinationX
=====================

.. py:class:: br.ok.core.stkobjects.astrogator.StateCalcInclinationX

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   InclinationX Calc objects.

.. py:currentmodule:: StateCalcInclinationX

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcInclinationX.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcInclinationX.inclination_magnitude_type`
              - Magnitude to use when computing the inclination vector.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import StateCalcInclinationX


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcInclinationX.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: inclination_magnitude_type
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcInclinationX.inclination_magnitude_type
    :type: GeoStationaryInclinationMagnitude

    Magnitude to use when computing the inclination vector.


