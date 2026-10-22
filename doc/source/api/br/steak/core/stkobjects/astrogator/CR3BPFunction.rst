CR3BPFunction
=============

.. py:class:: br.steak.core.stkobjects.astrogator.CR3BPFunction

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.astrogator.ICloneable`

   CR3BP Function.

.. py:currentmodule:: CR3BPFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.CR3BPFunction.characteristic_acceleration`
              - Get the characteristic acceleration computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.CR3BPFunction.characteristic_distance`
              - Get the characteristic distance computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.CR3BPFunction.characteristic_time`
              - Get the characteristic time computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.CR3BPFunction.characteristic_velocity`
              - Get the characteristic velocity computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.CR3BPFunction.eccentricity`
              - Get the eccentricity at the reference epoch for the secondary's orbit.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.CR3BPFunction.ephemeris_epoch`
              - Get the epoch from which the eccentricity value is reported from the secondary.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.CR3BPFunction.mass_parameter`
              - Get the mass parameter computed from the primary and secondary bodies.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.CR3BPFunction.secondary_name`
              - Get or set the secondary body  which should be consistently defined with CR3BP model definitions.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import CR3BPFunction


Property detail
---------------

.. py:property:: characteristic_acceleration
    :canonical: br.steak.core.stkobjects.astrogator.CR3BPFunction.characteristic_acceleration
    :type: float

    Get the characteristic acceleration computed from the primary and secondary bodies.

.. py:property:: characteristic_distance
    :canonical: br.steak.core.stkobjects.astrogator.CR3BPFunction.characteristic_distance
    :type: float

    Get the characteristic distance computed from the primary and secondary bodies.

.. py:property:: characteristic_time
    :canonical: br.steak.core.stkobjects.astrogator.CR3BPFunction.characteristic_time
    :type: float

    Get the characteristic time computed from the primary and secondary bodies.

.. py:property:: characteristic_velocity
    :canonical: br.steak.core.stkobjects.astrogator.CR3BPFunction.characteristic_velocity
    :type: float

    Get the characteristic velocity computed from the primary and secondary bodies.

.. py:property:: eccentricity
    :canonical: br.steak.core.stkobjects.astrogator.CR3BPFunction.eccentricity
    :type: float

    Get the eccentricity at the reference epoch for the secondary's orbit.

.. py:property:: ephemeris_epoch
    :canonical: br.steak.core.stkobjects.astrogator.CR3BPFunction.ephemeris_epoch
    :type: typing.Any

    Get the epoch from which the eccentricity value is reported from the secondary.

.. py:property:: mass_parameter
    :canonical: br.steak.core.stkobjects.astrogator.CR3BPFunction.mass_parameter
    :type: float

    Get the mass parameter computed from the primary and secondary bodies.

.. py:property:: secondary_name
    :canonical: br.steak.core.stkobjects.astrogator.CR3BPFunction.secondary_name
    :type: str

    Get or set the secondary body  which should be consistently defined with CR3BP model definitions.


