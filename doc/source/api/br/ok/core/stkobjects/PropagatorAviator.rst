PropagatorAviator
=================

.. py:class:: br.ok.core.stkobjects.PropagatorAviator

   Bases: :py:class:`~br.ok.core.stkobjects.IPropagator`

   Class defining the Mission Modler propagator for an Aircraft.

.. py:currentmodule:: PropagatorAviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorAviator.get_flight_mission`
              - Return the underlying Flight Mission object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PropagatorAviator.aviator_propagator`
              - Aviator propagator object.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import PropagatorAviator


Property detail
---------------

.. py:property:: aviator_propagator
    :canonical: br.ok.core.stkobjects.PropagatorAviator.aviator_propagator
    :type: typing.Any

    Aviator propagator object.


Method detail
-------------


.. py:method:: get_flight_mission(self) -> typing.Any
    :canonical: br.ok.core.stkobjects.PropagatorAviator.get_flight_mission

    Return the underlying Flight Mission object.

    :Returns:

        :obj:`~typing.Any`

