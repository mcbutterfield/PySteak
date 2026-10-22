PropagatorRealtimeCartesianPoints
=================================

.. py:class:: br.steak.core.stkobjects.PropagatorRealtimeCartesianPoints

   PropagatorRealtimeCartesianPoints Class.

.. py:currentmodule:: PropagatorRealtimeCartesianPoints

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.PropagatorRealtimeCartesianPoints.add`
              - Add an ephemeris point using position and velocity. Epoch uses DateFormat dimension.
            * - :py:attr:`~br.steak.core.stkobjects.PropagatorRealtimeCartesianPoints.add_position`
              - Add an ephemeris point. Epoch uses DateFormat dimension.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import PropagatorRealtimeCartesianPoints



Method detail
-------------

.. py:method:: add(self, time: typing.Any, x: float, y: float, z: float, vx: float, vy: float, vz: float) -> None
    :canonical: br.steak.core.stkobjects.PropagatorRealtimeCartesianPoints.add

    Add an ephemeris point using position and velocity. Epoch uses DateFormat dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`

        **x** : :obj:`~float`

        **y** : :obj:`~float`

        **z** : :obj:`~float`

        **vx** : :obj:`~float`

        **vy** : :obj:`~float`

        **vz** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: add_position(self, time: typing.Any, x: float, y: float, z: float) -> None
    :canonical: br.steak.core.stkobjects.PropagatorRealtimeCartesianPoints.add_position

    Add an ephemeris point. Epoch uses DateFormat dimension.

    :Parameters:

        **time** : :obj:`~typing.Any`

        **x** : :obj:`~float`

        **y** : :obj:`~float`

        **z** : :obj:`~float`


    :Returns:

        :obj:`~None`

