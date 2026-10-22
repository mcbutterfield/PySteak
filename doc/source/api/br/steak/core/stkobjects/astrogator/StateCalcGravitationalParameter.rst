StateCalcGravitationalParameter
===============================

.. py:class:: br.steak.core.stkobjects.astrogator.StateCalcGravitationalParameter

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   GravitationalParameter Calc objects.

.. py:currentmodule:: StateCalcGravitationalParameter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcGravitationalParameter.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcGravitationalParameter.gravitational_parameter_source`
              - Get or set the source for the gravitational parameter.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.StateCalcGravitationalParameter.gravity_filename`
              - Source for the gravitational parameter if GravSource is set to Gravity File.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import StateCalcGravitationalParameter


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcGravitationalParameter.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: gravitational_parameter_source
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcGravitationalParameter.gravitational_parameter_source
    :type: GravitationalParameterSource

    Get or set the source for the gravitational parameter.

.. py:property:: gravity_filename
    :canonical: br.steak.core.stkobjects.astrogator.StateCalcGravitationalParameter.gravity_filename
    :type: str

    Source for the gravitational parameter if GravSource is set to Gravity File.


