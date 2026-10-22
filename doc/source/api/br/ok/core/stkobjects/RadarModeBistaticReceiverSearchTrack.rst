RadarModeBistaticReceiverSearchTrack
====================================

.. py:class:: br.ok.core.stkobjects.RadarModeBistaticReceiverSearchTrack

   Bases: :py:class:`~br.ok.core.stkobjects.IRadarModeBistaticReceiver`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a bistatic receiver search/track radar mode.

.. py:currentmodule:: RadarModeBistaticReceiverSearchTrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModeBistaticReceiverSearchTrack.set_waveform_type`
              - Set the waveform type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModeBistaticReceiverSearchTrack.doppler_clutter_filters`
              - Get the RadarDopplerClutterFilters interface for configuring the doppler clutter filters.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModeBistaticReceiverSearchTrack.waveform`
              - Get the interface for configuring the search/track waveform.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarModeBistaticReceiverSearchTrack


Property detail
---------------

.. py:property:: doppler_clutter_filters
    :canonical: br.ok.core.stkobjects.RadarModeBistaticReceiverSearchTrack.doppler_clutter_filters
    :type: RadarDopplerClutterFilters

    Get the RadarDopplerClutterFilters interface for configuring the doppler clutter filters.

.. py:property:: waveform
    :canonical: br.ok.core.stkobjects.RadarModeBistaticReceiverSearchTrack.waveform
    :type: IRadarWaveformSearchTrack

    Get the interface for configuring the search/track waveform.


Method detail
-------------


.. py:method:: set_waveform_type(self, value: RadarWaveformSearchTrackType) -> None
    :canonical: br.ok.core.stkobjects.RadarModeBistaticReceiverSearchTrack.set_waveform_type

    Set the waveform type.

    :Parameters:

        **value** : :obj:`~RadarWaveformSearchTrackType`


    :Returns:

        :obj:`~None`


