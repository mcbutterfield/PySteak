RadarModelBistaticTransmitter
=============================

.. py:class:: br.ok.core.stkobjects.RadarModelBistaticTransmitter

   Bases: :py:class:`~br.ok.core.stkobjects.IRadarModel`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a bistatic transmitter radar model.

.. py:currentmodule:: RadarModelBistaticTransmitter

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticTransmitter.antenna_control`
              - Get the radar antenna control.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticTransmitter.bistatic_receivers`
              - Get the bistatic receiver collection.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticTransmitter.mode_component_linking`
              - Get the link/embed controller for managing the radar mode component.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModelBistaticTransmitter.transmitter`
              - Get the radar transmitter.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarModelBistaticTransmitter


Property detail
---------------

.. py:property:: antenna_control
    :canonical: br.ok.core.stkobjects.RadarModelBistaticTransmitter.antenna_control
    :type: AntennaControl

    Get the radar antenna control.

.. py:property:: bistatic_receivers
    :canonical: br.ok.core.stkobjects.RadarModelBistaticTransmitter.bistatic_receivers
    :type: ObjectLinkCollection

    Get the bistatic receiver collection.

.. py:property:: mode_component_linking
    :canonical: br.ok.core.stkobjects.RadarModelBistaticTransmitter.mode_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the radar mode component.

.. py:property:: transmitter
    :canonical: br.ok.core.stkobjects.RadarModelBistaticTransmitter.transmitter
    :type: RadarTransmitter

    Get the radar transmitter.


