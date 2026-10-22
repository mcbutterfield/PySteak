VehicleZonalPropagatorInitialState
==================================

.. py:class:: br.ok.core.stkobjects.VehicleZonalPropagatorInitialState

   Class defining initial state for the J2/4 propagators.

.. py:currentmodule:: VehicleZonalPropagatorInitialState

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.ellipse_options`
              - Options for modeling elliptical motion.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.orbit_epoch`
              - Get the smart epoch component to configure the orbit state epoch.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.propagation_frame`
              - Get or set the propagation frame.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.representation`
              - Representation.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.supported_propagation_frames`
              - Return supported propagation frames.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleZonalPropagatorInitialState


Property detail
---------------

.. py:property:: ellipse_options
    :canonical: br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.ellipse_options
    :type: VehicleEllipseOptionType

    Options for modeling elliptical motion.

.. py:property:: orbit_epoch
    :canonical: br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.orbit_epoch
    :type: ITimeToolInstantSmartEpoch

    Get the smart epoch component to configure the orbit state epoch.

.. py:property:: propagation_frame
    :canonical: br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.propagation_frame
    :type: VehiclePropagationFrame

    Get or set the propagation frame.

.. py:property:: representation
    :canonical: br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.representation
    :type: IOrbitState

    Representation.

.. py:property:: supported_propagation_frames
    :canonical: br.ok.core.stkobjects.VehicleZonalPropagatorInitialState.supported_propagation_frames
    :type: list

    Return supported propagation frames.


