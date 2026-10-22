RadarModelBistaticReceiver
==========================

.. py:class:: br.ok.core.stkobjects.RadarModelBistaticReceiver

   Bases: :py:class:`~br.ok.core.stkobjects.IRadarModel`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a bistatic receiver radar model.

.. py:currentmodule:: RadarModelBistaticReceiver

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticReceiver.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticReceiver.bistatic_transmitters`
              - Get the bistatic transmitter collection.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticReceiver.clutter`
              - Get the radar clutter settings.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticReceiver.jamming`
              - Get the radar jamming.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticReceiver.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticReceiver.receiver`
              - Get the radar receiver.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarModelBistaticReceiver


Property detail
---------------

.. py:property:: antenna_control
    :canonical: br.ok.core.stkobjects.RadarModelBistaticReceiver.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: bistatic_transmitters
    :canonical: br.ok.core.stkobjects.RadarModelBistaticReceiver.bistatic_transmitters
    :type: ObjectLinkCollection

    Get the bistatic transmitter collection.

.. py:property:: clutter
    :canonical: br.ok.core.stkobjects.RadarModelBistaticReceiver.clutter
    :type: RadarClutter

    Get the radar clutter settings.

.. py:property:: jamming
    :canonical: br.ok.core.stkobjects.RadarModelBistaticReceiver.jamming
    :type: RadarJamming

    Get the radar jamming.

.. py:property:: mode_component_linking
    :canonical: br.ok.core.stkobjects.RadarModelBistaticReceiver.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.

.. py:property:: receiver
    :canonical: br.ok.core.stkobjects.RadarModelBistaticReceiver.receiver
    :type: RadarReceiver

    Get the radar receiver.


