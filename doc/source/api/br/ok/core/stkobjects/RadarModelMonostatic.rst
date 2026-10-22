RadarModelMonostatic
====================

.. py:class:: br.ok.core.stkobjects.RadarModelMonostatic

   Bases: :py:class:`~br.ok.core.stkobjects.IRadarModel`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a monostatic radar model.

.. py:currentmodule:: RadarModelMonostatic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMonostatic.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMonostatic.clutter`
              - Get the radar clutter settings.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMonostatic.jamming`
              - Get the radar jamming.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMonostatic.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMonostatic.receiver`
              - Get the radar receiver.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelMonostatic.transmitter`
              - Get the radar transmitter.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarModelMonostatic


Property detail
---------------

.. py:property:: antenna_control
    :canonical: br.ok.core.stkobjects.RadarModelMonostatic.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: clutter
    :canonical: br.ok.core.stkobjects.RadarModelMonostatic.clutter
    :type: RadarClutter

    Get the radar clutter settings.

.. py:property:: jamming
    :canonical: br.ok.core.stkobjects.RadarModelMonostatic.jamming
    :type: RadarJamming

    Get the radar jamming.

.. py:property:: mode_component_linking
    :canonical: br.ok.core.stkobjects.RadarModelMonostatic.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.

.. py:property:: receiver
    :canonical: br.ok.core.stkobjects.RadarModelMonostatic.receiver
    :type: RadarReceiver

    Get the radar receiver.

.. py:property:: transmitter
    :canonical: br.ok.core.stkobjects.RadarModelMonostatic.transmitter
    :type: RadarTransmitter

    Get the radar transmitter.


