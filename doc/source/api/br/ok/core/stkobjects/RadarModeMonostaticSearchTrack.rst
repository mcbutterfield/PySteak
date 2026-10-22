RadarModeMonostaticSearchTrack
==============================

.. py:class:: br.ok.core.stkobjects.RadarModeMonostaticSearchTrack

   Bases: :py:class:`~br.ok.core.stkobjects.IRadarModeMonostatic`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining a monostatic search/track radar mode.

.. py:currentmodule:: RadarModeMonostaticSearchTrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModeMonostaticSearchTrack.set_waveform_type`
              - Set the waveform type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RadarModeMonostaticSearchTrack.doppler_clutter_filters`
              - Get the RadarDopplerClutterFilters interface for configuring the doppler clutter filters.
            * - :py:attr:`~br.ok.core.stkobjects.RadarModeMonostaticSearchTrack.waveform`
              - Get the interface for configuring the search/track waveform.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RadarModeMonostaticSearchTrack


Property detail
---------------

.. py:property:: doppler_clutter_filters
    :canonical: br.ok.core.stkobjects.RadarModeMonostaticSearchTrack.doppler_clutter_filters
    :type: RadarDopplerClutterFilters

    Get the RadarDopplerClutterFilters interface for configuring the doppler clutter filters.

.. py:property:: waveform
    :canonical: br.ok.core.stkobjects.RadarModeMonostaticSearchTrack.waveform
    :type: IRadarWaveformSearchTrack

    Get the interface for configuring the search/track waveform.


Method detail
-------------


.. py:method:: set_waveform_type(self, value: RadarWaveformSearchTrackType) -> None
    :canonical: br.ok.core.stkobjects.RadarModeMonostaticSearchTrack.set_waveform_type

    Set the waveform type.

    :Parameters:

        **value** : :obj:`~RadarWaveformSearchTrackType`


    :Returns:

        :obj:`~None`


