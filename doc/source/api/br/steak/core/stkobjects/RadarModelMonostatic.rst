RadarModelMonostatic
====================

.. py:class:: br.steak.core.stkobjects.RadarModelMonostatic

   Bases: :py:class:`~br.steak.core.stkobjects.IRadarModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a monostatic radar model.

.. py:currentmodule:: RadarModelMonostatic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RadarModelMonostatic.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~br.steak.core.stkobjects.RadarModelMonostatic.clutter`
              - Get the radar clutter settings.
            * - :py:attr:`~br.steak.core.stkobjects.RadarModelMonostatic.jamming`
              - Get the radar jamming.
            * - :py:attr:`~br.steak.core.stkobjects.RadarModelMonostatic.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.
            * - :py:attr:`~br.steak.core.stkobjects.RadarModelMonostatic.receiver`
              - Get the radar receiver.
            * - :py:attr:`~br.steak.core.stkobjects.RadarModelMonostatic.transmitter`
              - Get the radar transmitter.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RadarModelMonostatic


Property detail
---------------

.. py:property:: antenna_control
    :canonical: br.steak.core.stkobjects.RadarModelMonostatic.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: clutter
    :canonical: br.steak.core.stkobjects.RadarModelMonostatic.clutter
    :type: RadarClutter

    Get the radar clutter settings.

.. py:property:: jamming
    :canonical: br.steak.core.stkobjects.RadarModelMonostatic.jamming
    :type: RadarJamming

    Get the radar jamming.

.. py:property:: mode_component_linking
    :canonical: br.steak.core.stkobjects.RadarModelMonostatic.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.

.. py:property:: receiver
    :canonical: br.steak.core.stkobjects.RadarModelMonostatic.receiver
    :type: RadarReceiver

    Get the radar receiver.

.. py:property:: transmitter
    :canonical: br.steak.core.stkobjects.RadarModelMonostatic.transmitter
    :type: RadarTransmitter

    Get the radar transmitter.


