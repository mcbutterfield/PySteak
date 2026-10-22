MissileAerodynamic
==================

.. py:class:: br.ok.core.stkobjects.aviator.MissileAerodynamic

   Class defining the aerodynamic options for a missile.

.. py:currentmodule:: MissileAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileAerodynamic.aerodynamic_strategy`
              - Get or set the aerodynamic strategy type.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileAerodynamic.mode_as_advanced`
              - Get the interface for an advanced aerodynamics strategy.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileAerodynamic.mode_as_external`
              - Get the interface for an external file aerodynamics strategy.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileAerodynamic.mode_as_four_point`
              - Get the interface for an four point aerodynamics strategy.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileAerodynamic.mode_as_simple`
              - Get the interface for a simple aerodynamics strategy.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import MissileAerodynamic


Property detail
---------------

.. py:property:: aerodynamic_strategy
    :canonical: br.ok.core.stkobjects.aviator.MissileAerodynamic.aerodynamic_strategy
    :type: MissileAerodynamicStrategy

    Get or set the aerodynamic strategy type.

.. py:property:: mode_as_advanced
    :canonical: br.ok.core.stkobjects.aviator.MissileAerodynamic.mode_as_advanced
    :type: MissileAdvancedAerodynamic

    Get the interface for an advanced aerodynamics strategy.

.. py:property:: mode_as_external
    :canonical: br.ok.core.stkobjects.aviator.MissileAerodynamic.mode_as_external
    :type: MissileExternalAerodynamic

    Get the interface for an external file aerodynamics strategy.

.. py:property:: mode_as_four_point
    :canonical: br.ok.core.stkobjects.aviator.MissileAerodynamic.mode_as_four_point
    :type: MissileFourPointAerodynamic

    Get the interface for an four point aerodynamics strategy.

.. py:property:: mode_as_simple
    :canonical: br.ok.core.stkobjects.aviator.MissileAerodynamic.mode_as_simple
    :type: MissileSimpleAerodynamic

    Get the interface for a simple aerodynamics strategy.


